import cv2 as cv
import detector as det
import stream_getter as stream_get
import stream_viewer as stream_view
import time

VIDEO_SOURCE = 'http://nyn_cam:Means1122@192.168.1.92:8080/video'
VIEW_MODE = False

def main():
    
    stream_getter = stream_get.StreamGetter(VIDEO_SOURCE)
    stream_getter.startStream()
    detector = det.Detector()
    if VIEW_MODE:
        stream_viewer = stream_view.StreamViewer(stream_getter.getFrame())
        stream_viewer.startView()

    while True:
        if VIEW_MODE:
            if stream_viewer.isStopped():
                break

        frame = stream_getter.getFrame()
        if not stream_getter.getRetrieved():
            print("Can't retrieve frame. Exiting...")
            break

        detector.Find(frame)
        if VIEW_MODE:
            detector.Draw(frame)
            stream_viewer.setFrame(frame)

    if VIEW_MODE:
        stream_viewer.endView()
    stream_getter.endStream()



if __name__ == "__main__":
    main()
