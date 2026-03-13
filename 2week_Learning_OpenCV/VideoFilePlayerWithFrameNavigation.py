import cv2 as cv
import numpy as np

video_file = 'data/PETS09-S2L1-raw.webm'
video = cv.VideoCapture(video_file)
if video.isOpened():
    frame_total = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    frame_shift = 10
    speed_table = [1/10, 1/8, 1/4, 1/2, 1, 2, 3, 4, 5, 8, 10]
    speed_index = 4

    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1/fps*1000)

    while True:
        frame = int(video.get(cv.CAP_PROP_POS_FRAMES))
        valid, img = video.read()
        if not valid:
            break
            
        cv.imshow("Video Player",img)


        key = cv.waitKey(max(int(wait_msec / speed_table[speed_index]),1))
        if key == ord(' '):
            key = cv.waitKey()
        if key == 27:
            break
        elif key == ord('\t'):
            speed_index = 4
        elif key == ord('>') or key == ord('.'):
            speed_index = min(speed_index + 1, len(speed_table) - 1)
        elif key == ord('<') or key == ord(','):
            speed_index = max(speed_index - 1,0)
        elif key == ord(']') or key == ord('}'):
            video.set(cv.CAP_PROP_POS_FRAMES, frame + frame_shift)
        elif key == ord('[') or key == ord('{'):
            video.set(cv.CAP_PROP_POS_FRAMES, max(frame - frame_shift, 0))

            