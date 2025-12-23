# predict_price.py
# پروژه: پیش‌بینی قیمت با Linear Regression
# این پروژه قیمت را بر اساس داده‌های نمونه پیش‌بینی می‌کند

from sklearn.linear_model import LinearRegression
import numpy as np

# داده‌های ورودی (ویژگی‌ها) و خروجی (قیمت‌ها)
x = np.array([50, 70, 90, 110]).reshape(-1, 1)
y = np.array([200, 280, 350, 430])

# ساخت مدل و آموزش
model = LinearRegression()
model.fit(x, y)

# گرفتن ورودی از کاربر
try:
    user_input = float(input("عدد مورد نظر برای پیش‌بینی قیمت (مثلاً 80): "))
    prediction = model.predict([[user_input]])
    print(f"قیمت پیش‌بینی: {prediction[0]:.0f} میلیون تومان")
except ValueError:
    print("لطفاً یک عدد معتبر وارد کنید.")
