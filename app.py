from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process')
def process():
    # Your Python code here
    mask = 'L:\project\ParkPro\mask_1920_1080.png'
    video_path = 'L:\project\ParkPro\parking_1920_1080.mp4'

    # ... (the rest of your Python code)

    return "Process completed"  # Return a message to display on the webpage


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080")
