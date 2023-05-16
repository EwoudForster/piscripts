from flask import Flask, render_template, request, redirect, Response
import cv2
import time
import wiringpi
import sys

app = Flask(__name__)
new_status = ""

@app.route('/')
def index():
    # Importing here to avoid circular import
    import OwnProject
    current_status = OwnProject.checkstatus()
    templateData = {'current_status': current_status}
    return render_template('index.html', **templateData)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/reset')
def reset():
    global new_status
    new_status = "reset"
    return redirect('/')

@app.route('/close')
def close():
    global new_status
    new_status = "close"
    return redirect('/')

@app.route('/arm')
def arm():
    global new_status
    new_status = "arm"
    return redirect('/')

def deploy():
    app.run(host='0.0.0.0', port=8080, threaded=True)


def checkstatus():
    global new_status
    return new_status

def generate_frames():
    camera = cv2.VideoCapture(1)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()

