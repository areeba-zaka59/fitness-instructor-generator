import streamlit.components.v1 as components

class JSAnimationEngine:
    """JavaScript-based exercise animation engine with REAL video demonstrations"""
    
    # Dictionary of YouTube video URLs for each exercise
    EXERCISE_VIDEOS = {
        "squat": "https://www.youtube.com/embed/aclHkVaku9U",
        "push": "https://www.youtube.com/embed/IODxDxX7oi4",
        "push-up": "https://www.youtube.com/embed/IODxDxX7oi4",
        "lunge": "https://www.youtube.com/embed/QOVaHwm-Q6U",
        "plank": "https://www.youtube.com/embed/pSHjTRCQxIw",
        "jumping": "https://www.youtube.com/embed/c4DAnQ6DtF8",
        "jack": "https://www.youtube.com/embed/c4DAnQ6DtF8",
        "sit": "https://www.youtube.com/embed/jDwoBpPH2HA",
        "burpee": "https://www.youtube.com/embed/TU8QYVW0gDU",
        "mountain": "https://www.youtube.com/embed/AMy3hxLGROA",
        "climber": "https://www.youtube.com/embed/AMy3hxLGROA",
        "curl": "https://www.youtube.com/embed/ykJmrZ5v0Oo",
        "bicep": "https://www.youtube.com/embed/ykJmrZ5v0Oo",
    }
    
    @staticmethod
    def get_animation_code(exercise_type: str, speed: float = 1.0, color: str = "#4CAF50"):
        """Return HTML/JS code for specific exercise with REAL videos"""
        
        exercise_type = exercise_type.lower()
        
        # Find matching video
        video_url = None
        for key, url in JSAnimationEngine.EXERCISE_VIDEOS.items():
            if key in exercise_type:
                video_url = url
                break
        
        if video_url:
            return JSAnimationEngine._video_animation(video_url, exercise_type, speed)
        else:
            return JSAnimationEngine._default_animation(color, speed)
    
    @staticmethod
    def _video_animation(video_url: str, exercise_name: str, speed: float):
        """Embed real exercise video from YouTube - MUTED by default, plays only when visible"""
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                .video-card {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 20px;
                    padding: 15px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                }}
                .video-container {{
                    position: relative;
                    width: 100%;
                    border-radius: 15px;
                    overflow: hidden;
                    background: #000;
                }}
                .video-container iframe {{
                    width: 100%;
                    height: 320px;
                    border: none;
                }}
                .exercise-title {{
                    text-align: center;
                    font-size: 20px;
                    font-weight: bold;
                    margin-top: 12px;
                    margin-bottom: 5px;
                    color: white;
                }}
                .instruction {{
                    text-align: center;
                    font-size: 13px;
                    color: #e0e0e0;
                    margin-bottom: 5px;
                }}
                .badge {{
                    display: inline-block;
                    background: #ff6b6b;
                    color: white;
                    padding: 3px 10px;
                    border-radius: 20px;
                    font-size: 11px;
                    margin-top: 8px;
                }}
                .sound-warning {{
                    text-align: center;
                    font-size: 12px;
                    color: #FFD700;
                    margin-top: 8px;
                    padding: 5px;
                    background: rgba(0,0,0,0.3);
                    border-radius: 10px;
                }}
                .sound-btn {{
                    background: #4CAF50;
                    color: white;
                    border: none;
                    padding: 5px 12px;
                    border-radius: 20px;
                    cursor: pointer;
                    font-size: 12px;
                    margin-left: 10px;
                }}
                .sound-btn:hover {{
                    background: #45a049;
                }}
            </style>
        </head>
        <body>
            <div class="video-card">
                <div class="video-container">
                    <iframe 
                        id="exercise-video-{hash(exercise_name)}"
                        src="{video_url}?autoplay=0&mute=1&controls=1&modestbranding=1&rel=0"
                        title="{exercise_name} demonstration"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                <div class="exercise-title">
                    🏋️‍♀️ {exercise_name.title()}
                </div>
                <div class="instruction">
                    👆 Click PLAY to start | 🔇 Video starts muted to prevent overlapping audio
                </div>
                <div class="sound-warning">
                    🔊 <strong>Tip:</strong> Click the volume icon on the video to unmute when you're ready!
                    <button class="sound-btn" onclick="document.getElementById('exercise-video-{hash(exercise_name)}').contentWindow.postMessage('{{"event":"command","func":"unMute","args":[]}}', '*')">
                        🔊 Unmute Video
                    </button>
                </div>
                <div style="text-align: center;">
                    <span class="badge">💪 Follow Along</span>
                    <span class="badge">🎯 Perfect Form</span>
                    <span class="badge">🔇 Click to Unmute</span>
                </div>
            </div>
        </body>
        </html>
        '''
    
    @staticmethod
    def _default_animation(color: str, speed: float):
        """Default animation when no video is found"""
        return f'''
        <!DOCTYPE html>
        <html>
        <body>
            <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #667eea 20%, #764ba2 100%); border-radius: 20px;">
                <div style="font-size: 60px; margin-bottom: 15px;">🏋️‍♀️</div>
                <div style="font-size: 22px; color: white; font-weight: bold;">Exercise Demonstration</div>
                <div style="font-size: 14px; color: #e0e0e0; margin-top: 10px;">Click play below to watch proper form!</div>
                <div style="margin-top: 20px;">
                    <div style="width: 80px; height: 3px; background: white; margin: 0 auto; border-radius: 2px;"></div>
                </div>
            </div>
        </body>
        </html>
        '''