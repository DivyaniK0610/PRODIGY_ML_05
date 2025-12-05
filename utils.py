# Food-101 Class Labels (Alphabetical Order is standard for Keras DataGenerators)
FOOD_CLASSES = [
    'apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare',
    'beet_salad', 'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito',
    'bruschetta', 'caesar_salad', 'cannoli', 'caprese_salad', 'carrot_cake',
    'ceviche', 'cheesecake', 'cheese_plate', 'chicken_curry', 'chicken_quesadilla',
    'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder',
    'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes',
    'deviled_eggs', 'donuts', 'dumplings', 'edamame', 'eggs_benedict',
    'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 'foie_gras',
    'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice',
    'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich',
    'grilled_salmon', 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup',
    'hot_dog', 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna',
    'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons', 'miso_soup',
    'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters',
    'pad_thai', 'paella', 'pancakes', 'panna_cotta', 'peking_duck',
    'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib',
    'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto',
    'samosa', 'sashimi', 'scallops', 'seaweed_salad', 'shrimp_and_grits',
    'spaghetti_bolognese', 'spaghetti_carbonara', 'spring_rolls', 'steak', 'strawberry_shortcake',
    'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare',
    'waffles'
]

# Mock Nutrition Database (Innovation Feature)
# In a real app, this would connect to an API like Edamam or Nutritionix
def get_nutrition_info(food_name):
    # Default values
    data = {
        "calories": "350 kcal",
        "protein": "12g",
        "fat": "15g",
        "carbs": "45g",
        "health_score": "7/10 - Balanced",
        "tip": "Great choice! Enjoy in moderation."
    }
    
    # Custom overrides for specific examples
    if "salad" in food_name:
        data = {"calories": "220 kcal", "protein": "5g", "fat": "12g", "carbs": "15g", "health_score": "9/10 - Excellent", "tip": "High in vitamins!"}
    elif "cake" in food_name or "chocolate" in food_name or "donut" in food_name:
        data = {"calories": "550 kcal", "protein": "4g", "fat": "25g", "carbs": "60g", "health_score": "3/10 - Indulgent", "tip": "A tasty treat. Maybe go for a walk later?"}
    elif "burger" in food_name or "steak" in food_name or "ribs" in food_name:
        data = {"calories": "700 kcal", "protein": "40g", "fat": "35g", "carbs": "40g", "health_score": "5/10 - Protein Packed", "tip": "High protein, but watch the saturated fats."}
    elif "sushi" in food_name or "sashimi" in food_name:
        data = {"calories": "300 kcal", "protein": "20g", "fat": "5g", "carbs": "40g", "health_score": "8/10 - Heart Healthy", "tip": "Rich in Omega-3 fatty acids."}
        
    return data