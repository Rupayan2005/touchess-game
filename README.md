# SnakeVision - Touchless Snake Game 🐍

A modern implementation of the classic Snake game featuring computer vision-based gesture control. Experience hands-free gaming using advanced hand tracking technology powered by MediaPipe and OpenCV.

## 🎯 Overview

This project combines traditional arcade gaming with cutting-edge computer vision technology to create an immersive, touchless gaming experience. The game features smooth animations, particle effects, and dual control modes for both traditional keyboard and gesture-based interaction.

## ✨ Key Features

### Core Gameplay
- **Touchless Control**: Play using hand gestures captured via webcam
- **Dual Input Modes**: Seamlessly switch between keyboard and gesture controls
- **Performance Optimization**: Smooth 60 FPS gameplay with efficient rendering
- **Persistent Storage**: High scores saved locally with automatic session management

### Visual Experience
- **Modern UI Design**: Clean, minimalist interface with smooth animations
- **Particle Effects**: Dynamic visual effects for enhanced gameplay experience
- **Responsive Design**: Optimized for various screen resolutions
- **Performance Toggles**: Adjustable visual effects for optimal performance

### Technical Implementation
- **Real-time Hand Tracking**: MediaPipe-powered gesture recognition
- **Efficient Particle System**: Optimized rendering for smooth performance
- **Input Buffering**: Responsive controls with minimal latency
- **Gesture Smoothing**: Advanced filtering for accurate gesture detection

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Webcam (for gesture control)
- Operating System: Windows, macOS, or Linux

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/geothermal-1408/touchless-snake-game.git
   cd touchless-snake-game
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

## 🎮 Controls & Usage

### Keyboard Controls
| Key | Action |
|-----|--------|
| `↑` `↓` `←` `→` | Move snake |
| `G` | Toggle gesture control |
| `Space` | Restart game (when game over) |
| `ESC` | Exit application |

### Gesture Controls
| Gesture | Action |
|---------|--------|
| Swipe Up | Move snake up |
| Swipe Down | Move snake down |
| Swipe Left | Move snake left |
| Swipe Right | Move snake right |
| `ESC` (camera window) | Close camera view |

### Getting Started
1. Launch the application using `python app.py`
2. Use arrow keys to control the snake initially
3. Press `G` to activate gesture control mode
4. Position your hand in front of the webcam
5. Use clear, deliberate finger swipes to control the snake
6. Collect food items while avoiding the snake's body

## 🔧 Technical Architecture

### Core Components
- **Game Engine**: Built on Pygame framework for cross-platform compatibility
- **Computer Vision**: MediaPipe integration for real-time hand landmark detection
- **Input Processing**: Multi-threaded input handling for responsive gameplay
- **Graphics Rendering**: Efficient sprite management and particle system

### Performance Optimizations
- Frame rate capping at 60 FPS for consistent gameplay
- Efficient collision detection algorithms
- Optimized particle rendering with object pooling
- Memory-efficient score persistence

## 📋 Dependencies

Core dependencies are listed in `requirements.txt`:

```
pygame>=2.0.0
opencv-python>=4.5.0
mediapipe>=0.8.0
numpy>=1.20.0
```

## 🛠️ Configuration

### Camera Settings
- Default camera index: 0 (adjustable in source code)
- Minimum resolution: 640x480
- Recommended lighting: Well-lit environment for optimal gesture recognition

### Performance Settings
- Visual effects can be toggled for performance optimization
- Particle count automatically adjusts based on system performance
- Frame rate limiting ensures consistent gameplay across different hardware

## 🐛 Troubleshooting

### Common Issues

**Camera Not Detected**
- Ensure webcam is connected and not in use by other applications
- Check camera permissions in your operating system
- Try different camera indices if multiple cameras are available

**Poor Gesture Recognition**
- Ensure adequate lighting in the environment
- Keep hand clearly visible within camera frame
- Maintain appropriate distance from camera (arm's length)
- Avoid cluttered backgrounds

**Performance Issues**
- Close other resource-intensive applications
- Ensure adequate system resources are available

**Installation Problems**
- Verify Python version compatibility (3.7+)
- Use virtual environment for dependency isolation
- Check system-specific installation requirements for OpenCV

## 📊 System Requirements

### Minimum Requirements
- CPU: Dual-core processor, 2.0 GHz
- RAM: 4 GB
- Storage: 100 MB available space
- Camera: USB webcam or built-in camera
- Python: 3.7+

### Recommended Requirements
- CPU: Quad-core processor, 2.5 GHz or higher
- RAM: 8 GB or more
- Storage: 500 MB available space
- Camera: HD webcam for optimal gesture recognition
- Python: 3.8+

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Getting Started
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation as needed
- Ensure compatibility with existing functionality

### Areas for Contribution
- Additional gesture recognition patterns
- Performance optimizations
- New visual effects and themes
- Cross-platform compatibility improvements
- Documentation enhancements

## 📝 License

This project is licensed under the BSD-2-Clause License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MediaPipe**: Google's framework for building perception pipelines
- **OpenCV**: Open source computer vision library
- **Pygame**: Cross-platform set of Python modules designed for writing video games
- **NumPy**: Fundamental package for scientific computing with Python

## 📞 Support

For support, feature requests, or bug reports:
- Create an issue on GitHub
- Check existing issues for similar problems
- Provide detailed information about your environment and the issue


---

**Made with ❤️ by Geothermal and Shadow**
