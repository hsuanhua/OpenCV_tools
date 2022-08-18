import cv2
import pandas as pd
import time
from pathlib import Path


def click():
    cap = cv2.VideoCapture(
        "{http://......}"
    )
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    return cap


def save_path():
    today = pd.to_datetime("today", format="%Y/%m/%d %H:%M:%S").strftime("%Y%m%d%H%M%S")
    dir = today[0:8]
    path = Path(dir)
    if path.is_dir() != True:
        Path(dir).mkdir(parents=True, exist_ok=True)
    return dir, today


cap = click()
while True:
    success, frame = cap.read()
    if not success:
        print("closed")
        break

    dir, today = save_path()
    cv2.imwrite(dir + "/" + today + ".jpg", frame)
    time.sleep(5)
    cap = click()

cap.release()
cv2.destroyAllWindows()
