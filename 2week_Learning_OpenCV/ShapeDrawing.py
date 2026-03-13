import cv2 as cv
import numpy as np

canvas = np.full((480,640,3), 255, dtype=np.uint8)

cv.line(canvas, (10,10),(640-10,480-10), color=(200,200,200),thickness=2)
cv.line(canvas, (640-10,10),(10,480-10), color=(200,200,200),thickness=2)
cv.line(canvas, (320,10), (320,480-10), color=(200,200,200), thickness=2)
cv.line(canvas, (10,240),(640-10,240), color=(200,200,200), thickness=2)
cv.putText(canvas, 'Line', (10,20), cv.FONT_HERSHEY_DUPLEX,0.5,(0,0,0))

center = (100,240)
cv.circle(canvas, center, radius=60, color= (0,0,255),thickness = 5)
cv.putText(canvas, 'Circle', center, cv.FONT_HERSHEY_DUPLEX, 0.5, (255,255,0))

pt1,pt2 = (320-60,240-50), (320+60,240+60)
cv.rectangle(canvas, pt1, pt2, color=(0,255,0), thickness = -1)
cv.putText(canvas, 'Rectangle', pt1, cv.FONT_HERSHEY_DUPLEX, 0.5, (255,0,255))

pts = np.array([(540,240-50),(540-55,240+50),(540+55,240+50)])
cv.polylines(canvas,[pts], True,color=(255,0,0),thickness = 5)
cv.putText(canvas, 'Polylines', pts[0].flatten(), cv.FONT_HERSHEY_DUPLEX, 0.5, (0,200,200))

cv.imshow('Shape Drawing', canvas)
cv.waitKey()
cv.destroyAllWindows()