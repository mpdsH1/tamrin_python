# برنامه‌ای که عددی از کاربر می‌گیرد و می‌گوید چه روزی از هفته است

number = int(input("لطفاً یک عدد بین 1 تا 7 وارد کنید: "))

if number == 1:
    print("شنبه")
elif number == 2:
    print("یک‌شنبه")
elif number == 3:
    print("دو‌شنبه")
elif number == 4:
    print("سه‌شنبه")
elif number == 5:
    print("چهار‌شنبه")
elif number == 6:
    print("پنج‌شنبه")
elif number == 7:
    print("جمعه")
else:
    print("عدد وارد شده معتبر نیست. لطفاً عددی بین 1 تا 7 وارد کنید.")




import datetime

# گرفتن تاریخ از کاربر به صورت رشته
date_input = input("لطفاً یک تاریخ وارد کنید (مثلاً 2025-05-10): ")

try:
    # تبدیل رشته به شیء تاریخ
    date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")

    # لیست روزهای هفته به فارسی
    days = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یک‌شنبه"]

    # گرفتن شماره‌ی روز هفته و نمایش آن (weekday از 0 تا 6 شروع میشه)
    day_index = date_obj.weekday()
    print("روز هفته:", days[day_index])

except ValueError:
    print("فرمت تاریخ اشتباه است! لطفاً به صورت YYYY-MM-DD وارد کنید.")




'''

    import jdatetime

# گرفتن تاریخ از کاربر
date_input = input("لطفاً یک تاریخ شمسی وارد کنید (مثلاً 1404-02-20): ")

try:
    # تبدیل رشته به تاریخ شمسی
    year, month, day = map(int, date_input.split("-"))
    shamsi_date = jdatetime.date(year, month, day)

    # گرفتن نام روز هفته
    weekday = shamsi_date.strftime("%A")

    # تبدیل روز هفته از انگلیسی به فارسی (اختیاری)
    days_fa = {
        "Saturday": "شنبه",
        "Sunday": "یک‌شنبه",
        "Monday": "دو‌شنبه",
        "Tuesday": "سه‌شنبه",
        "Wednesday": "چهار‌شنبه",
        "Thursday": "پنج‌شنبه",
        "Friday": "جمعه"
    }

    print("روز هفته:", days_fa.get(weekday, "نامشخص"))

except ValueError:
    print("فرمت تاریخ اشتباه است! لطفاً به صورت 1404-02-20 وارد کنید.")

'''