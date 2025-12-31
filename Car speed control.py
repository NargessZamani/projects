import cv2
import numpy
def rescale_frame (frame , percent = 75) :
    width = int (frame.shape[1]* percent/100)
    height = int (frame.shape[0]* percent/100)
    dim = (width , height)
    return cv2.resize (frame , dim , interpolation=cv2.INTER_AREA)
cap = cv2.VideoCapture("16f5e6a0bc7f5bb57289c52d9041e40b50522134-360p.mp4")
while True :
    rec , frame1 = cap.read()
    rec , frame2 = cap.read()
    resize_frame1 = rescale_frame(frame1)
    resize_frame2 = rescale_frame(frame2)
    frame_diff = cv2.absdiff(resize_frame1 , resize_frame2)
    frame_diff_gr = cv2.cvtColor(frame_diff , cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(frame_diff_gr , (9 , 9) , 1)
    _ , mask = cv2.threshold(blurred_frame , 10 , 255 , cv2.THRESH_BINARY)
    contours , _ = cv2.findContours(mask , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours :
        if cv2.contourArea(contour) > 1000 :
            (x , y , w , h) = cv2.boundingRect(contour)
            cv2.rectangle(resize_frame1 , (x , y) , (x+w-100 , y+h-50) , (0 , 0 , 255) , 2)
            cv2.imshow("frame" , resize_frame1)
            cv2.imshow("frame_diff" , frame_diff)
            cv2.imshow("mask"  , mask)
            keyexit = cv2.waitKey(5) & 0xFF
            if keyexit == 27 :
                break
cv2.destroyAllWindows()
cap.release()
