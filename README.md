
# 🧠 AI-Based Smart Presentation System

A smart Python-powered project designed for semi-automated multimedia presentations. This system allows users to switch seamlessly between slide presentations and media content, leveraging a web-based interface. Ideal for smart classrooms, seminars, or automated teaching environments.

---

## 🎥 Demo Video

https://user-images.githubusercontent.com/demo-video-link/sample.mp4  
> 📌 *(Replace with your actual uploaded video GitHub link)*

---

## 🚀 Features

- 📽️ **Media Playback Module** – Play audio/video files with custom control.
- 📊 **Presentation Viewer** – Automatically display slides from a folder.
- 🧠 **AI-Driven Interface** – Uses Python logic to seamlessly switch between media types.
- 🖥️ **Web Interface** – Launch and control everything from a browser using Flask.
- 📂 **Modular Code** – Well-structured Python scripts for extensibility.

---

## 🗃️ Folder Structure

```
Hand_Gesture /
├── app.py                            # Main app controller
├── MediaPlayer/
│   └── Main2.py                      # Media player logic
├── PPT/
│   ├── Main1.py                      # Presentation handler
│   ├── Presentation/
│   │   ├── 1.png                     # Slide 1
│   │   └── ...                       # More slides
│   └── templates/
│       └── index1.html              # Web template for PPT
├── templates/
│   └── index.html                    # Flask HTML template
└── .vscode/
    └── launch.json                   # IDE config
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Core language |
| **Flask** | Web server for presentation interface |
| **OpenCV** | (optional) could be used for camera or frame handling |
| **HTML/CSS** | Frontend for web interface |
| **VS Code** | Project development environment |

---

## 📦 Requirements

Create a `requirements.txt` file with the following content:

```
Flask==2.2.5
opencv-python==4.10.0.0
Werkzeug==2.2.3
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🖥️ How to Run

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/smart-presentation-system.git
   cd smart-presentation-system
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**  
   ```bash
   python app.py
   ```

4. **Open in Browser**  
   Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)


## 📚 Use Cases

- Smart Classrooms
- AI-Integrated Seminars
- Hands-free Presentation Control
- Remote Learning Environments

---

## 📌 Future Enhancements

- Integrate voice commands for slide navigation
- Add gesture-based control using a webcam
- Cloud sync for presentations and media
