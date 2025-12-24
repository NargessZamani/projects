import cv2
import numpy as np

# باز کردن وب‌کم
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("وب‌کم پیدا نشد!")
    exit()

# ایجاد Background Subtractor
fg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        print("فریم وب‌کم قابل دریافت نیست!")
        break

    # اعمال ماسک پس‌زمینه
    fmask = fg.apply(frame)

    # نمایش تصویر اصلی و ماسک
    cv2.imshow("Original", frame)
    cv2.imshow("Foreground Mask", fmask)

    # خروج با ESC
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        print("خروج از برنامه...")
        break

# آزادسازی منابع
cap.release()
cv2.destroyAllWindows()
