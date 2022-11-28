import cv2 as cv
from threading import Thread

class StreamViewer:
    def __init__(self, frame = None):
        self.stopped = False
        self.frame = frame

    def startView(self):
        self.th = Thread(target = self.view, args = ())
        self.th.start()
        return self

    def setFrame(self, frame):
        self.frame = frame

    def view(self):
        while not self.stopped:
            cv.imshow('pointer', self.frame)
            if cv.waitKey(2) == 27:
                self.stopped = True
    
    def isStopped(self):
        return self.stopped

    def endView(self):
        self.stopped = True
        cv.destroyAllWindows()
