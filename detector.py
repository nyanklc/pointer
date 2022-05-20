import hand as hnd
import cv2 as cv

class Detector:

    def __init__(self):
        self.hand = hnd.Hand()
        self.toggle_draw = False
        self.draw_mode_on = False

    def Find(self, frame_rgb):
        self.hand.Find(frame_rgb)

    def Draw(self, frame):
        self.draw_mode_on = not self.draw_mode_on
        if self.draw_mode_on:
            cv.putText(frame, "draw mode: on", (10, 20), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        
        self.hand.Draw(frame)

    def GetHand(self):
        return self.hand

    def ToggleDraw(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            self.toggle_draw = not self.toggle_draw

    def IsDrawing(self):
        return self.toggle_draw