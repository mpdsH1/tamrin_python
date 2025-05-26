#1. دریافت عدد و چاپ اعداد کوچکتر از آن
n = int(input("یک عدد وارد کنید: "))
for i in range(n):
    print(i)

#2. چاپ مقسوم‌علیه‌های عدد
n = int(input("یک عدد وارد کنید: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

#3. تشخیص عدد اول
n = int(input("یک عدد وارد کنید: "))
if n < 2:
    print("عدد اول نیست")
else:
    for i in range(2, n):
        if n % i == 0:
            print("عدد اول نیست")
            break
    else:
        print("عدد اول است")

#4. چاپ اعداد زوج کوچکتر از عدد
n = int(input("یک عدد وارد کنید: "))
for i in range(0, n):
    if i % 2 == 0:
        print(i)

#5. چاپ اعداد اول کوچکتر از عدد
n = int(input("یک عدد وارد کنید: "))
for num in range(2, n):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

#6. اعداد زوج دو رقمی کوچکتر از عدد
n = int(input("یک عدد وارد کنید: "))
for i in range(10, min(n, 100)):
    if i % 2 == 0:
        print(i)

#7. مقسوم‌علیه‌های مشترک دو عدد
a = int(input("عدد اول: "))
b = int(input("عدد دوم: "))
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        print(i)

#8. چاپ اعداد زوج یا فرد بین دو عدد با انتخاب کاربر
a = int(input("عدد اول: "))
b = int(input("عدد دوم: "))
mode = input("زوج یا فرد؟ (z/f): ").lower()

start = min(a, b)
end = max(a, b)

for i in range(start, end+1):
    if mode == 'z' and i % 2 == 0:
        print(i)
    elif mode == 'f' and i % 2 == 1:
        print(i)

#9. دریافت اعداد و چاپ بیشینه و مجموع (ورود صفر پایان‌دهنده)
numbers = []
while True:
    n = int(input("عدد وارد کنید (برای پایان 0): "))
    if n == 0:
        break
    numbers.append(n)

if numbers:
    print("بزرگ‌ترین عدد:", max(numbers))
    print("مجموع:", sum(numbers))
else:
    print("عددی وارد نشد.")

#9. دریافت اعداد و چاپ بیشینه و مجموع (ورود صفر پایان‌دهنده)
mode = input("تبدیل از ده‌دهی به دودویی (1) یا برعکس (2)؟ ")

if mode == "1":
    n = int(input("عدد ده‌دهی را وارد کنید: "))
    print("باینری:", bin(n)[2:])
elif mode == "2":
    b = input("عدد دودویی را وارد کنید: ")
    print("ده‌دهی:", int(b, 2))
else:
    print("گزینه نامعتبر.")


