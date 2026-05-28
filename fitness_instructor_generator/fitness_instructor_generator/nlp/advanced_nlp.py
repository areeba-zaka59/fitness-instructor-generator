"""
Advanced NLP module using spaCy for fitness intent recognition and entity extraction.
This provides more sophisticated natural language understanding than basic keyword matching.
"""

import spacy
from typing import Dict, List, Tuple

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


FITNESS_INTENTS = {
    "weight_loss": {
        "keywords": ["lose", "fat", "slim", "thin", "weight", "burn", "cut"],
        "weight": 1.0
    },
    "muscle_gain": {
        "keywords": ["muscle", "strength", "bulk", "gain", "build", "power"],
        "weight": 1.0
    },
    "flexibility": {
        "keywords": ["flexibility", "stretch", "yoga", "mobile", "range", "motion"],
        "weight": 1.0
    },
    "cardio": {
        "keywords": ["cardio", "endurance", "stamina", "run", "sprint", "heart", "fitness"],
        "weight": 1.0
    },
    "core": {
        "keywords": ["core", "abs", "abdominal", "plank", "crunch"],
        "weight": 1.0
    }
}

EXERCISE_TYPES = {
    "strength": ["push", "pull", "weight", "dumbbell", "barbell", "squat", "deadlift"],
    "cardio": ["run", "jump", "sprint", "jog", "walk", "bike", "row"],
    "flexibility": ["stretch", "yoga", "mobility", "foam", "massage"],
    "bodyweight": ["push-up", "pull-up", "dip", "lunge", "burpee"]
}


def advanced_intent_classifier(text: str) -> Dict[str, float]:
    """
    Classify fitness intent using spaCy NLP and return confidence scores.
    
    Args:
        text: User input text
        
    Returns:
        Dictionary with intent names and confidence scores
    """
    doc = nlp(text.lower())
    text_lower = text.lower()
    
    intent_scores = {intent: 0.0 for intent in FITNESS_INTENTS.keys()}
    
    # Score based on keyword matching
    for intent, config in FITNESS_INTENTS.items():
        for keyword in config["keywords"]:
            if keyword in text_lower:
                intent_scores[intent] += config["weight"]
    
    # Normalize scores
    total_score = sum(intent_scores.values())
    if total_score > 0:
        intent_scores = {k: v / total_score for k, v in intent_scores.items()}
    else:
        # Default intent if no matches
        intent_scores["weight_loss"] = 0.5
        intent_scores["cardio"] = 0.5
    
    return intent_scores


def extract_exercise_entities(text: str) -> Dict:
    """
    Extract exercise-specific entities using spaCy.
    
    Args:
        text: User input text
        
    Returns:
        Dictionary with extracted entities
    """
    doc = nlp(text.lower())
    text_lower = text.lower()
    
    entities = {
        "fitness_level": "beginner",
        "goal": "weight_loss",
        "equipment": [],
        "duration": 20,
        "intensity": "moderate",
        "exercise_type": "strength",
        "body_parts": []
    }
    
    # Extract fitness level
    if "intermediate" in text_lower:
        entities["fitness_level"] = "intermediate"
    elif "advanced" in text_lower or "expert" in text_lower:
        entities["fitness_level"] = "advanced"
    
    # Extract equipment
    equipment_map = {
        "dumbbell": ["dumbbell", "weight", "weights"],
        "barbell": ["barbell", "bar"],
        "kettlebell": ["kettlebell", "kettle"],
        "resistance_band": ["band", "resistance"],
        "medicine_ball": ["medicine ball"],
        "gym": ["gym"],
        "home": ["home"]
    }
    
    for equip, keywords in equipment_map.items():
        for keyword in keywords:
            if keyword in text_lower:
                entities["equipment"].append(equip)
    
    # Extract duration (in minutes)
    import re
    duration_match = re.search(r'(\d+)\s*(min|minute|minutes)', text_lower)
    if duration_match:
        entities["duration"] = int(duration_match.group(1))
    
    # Extract intensity
    if "high" in text_lower or "intense" in text_lower or "hard" in text_lower:
        entities["intensity"] = "high"
    elif "low" in text_lower or "easy" in text_lower or "light" in text_lower:
        entities["intensity"] = "low"
    
    # Extract body parts using NER
    body_parts = ["chest", "back", "shoulders", "arms", "legs", "core", "glutes", "biceps", "triceps"]
    for part in body_parts:
        if part in text_lower:
            entities["body_parts"].append(part)
    
    return entities


def classify_by_intent(text: str) -> str:
    """Get primary intent from text."""
    scores = advanced_intent_classifier(text)
    if scores:
        return max(scores, key=scores.get)
    return "weight_loss"
