# Sauron

A one place to look into all the cameras at home.
*Because the propietary software sucks*

## Using

Install `requirements.txt` also [install openCV](https://docs.opencv.org/4.x/d5/de5/tutorial_py_setup_in_windows.html)
I tested most of it on windows for convenience, should work in linux without much problem

## Server

There's a small server so I don't need to use the NVR propietary software.

	python server.py -p <password>

This will open a very simple UI with all the cameras

## Recording

If you want to record a camera you can use the main file

	python main.py -p <password> -c 2

This will record a max of 60m of the given channel or until you close the screen.

The file will be saved on the root as `recording_<channel>.avi`
Note: using avi since I found some issues on mp4 recording with python-windows...

## Gear

I'm using a CCTV by FLOUREON with 8 channels.
Cameras are exposed via rtsp via the CCTV.

CCTV has a few features like recording, motion detection and other things.
But all of them are shit so I built better features on top of it

## Resources used
https://medium.com/analytics-vidhya/detecting-objects-on-ip-camera-video-with-tensorflow-and-opencv-e2c25297a75a
https://studymachinelearning.com/stream-cctv-ip-camera-rtsp-feed-into-aws-kinesis-video-streams/
https://www.youtube.com/watch?v=yqkISICHH-U&ab_channel=NicholasRenotte
https://blog.miguelgrinberg.com/post/video-streaming-with-flask