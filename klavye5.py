import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller

# Kamera ayarları
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = HandDetector(detectionCon=0.8, maxHands=2)
keyboard = Controller()

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M", "SPACE", "DEL"]
]


class Button:
    def __init__(self, pos, text, size=(85, 85)):
        self.pos = pos
        self.size = size
        self.text = text


button_list = []
for i, row in enumerate(keys):
    x_offset = 50
    for j, key in enumerate(row):
        if key == "SPACE":
            button_size = (250, 85)
        elif key == "DEL":
            button_size = (150, 85)
        else:
            button_size = (85, 85)
        button_list.append(Button((x_offset, 200 + 100 * i), key, size=button_size))
        x_offset += button_size[0] + 10

text = ""
last_pressed_time = 0
press_cooldown = 500

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True)

    for button in button_list:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 20, rt=0, colorC=(255, 255, 0))
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 0, 255), -1)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

    current_time = cv2.getTickCount() / cv2.getTickFrequency() * 2000

    if hands and (current_time - last_pressed_time > press_cooldown):
        for hand in hands:
            lm_list = hand["lmList"]
            thumb_tip = lm_list[4][:2]
            index_finger_tip = lm_list[8][:2]

            distance, _, _ = detector.findDistance(thumb_tip, index_finger_tip)

            # İşaret parmağının ucuna farklı renk nokta ekle
            cv2.circle(img, tuple(index_finger_tip), 10, (190 ,0 , 0), -1)

            if distance < 40:
                for button in button_list:
                    x, y = button.pos
                    w, h = button.size

                    if x < index_finger_tip[0] < x + w and y < index_finger_tip[1] < y + h:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), -1)
                        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        midpoint = ((x + x + w) // 2, (y + y + h) // 2)
                        cv2.circle(img, midpoint, 10, (0, 0, 255), -1)

                        if button.text == "SPACE":
                            text += " "
                        elif button.text == "DEL":
                            text = text[:-1]
                        else:
                            text += button.text
                        last_pressed_time = current_time

    cv2.rectangle(img, (50, 50), (900, 150), (200, 200, 200), -1)
    cv2.putText(img, text, (60, 120), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

    cv2.imshow("Sanal Klavye", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
