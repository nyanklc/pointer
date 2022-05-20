import cv2 as cv
import hand as hd

def main():

    global toggle_draw
    toggle_draw = False

    # start capture
    cap = cv.VideoCapture(0)
    retrieved, frame = cap.read()

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    show_lines = False

    hand = hd.Hand()


    # callbacks
    cv.namedWindow('frame')
    cv.setMouseCallback('frame', ToggleDraw)

    # display loop
    while True:

        # get frame
        retrieved, frame = cap.read()
        if not retrieved:
            print("Can't receive frame. Exiting ...")
            break
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        # find hand and face
        hand.Find(frame_rgb)
        
        # q: quit program
        if cv.waitKey(2) == ord('q'):
            break
        if toggle_draw:
            hand.Draw(frame)
        
        cv.imshow('frame', frame)
                
    cap.release()
    cv.destroyAllWindows()


def ToggleDraw(event, x, y, flags, param):
    
    global toggle_draw

    if event == cv.EVENT_LBUTTONDBLCLK:
        toggle_draw = not toggle_draw


if __name__ == "__main__":
    main()