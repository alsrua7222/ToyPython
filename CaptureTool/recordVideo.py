from tkinter import *
from PIL import ImageGrab
from Func import * # 사용자 함수
import cv2
import datetime
import time
import numpy as np
import keyboard

class recordVideo:
    def __init__(self, key="space"):
        self.isRecording = False
        self.output = None
        self.ButtonKey = key
        return

    def getFileName(self):
        return "Record_" + getDateTimeCurrent()

    def getFramerate(self, point):
        sum = 0
        for i in range(11):
            last_time = time.time()
            frame = cv2.cvtColor(np.array(ImageGrab.grab(bbox=point)), cv2.COLOR_BGR2RGB)
            cv2.waitKey(1)
            
            if not i == 0: # 첫 프레임은 불안정하기 때문에 제외.
                sum += 1 / (time.time() - last_time)
        return sum / 10
    
    def StartRecord(self, root: Tk, point):
        if self.isRecording:
            return
        root.wm_attributes("-topmost", True)
        width = point[2] - point[0]
        height = point[3] - point[1]
        codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        frame_rate = self.getFramerate(point)

        self.output = cv2.VideoWriter(self.getFileName() + ".mp4", codec, frame_rate, (width, height))

        while self.output.isOpened():
            img = ImageGrab.grab(bbox=point)
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            self.output.write(frame)

            cv2.waitKey(1)
            
            if keyboard.is_pressed(self.ButtonKey):
                self.StopRecord(root)
                break
        return

    def StopRecord(self, root: Tk):
        root.attributes("-topmost", False)
        cv2.destroyAllWindows()
        self.output.release()
        return