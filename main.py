#!/usr/bin/python

import cv2
import getopt, sys
import numpy as np
import time

def main(argv):
  password = ""
  channel = 1

  try:
    opts, args = getopt.getopt(argv,"p:c:",["password:channel"])
  except getopt.GetoptError:
    print('main.py -p <password> -c <channel:1-8>')
    sys.exit(2)

  for opt, arg in opts:
    if opt in ('-p', '--password'):
      password = arg
    elif opt in ('-c', '--channel'):
      channel = arg


  if password == '':
    print('missing password. use main.py -p <password>')
    sys.exit(3)

  # stream=0.sdp -> weird format too long not enough wide
  # stream=1.sdp -> small image
  url = 'rtsp://admin:' + password + '@192.168.1.200:554/user=admin_password=' + password + '_channel='+ str(channel) + '_stream=1.sdp'

  record(url, channel)


def record(url, channel):
  cap = cv2.VideoCapture(url)
  cap.set(cv2.CAP_PROP_BUFFERSIZE,1)

  if (cap.isOpened() == False): 
    print("Unable to read camera feed")
    return

  frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  out = cv2.VideoWriter('recording_' + str(channel) +'.avi',cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width,frame_height))

  MAX_SECS = 60 * 60

  startTime = time.time()

  while True:
    currentTime = time.time()

    if currentTime - startTime > MAX_SECS:
      break

    ret, frame = cap.read()

    if ret == True: 
      out.write(frame)
      cv2.imshow('VIDEO',frame)
    else:
      break

    # Press q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  out.release()

  cv2.destroyAllWindows() 

if __name__ == "__main__":
  main(sys.argv[1:])