import cv2
import threading
import time
from playsound import playsound
from moviepy.editor import VideoFileClip

class VedioAndSound(object):
    cap = cv2.VideoCapture("test.mp4")
    # 获取视频基本信息

    fps = int(cap.get(cv2.CAP_PROP_FPS))      # 帧率(秒/帧)
    cfps = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 总帧数
    # fps = cap.get(5)
    #print(f"视频帧率 = {fps},视频总帧数 = {cfps}")

    voide = VideoFileClip("test.mp4")
    voide.audio.write_audiofile("test.mp3")


    # 先播放一秒，如果当前时间对不上，视频就等一下，等音频跟上再继续播放
    def video(self):
        cap = cv2.VideoCapture("test.mp4")
        rate = cap.get(5)  # 读取视频帧率
        startTime = time.time()
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                zhen = cap.get(1)   # 获取当前帧数
                frame = cv2.resize(frame, (1080, 640))
                cv2.imshow('frame', frame)
                cv2.waitKey(1)  # 等待1毫秒 （1秒=1000毫秒）
                sleepTime = zhen/rate - time.time() + startTime
                if sleepTime > 0:  # 播放时间快了就等一下
                    time.sleep(sleepTime)


    def music(self):
        playsound("test.mp3")

show=VedioAndSound()
vd = threading.Thread(target=show.video)
mc = threading.Thread(target=show.music)
vd.start()
mc.start()


