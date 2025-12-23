import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# باز کردن پنجره انتخاب فایل (Tkinter)
Tk().withdraw()  # پنجره اصلی Tkinter مخفی می‌شود
input_path = askopenfilename(
    title="یک تصویر انتخاب کنید",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.jfif")]
)

# بررسی انتخاب تصویر
if not input_path:
    print("تصویری انتخاب نشد!")
    exit()

# بارگذاری تصویر
image = cv2.imread(input_path)
if image is None:
    print("تصویر بارگذاری نشد!")
    exit()

# تبدیل به HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# نمایش تصویر HSV
cv2.imshow("HSV Image", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ایجاد پوشه خروجی در صورت عدم وجود
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# ذخیره تصویر خروجی
output_path = os.path.join(output_dir, "hsv_image.jpg")
cv2.imwrite(output_path, hsv_image)
print(f"تصویر HSV ذخیره شد در: {output_path}")
