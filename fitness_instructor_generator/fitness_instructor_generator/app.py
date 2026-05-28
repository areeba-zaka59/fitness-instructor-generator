import streamlit as st
import time
from pathlib import Path
from animation.animation_engine import JSAnimationEngine
from nlp.intent_classifier import classify_intent
from nlp.entity_extractor import extract_entities
from workout_engine.generator import generate_workout
from workout_engine.pose_visualizer import create_exercise_guide
from workout_engine.detailed_animator import DetailedExerciseAnimator, get_exercise_narration
from workout_engine.nutrition import get_nutrition_plan, get_weekly_meal_plan, get_macro_targets
from audio.narrator import ExerciseNarrator

def display_js_animation(exercise_name: str, intensity: str = "medium"):
    speed_map = {"low": 0.8, "medium": 1.0, "high": 1.5}
    speed = speed_map.get(intensity.lower(), 1.0)
    color_map = {"low": "#4CAF50", "medium": "#2196F3", "high": "#FF5722"}
    color = color_map.get(intensity.lower(), "#4CAF50")
    html_code = JSAnimationEngine.get_animation_code(exercise_name, speed, color)
    st.components.v1.html(html_code, height=350)

st.set_page_config(page_title="Fitness Instructor Generator", layout="wide")

st.markdown("""
<style>
    .header-style {
        color: #FF6B6B;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subheader-style {
        color: #4ECDC4;
        text-align: center;
        font-size: 1.2em;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header-style">🏋️‍♀️ Fitness Instructor Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader-style">AI-Powered Personalized Workout Plans with Avatar Animation</div>', unsafe_allow_html=True)
st.write("")

with st.sidebar:
    st.header("⚙️ Settings")
    enable_voice = st.checkbox("🔊 Enable voice guidance", value=False)
    show_avatar_animation = st.checkbox("🎬 Show avatar animations", value=True)
    show_nutrition = st.checkbox("🥗 Show nutrition tips", value=True)
    show_form_tips = st.checkbox("📋 Show form tips", value=True)
    animation_speed = st.slider("⚡ Animation Speed", 0.5, 2.0, 1.0, 0.1)

col1, col2 = st.columns(2)

with col1:
    goal = st.radio(
        "🎯 Select your fitness goal:",
        ("Weight Loss", "Muscle Gain", "Flexibility", "Cardio", "Core Strength")
    )

with col2:
    fitness_level = st.radio(
        "💪 Your fitness level:",
        ("Beginner", "Intermediate", "Advanced")
    )

user_input = st.text_area(
    "📝 Describe your preference (optional):",
    placeholder="e.g., 30 minute home workout with dumbbells",
    height=80
)

if st.button("🚀 Generate Personalized Workout Plan"):
    
    entities = {}
    
    if goal == "Weight Loss":
        entities["goal"] = "weight_loss"
    elif goal == "Muscle Gain":
        entities["goal"] = "muscle_gain"
    elif goal == "Flexibility":
        entities["goal"] = "flexibility"
    elif goal == "Cardio":
        entities["goal"] = "cardio"
    elif goal == "Core Strength":
        entities["goal"] = "core"
    
    if fitness_level == "Beginner":
        entities["fitness_level"] = "beginner"
    elif fitness_level == "Intermediate":
        entities["fitness_level"] = "intermediate"
    else:
        entities["fitness_level"] = "advanced"
    
    workout_plan = generate_workout(entities)
    
    if not workout_plan:
        workout_plan = [
            {"name": "Push-up", "sets": 3, "type": "reps", "value": 10, "rest": 30},
            {"name": "Squat", "sets": 3, "type": "reps", "value": 12, "rest": 30},
            {"name": "Plank", "sets": 3, "type": "time", "value": 20, "rest": 30}
        ]
    
    st.divider()
    st.header("🔥 Your Personalized Workout Plan")
    
    for ex_idx, exercise in enumerate(workout_plan, 1):
        st.markdown(f"### 💪 Exercise {ex_idx}: {exercise['name']}")
        
        if show_avatar_animation:
            with st.expander(f"📹 Watch {exercise['name']} - Avatar Demo", expanded=True):
                st.write("**Live Exercise Animation:**")
                intensity = entities.get("intensity", "medium")
                display_js_animation(exercise["name"], intensity)
        
        with st.expander(f"📋 How to do {exercise['name']}", expanded=False):
            narration_data = get_exercise_narration(exercise["name"])
            st.write(narration_data.get('intro', 'Follow the steps below.'))
        
        if show_form_tips:
            with st.expander(f"💡 Form Tips for {exercise['name']}", expanded=False):
                guide = create_exercise_guide(exercise["name"])
                if "form_tips" in guide:
                    for tip in guide["form_tips"]:
                        st.write(f"✓ {tip}")
        
        st.write(f"**Sets:** {exercise['sets']} | **Rest:** {exercise['rest']}s")
        st.divider()
    
    if show_nutrition:
        st.header("🥗 Nutrition & Diet Plan")
        nutrition_plan = get_nutrition_plan(entities.get("goal", "weight_loss"), entities.get("fitness_level", "beginner"))
        st.subheader(f"📋 {nutrition_plan['name']}")
        st.write(f"**Focus:** {nutrition_plan['calorie_focus'].title()}")
        
        with st.expander("💡 Daily Nutrition Tips", expanded=True):
            for tip in nutrition_plan["daily_tips"]:
                st.write(f"• {tip}")
        
        with st.expander("📊 Daily Macro Targets"):
            macros = get_macro_targets(entities.get("goal", "weight_loss"), daily_calories=2000)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🥩 Protein (g)", f"{macros['protein_grams']:.0f}g")
            with col2:
                st.metric("🌾 Carbs (g)", f"{macros['carbs_grams']:.0f}g")
            with col3:
                st.metric("🥑 Fats (g)", f"{macros['fats_grams']:.0f}g")
        
        with st.expander("📅 7-Day Meal Plan"):
            weekly_plan = get_weekly_meal_plan(entities.get("goal", "weight_loss"))
            for day_plan in weekly_plan:
                st.write(f"**Day {day_plan['day']}:**")
                st.write(f"  🌅 Breakfast: {day_plan['breakfast']}")
                st.write(f"  🍽️ Lunch: {day_plan['lunch']}")
                st.write(f"  🌙 Dinner: {day_plan['dinner']}")
                st.write(f"  🥤 Snack: {day_plan['snack']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"💧 **Hydration:** {nutrition_plan['hydration']}")
        with col2:
            st.info(f"⏰ **Meal Timing:** {nutrition_plan['timing']}")
    
    st.success("🎉 Workout Plan Complete! Good luck with your training!")