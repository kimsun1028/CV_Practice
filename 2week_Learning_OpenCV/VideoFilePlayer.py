import cv2 as cv

video_file = 'data/PETS09-S2L1-raw.webm'
video = cv.VideoCapture(video_file)

if video.isOpened():  # video 객체를 만들고 파일 열기가 성공했을때
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1/fps * 1000)

    while True:
        valid, img = video.read() # 실행될 때 마다 다음 프레임 한장씩 읽어옴
        if not valid:
            break
        
        cv.imshow('Video Player', img)
        key = cv.waitKey(wait_msec)
        if key == 27:
            break

    cv.destroyAllWindows()