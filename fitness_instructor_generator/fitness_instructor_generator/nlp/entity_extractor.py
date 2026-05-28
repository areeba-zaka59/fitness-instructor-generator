def extract_entities(text: str) -> dict:
    """Extract fitness-related entities from user input."""
    text = text.lower()

    entities = {
        "fitness_level": "beginner",
        "goal": "weight_loss",
        "equipment": "none",
        "duration": 20,
        "intensity": "moderate"
    }

    # Fitness level detection
    if "intermediate" in text:
        entities["fitness_level"] = "intermediate"
    elif "advanced" in text or "expert" in text or "professional" in text:
        entities["fitness_level"] = "advanced"

    # Goal detection
    if "muscle" in text or "bulk" in text or "strength" in text:
        entities["goal"] = "muscle_gain"
    elif "flexibility" in text or "stretch" in text or "yoga" in text or "mobile" in text:
        entities["goal"] = "flexibility"
    elif "cardio" in text or "endurance" in text or "stamina" in text:
        entities["goal"] = "cardio"
    elif "lose" in text or "weight" in text or "fat" in text or "slim" in text:
        entities["goal"] = "weight_loss"

    # Equipment detection
    if "dumbbell" in text or "weights" in text:
        entities["equipment"] = "dumbbells"
    elif "gym" in text:
        entities["equipment"] = "gym"
    elif "home" in text:
        entities["equipment"] = "home"

    # Duration detection
    for d in [10, 15, 20, 30, 45, 60]:
        if str(d) in text:
            entities["duration"] = d
            break

    # Intensity detection
    if "high" in text or "intense" in text or "hard" in text:
        entities["intensity"] = "high"
    elif "low" in text or "easy" in text or "light" in text:
        entities["intensity"] = "low"

    return entities
