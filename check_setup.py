import os

print("--- Checking Project Setup ---")

# 1. Check Model
if os.path.exists('models/food_model.h5'):
    print("✅ Model found.")
else:
    print("❌ ERROR: 'models/food_model.h5' is MISSING.")
    print("   -> Create a folder named 'models' and put your .h5 file inside.")

# 2. Check Utils
if os.path.exists('utils.py'):
    print("✅ utils.py found.")
else:
    print("❌ ERROR: 'utils.py' is MISSING.")
    print("   -> Create this file and paste the 'FOOD_CLASSES' code.")

# 3. Check Templates
if os.path.exists('templates/index.html'):
    print("✅ index.html found.")
else:
    print("❌ ERROR: 'templates/index.html' is MISSING.")

print("------------------------------")
