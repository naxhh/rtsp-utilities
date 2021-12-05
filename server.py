#!/usr/bin/python
from flask import Flask, render_template, Response, request
import cv2
import getopt, sys

app = Flask(__name__)
password = ""

def main(argv):
  global password
  try:
    opts, args = getopt.getopt(argv,"p:",["password"])
  except getopt.GetoptError:
    print('main.py -p <password>')
    sys.exit(2)

  for opt, arg in opts:
    if opt in ('-p', '--password'):
      password = arg

  if password == '':
    print('missing password. use main.py -p <password>')
    sys.exit(3)

  app.run(host='0.0.0.0', threaded=True)
  


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video_feed')
def video_feed():
  channel = request.args.get('channel')
  return Response(gen(channel), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(channel):
  while True:
    for frame in get_frame(channel):
      yield (b'--frame\r\n'
             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def get_frame(channel):
  # stream=0.sdp -> weird format too long not enough wide
  # stream=1.sdp -> small image
  url = 'rtsp://admin:' + password + '@192.168.1.200:554/user=admin_password=' + password + '_channel='+ str(channel) + '_stream=1.sdp'

  camera = cv2.VideoCapture(url)

  if not camera.isOpened():
    raise RuntimeError('Could not start camera ' + str(channel))

  while True:
    # read current frame
    _, img = camera.read()

    # encode as a jpeg image and return it
    yield cv2.imencode('.jpg', img)[1].tobytes()


if __name__ == '__main__':
  main(sys.argv[1:])
