import cv2 as cv
 
 
def main():
    # 导入视频文件，参数：0 自带摄像头，1 USB摄像头，为文件名时读取视频文件
    video_caputre = cv.VideoCapture(0)
    video_caputre.set(cv.CAP_PROP_FRAME_WIDTH, 2560)
    video_caputre.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    # 获取读入视频的参数
    fps = video_caputre.get(cv.CAP_PROP_FPS)
    width = video_caputre.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video_caputre.get(cv.CAP_PROP_FRAME_HEIGHT)
 
    print("fps:", fps)
    print("width:", width)
    print("height:", height)
 
    # 定义截取尺寸,后面定义的每帧的h和w要于此一致，否则视频无法播放
    # 注意 这里是高宽 (height, width)
    # size = (int(height), int(width / 2))
    size = (int(width / 2), int(height))
 
    # 创建视频写入对象
    videp_write_left = cv.VideoWriter("C:\\Users\\Citydo\\Documents\\yyk\\zju\\mypaper\\code\\DeepLabCut76\\videos\\v3\\video_left.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
    videp_write_right = cv.VideoWriter("C:\\Users\\Citydo\\Documents\\yyk\\zju\\mypaper\\code\\DeepLabCut76\\videos\\v3\\video_right.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
 
    # 读取视频帧，然后写入文件并在窗口显示
    success, frame_src = video_caputre.read()
    while success and not cv.waitKey(1) == 27: #读完退出或者按下 esc 退出
        # [width, height] 要与上面定义的size参数一致，注意参数的位置
        frame_left = frame_src[0:int(height),0:int(width/2)]
        frame_right = frame_src[0:int(height),int(width/2):int(width)]
        # 写入视频文件
        videp_write_left.write(frame_left)
        videp_write_right.write(frame_right)
        # 显示裁剪的视频和原视频
        cv.imshow("video_left", frame_left)
        cv.imshow("frame_right", frame_right)
        cv.imshow("Video_src", frame_src)
 
        # 不断读取
        success, frame_src = video_caputre.read()
 
    print("视频裁剪完成")
 
    # 销毁窗口，释放资源
    cv.destroyWindow("video")
    cv.destroyWindow("Video_src")
    video_caputre.release()
 
if __name__=="__main__":
    main()