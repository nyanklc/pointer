import cv2 as cv
from threading import Thread, Lock

class StreamGetter:
    def __init__(self, src=0):
        self.cap = cv.VideoCapture(src)
        (self.retrieved, self.frame) = self.cap.read()
        self.stopped = False
        self.read_lock = Lock()

    def startStream(self):
        self.th = Thread(target = self.getStream, args = ())
        self.th.start()
        return self

    def getStream(self):
        while not self.stopped:
            if not self.retrieved:
                self.stopStream()
            else:
                (retrieved, frame) = self.cap.read()
                self.read_lock.acquire()
                self.retrieved, self.frame = retrieved, frame
                self.read_lock.release()

    def stopStream(self):
        self.stopped = True
        self.th.join()

    def endStream(self):
        self.stopped = True
        self.cap.release()

    def getFrame(self):
        self.read_lock.acquire()
        frame = self.frame
        self.read_lock.release()
        return frame

    def getRetrieved(self):
        self.read_lock.acquire()
        retrieved = self.retrieved
        self.read_lock.release()
        return retrieved


