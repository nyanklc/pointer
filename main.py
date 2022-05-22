import cv2 as cv
import detector as det

def main():
    # start capture
    cap = cv.VideoCapture(0)
    retrieved, frame = cap.read()
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # init objects
    detector = det.Detector()

    # callbacks on window "pointer"
    cv.namedWindow('pointer')
    cv.setMouseCallback('pointer', detector.ToggleDraw)

    while True:
        # get frame
        retrieved, frame = cap.read()
        if not retrieved:
            print("Can't receive frame. Exiting ...")
            break
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        # find features on frame
        detector.Find(frame_rgb)
        
        # draw on frame
        if detector.IsDrawing():
            detector.Draw(frame)
        else:
            ShowInfo(frame)
        
        # display frame
        cv.imshow('pointer', frame)

        # esc: quit program
        if cv.waitKey(2) == 27:
            break
                
    cap.release()
    cv.destroyAllWindows()


def ShowInfo(frame):
    info_text = "double click to turn on draw mode, esc to quit"
    cv.putText(frame, info_text, (200, 20), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))

if __name__ == "__main__":
    main()