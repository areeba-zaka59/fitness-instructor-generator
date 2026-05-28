"""
Voice Narration Module - Guides users through exercises with voice narration.
Provides step-by-step voice guidance and tips.
"""

import pyttsx3
import threading
from typing import List, Optional


class ExerciseNarrator:
    """Handles voice narration for exercises with step-by-step guidance."""
    
    def __init__(self):
        """Initialize text-to-speech engine."""
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)  # Slower for clarity
            self.engine.setProperty('volume', 0.9)
            self.narrator_available = True
        except Exception as e:
            print(f"Warning: Text-to-speech unavailable: {e}")
            self.narrator_available = False
    
    def speak(self, text: str, wait: bool = True):
        """
        Speak text using text-to-speech.
        
        Args:
            text: Text to speak
            wait: Whether to wait for speech to finish
        """
        if not self.narrator_available:
            return
        
        try:
            self.engine.say(text)
            if wait:
                self.engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")
    
    def narrate_exercise_intro(self, exercise_name: str, sets: int, reps_or_duration: int, is_time: bool = False):
        """Narrate exercise introduction."""
        duration_text = f"{reps_or_duration} seconds" if is_time else f"{reps_or_duration} reps"
        intro = f"Starting exercise: {exercise_name}. You will perform {sets} sets of {duration_text}. "
        intro += "Focus on proper form and controlled movements. Let's begin!"
        self.speak(intro)
    
    def narrate_step(self, step_name: str, description: str, step_number: int, total_steps: int):
        """Narrate a specific exercise step."""
        narration = f"Step {step_number} of {total_steps}: {step_name}. {description}. "
        self.speak(narration)
    
    def narrate_tips(self, tips: List[str]):
        """Narrate form tips for an exercise."""
        if not tips:
            return
        
        narration = "Form tips: "
        for i, tip in enumerate(tips[:3], 1):  # Only first 3 tips
            narration += f"Number {i}: {tip}. "
        self.speak(narration)
    
    def narrate_countdown(self, seconds: int):
        """Narrate final countdown before starting."""
        self.speak(f"Get ready! Starting in {seconds} seconds.")
    
    def narrate_completion(self, exercise_name: str):
        """Narrate exercise completion."""
        messages = [
            f"Excellent! You completed {exercise_name}.",
            f"Great job on {exercise_name}!",
            f"Well done! {exercise_name} is finished."
        ]
        import random
        self.speak(random.choice(messages))
    
    def narrate_rest(self, duration: int, set_number: int, total_sets: int):
        """Narrate rest period."""
        remaining = f"Rest for {duration} seconds. " if duration > 0 else "Rest period starting. "
        remaining += f"You are on set {set_number} of {total_sets}."
        self.speak(remaining)
    
    def narrate_nutrition_tip(self, tip: str):
        """Narrate a nutrition tip."""
        narration = f"Nutrition tip: {tip}"
        self.speak(narration)
    
    def narrate_workout_summary(self, total_exercises: int, total_time: int):
        """Narrate workout completion summary."""
        minutes = total_time // 60
        seconds = total_time % 60
        summary = f"Congratulations! You completed your workout with {total_exercises} exercises. "
        summary += f"Total time: {minutes} minutes and {seconds} seconds. Great job!"
        self.speak(summary)
    
    @staticmethod
    def get_exercise_narrative(exercise_name: str) -> dict:
        """Get complete narrative structure for an exercise."""
        narratives = {
            "Push-up": {
                "intro": "We're starting with push-ups. This is an excellent upper body exercise that works your chest, shoulders, and triceps.",
                "steps": [
                    {
                        "step": 1,
                        "narration": "First, get into plank position. Place your hands slightly wider than shoulder-width apart on the ground. Your body should form a straight line from your head to your heels. Engage your core."
                    },
                    {
                        "step": 2,
                        "narration": "Now, lower your body by bending your elbows. Keep your elbows at approximately 45 degrees from your body. Lower until your chest nearly touches the ground. Maintain that straight body alignment."
                    },
                    {
                        "step": 3,
                        "narration": "Hold this bottom position for a moment. Feel the stretch and tension in your muscles. Keep your core tight and don't let your hips sag."
                    },
                    {
                        "step": 4,
                        "narration": "Now push through your hands to return to the starting position. Exhale as you press up. Keep your body straight and maintain control throughout the movement."
                    }
                ],
                "tips": [
                    "Keep your body in a straight line from head to heels",
                    "Elbows should be at about 45 degrees from your body",
                    "Lower your chest all the way down",
                    "Engage your core throughout the entire movement",
                    "Don't let your hips sag or pike up"
                ]
            },
            "Squat": {
                "intro": "We're doing squats. This is a powerful lower body exercise that works your quads, glutes, and hamstrings.",
                "steps": [
                    {
                        "step": 1,
                        "narration": "Start by standing with your feet shoulder-width apart. Point your toes slightly outward. Keep your chest up and your weight in your heels. This is your starting position."
                    },
                    {
                        "step": 2,
                        "narration": "Begin your squat by pushing your hips back and bending your knees. Imagine sitting back into a chair. Keep your chest up and knees tracking over your toes throughout the movement."
                    },
                    {
                        "step": 3,
                        "narration": "Continue lowering until your thighs are parallel to the ground. Your weight should remain in your heels, not on your toes. Keep your chest up and core engaged."
                    },
                    {
                        "step": 4,
                        "narration": "Now drive through your heels to push yourself back up to the starting position. Exhale as you extend your hips and knees. Maintain control throughout."
                    }
                ],
                "tips": [
                    "Feet should be shoulder-width apart",
                    "Keep your chest up throughout the movement",
                    "Knees should track over your toes",
                    "Lower until thighs are parallel to the ground",
                    "Drive through your heels, not your toes"
                ]
            },
            "Plank": {
                "intro": "We're doing a plank. This is an excellent core strengthening exercise that also engages your shoulders and back.",
                "steps": [
                    {
                        "step": 1,
                        "narration": "Start by getting into a plank position. Place your forearms on the ground with shoulders directly over your elbows. Your body should form a straight line from your head to your heels. Engage your core."
                    },
                    {
                        "step": 2,
                        "narration": "Tighten your core and glute muscles. Don't let your hips sag toward the ground. Maintain a neutral neck position by looking straight ahead. Keep your breathing steady."
                    },
                    {
                        "step": 3,
                        "narration": "Hold this position with maximum core engagement. Resist any movement. Keep your body in a perfect straight line. Continue breathing steadily throughout the hold."
                    },
                    {
                        "step": 4,
                        "narration": "When you're ready to rest, slowly lower your knees or hips to the ground. Take a brief recovery before starting your next set."
                    }
                ],
                "tips": [
                    "Shoulders should be directly over elbows",
                    "Maintain a straight line from head to heels",
                    "Engage your core and glutes",
                    "Don't let your hips sag",
                    "Keep your neck in a neutral position"
                ]
            },
            "Jumping Jack": {
                "intro": "We're doing jumping jacks. This is a full-body cardio exercise that gets your heart rate up.",
                "steps": [
                    {
                        "step": 1,
                        "narration": "Start with your feet together and arms at your sides. Stand with good posture and keep your chest up. This is your starting position. Get ready to move."
                    },
                    {
                        "step": 2,
                        "narration": "Jump explosively while simultaneously spreading your feet to shoulder-width apart and raising your arms overhead. The movement should be one continuous, explosive motion."
                    },
                    {
                        "step": 3,
                        "narration": "Land softly on the balls of your feet with your full body engaged. Keep your core tight and stay balanced. Your feet should be wide and your arms overhead."
                    },
                    {
                        "step": 4,
                        "narration": "Jump again to return to the starting position with feet together and arms at your sides. Maintain a steady pace and continue moving."
                    }
                ],
                "tips": [
                    "Land softly on the balls of your feet",
                    "Keep your chest up throughout the movement",
                    "Move your arms through their full range",
                    "Maintain a steady, consistent pace",
                    "Keep your core engaged"
                ]
            }
        }
        
        return narratives.get(exercise_name, {
            "intro": f"Starting {exercise_name} exercise.",
            "steps": [],
            "tips": []
        })


def speak_async(text: str, narrator: Optional[ExerciseNarrator] = None):
    """Speak text in background thread without blocking UI."""
    if narrator and narrator.narrator_available:
        thread = threading.Thread(target=narrator.speak, args=(text, True))
        thread.daemon = True
        thread.start()
