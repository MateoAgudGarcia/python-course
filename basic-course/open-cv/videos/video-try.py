import cv2,time

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
img = cv2.imread('try1.jpg')
recolor = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imwrite('try2.jpg',recolor)

while True:
    check, frame = video.read()
    color = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("Camera",color)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('c'):
        cv2.imwrite('try1.jpg',color)

video.release()
cv2.destroyAllWindows()