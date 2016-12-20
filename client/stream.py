import subprocess
import sys
import cv2
import urllib2
import requests
import urllib
import json

cam = cv2.VideoCapture(0)
cam_width = cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
cam_height = cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
cam.release()
streamer_name = sys.argv[1]

ip = "46.101.172.142"

resuls = subprocess.Popen(['xrandr'],stdout=subprocess.PIPE).communicate()[0].split("current")[1].split(",")[0]
w = resuls.split("x")[0].strip()
h = resuls.split("x")[1].strip()

screen_width = int(w)
screen_height = int(h)

screen="""ffmpeg -f x11grab -s %dx%d -framerate 15 -i :0.0 \\
    -c:v libx264 -preset fast -pix_fmt yuv420p -s %dx%d \\
    -threads 0 -f flv \"rtmp://%s/live/%s.sdp\" """

camera = """ffmpeg -f v4l2  -framerate 15 -video_size %dx%d -i /dev/video0 \\
    -c:v libx264 -preset fast -pix_fmt yuv420p -s %dx%d \\
    -threads 0 -f flv \"rtmp://%s/live/%s.sdp\" """

screen_low = screen%(screen_width,screen_height,screen_width/4,screen_height/4,ip,streamer_name+"-sl")
screen_high = screen%(screen_width,screen_height,screen_width/2,screen_height/2,ip,streamer_name+"-sh")

camera_low = camera%(cam_width,cam_height,cam_width/4,cam_height/4,ip,streamer_name+"-cl")
camera_high = camera%(cam_width,cam_height,cam_width/2,cam_height/2,ip,streamer_name+"-ch")

print screen_low
print screen_high
print camera_low
print camera_high

# subprocess.Popen(camera_high,shell=True)
# subprocess.Popen(camera_low,shell=True)
# subprocess.Popen(screen_low,shell=True)
# subprocess.Popen(screen_high,shell=True)

streamer_channels = {
    'cl' : camera_low,
    'ch' : camera_high,
    'sl' : screen_low,
    'sh' : screen_high
}

screen_dict = {
    'name' : streamer_name,
    'channels' : streamer_channels
}

url = ("http://"+ip+":8000/init_stream")
# req.add_header('Content-Type','application/json')
# resp = urllib2.urlopen(req,json.dumps(screen_dict))
#r = urllib2.urlopen(req)
r = requests.post(url, json=screen_dict)
print r.status_code
# print r.read()
