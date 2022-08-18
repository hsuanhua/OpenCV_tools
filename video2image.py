"""
Video to images
python video2image.py --video {video path} --save {save path}
"""
import cv2
import pandas as pd
import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--video", default="./", type=str, help="video path"
    )
    parser.add_argument("--save", default="./", type=str, help="to saved folder path")
    return parser

parser = get_parser()
args = parser.parse_args()
cap = cv2.VideoCapture(args.video)
savePath = args.save
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    dt = pd.to_datetime("today",format='%Y/%m/%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
    cv2.imwrite('{2}/{0}_{1}.jpg'.format(dt, count, savePath), frame)
    count += 1

cap.release()
cv2.destroyAllWindows()