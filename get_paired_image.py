import cv2
import numpy as np
import datetime


video_caputre = cv2.VideoCapture(0)
video_caputre.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
video_caputre.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# 获取读入视频的参数
fps = video_caputre.get(cv2.CAP_PROP_FPS)
width = video_caputre.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video_caputre.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("fps:", fps)
print("width:", width)
print("height:", height)



##选择摄像头

dstDir = r'C:\Users\Citydo\Documents\yyk\zju\mypaper\code\DeepLabCut76\paired_imgs\v1\ '
count = 1
font = cv2.FONT_HERSHEY_SIMPLEX
success, frame_src = video_caputre.read()
while success and   count < 101 :
    print('当前是第:' + str(count) + '张' )

    frame_left = frame_src[0:int(height),0:int(width/2)]
    frame_right = frame_src[0:int(height),int(width/2):int(width)]
    # frameLeftUp = cv2.resize(frameLeftUp, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
    # frameRightUp = cv2.resize(frameRightUp, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
    
    frame_left = cv2.putText(frame_left, str(datetime.datetime.now()), (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    frame_right = cv2.putText(frame_right, str(datetime.datetime.now()), (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    frameUp = np.hstack((frame_left, frame_right))
    # cv2.imshow('frame', frameUp)
    cv2.imwrite(dstDir + 'camera-1-' + ('%s' % count) + ".jpg", frame_left)
    cv2.imwrite(dstDir + 'camera-2-' + ('%s' % count) + ".jpg", frame_right)

    key = cv2.waitKey(1000)
    if int(key) == 113:
        break

    count += 1
    success, frame_src = video_caputre.read()

frame_left.release()
frame_right.release()
