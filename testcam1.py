import cv2
import requests
from yolo_predictions import YOLO_Pred
import numpy as np
from ultralytics import YOLO

token = '2sXkjJrlV61QZF0ue6jCaNQBZbyC30GkF3WOGCJs6Od'
url = 'https://notify-api.line.me/api/notify'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}
session = requests.Session()
img_url = 'https://th.pngtree.com/freepng/action-cartoon-cute-godzilla-character-avatar_7400326.html'
data = {'message' : 'CCTV ON','imageThumbnail': img_url , 'imageFullsize' : img_url}
session.post(url, headers=headers,data=data)


yolo = YOLO_Pred('ex20obj.onnx','ex20obj.yaml')

#url = 'rtsp://admin:NTOPNH@192.168.99.116/11/subtype=01' #RTSP URL ที่ได้มาจากข้อก่อนหน้า
url = 'rtsp://admin:Hikvision@192.168.99.11/Streaming/Channels/101'
#url = 'rtsp://admin:Hikvision@192.168.99.50/Streaming/Channels/101'
cap = cv2.VideoCapture(url) 

model_path = 'C:/last.pt'
model = YOLO(model_path)  # load a custom model
count_frame = 0
n_frame = 10
obj_box = []

if not cap.isOpened():
 print("Cannot open camera")
 exit()
# Load a model

while True:
  try:
    ret, img = cap.read()
    results = model(img)[0]
    key = cv2.waitKey(1)
    
    for result in results.boxes.data.tolist():          
           x1, y1, x2, y2, score, class_id = result

      
    pred_image, obj_box = yolo.predictions(img)
    cv2.imshow('pred_image',pred_image)
    #count_frame = count_frame + 1

    if (key == ord('q')) or (ret == False):   
     break
  except: 
    print("error") 
    #count_frame = count_frame + 1

token = '2sXkjJrlV61QZF0ue6jCaNQBZbyC30GkF3WOGCJs6Od'
url = 'https://notify-api.line.me/api/notify'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}
session = requests.Session()
img_url = 'https://th.pngtree.com/freepng/action-cartoon-cute-godzilla-character-avatar_7400326.html'
data = {'message' : 'CCTV OFF','imageThumbnail': img_url , 'imageFullsize' : img_url}
session.post(url, headers=headers,data=data)

cv2.destroyAllWindows()
cv2.waitKey(0)
cap.release()
