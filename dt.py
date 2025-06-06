import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import math

# Initialize webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2, detectionCon=0.8)

# Function to play music using AppleScript
def play_apple_music(song_name):
    apple_script = f'''
    tell application "Music"
        activate
        play (first track whose name contains "{song_name}")
    end tell
    '''
    subprocess.run(['osascript', '-e', apple_script])

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Returns hands and draws landmarks

    if len(hands) == 2:
        lmList1 = hands[0]["lmList"]
        lmList2 = hands[1]["lmList"]

        # Get tip of index fingers (landmark 8)
        x1, y1 = lmList1[8]
        x2, y2 = lmList2[8]

        # Distance between index finger tips
        dist = math.hypot(x2 - x1, y2 - y1)

        # If fingers are close enough (simulate heart shape)
        if dist < 50:
            print("❤️ Heart gesture detected! Playing 'Dil Ruba'")
            play_apple_music("Dil Ruba")
            break

    cv2.imshow("Heart Gesture Detection", img)
    if cv2.waitKey(1) == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()