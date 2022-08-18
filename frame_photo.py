"""
錄影
"""
import cv2
import pandas as pd

now = pd.to_datetime("today",format='%Y/%m/%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
savePath = ''
out = cv2.VideoWriter(savePath+str(now)+'.avi', fourcc, 20.0, (640, 480))
while True:
    success, frame = cap.read()
    if not success:
        print('closed')
        break

    frame = cv2.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imwrite(savePath+str(now)+'.jpg',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


"""
拍照

import cv2
import pandas as pd

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
savePath = ''
def click(frame):
    now = pd.to_datetime("today",format='%Y/%m/%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite(savePath+now+'.jpg',frame)
        return True

    elif cv2.waitKey(1) == ord('q'):
        return False

while True:
    success, frame = cap.read()
    if not success:
        print('closed')
        break

    # write the flipped frame
    cv2.imshow('frame', frame)
    if click(frame) == False:
        break
    else:
        click(frame)

cap.release()
cv2.destroyAllWindows()
"""