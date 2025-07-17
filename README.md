# Modern Touchless Snake Game 🐍

A smooth, modern Snake game with gesture control using computer vision. Play the classic game with your hands—no keyboard required!

## ✨ Features

- Touchless gesture control using your webcam
- Modern visual effects and smooth animations
- Keyboard and gesture dual control modes
- Persistent high scores
- Toggleable visual effects for performance

## 🎮 Controls

**Keyboard:**

- Arrow keys or WASD: Move the snake
- G: Toggle gesture control
- E: Toggle visual effects
- Space: Restart (when game over)

**Gesture:**

- Swipe Up/Down/Left/Right with your index finger
- ESC (in camera window): Close camera view

## 🚀 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/geothermal-1408/touchess-game.git
   cd touchess-game
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the game:
   ```sh
   python app.py
   ```

## 📋 Requirements

- Python 3.7+
- Webcam
- Dependencies in `requirements.txt`:
  - pygame
  - opencv-python
  - mediapipe
  - numpy

## 🎯 How to Play

1. Run the game with `python app.py`
2. Use arrow keys to control the snake
3. Press G to enable gesture control
4. Swipe with your index finger to move the snake
5. Eat the food, avoid walls and yourself

## 🔧 Technical Features

- Efficient particle system
- Frame rate capping for smooth 60 FPS
- Input buffering for responsive controls
- MediaPipe hand tracking
- Smoothed gesture detection

## 🐛 Troubleshooting

- Camera not working: Ensure your webcam is connected and not used by other apps
- Poor gesture recognition: Use good lighting and keep your hand visible
- Low performance: Press E to disable effects

## 📝 License

BSD-2-Clause License

## 🤝 Contributing

Contributions welcome! Submit a Pull Request.
