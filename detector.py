import hand as hnd
import cv2 as cv

class Detector:

    def __init__(self):
        self.hand = hnd.Hand()

    def find(self, frame_rgb):
        self.hand.Find(frame_rgb)

    def draw(self, frame):
        cv.putText(frame, "draw mode: on", (10, 20), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        self.hand.Draw(frame)

    def getHand(self):
        return self.hand