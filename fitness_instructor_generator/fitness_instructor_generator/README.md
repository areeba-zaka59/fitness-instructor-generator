# 🏋️ Advanced Fitness Instructor Generator

A sophisticated AI-powered fitness application featuring advanced NLP for personalized workout planning, real-time exercise animations with avatar demonstrations, and pose estimation for form checking.

## ✨ Features

### 🧠 Advanced NLP (Natural Language Processing)
- **Intent Classification**: Uses spaCy for accurate fitness goal detection
- **Entity Extraction**: Intelligently extracts fitness level, duration, equipment, and intensity from natural language input
- **Confidence Scoring**: Provides confidence scores for different fitness intents
- **Body Part Recognition**: Detects which body parts to focus on

### 🎬 Exercise Animations
- **Animated Avatars**: Stick figure demonstrations showing proper exercise form
- **Multiple Exercise Types**: Push-ups, squats, jumping jacks, and more
- **Frame-by-Frame Animation**: Smooth motion demonstrations
- **Real-Time Visualization**: Watch the avatar perform movements

### 📹 Pose Estimation & Form Checking
- **MediaPipe Integration**: Real-time human pose detection
- **Joint Tracking**: Monitors shoulders, elbows, knees, hips alignment
- **Form Feedback**: Provides corrections for improper form
- **Exercise Guides**: Detailed tips for each exercise

### 🎯 Personalization
- **Multiple Fitness Goals**: Weight Loss, Muscle Gain, Flexibility, Cardio, Core Strength
- **Fitness Levels**: Beginner, Intermediate, Advanced
- **Custom Duration**: Adjustable workout lengths
- **Equipment Selection**: Supports home, gym, dumbbells, resistance bands

### 🔊 Voice Feedback
- **Text-to-Speech**: Audio guidance for exercises using pyttsx3
- **Real-Time Timers**: Visual and audio countdown timers

## 🚀 Installation

### Prerequisites
- Python 3.10+
- pip package manager

### Setup

1. **Clone or navigate to the project:**
   ```bash
   cd fitness_instructor_generator
   ```

2. **Create virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate      # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy model (required for advanced NLP):**
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Download NLTK data (required for text preprocessing):**
   ```bash
   python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
   ```

## 🏃 Running the App

### Start the Streamlit Application:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Select Fitness Goal**: Choose from Weight Loss, Muscle Gain, Flexibility, Cardio, or Core Strength

2. **Specify Fitness Level**: Select your current fitness level (Beginner, Intermediate, Advanced)

3. **Provide Preferences** (Optional): Describe your preferences in natural language:
   - "30 minute home workout with dumbbells"
   - "Advanced core training focusing on abs"
   - "Low intensity flexibility and stretching"

4. **Configure Settings**:
   - Enable voice instructions for audio guidance
   - Show exercise animations to see proper form
   - Display form tips and common mistakes
   - Adjust animation speed

5. **Generate Workout**: Click "Generate Advanced Workout Plan"

6. **Review Analysis**: Check NLP analysis to see how the system understood your input

7. **Execute Workout**: 
   - View exercise animations and form guides
   - Click "Start Set" to begin timed exercises
   - Follow the countdown timer
   - Complete rest periods between sets

## 📊 Project Structure

```
fitness_instructor_generator/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── nlp/
│   ├── __init__.py
│   ├── intent_classifier.py        # Basic intent classification
│   ├── entity_extractor.py         # Entity extraction
│   ├── advanced_nlp.py             # spaCy-based advanced NLP
│   └── preprocess.py               # Text preprocessing
├── workout_engine/
│   ├── __init__.py
│   ├── generator.py                # Workout plan generation
│   ├── pose_visualizer.py          # MediaPipe pose estimation
│   └── animator.py                 # Exercise animations
└── audio/
    ├── __init__.py
    └── tts.py                      # Text-to-speech functionality
```

## 🔧 Advanced Features

### Advanced NLP Module (`nlp/advanced_nlp.py`)
- **Intent Classification**: Scores user input against fitness intents
- **Entity Recognition**: Extracts fitness-specific entities like body parts
- **Confidence-Based Recommendations**: Uses scores to refine workout suggestions

### Pose Visualization (`workout_engine/pose_visualizer.py`)
- **PoseVisualizer Class**: Main pose detection and visualization engine
- **Stick Figure Rendering**: Creates matplotlib-based visualizations
- **Angle Estimation**: Calculates joint angles for form analysis
- **Form Feedback**: Provides real-time corrections

### Animation Engine (`workout_engine/animator.py`)
- **ExerciseAnimator Class**: Generates exercise demonstrations
- **Multiple Exercises**: Push-ups, squats, jumping jacks
- **Configurable Frames**: Adjust animation frame count and speed
- **Exercise Guides**: Pre-built guides with form tips

## 💡 Use Cases for Teachers/Trainers

### 1. **Virtual Classroom Instruction**
- Display animations and form guides to students
- Use NLP analysis to understand student fitness goals
- Provide personalized recommendations

### 2. **Online Coaching**
- Students describe their preferences in natural language
- System automatically generates appropriate workouts
- Detailed form checking and corrections

### 3. **Form Analysis**
- Use pose estimation to check student form
- Provide real-time feedback on exercise execution
- Track progress and identify improvement areas

### 4. **Curriculum Development**
- Use the modular structure to create exercise libraries
- Customize animations and guides for specific exercises
- Build progressive training programs

## 🎓 Educational Value

This project demonstrates:
- **Natural Language Processing**: Intent classification and entity extraction
- **Computer Vision**: Pose estimation using MediaPipe
- **Web Application Development**: Streamlit framework
- **Software Architecture**: Modular design with separate NLP, visualization, and animation components
- **Data Visualization**: matplotlib and Pillow for creating visualizations
- **Audio Processing**: pyttsx3 for text-to-speech

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'spacy'"
**Solution**: Ensure spaCy is installed and the model is downloaded:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Issue: "No module named 'mediapipe'"
**Solution**: Install MediaPipe:
```bash
pip install mediapipe
```

### Issue: Text-to-speech not working
**Solution**: pyttsx3 may require system dependencies. On Linux, install:
```bash
sudo apt-get install espeak ffmpeg libespeak1
```

### Issue: Animation not displaying
**Solution**: Ensure matplotlib and Pillow are properly installed:
```bash
pip install --upgrade matplotlib Pillow
```

## 🔐 System Requirements

- **Minimum RAM**: 4GB (for running Streamlit + MediaPipe)
- **Processor**: Dual-core or better
- **Disk Space**: ~2GB (for dependencies and models)
- **Python Version**: 3.10 or higher

## 📝 Example Inputs

Try these natural language inputs for best results:

1. **"I want to lose weight in 30 minutes using dumbbells at home"**
   - Goal: Weight Loss
   - Duration: 30 min
   - Equipment: Dumbbells
   - Type: Home workout

2. **"Advanced 45 minute muscle building session at the gym"**
   - Goal: Muscle Gain
   - Level: Advanced
   - Duration: 45 min
   - Equipment: Gym

3. **"Easy 20 minute yoga and flexibility routine"**
   - Goal: Flexibility
   - Intensity: Low
   - Duration: 20 min
   - Type: Yoga

4. **"High intensity cardio workout, intermediate level"**
   - Goal: Cardio
   - Level: Intermediate
   - Intensity: High

## 🤝 Contributing

Suggestions for enhancements:
- Add more exercise animations
- Implement gesture recognition
- Add workout history and progress tracking
- Create exercise video library
- Implement AI trainer voice
- Add social sharing features

## 📄 License

This project is open source and available for educational purposes.

## 👨‍🏫 For Teachers

**Key Features to Demonstrate**:
1. Show how NLP understands different user descriptions
2. Demonstrate pose estimation accuracy
3. Highlight the modular architecture
4. Explain intent classification confidence scores
5. Show customization possibilities

**Assignment Ideas**:
1. Modify exercises and add new ones
2. Create custom animation styles
3. Implement new exercise guides
4. Add new fitness goals and intents
5. Enhance form checking logic

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments for detailed explanations
3. Examine the project structure for module organization

---

**Created with ❤️ for fitness enthusiasts and educators**
