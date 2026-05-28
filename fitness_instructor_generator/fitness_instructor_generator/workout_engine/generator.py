def generate_workout(entities: dict) -> list:
    goal = entities["goal"]
def generate_workout(entities: dict) -> list:
    goal = entities["goal"]

    if goal == "weight_loss":
        return [
            {"name": "Jumping Jacks", "type": "time", "value": 30, "sets": 3, "rest": 20},
            {"name": "Squats", "type": "reps", "value": 12, "sets": 3, "rest": 30},
            {"name": "Plank", "type": "time", "value": 30, "sets": 3, "rest": 30},
        ]

    if goal == "muscle_gain":
        return [
            {"name": "Push-ups", "type": "reps", "value": 10, "sets": 3, "rest": 30},
            {"name": "Dumbbell Curls", "type": "reps", "value": 12, "sets": 3, "rest": 30},
            {"name": "Lunges", "type": "reps", "value": 10, "sets": 3, "rest": 30},
        ]

    if goal == "flexibility":
        return [
            {"name": "Neck Stretch", "type": "time", "value": 30, "sets": 2, "rest": 15},
            {"name": "Hamstring Stretch", "type": "time", "value": 30, "sets": 2, "rest": 15},
            {"name": "Child Pose", "type": "time", "value": 60, "sets": 1, "rest": 0},
        ]

    return []
