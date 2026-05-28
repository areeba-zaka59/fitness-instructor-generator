"""
Exercise animation module - creates animated avatars demonstrating exercise movements.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle
from PIL import Image
import io
from typing import List


class ExerciseAnimator:
    """Creates animated demonstrations of exercises with avatar figures."""
    
    @staticmethod
    def create_pushup_animation(num_frames: int = 20) -> List[Image.Image]:
        """
        Create animated push-up demonstration.
        
        Args:
            num_frames: Number of animation frames
            
        Returns:
            List of PIL Images
        """
        frames = []
        
        for frame_num in range(num_frames):
            fig, ax = plt.subplots(1, 1, figsize=(6, 8), dpi=100)
            ax.set_xlim(-1, 5)
            ax.set_ylim(-1, 8)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Animation progress (0 to 1 and back)
            progress = (frame_num % (num_frames // 2)) / (num_frames // 2)
            
            # Ground
            ax.plot([-1, 5], [0, 0], 'k-', linewidth=3)
            
            # Body position changes with push-up motion
            center_x = 2
            center_y = 3 + progress * 2  # Height changes
            
            # Draw stick figure in push-up position
            # Head
            head = Circle((center_x, center_y + 1.5), 0.3, color='orange', zorder=10)
            ax.add_patch(head)
            
            # Torso
            ax.plot([center_x, center_x], [center_y + 1.2, center_y - 0.5], 'b-', linewidth=4)
            
            # Arms (angle changes with push-up)
            arm_angle = 30 + progress * 60  # Rotates during motion
            arm_rad = np.radians(arm_angle)
            
            # Left arm
            left_arm_x = center_x - 0.6
            ax.plot([left_arm_x, left_arm_x - 0.8*np.cos(arm_rad)], 
                   [center_y + 0.8, center_y + 0.8 - 0.8*np.sin(arm_rad)], 'r-', linewidth=3)
            
            # Right arm
            right_arm_x = center_x + 0.6
            ax.plot([right_arm_x, right_arm_x + 0.8*np.cos(arm_rad)],
                   [center_y + 0.8, center_y + 0.8 - 0.8*np.sin(arm_rad)], 'r-', linewidth=3)
            
            # Legs
            ax.plot([center_x - 0.3, center_x - 0.2], [center_y - 0.5, -0.3], 'g-', linewidth=3)
            ax.plot([center_x + 0.3, center_x + 0.2], [center_y - 0.5, -0.3], 'g-', linewidth=3)
            
            # Add text
            rep_num = frame_num // (num_frames // 10) + 1
            ax.text(2, 7, f"Push-up Form Guide", ha='center', fontsize=14, weight='bold')
            ax.text(2, 6.5, f"Keep body straight | Push through arms", ha='center', fontsize=10)
            
            # Convert to PIL Image
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
            buf.seek(0)
            frames.append(Image.open(buf).copy())
            plt.close(fig)
        
        return frames
    
    @staticmethod
    def create_squat_animation(num_frames: int = 20) -> List[Image.Image]:
        """
        Create animated squat demonstration.
        
        Args:
            num_frames: Number of animation frames
            
        Returns:
            List of PIL Images
        """
        frames = []
        
        for frame_num in range(num_frames):
            fig, ax = plt.subplots(1, 1, figsize=(6, 8), dpi=100)
            ax.set_xlim(-1, 5)
            ax.set_ylim(-1, 8)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Animation progress
            progress = (frame_num % (num_frames // 2)) / (num_frames // 2)
            
            # Ground
            ax.plot([-1, 5], [0, 0], 'k-', linewidth=3)
            
            center_x = 2
            # Head height changes with squat depth
            center_y = 5 - progress * 1.5
            
            # Head
            head = Circle((center_x, center_y + 1.2), 0.3, color='orange', zorder=10)
            ax.add_patch(head)
            
            # Torso (bends forward slightly)
            torso_angle = progress * 15
            torso_rad = np.radians(torso_angle)
            ax.plot([center_x, center_x + 0.3*np.sin(torso_rad)], 
                   [center_y + 0.9, center_y - 0.8 + 0.3*np.cos(torso_rad)], 'b-', linewidth=4)
            
            # Arms
            ax.plot([center_x - 0.4, center_x - 0.4], [center_y + 0.5, center_y - 0.3], 'r-', linewidth=3)
            ax.plot([center_x + 0.4, center_x + 0.4], [center_y + 0.5, center_y - 0.3], 'r-', linewidth=3)
            
            # Legs (bend with squat)
            knee_bend = progress * 1.2
            
            # Left leg
            ax.plot([center_x - 0.3, center_x - 0.3 - 0.1*progress], 
                   [center_y - 0.8, center_y - 0.8 - knee_bend], 'g-', linewidth=3)
            ax.plot([center_x - 0.3 - 0.1*progress, center_x - 0.25], 
                   [center_y - 0.8 - knee_bend, -0.2], 'g-', linewidth=3)
            
            # Right leg
            ax.plot([center_x + 0.3, center_x + 0.3 + 0.1*progress],
                   [center_y - 0.8, center_y - 0.8 - knee_bend], 'g-', linewidth=3)
            ax.plot([center_x + 0.3 + 0.1*progress, center_x + 0.25],
                   [center_y - 0.8 - knee_bend, -0.2], 'g-', linewidth=3)
            
            # Text guidance
            ax.text(2, 7, "Squat Form Guide", ha='center', fontsize=14, weight='bold')
            ax.text(2, 6.5, "Knees track over toes | Lower to parallel", ha='center', fontsize=10)
            
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
            buf.seek(0)
            frames.append(Image.open(buf).copy())
            plt.close(fig)
        
        return frames
    
    @staticmethod
    def create_jumping_jack_animation(num_frames: int = 20) -> List[Image.Image]:
        """
        Create animated jumping jack demonstration.
        
        Args:
            num_frames: Number of animation frames
            
        Returns:
            List of PIL Images
        """
        frames = []
        
        for frame_num in range(num_frames):
            fig, ax = plt.subplots(1, 1, figsize=(6, 8), dpi=100)
            ax.set_xlim(-1.5, 5.5)
            ax.set_ylim(-1, 8)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Animation progress
            progress = (frame_num % (num_frames // 2)) / (num_frames // 2)
            
            # Ground
            ax.plot([-1.5, 5.5], [0, 0], 'k-', linewidth=3)
            
            center_x = 2
            # Jump height
            center_y = 3 + progress * 1.5
            
            # Head
            head = Circle((center_x, center_y + 1.5), 0.3, color='orange', zorder=10)
            ax.add_patch(head)
            
            # Torso
            ax.plot([center_x, center_x], [center_y + 1.2, center_y - 0.5], 'b-', linewidth=4)
            
            # Arms (raise during jump)
            arm_spread = progress * 1.2
            ax.plot([center_x, center_x - arm_spread], [center_y + 0.8, center_y + 0.8 + arm_spread], 'r-', linewidth=3)
            ax.plot([center_x, center_x + arm_spread], [center_y + 0.8, center_y + 0.8 + arm_spread], 'r-', linewidth=3)
            
            # Legs (spread during jump)
            leg_spread = progress * 0.8
            
            # Left leg
            ax.plot([center_x - 0.2, center_x - 0.3 - leg_spread],
                   [center_y - 0.5, -0.2], 'g-', linewidth=3)
            
            # Right leg
            ax.plot([center_x + 0.2, center_x + 0.3 + leg_spread],
                   [center_y - 0.5, -0.2], 'g-', linewidth=3)
            
            # Text
            ax.text(2, 7, "Jumping Jack Form", ha='center', fontsize=14, weight='bold')
            ax.text(2, 6.5, "Jump & spread legs while raising arms", ha='center', fontsize=10)
            
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
            buf.seek(0)
            frames.append(Image.open(buf).copy())
            plt.close(fig)
        
        return frames


def get_exercise_animation(exercise_name: str, num_frames: int = 20) -> List[Image.Image]:
    """
    Get animation frames for a given exercise.
    
    Args:
        exercise_name: Name of the exercise
        num_frames: Number of animation frames
        
    Returns:
        List of PIL Images for the animation
    """
    exercise_lower = exercise_name.lower()
    
    if "push" in exercise_lower:
        return ExerciseAnimator.create_pushup_animation(num_frames)
    elif "squat" in exercise_lower:
        return ExerciseAnimator.create_squat_animation(num_frames)
    elif "jumping jack" in exercise_lower or "jack" in exercise_lower:
        return ExerciseAnimator.create_jumping_jack_animation(num_frames)
    else:
        # Return a default message
        return None
