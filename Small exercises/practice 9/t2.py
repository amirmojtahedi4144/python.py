import os
DATA_DIR = "exam_data"
os.makedirs(DATA_DIR, exist_ok=True)
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.txt")

def load_questions():
    questions = []
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if '||' in line:
                    q, a = line.strip().split('||', 1)
                    questions.append({"question": q.strip(), "answer": a.strip()})
    return questions

def save_questions(questions):
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        for q in questions:
            f.write(f"{q['question']} || {q['answer']}\n")

def create_questions():
    questions = load_questions()
    print("\n اضافه کردن سؤال جدید (برای خروج Enter بزن)")
    while True:
        q = input("\nمتن سؤال: ").strip()
        if not q:
            break
        a = input("پاسخ صحیح: ").strip()
        questions.append({"question": q, "answer": a})
        print(" سؤال اضافه شد.")
    save_questions(questions)
    print(" سؤالات ذخیره شدند.")

def review_questions():
    questions = load_questions()
    if not questions:
        print("\n️ هنوز سؤالی تعریف نشده.")
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== بازبینی و مدیریت سؤالات ===\n")
        for i, q in enumerate(questions, 1):
            print(f"{i}. {q['question']} -> [{q['answer']}]")

        print("\nگزینه‌ها:")
        print("E: ویرایش سؤال")
        print("D: حذف سؤال")
        print("B: بازگشت")
        choice = input("\nانتخاب: ").strip().lower()

        if choice == 'b':
            break
        elif choice == 'e':
            num = input("شماره سؤال برای ویرایش: ").strip()
            if not num.isdigit() or not (1 <= int(num) <= len(questions)):
                print(" شماره نامعتبر.")
                input("Enter بزن برای ادامه...")
                continue
            idx = int(num) - 1
            new_q = input(f"متن جدید (قدیم: {questions[idx]['question']}): ").strip()
            new_a = input(f"پاسخ جدید (قدیم: {questions[idx]['answer']}): ").strip()
            if new_q:
                questions[idx]['question'] = new_q
            if new_a:
                questions[idx]['answer'] = new_a
            save_questions(questions)
            print(" سؤال به‌روزرسانی شد.")
            input("Enter بزن برای ادامه...")
        elif choice == 'd':
            num = input("شماره سؤال برای حذف: ").strip()
            if not num.isdigit() or not (1 <= int(num) <= len(questions)):
                print(" شماره نامعتبر.")
                input("Enter بزن...")
                continue
            idx = int(num) - 1
            confirm = input(f"آیا از حذف '{questions[idx]['question']}' مطمئنی؟ (yes/no): ").lower()
            if confirm == 'yes':
                del questions[idx]
                save_questions(questions)
                print(" سؤال حذف شد.")
            input("Enter بزن...")
        else:
            print("گزینه نامعتبر.")
            input("Enter بزن...")

def take_exam():
    questions = load_questions()
    if not questions:
        print(" سؤالی برای امتحان وجود ندارد.")
        return

    print("\n شروع امتحان!\n")
    correct = 0
    wrong_details = []

    for i, q in enumerate(questions, 1):
        ans = input(f"{i}. {q['question']}\nپاسخ شما: ").strip()
        if ans.lower() == q['answer'].lower():
            print(" درست!\n")
            correct += 1
        else:
            print(f" پاسخ صحیح: {q['answer']}\n")
            wrong_details.append((q['question'], ans, q['answer']))

    total = len(questions)
    percent = (correct / total) * 100
    grade = round((correct / total) * 20, 2)

    print("=" * 40)
    print(f" درست: {correct} | غلط: {total - correct}")
    print(f"درصد موفقیت: {percent:.2f}%")
    print(f"نمره نهایی (از ۲۰): {grade}")
    print("=" * 40)

    if wrong_details:
        print("\n پاسخ‌های اشتباه:")
        for tq, ua, ca in wrong_details:
            print(f"- {tq}\n  پاسخ شما: {ua}\n  پاسخ صحیح: {ca}")
    input("\nبرای ادامه Enter بزن...")

def manage_data():
    print("\n مدیریت فایل‌ها:")
    print("1. نمایش فایل‌های موجود")
    print("2. حذف همه داده‌ها")
    print("3. بازگشت")
    choice = input("انتخاب: ").strip()
    if choice == '1':
        print(f"\n محتویات '{DATA_DIR}':")
        for f in os.listdir(DATA_DIR):
            print(f" - {f}")
    elif choice == '2':
        confirm = input("آیا مطمئنی که می‌خواهی همه داده‌ها را حذف کنی؟ (yes/no): ").lower()
        if confirm == 'yes':
            for f in os.listdir(DATA_DIR):
                os.remove(os.path.join(DATA_DIR, f))
            print(" همه داده‌ها حذف شدند.")
    input("\nبرای ادامه Enter بزن...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== سیستم امتحان و سؤال‌ساز پیشرفته بدون ===")
        print("1. افزودن سؤال جدید")
        print("2. شروع امتحان")
        print("3. بازبینی / حذف / ویرایش سؤال")
        print("4. مدیریت فایل‌ها")
        print("5. خروج")

        choice = input("انتخاب: ").strip()
        if choice == '1':
            create_questions()
        elif choice == '2':
            take_exam()
        elif choice == '3':
            review_questions()
        elif choice == '4':
            manage_data()
        elif choice == '5':
            print(" خداحافظ!")
            break
        else:
            print(" گزینه نامعتبر.")
            input("Enter بزن برای ادامه...")

if __name__ == "__main__":
    main()