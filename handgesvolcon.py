import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _ , image=webcam.read()
    cv2.imshow("Hand volume control using python",image)
    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output=my_hands.process(rgb_image)
    hands=output.multi_hands_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand)

    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()