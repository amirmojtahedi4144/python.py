import os
from nomreh import nomreh
from ezaf_be_soal import ezafekardanbesoal
from hazfsoal import hazfsoal
from writeexam import soalsaz
def save_result_to_file(exam_name: str, results: list, filename: str = "results.txt"):
    try:
        with open(filename, "w") as f:
            f.write(f"--- آزمون: {exam_name} ---\n")
            for result in results:
                f.write(f"{result}\n")
            f.write("--------------------\n\n")
        print(f"نتایج آزمون '{exam_name}' با موفقیت در فایل '{filename}' ذخیره شد.")
    except Exception as e:
        print(f"خطا در ذخیره نتایج آزمون '{exam_name}': {e}")
def save_analysis_results(analysis_data: dict, filename: str = "analysis_results.txt"):
    try:
        with open(filename, "w") as f:
            line_to_write = f"نام دانش آموز: {analysis_data["student_name"]} - درس: {analysis_data["lesson_name"]} - نمره: {analysis_data["score"]}\n"
            f.write(line_to_write)
        print(f"نتایج آنالیز با موفقیت در فایل '{filename}' ذخیره شد.")
    except Exception as e:
        print(f"خطا در ذخیره نتایج آنالیز: {e}")
def display_menu():
    print("\n===== منوی مدیریت آزمون =====")
    print("1. نوشتن آزمون جدید")
    print("2. حذف سوالات")
    print("3. ویرایش سوالات")
    print("4. شرکت در آزمون")
    print("5. آنالیز نمرات")
    print("6. خروج")
    print("============================")
if __name__ == "__main__":
    results_log = []
    while True:
        display_menu()
        user_choice = input("گزینه مورد نظر را انتخاب کنید: ")
        if user_choice == "1":
            exam_title = input("عنوان آزمون جدید را وارد کنید: ")
            soalsaz("ریاضی","mahdavi","math","1404")
        elif user_choice == "2":
            exam_to_modify = input("نام فایل آزمونی که می خواهید سوالاتش را حذف کنید (بدون پسوند .txt): ")
            hazfsoal(exam_to_modify + ".txt")
        elif user_choice == "3":
            exam_to_edit = input("نام فایل آزمونی که می خواهید ویرایش کنید (بدون پسوند .txt): ")
            ezafekardanbesoal((exam_to_edit + ".txt"))
        elif user_choice == "4":
            exam_file_name = input("نام فایل آزمون مورد نظر (مثلا List_soalat.txt): ")
            student_name_input = input("نام و نام خانوادگی خود را وارد کنید: ")
            lesson_name_input = input("نام درس را وارد کنید: ")
            if not os.path.exists(exam_file_name):
                print(f"خطا: فایل آزمون '{exam_file_name}' یافت نشد.")
                continue
            analysis_result = nomreh(student_name_input, exam_file_name, lesson_name_input)
            if analysis_result:
                save_analysis_results(analysis_result)
                results_log.append(f"{student_name_input}: {analysis_result['score']} از {lesson_name_input}")
        elif user_choice == "5":
            print("\n--- خلاصه نتایج آزمون ها ---")
            if not results_log:
                print("هنوز هیچ آزمونی انجام نشده است.")
            else:
                for log_entry in results_log:
                    print(log_entry)
            print("\nبرای مشاهده جزئیات کامل آنالیز، فایل 'analysis_results.txt' را بررسی کنید.")
        elif user_choice == "6":
            print("از برنامه خارج می شوید. خدانگهدار!")
            break
        else:
            print("گزینه نامعتبر. لطفاً دوباره تلاش کنید.")