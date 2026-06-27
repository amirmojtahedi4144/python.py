import os
def nomreh(student_name: str, exam_file: str, lesson_name: str):
    if not os.path.exists(exam_file):
        print(f"خطا: فایل سوالات '{exam_file}' یافت نشد.")
        return
    try:
        with open(exam_file, "r") as f:
            lines = f.read().split("\n")
    except Exception as e:
        print(f"خطا در خواندن فایل '{exam_file}': {e}")
        return
    if len(lines) < 7:
        print(f"خطا: فایل '{exam_file}' فرمت صحیحی ندارد (خطوط کم است).")
        return None
    try:
        tedadsoalat = (len(lines) - 7) // 2
        kol_soalat_data = lines[4:(4 + tedadsoalat * 2)]
        correct_answers = lines[-1].split(",")
        if len(correct_answers) != tedadsoalat:
            print(
                f"هشدار: تعداد پاسخ های صحیح در آخرین خط فایل ({len(correct_answers)}) با تعداد سوالات محاسبه شده ({tedadsoalat}) مطابقت ندارد.")
        student_answers = []
        calculated_score = 0
        print(f"\n--- شروع آزمون برای {student_name} ---")
        for i in range(tedadsoalat):
            question_line = kol_soalat_data[i * 2]
            score_line = kol_soalat_data[i * 2 + 1]
            try:
                score_str = score_line.strip()[-9:].strip()
                question_score = int(score_str)
                if question_score <= 0: question_score = 1
            except:
                question_score = 1
                print(f"هشدار: امکان استخراج نمره برای سوال {i + 1} وجود نداشت. نمره پیش فرض 1 در نظر گرفته شد.")
            print(f"سوال {i + 1}: {question_line}")
            answer = input("پاسخ شما: ")
            student_answers.append(answer)
            if i < len(correct_answers) and answer.strip() == correct_answers[i].strip():
                calculated_score += question_score
                print(f"پاسخ صحیح! +{question_score} نمره")
            else:
                print("پاسخ اشتباه.")
        print("--- پایان آزمون ---")
        return {
            "student_name": student_name,
            "lesson_name": lesson_name,
            "score": calculated_score
        }
    except Exception as e:
        print(f"خطا در پردازش فایل سوالات یا محاسبه نمرات: {e}")
        import traceback
        traceback.print_exc()
        return