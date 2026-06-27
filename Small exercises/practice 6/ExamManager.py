import os
from writeexam import soalsaz
from hazfsoal import hazfsoal
from ezaf_be_soal import ezafekardanbesoal
from nomreh import nomreh
instructions = ("به نرم افزار سوال سازی و امتحان دهی خوش آمدید!!!\n"
                "برای اجرای دستورات اعداد زیر را وارد کنید\n"
                "1. ذخیره سوال جدید\n"
                "2. حذف نمونه سوال\n"
                "3. باز نویسی نمونه سوال / اصلاح نمونه سوال\n"
                "4. امتحان دادن سوالات مد نظر\n"
                "5. آنالیز نمرات دانش آموزان\n"
                "6. خروج\n ")
while True:
    print(instructions)
    user_choice = input("لطفا عدد مورد نظر را وارد کنید: ")

    if user_choice == "1":
        print("وارد بخش سوال سازی شدید\n"
              "مقادیر نام استاد.موضوع درسی.تاریخ.نام برگه آزمون را با ویرگول در بینشان انجام دهید\n")
        try:
            temp_data = input().split(",")
            soalsaz(temp_data[0].strip(), temp_data[1].strip(), temp_data[2].strip(), temp_data[3].strip())
            print("سوال جدید با موفقیت ذخیره شد.")
        except IndexError:
            print("ورودی نامعتبر است. لطفا مقادیر را با ویرگول جدا کنید.")
        except Exception as e:
            print(f"خطایی رخ داد: {e}")
    elif user_choice == "2":
        m = input("آیا میخواهید سوالات را حذف کنید؟ (بله/خیر)\n")
        if m == "بله":
            y = input("اسم فایل سوال را با پسوند .txt وارد کنید: ")
            try:
                hazfsoal(y)
                print(f"فایل {y} حذف شد.")
            except FileNotFoundError:
                print(f"خطا: فایل {y} یافت نشد.")
            except Exception as e:
                print(f"خطایی در حذف فایل رخ داد: {e}")
    elif user_choice == "3":
        print("شما وارد بخش ادیت سوال شدید. لطفا نام فایل سوال مورد نظر را وارد کنید:")
        q_file = input("نام فایل سوال: ")
        print("عملکرد ویرایش سوال هنوز پیاده سازی نشده است.")
    elif user_choice == "4":
        print("شما وارد آزمون شدید. لطفا نام فایل سوالات آزمون را وارد کنید:")
        exam_file = input("نام فایل سوالات: ")
        print("عملکرد شروع آزمون هنوز پیاده سازی نشده است.")
    elif user_choice == "5":
        print("در این بخش نمرات دانش آموزان آنالیز می شود.")
        n = input("اسم فایل سوالات (برای بررسی نمرات) با پسوند .txt وارد کنید: ")
        try:
            nomreh(n)
            print(f"آنالیز نمرات برای {n} انجام شد.")
        except FileNotFoundError:
            print(f"خطا: فایل {n} برای آنالیز یافت نشد.")
        except Exception as e:
            print(f"خطایی در آنالیز نمرات رخ داد: {e}")
    elif user_choice == "6":
        print("خروج از برنامه...")
        break
    else:
        print("ورودی نامعتبر است. لطفا یکی از اعداد 1 تا 6 را وارد کنید.")
    print("\n" + "="*20 + "\n")