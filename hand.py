import mediapipe as mp
import cv2 as cv

class Hand:
    
    def __init__(self):    
        self.mpHands = mp.solutions.hands
        self.hand = self.mpHands.Hands(max_num_hands=1)
        self.mpDraw = mp.solutions.drawing_utils

    def isPointing(self):
        # TODO: check if pointing

        return self.is_pointing

    def Draw(self, frame):
        if self.hand_detected:
            self.DrawLines(frame)
            self.DrawPointer(frame)
        else:
            cv.putText(frame, "no hand detected", (10, 30), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
            return

    def DrawLines(self, frame):
        for landmark in self.multi_landmarks:
            self.mpDraw.draw_landmarks(frame, landmark, self.mpHands.HAND_CONNECTIONS)
        

    def DrawPointer(self, frame):
        pass
        # TODO: draw pointer on the frame

    def Find(self, frame_rgb):      
        self.processed_hand = self.hand.process(frame_rgb)        
        self.multi_landmarks = self.processed_hand.multi_hand_landmarks
        self.hand_detected = self.multi_landmarks
        self.threeD_landmarks = self.processed_hand.multi_hand_world_landmarks
