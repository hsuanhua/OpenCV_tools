## OpenCV_tools
做專案時，簡單寫了幾個小工具，紀錄一下，還可以改寫更好

- clickImg.py
  - 使用 opencv 的 VideoCapture 自動載取某個 IP Camera 的影像
  
- video2Image.py
  - 將影像串流檔存成一張張的圖片
  - 使用 python argparse
    - python video2image.py --video {video path} --save {save path}

- frame_photo.py
  - 外接 camera ，使用 VideoCapture 進行錄影或是拍圖片
