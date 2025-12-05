import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from werkzeug.utils import secure_filename
import utils # Import our labels and nutrition logic

app = Flask(__name__)

# Configuration
MODEL_PATH = 'models/food_model.h5'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load Model (Global to load only once)
print("Loading Model...")
try:
    # We use compile=False because we only need inference, 
    # and sometimes custom optimizers cause loading issues.
    model = load_model(MODEL_PATH, compile=False) 
    print("Model Loaded Successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Ensure 'food_model.h5' is in the 'models/' directory.")
    model = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(img_path):
    if model is None:
        return "Model not loaded", 0.0
        
    # Preprocess image to match training requirements (224x224)
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x) # Normalizes data (e.g. /255 or -1 to 1)

    # Predict
    preds = model.predict(x)
    pred_class_index = np.argmax(preds, axis=1)[0]
    confidence = np.max(preds)
    
    # Get Label
    pred_class = utils.FOOD_CLASSES[pred_class_index]
    
    # Format label (remove underscores)
    formatted_class = pred_class.replace('_', ' ').title()
    
    return formatted_class, round(confidence * 100, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if file is present
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Create upload folder if not exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
                
            file.save(filepath)
            
            # Run Prediction
            prediction, confidence = predict_image(filepath)
            
            # Get Innovative Nutrition Data
            nutrition = utils.get_nutrition_info(prediction.lower())
            
            return render_template('index.html', 
                                   filename=filename, 
                                   prediction=prediction, 
                                   confidence=confidence,
                                   nutrition=nutrition)
                                   
    return render_template('index.html')

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename))

if __name__ == '__main__':
    app.run(debug=True, port=5000)