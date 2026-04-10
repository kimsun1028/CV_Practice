import numpy as np
import cv2 as cv

#param = pts_src
def mouse_event_handler(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        param.append((x,y))

if __name__ == '__main__':
    img_file = 'data/sunglok_card.jpg'
    card_size =  (450,250)
    offset = 10


    # 4점 정보 담긴 2차원 배열
    pts_dst = np.array([[0,0], [card_size[0],0], [0,card_size[1]], [card_size[0], card_size[1]]])    

    img = cv.imread(img_file)

    # 단언문, img is None일 경우 따라오는 메시지 띄우며 강종
    assert img is not None, 'Cannot read the given image, ' + img_file

    pts_src = []
    wnd_name = 'Perspective Correction: Point Selection'
    cv.namedWindow(wnd_name)

    # 마우스 이벤트 감지할 창 이름, 마우스 이벤트가 발생했을 때 호출할 함수, 호출될 함수에 전달할 매개변수
    cv.setMouseCallback(wnd_name, mouse_event_handler, pts_src)

    while len(pts_src) < 4:
        img_display = img.copy()

        # 이미지 위 직사각형 cv.rectangle(img, pt1, pt2, color, thickness) 
        cv.rectangle(img_display, (offset, offset), (offset + card_size[0], offset + card_size[1]), (0,0,255),2)

        # 지금까지 찍은 포인트 개수(4를 넘지 않음)
        idx = min(len(pts_src), len(pts_dst))

        # cv.circle(img, center, radius, color, thickness) 모서리 위치 알려줌
        cv.circle(img_display, offset+ pts_dst[idx], 5, (0,255,0),-1)

        cv.imshow(wnd_name, img_display)

        key = cv.waitKey(10)
        if key == 27:
            break

    if len(pts_src) == 4:

        # M,mask = cv2.findHomography(srcPoints, dstPoints) srcPoints -> dstPoints로 가는 행렬 M(H) 구해다줌
        H, _ = cv.findHomography(np.array(pts_src), pts_dst)

        print(f'pts_src = {pts_src}')
        print(f'pts_dst = {pts_dst}')
        print(f'H = {H}')

        #dst = cv2.warpPerspective(src, M, dsize) M(H)를 통해 이미지 변형
        img_rectify = cv.warpPerspective(img, H, card_size)

        cv.imshow('Perspective Distortion CorrectionL Rectified Image', img_rectify)
        cv.waitKey(0)

    cv.destroyAllWindows()