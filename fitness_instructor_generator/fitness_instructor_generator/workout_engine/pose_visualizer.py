"""
Pose estimation and visualization module using MediaPipe.
Detects human poses in images/video and renders exercise form visualization.
"""

import mediapipe as mp
import cv2
import numpy as np
from typing import Tuple, List, Optional
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import io
from PIL import Image


class PoseVisualizer:
    """Visualize human poses and exercise forms using MediaPipe."""
    
    def __init__(self):
        """Initialize MediaPipe pose detector."""
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
    def detect_pose(self, image: np.ndarray) -> Tuple[np.ndarray, Optional[object]]:
        """
        Detect pose landmarks in an image.
        
        Args:
            image: Input image as numpy array (BGR format)
            
        Returns:
            Tuple of (processed_image, pose_results)
        """
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)
        
        # Draw pose landmarks on image
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                self.mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
            )
        
        return image, results
    
    def create_stick_figure(self, landmarks, image_width: int = 400, image_height: int = 600) -> Image.Image:
        """
        Create a stick figure visualization from pose landmarks.
        
        Args:
            landmarks: MediaPipe landmarks object
            image_width: Width of output image
            image_height: Height of output image
            
        Returns:
            PIL Image of stick figure
        """
        fig, ax = plt.subplots(1, 1, figsize=(6, 8), dpi=100)
        ax.set_xlim(0, image_width)
        ax.set_ylim(image_height, 0)
        ax.set_aspect('equal')
        ax.axis('off')
        
        if landmarks is None:
            ax.text(image_width//2, image_height//2, "No pose detected", 
                   ha='center', va='center', fontsize=14)
        else:
            # Draw connections (skeleton)
            connections = [
                (11, 13), (13, 15),  # Left arm
                (12, 14), (14, 16),  # Right arm
                (11, 12),  # Shoulders
                (11, 23), (12, 24),  # Torso
                (23, 25), (25, 27),  # Left leg
                (24, 26), (26, 28),  # Right leg
                (23, 24),  # Hips
            ]
            
            for connection in connections:
                idx1, idx2 = connection
                if idx1 < len(landmarks) and idx2 < len(landmarks):
                    x1 = landmarks[idx1].x * image_width
                    y1 = landmarks[idx1].y * image_height
                    x2 = landmarks[idx2].x * image_width
                    y2 = landmarks[idx2].y * image_height
                    
                    if landmarks[idx1].visibility > 0.3 and landmarks[idx2].visibility > 0.3:
                        ax.plot([x1, x2], [y1, y2], 'b-', linewidth=2)
            
            # Draw joints as circles
            for idx, landmark in enumerate(landmarks):
                if landmark.visibility > 0.3:
                    x = landmark.x * image_width
                    y = landmark.y * image_height
                    circle = Circle((x, y), 4, color='red', zorder=10)
                    ax.add_patch(circle)
        
        # Convert matplotlib figure to PIL Image
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
        buf.seek(0)
        img = Image.open(buf)
        plt.close(fig)
        
        return img
    
    def estimate_angle(self, point_a, point_b, point_c) -> float:
        """
        Calculate angle between three points (for form checking).
        
        Args:
            point_a, point_b, point_c: Landmark objects from MediaPipe
            
        Returns:
            Angle in degrees
        """
        a = np.array([point_a.x, point_a.y])
        b = np.array([point_b.x, point_b.y])
        c = np.array([point_c.x, point_c.y])
        
        ba = a - b
        bc = c - b
        
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
        cosine_angle = np.clip(cosine_angle, -1.0, 1.0)
        angle = np.arccos(cosine_angle)
        
        return np.degrees(angle)
    
    def check_form(self, landmarks) -> dict:
        """
        Basic form checking for common exercises.
        
        Args:
            landmarks: MediaPipe landmarks
            
        Returns:
            Dictionary with form feedback
        """
        feedback = {
            "posture": "good",
            "alignment": "good",
            "depth": "good",
            "issues": []
        }
        
        if landmarks is None:
            return feedback
        
        try:
            # Check shoulder alignment (landmarks 11, 12)
            left_shoulder = landmarks[11]
            right_shoulder = landmarks[12]
            
            if abs(left_shoulder.y - right_shoulder.y) > 0.05:
                feedback["issues"].append("Uneven shoulders - keep them level")
                feedback["posture"] = "needs_correction"
            
            # Check back alignment (using hip landmarks 23, 24)
            left_hip = landmarks[23]
            right_hip = landmarks[24]
            
            if abs(left_hip.y - right_hip.y) > 0.08:
                feedback["issues"].append("Hips are not level - maintain stability")
                feedback["alignment"] = "needs_correction"
            
        except (IndexError, AttributeError):
            pass
        
        return feedback
    
    def __del__(self):
        """Cleanup resources."""
        if hasattr(self, 'pose'):
            self.pose.close()


def create_exercise_guide(exercise_name: str) -> dict:
    """
    Create exercise guides with form tips and pose requirements.
    
    Args:
        exercise_name: Name of the exercise
        
    Returns:
        Dictionary with exercise guide information
    """
    guides = {
        "Push-up": {
            "description": "Upper body strength exercise",
            "key_joints": [11, 12, 13, 14, 15, 16],  # Shoulders, elbows, wrists
            "target_angles": {
                "elbow": (45, 90),  # Elbow should bend 45-90 degrees
                "shoulder": (45, 180),
            },
            "form_tips": [
                "Keep your body in a straight line",
                "Lower until your chest nearly touches the ground",
                "Keep elbows close to your body",
                "Maintain neutral head position"
            ],
            "common_mistakes": [
                "Sagging hips",
                "Elbows flared out too wide",
                "Head dropping forward",
                "Incomplete range of motion"
            ]
        },
        "Squat": {
            "description": "Lower body strength exercise",
            "key_joints": [23, 24, 25, 26, 27, 28],  # Hips, knees, ankles
            "target_angles": {
                "knee": (70, 90),
                "hip": (45, 90),
            },
            "form_tips": [
                "Feet shoulder-width apart",
                "Keep chest up and back straight",
                "Knees should track over toes",
                "Lower until thighs are parallel to ground"
            ],
            "common_mistakes": [
                "Knees caving inward",
                "Leaning too far forward",
                "Incomplete depth",
                "Heels lifting off ground"
            ]
        },
        "Plank": {
            "description": "Core stability exercise",
            "key_joints": [11, 12, 23, 24, 25, 26],  # Shoulders, hips, knees
            "form_tips": [
                "Body should form a straight line",
                "Engage your core",
                "Don't let hips sag",
                "Keep shoulders directly over wrists"
            ],
            "common_mistakes": [
                "Hips sagging or raised",
                "Shoulders not aligned",
                "Neck strain",
                "Shallow core engagement"
            ]
        },
        "Jumping Jack": {
            "description": "Full body cardio exercise",
            "key_joints": [11, 12, 13, 14, 15, 16, 23, 24],
            "form_tips": [
                "Start with feet together",
                "Jump while spreading legs and raising arms",
                "Land softly on the balls of your feet",
                "Return to starting position"
            ]
        }
    }
    
    return guides.get(exercise_name, {
        "description": exercise_name,
        "form_tips": ["Maintain proper form", "Control your movements", "Breathe steadily"],
        "common_mistakes": ["Poor form", "Moving too quickly"]
    })
