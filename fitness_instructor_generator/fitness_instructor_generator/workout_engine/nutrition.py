"""
Nutrition and Diet Planning Module
Provides meal plans, macros, and dietary tips based on fitness goals.
"""

from typing import Dict, List


NUTRITION_PLANS = {
    "weight_loss": {
        "name": "Weight Loss Nutrition Plan",
        "calorie_focus": "caloric deficit",
        "macros": {
            "protein_percent": 35,
            "carbs_percent": 35,
            "fats_percent": 30
        },
        "daily_tips": [
            "Drink plenty of water (8-10 glasses daily)",
            "Eat lean proteins like chicken, fish, and tofu",
            "Include lots of vegetables and fiber",
            "Avoid sugary drinks and processed foods",
            "Eat in a caloric deficit (300-500 calories below maintenance)",
            "Practice portion control",
            "Don't skip meals - eat smaller frequent meals"
        ],
        "meal_plan": {
            "breakfast": [
                "Oatmeal with berries and protein powder",
                "Eggs (3 whites, 1 yolk) with whole wheat toast",
                "Greek yogurt with granola and honey",
                "Smoothie: banana, spinach, protein powder, almond milk"
            ],
            "lunch": [
                "Grilled chicken (150g) with brown rice and broccoli",
                "Fish (150g) with sweet potato and green beans",
                "Turkey breast with quinoa and asparagus",
                "Lean beef (120g) with whole wheat pasta and tomato sauce"
            ],
            "dinner": [
                "Salmon (150g) with sweet potato and salad",
                "Chicken breast (150g) with white rice and vegetables",
                "Lean turkey (150g) with barley and steamed broccoli",
                "Tofu stir-fry with brown rice"
            ],
            "snacks": [
                "Apple with almond butter",
                "Protein shake",
                "Greek yogurt",
                "Almonds (1 oz)",
                "Cottage cheese with berries"
            ]
        },
        "hydration": "Drink 3-4 liters of water daily. Increase intake during workouts.",
        "timing": "Eat protein and carbs within 1-2 hours after workout for recovery"
    },
    
    "muscle_gain": {
        "name": "Muscle Gain Nutrition Plan",
        "calorie_focus": "caloric surplus",
        "macros": {
            "protein_percent": 40,
            "carbs_percent": 40,
            "fats_percent": 20
        },
        "daily_tips": [
            "Eat in a slight caloric surplus (300-500 calories above maintenance)",
            "Consume 1.6-2.2g of protein per kg of body weight daily",
            "Eat complex carbs for energy during workouts",
            "Include healthy fats for hormone production",
            "Eat more frequently - 5-6 meals per day",
            "Time carbs and protein around your workouts",
            "Track your caloric and protein intake"
        ],
        "meal_plan": {
            "breakfast": [
                "Pancakes with protein powder and berries",
                "Eggs (4) with oatmeal and banana",
                "Breakfast burrito: eggs, cheese, beans, tortilla",
                "Granola with whole milk and protein powder"
            ],
            "lunch": [
                "Chicken (200g) with rice and vegetables",
                "Beef (200g) with pasta and sauce",
                "Fish (200g) with sweet potato and salad",
                "Turkey (200g) with quinoa"
            ],
            "dinner": [
                "Salmon (200g) with rice and broccoli",
                "Chicken (200g) with pasta and olive oil",
                "Lean beef (200g) with sweet potato and greens",
                "Turkey (200g) with barley and vegetables"
            ],
            "snacks": [
                "Protein shake with banana and oats",
                "Peanut butter sandwich",
                "Trail mix with nuts and dried fruit",
                "Cottage cheese with granola",
                "Almonds and raisins"
            ]
        },
        "hydration": "Drink 4-5 liters of water daily, especially around workouts.",
        "timing": "Consume carbs and protein 1-2 hours before workout. Protein shake within 30 min after workout."
    },
    
    "flexibility": {
        "name": "Flexibility & Mobility Nutrition Plan",
        "calorie_focus": "maintenance",
        "macros": {
            "protein_percent": 30,
            "carbs_percent": 45,
            "fats_percent": 25
        },
        "daily_tips": [
            "Eat balanced macronutrients for overall health",
            "Include anti-inflammatory foods (turmeric, ginger, omega-3s)",
            "Eat enough protein for muscle recovery",
            "Stay hydrated for joint health",
            "Include foods rich in collagen and amino acids",
            "Avoid excess sodium and processed foods",
            "Include fresh fruits and vegetables"
        ],
        "meal_plan": {
            "breakfast": [
                "Yogurt with granola, honey, and berries",
                "Whole grain toast with avocado and eggs",
                "Smoothie bowl with nuts and seeds",
                "Oatmeal with turmeric and cinnamon"
            ],
            "lunch": [
                "Grilled chicken (150g) with quinoa and vegetables",
                "Fish (150g) with sweet potato and salad",
                "Lentil soup with whole grain bread",
                "Turkey wrap with vegetables and hummus"
            ],
            "dinner": [
                "Salmon (150g) with brown rice and steamed greens",
                "Vegetable stir-fry with tofu (150g)",
                "Chicken (150g) with pasta and tomato sauce",
                "Bean and vegetable curry with rice"
            ],
            "snacks": [
                "Mixed nuts and berries",
                "Apple with almond butter",
                "Yogurt with honey",
                "Carrot sticks with hummus",
                "Green tea with almonds"
            ]
        },
        "hydration": "Drink 2.5-3 liters of water daily. Add lemon for antioxidants.",
        "timing": "Eat light meals to support yoga and stretching practices."
    },
    
    "cardio": {
        "name": "Cardio & Endurance Nutrition Plan",
        "calorie_focus": "slight deficit or maintenance",
        "macros": {
            "protein_percent": 25,
            "carbs_percent": 55,
            "fats_percent": 20
        },
        "daily_tips": [
            "Prioritize carbohydrates for energy",
            "Include adequate protein for muscle preservation",
            "Eat enough calories to sustain high-intensity training",
            "Hydrate consistently throughout the day",
            "Include electrolytes during long cardio sessions",
            "Eat easily digestible carbs before cardio",
            "Recovery carbs within 30 minutes after workout"
        ],
        "meal_plan": {
            "breakfast": [
                "Bagel with peanut butter and banana",
                "Cereal with milk and berries",
                "Toast with honey and eggs",
                "Oatmeal with brown sugar and banana"
            ],
            "lunch": [
                "Pasta (200g) with chicken (120g) and vegetables",
                "Rice (200g) with fish (120g) and steamed broccoli",
                "Sandwich: turkey, cheese, veggies with chips",
                "Noodles with shrimp and mixed vegetables"
            ],
            "dinner": [
                "Chicken (150g) with rice (200g) and vegetables",
                "Fish (150g) with pasta (200g) and sauce",
                "Lean beef (150g) with sweet potato (200g)",
                "Turkey (150g) with quinoa (200g) and salad"
            ],
            "snacks": [
                "Banana with peanut butter",
                "Rice cakes with jam",
                "Sports drink or coconut water",
                "Energy bar",
                "Dates or dried fruit"
            ]
        },
        "hydration": "Drink 4-5 liters daily. Use sports drinks for workouts over 60 minutes.",
        "timing": "Eat carbs 1-2 hours before cardio. Refuel with carbs and protein within 30 min after."
    }
}


def get_nutrition_plan(goal: str, fitness_level: str = "beginner") -> Dict:
    """
    Get nutrition plan based on fitness goal.
    
    Args:
        goal: Fitness goal (weight_loss, muscle_gain, flexibility, cardio)
        fitness_level: Level of fitness (beginner, intermediate, advanced)
        
    Returns:
        Dictionary with complete nutrition plan
    """
    if goal not in NUTRITION_PLANS:
        goal = "weight_loss"
    
    plan = NUTRITION_PLANS[goal].copy()
    
    # Adjust portions based on fitness level
    if fitness_level == "advanced":
        plan["daily_tips"].append("Advanced: Periodize your nutrition with carb-loading and depletion phases")
        plan["daily_tips"].append("Advanced: Track macros with apps like MyFitnessPal for precision")
    elif fitness_level == "intermediate":
        plan["daily_tips"].append("Intermediate: Start tracking macros and calories")
    else:
        plan["daily_tips"].append("Beginner: Focus on consistency before perfection")
    
    return plan


def get_meal_suggestion(goal: str, meal_type: str) -> List[str]:
    """
    Get specific meal suggestions for a goal and meal type.
    
    Args:
        goal: Fitness goal
        meal_type: breakfast, lunch, dinner, snacks
        
    Returns:
        List of meal options
    """
    if goal not in NUTRITION_PLANS:
        goal = "weight_loss"
    
    return NUTRITION_PLANS[goal]["meal_plan"].get(meal_type, [])


def get_macro_targets(goal: str, daily_calories: int = 2000) -> Dict:
    """
    Calculate macro targets based on goal and daily calorie intake.
    
    Args:
        goal: Fitness goal
        daily_calories: Target daily calorie intake
        
    Returns:
        Dictionary with protein, carbs, fats in grams
    """
    if goal not in NUTRITION_PLANS:
        goal = "weight_loss"
    
    macros = NUTRITION_PLANS[goal]["macros"]
    
    return {
        "goal": goal,
        "daily_calories": daily_calories,
        "protein_grams": int((daily_calories * macros["protein_percent"] / 100) / 4),
        "carbs_grams": int((daily_calories * macros["carbs_percent"] / 100) / 4),
        "fats_grams": int((daily_calories * macros["fats_percent"] / 100) / 9),
        "macros_breakdown": macros
    }


def get_hydration_tips(goal: str) -> str:
    """Get hydration advice for specific goal."""
    return NUTRITION_PLANS.get(goal, NUTRITION_PLANS["weight_loss"])["hydration"]


def get_timing_tips(goal: str) -> str:
    """Get meal timing advice for specific goal."""
    return NUTRITION_PLANS.get(goal, NUTRITION_PLANS["weight_loss"])["timing"]


def get_weekly_meal_plan(goal: str) -> List[Dict]:
    """Get a 7-day meal plan for the given goal."""
    plan = NUTRITION_PLANS.get(goal, NUTRITION_PLANS["weight_loss"])
    
    week_plan = []
    for day in range(1, 8):
        day_plan = {
            "day": day,
            "breakfast": plan["meal_plan"]["breakfast"][(day - 1) % len(plan["meal_plan"]["breakfast"])],
            "lunch": plan["meal_plan"]["lunch"][(day - 1) % len(plan["meal_plan"]["lunch"])],
            "dinner": plan["meal_plan"]["dinner"][(day - 1) % len(plan["meal_plan"]["dinner"])],
            "snack": plan["meal_plan"]["snacks"][(day - 1) % len(plan["meal_plan"]["snacks"])]
        }
        week_plan.append(day_plan)
    
    return week_plan
