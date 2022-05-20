import mediapipe as mp

class Hand:
    
    def __init__(self):
        
        self.mpHands = mp.solutions.hands
        self.hand = self.mpHands.Hands(max_num_hands=1)
        self.mpDraw = mp.solutions.drawing_utils

    def isPointing(self):

        # TODO: check if pointing

        return self.is_pointing

    def Draw(self, frame):
        self.DrawLines(frame)
        self.DrawPointer(frame)

    def DrawLines(self, frame):
        if self.multi_landmarks:
            for landmark in self.multi_landmarks:
                self.mpDraw.draw_landmarks(frame, landmark, self.mpHands.HAND_CONNECTIONS)
        else:
            print("no hand detected")
            return

    def DrawPointer(self, frame):
        pass
        # TODO: draw pointer on the frame

    def Find(self, frame_rgb):
        
        self.processed_hand = self.hand.process(frame_rgb)        
        self.multi_landmarks = self.processed_hand.multi_hand_landmarks
        self.threeD_landmarks = self.processed_hand.multi_hand_world_landmarks
