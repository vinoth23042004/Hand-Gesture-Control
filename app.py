from flask import Flask, redirect, request
import subprocess
import os

app = Flask(__name__)

# Process handles to subprocesses
main1_process = None
main2_process = None

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buttons</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-image: url('https://giffiles.alphacoders.com/221/221517.gif');
            background-size: cover;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            margin: 10px;
            cursor: pointer;
            border-radius: 5px;
        }

        .button:hover {
            background-color: #45a049;
        }
    </style>
    <script>
        document.addEventListener('keydown', function(event) {
            if (event.key === 'q') {
                event.preventDefault();
                fetch('/turn_off_webcam', { method: 'POST' });
            }
        });
    </script>
    </head>
    <body>

    <div class="container">
        <a href="/presentation" class="button" target="_blank">Presentation</a>
        <a href="/media_player" class="button">Media Player</a>
    </div>

    </body>
    </html>
    """

@app.route('/presentation')
def presentation():
    global main1_process
    # Start Main1.py subprocess if it's not running
    if main1_process is None or main1_process.poll() is not None:
        main1_process = subprocess.Popen(["python", "D:/Sem Project/PPT/Main1.py"])
    return redirect("http://127.0.0.1:5002/", code=302)

@app.route('/media_player')
def media_player():
    global main1_process, main2_process
    # Stop Main1.py if it's running
    if main1_process and main1_process.poll() is None:
        main1_process.terminate()
        try:
            main1_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            main1_process.kill()
            main1_process.wait()
    # Start Main2.py
    if main2_process is None or main2_process.poll() is not None:
        main2_process = subprocess.Popen(["python", "D:/Sem Project/MediaPlayer/Main2.py"])
    # Redirect to YouTube
    return redirect("https://www.youtube.com", code=302)

@app.route('/turn_off_webcam', methods=['POST'])
def turn_off_webcam():
    # Add code here to turn off the webcam
    # For example, you can use subprocess to call a script or command to turn off the webcam
    # Example: subprocess.run(["command_to_turn_off_webcam"])
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
