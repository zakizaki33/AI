import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() is False:
    raise IOError

while(True):
    ret, frame = capture.read()
    if ret is False:
        raise IOError
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
