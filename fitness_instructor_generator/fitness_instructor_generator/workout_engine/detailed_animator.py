"""
Enhanced exercise animator with detailed step-by-step movements and narration.
Shows avatar performing exercises with detailed form breakdown.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, FancyArrowPatch
import numpy as np
from PIL import Image
import io
from typing import List, Dict, Tuple


class DetailedExerciseAnimator:
    """Create detailed step-by-step exercise animations with narration guidance."""
    
    EXERCISE_STEPS = {
        "Push-up": {
            "steps": [
                {
                    "phase": 1,
                    "name": "Starting Position",
                    "description": "Get into plank position with hands shoulder-width apart, body in a straight line.",
                    "duration": 2,
                    "body_angle": 0,
                    "arm_bend": 0,
                    "visual_note": "Straight body alignment"
                },
                {
                    "phase": 2,
                    "name": "Lower Down",
                    "description": "Bend your elbows and lower your chest towards the ground. Keep elbows at 45 degrees from body.",
                    "duration": 2,
                    "body_angle": 5,
                    "arm_bend": 60,
                    "visual_note": "Elbows tucked"
                },
                {
                    "phase": 3,
                    "name": "Bottom Position",
                    "description": "Lower until chest nearly touches ground. Maintain straight body and engaged core.",
                    "duration": 1,
                    "body_angle": 10,
                    "arm_bend": 90,
                    "visual_note": "Chest near ground"
                },
                {
                    "phase": 4,
                    "name": "Push Up",
                    "description": "Press through your hands and push your body back to starting position. Keep core tight.",
                    "duration": 2,
                    "body_angle": 0,
                    "arm_bend": 0,
                    "visual_note": "Explosive push"
                }
            ],
            "tips": [
                "Keep your body in a straight line from head to heels",
                "Don't let your hips sag or pike up",
                "Elbows should be at roughly 45-degree angle from body",
                "Lower until chest nearly touches ground",
                "Engage your core throughout the movement"
            ],
            "common_mistakes": [
                "Sagging hips",
                "Flared elbows",
                "Head dropping",
                "Incomplete range of motion",
                "Not engaging core"
            ]
        },
        "Squat": {
            "steps": [
                {
                    "phase": 1,
                    "name": "Starting Position",
                    "description": "Stand with feet shoulder-width apart, chest up, weight in heels.",
                    "duration": 2,
                    "knee_bend": 0,
                    "hip_depth": 0,
                    "visual_note": "Feet shoulder-width"
                },
                {
                    "phase": 2,
                    "name": "Descend",
                    "description": "Begin to squat by pushing hips back and bending knees. Keep chest up and knees tracking over toes.",
                    "duration": 2,
                    "knee_bend": 45,
                    "hip_depth": 2,
                    "visual_note": "Hips back, knees forward"
                },
                {
                    "phase": 3,
                    "name": "Bottom Position",
                    "description": "Lower until thighs are parallel to ground. Keep weight in heels and chest up.",
                    "duration": 1,
                    "knee_bend": 90,
                    "hip_depth": 4,
                    "visual_note": "Thighs parallel"
                },
                {
                    "phase": 4,
                    "name": "Ascend",
                    "description": "Drive through heels and extend hips and knees to return to starting position.",
                    "duration": 2,
                    "knee_bend": 0,
                    "hip_depth": 0,
                    "visual_note": "Drive through heels"
                }
            ],
            "tips": [
                "Feet should be shoulder-width apart",
                "Keep chest up throughout movement",
                "Knees should track over toes",
                "Lower until thighs are at least parallel to ground",
                "Drive through heels, not toes",
                "Maintain neutral spine"
            ],
            "common_mistakes": [
                "Knees caving inward",
                "Leaning too far forward",
                "Incomplete depth",
                "Heels lifting off ground",
                "Rounding lower back"
            ]
        },
        "Plank": {
            "steps": [
                {
                    "phase": 1,
                    "name": "Get into Position",
                    "description": "Start on forearms and toes. Shoulders directly over elbows, body in straight line.",
                    "duration": 2,
                    "hold_time": 0,
                    "visual_note": "Shoulders over elbows"
                },
                {
                    "phase": 2,
                    "name": "Engage Core",
                    "description": "Tighten your core and glutes. Don't let hips sag or rise. Maintain neutral neck.",
                    "duration": 3,
                    "hold_time": 10,
                    "visual_note": "Core engaged"
                },
                {
                    "phase": 3,
                    "name": "Hold Position",
                    "description": "Continue holding with body in straight line. Breathe steadily. Resist hip sag.",
                    "duration": 10,
                    "hold_time": 20,
                    "visual_note": "Steady hold"
                },
                {
                    "phase": 4,
                    "name": "Rest",
                    "description": "Lower to ground and rest. Recover for next set.",
                    "duration": 2,
                    "hold_time": 0,
                    "visual_note": "Recovery"
                }
            ],
            "tips": [
                "Body should form a straight line",
                "Shoulders directly over elbows",
                "Engage your core and glutes",
                "Don't let hips sag",
                "Maintain neutral neck position",
                "Breathe steadily"
            ],
            "common_mistakes": [
                "Hips sagging",
                "Hips too high",
                "Shoulders not aligned",
                "Neck strain",
                "Weak core engagement",
                "Holding breath"
            ]
        },
        "Jumping Jack": {
            "steps": [
                {
                    "phase": 1,
                    "name": "Starting Position",
                    "description": "Stand with feet together, arms at sides, good posture.",
                    "duration": 1,
                    "feet_apart": 0,
                    "arms_raised": 0,
                    "visual_note": "Feet together"
                },
                {
                    "phase": 2,
                    "name": "Jump and Spread",
                    "description": "Jump while spreading feet to shoulder-width apart and raising arms to overhead.",
                    "duration": 1,
                    "feet_apart": 1,
                    "arms_raised": 1,
                    "visual_note": "Explosive jump"
                },
                {
                    "phase": 3,
                    "name": "Landing Position",
                    "description": "Land softly on balls of feet with full body engaged. Arms overhead, feet wide.",
                    "duration": 0.5,
                    "feet_apart": 1,
                    "arms_raised": 1,
                    "visual_note": "Soft landing"
                },
                {
                    "phase": 4,
                    "name": "Return to Start",
                    "description": "Jump again to bring feet together and lower arms to sides.",
                    "duration": 1,
                    "feet_apart": 0,
                    "arms_raised": 0,
                    "visual_note": "Back to start"
                }
            ],
            "tips": [
                "Start with feet together",
                "Jump explosively",
                "Land softly on balls of feet",
                "Keep chest up",
                "Move arms in full range",
                "Maintain steady breathing"
            ],
            "common_mistakes": [
                "Landing hard (heel strike)",
                "Arms not going overhead",
                "Incomplete spread",
                "Poor posture",
                "Uneven landings"
            ]
        }
    }
    
    @staticmethod
    def draw_avatar(fig, ax, phase_data: dict, exercise_name: str):
        """Draw detailed avatar in specific exercise phase."""
        ax.set_xlim(-2, 2)
        ax.set_ylim(-1, 6)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Ground
        ax.plot([-2, 2], [0, 0], 'k-', linewidth=3)
        
        center_x = 0
        center_y = 2
        
        if exercise_name == "Push-up":
            body_angle = phase_data.get("body_angle", 0)
            arm_bend = phase_data.get("arm_bend", 0)
            
            # Head (darker color for visibility)
            head = Circle((center_x, center_y + 1.5), 0.28, color='#222222', zorder=10)
            ax.add_patch(head)

            # Body (angled based on position) - darker, thicker
            body_angle_rad = np.radians(body_angle)
            body_length = 1.6
            body_end_x = center_x + body_length * np.sin(body_angle_rad)
            body_end_y = center_y + 1.0 - body_length * np.cos(body_angle_rad)
            ax.plot([center_x, body_end_x], [center_y + 1.2, body_end_y], color='#111111', linewidth=8)

            # Arms (bent based on push-up phase) - ensure hands contact ground
            arm_angle_rad = np.radians(90 - arm_bend / 2)
            left_arm_x = center_x - 0.6
            left_hand_x = left_arm_x - 1.0 * np.cos(arm_angle_rad)
            left_hand_y = center_y + 0.6 - 1.0 * np.sin(arm_angle_rad)
            ax.plot([left_arm_x, left_hand_x], [center_y + 0.8, left_hand_y], color='#111111', linewidth=6)

            right_arm_x = center_x + 0.6
            right_hand_x = right_arm_x + 1.0 * np.cos(arm_angle_rad)
            right_hand_y = center_y + 0.6 - 1.0 * np.sin(arm_angle_rad)
            ax.plot([right_arm_x, right_hand_x], [center_y + 0.8, right_hand_y], color='#111111', linewidth=6)

            # Legs (thicker darker lines)
            ax.plot([center_x - 0.3, center_x - 0.2], [body_end_y, -0.2], color='#111111', linewidth=5)
            ax.plot([center_x + 0.3, center_x + 0.2], [body_end_y, -0.2], color='#111111', linewidth=5)
            
        elif exercise_name == "Squat":
            knee_bend = phase_data.get("knee_bend", 0)
            hip_depth = phase_data.get("hip_depth", 0)
            
            # Head
            head = Circle((center_x, center_y + 1.5), 0.25, color='#FF6B6B', zorder=10)
            ax.add_patch(head)
            
            # Torso (slight lean based on depth)
            torso_angle = knee_bend / 10
            ax.plot([center_x, center_x + 0.2 * torso_angle], 
                   [center_y + 1.2, center_y - 0.5], 'b-', linewidth=6)
            
            # Arms
            ax.plot([center_x - 0.4, center_x - 0.4], [center_y + 0.5, center_y - 0.2], 'r-', linewidth=4)
            ax.plot([center_x + 0.4, center_x + 0.4], [center_y + 0.5, center_y - 0.2], 'r-', linewidth=4)
            
            # Legs (bend with squat)
            leg_bend_offset = hip_depth * 0.3
            
            ax.plot([center_x - 0.25, center_x - 0.25 - 0.1 * (knee_bend / 90)],
                   [center_y - 0.5, center_y - 0.5 - leg_bend_offset], 'g-', linewidth=4)
            ax.plot([center_x - 0.25 - 0.1 * (knee_bend / 90), center_x - 0.2],
                   [center_y - 0.5 - leg_bend_offset, -0.2], 'g-', linewidth=4)
            
            ax.plot([center_x + 0.25, center_x + 0.25 + 0.1 * (knee_bend / 90)],
                   [center_y - 0.5, center_y - 0.5 - leg_bend_offset], 'g-', linewidth=4)
            ax.plot([center_x + 0.25 + 0.1 * (knee_bend / 90), center_x + 0.2],
                   [center_y - 0.5 - leg_bend_offset, -0.2], 'g-', linewidth=4)
    
    @staticmethod
    def create_step_frames(exercise_name: str, num_frames: int = 30) -> List[Tuple[Image.Image, Dict]]:
        """Create frames for each step of an exercise."""
        frames = []
        
        if exercise_name not in DetailedExerciseAnimator.EXERCISE_STEPS:
            return frames
        
        exercise_data = DetailedExerciseAnimator.EXERCISE_STEPS[exercise_name]
        steps = exercise_data["steps"]
        frames_per_step = max(1, num_frames // len(steps))
        
        for step_idx, step in enumerate(steps):
            step_name = step["name"]
            step_desc = step["description"]
            
            for frame_in_step in range(frames_per_step):
                fig, ax = plt.subplots(figsize=(8, 10), dpi=100)
                
                # Draw avatar
                DetailedExerciseAnimator.draw_avatar(fig, ax, step, exercise_name)
                
                # Add step information
                ax.text(0, 5.5, f"Step {step_idx + 1}: {step_name}", 
                       ha='center', fontsize=14, weight='bold', color='#4ECDC4')
                ax.text(0, 5.0, step_desc, ha='center', fontsize=11, 
                       style='italic', wrap=True, color='#333')
                
                # Add visual note
                ax.text(0, 4.5, f"📌 {step['visual_note']}", 
                       ha='center', fontsize=10, color='#FF6B6B', weight='bold')
                
                # Convert to PIL Image
                buf = io.BytesIO()
                plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
                buf.seek(0)
                frame_img = Image.open(buf).copy()
                plt.close(fig)
                
                frames.append((frame_img, {
                    "step": step_idx + 1,
                    "phase": step_name,
                    "narration": step_desc,
                    "tips": exercise_data.get("tips", []),
                    "common_mistakes": exercise_data.get("common_mistakes", [])
                }))
        
        return frames


def get_exercise_narration(exercise_name: str) -> Dict:
    """Get complete narration and tips for an exercise."""
    if exercise_name not in DetailedExerciseAnimator.EXERCISE_STEPS:
        return {"steps": [], "tips": [], "common_mistakes": []}
    
    exercise = DetailedExerciseAnimator.EXERCISE_STEPS[exercise_name]
    return {
        "name": exercise_name,
        "steps": exercise["steps"],
        "tips": exercise.get("tips", []),
        "common_mistakes": exercise.get("common_mistakes", [])
    }
