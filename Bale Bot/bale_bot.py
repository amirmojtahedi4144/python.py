import requests
import sqlite3
import re
import time
from datetime import datetime

TOKEN = "699085345:wZOloez3n5GSmi0pA0CM4D4BBh6SbZPzyn8"
BASE_URL = f"https://tapi.bale.ai/bot{"699085345:wZOloez3n5GSmi0pA0CM4D4BBh6SbZPzyn8"}"
last_update_id = 0

class GradeBot:
    def __init__(self):
        self.user_sessions = {}
        
    def get_updates(self):
        global last_update_id
        url = f"{BASE_URL}/getUpdates"
        params = {"offset": last_update_id + 1, "timeout": 30}
        
        try:
            response = requests.get(url, params=params, timeout=35)
            if response.status_code == 200:
                data = response.json()
                if data.get('ok'):
                    return data.get('result', [])
        except Exception as e:
            print(f"خطا: {e}")
        return []
    
    def send_message(self, chat_id, text, keyboard=None):
        url = f"{BASE_URL}/sendMessage"
        data = {"chat_id": chat_id, "text": text}
        
        if keyboard:
            data["reply_markup"] = keyboard
        
        try:
            requests.post(url, json=data)
        except Exception as e:
            print(f"خطا در ارسال پیام: {e}")
    
    def send_main_menu(self, chat_id):
        keyboard = {
            "keyboard": [
                ["مشاهده اطلاعات دانش آموز", "مشاهده کارنامه"],
                ["نمرات نیمسال اول", "نمرات نیمسال دوم"],
                ["وضعیت حضور و غیاب", "رتبه در کلاس"],
                ["درس های ضعیف", "درس های قوی"],
                ["پیشرفت ماهانه", "آمار و ارقام"],
                ["تاریخچه جستجو", "راهنما"]
            ],
            "resize_keyboard": True
        }
        
        welcome_msg = """
سیستم مدیریت دانش آموزان
================================

به ربات حرفه ای استعلام نمرات خوش آمدید

از منوی زیر گزینه مورد نظر را انتخاب کنید:

مشاهده اطلاعات دانش آموز - مشاهده مشخصات کامل
مشاهده کارنامه - کارنامه کامل تحصیلی
نمرات نیمسال اول - نمرات نیمسال اول
نمرات نیمسال دوم - نمرات نیمسال دوم
وضعیت حضور و غیاب - بررسی حضور در کلاس
رتبه در کلاس - مقایسه با همکلاسی ها
درس های ضعیف - شناسایی درس های نیازمند تقویت
درس های قوی - مشاهده بهترین درس ها
پیشرفت ماهانه - روند پیشرفت در ماه های مختلف
آمار و ارقام - آمار پیشرفته تحصیلی

برای راهنما گزینه راهنما را انتخاب کنید
"""
        self.send_message(chat_id, welcome_msg, keyboard)
    
    def get_student_info(self, national_code):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM students WHERE national_code = ?', (national_code,))
        student = c.fetchone()
        
        if not student:
            conn.close()
            return None
        
        c.execute('SELECT lesson_name, score, term, teacher_name FROM grades WHERE national_code = ?', (national_code,))
        grades = c.fetchall()
        
        c.execute('SELECT COUNT(*) FROM attendance WHERE national_code = ? AND status = ?', (national_code, 'حاضر'))
        present = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM attendance WHERE national_code = ?', (national_code,))
        total = c.fetchone()[0]
        
        conn.close()
        
        return {
            'info': student,
            'grades': grades,
            'attendance': {'present': present, 'total': total} if total > 0 else None
        }
    
    def calculate_average(self, grades, term=None):
        filtered = [g for g in grades if term is None or g[2] == term]
        if not filtered:
            return 0
        total = sum(g[1] for g in filtered)
        return total / len(filtered)
    
    def get_class_ranking(self, national_code, class_name):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        
        c.execute('''
            SELECT s.national_code, s.full_name, AVG(g.score) as avg_score
            FROM students s
            JOIN grades g ON s.national_code = g.national_code
            WHERE s.class_name = ?
            GROUP BY s.national_code
            ORDER BY avg_score DESC
        ''', (class_name,))
        
        rankings = c.fetchall()
        conn.close()
        
        for idx, rank in enumerate(rankings, 1):
            if rank[0] == national_code:
                return idx, len(rankings), rank[2]
        
        return None, len(rankings), None
    
    def get_lesson_analysis(self, grades):
        lessons = {}
        for lesson, score, term, teacher in grades:
            if lesson not in lessons:
                lessons[lesson] = {'scores': [], 'terms': []}
            lessons[lesson]['scores'].append(score)
            lessons[lesson]['terms'].append(term)
        
        analysis = []
        for lesson, data in lessons.items():
            avg = sum(data['scores']) / len(data['scores'])
            if len(data['scores']) > 1:
                trend = "در حال افزایش" if data['scores'][-1] > data['scores'][0] else "در حال کاهش"
            else:
                trend = "ثابت"
            analysis.append({
                'name': lesson,
                'average': avg,
                'trend': trend,
                'count': len(data['scores'])
            })
        
        analysis.sort(key=lambda x: x['average'])
        return analysis
    
    def get_monthly_progress(self, national_code):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute('''
            SELECT strftime('%m', exam_date) as month, AVG(score) as avg_score
            FROM grades
            WHERE national_code = ?
            GROUP BY month
            ORDER BY month
        ''', (national_code,))
        progress = c.fetchall()
        conn.close()
        return progress
    
    def get_statistics(self, national_code):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        
        c.execute('SELECT COUNT(DISTINCT lesson_name) FROM grades WHERE national_code = ?', (national_code,))
        total_lessons = c.fetchone()[0]
        
        c.execute('SELECT MAX(score), MIN(score), AVG(score) FROM grades WHERE national_code = ?', (national_code,))
        max_score, min_score, avg_score = c.fetchone()
        
        c.execute('''
            SELECT lesson_name, COUNT(*) 
            FROM grades 
            WHERE national_code = ? 
            GROUP BY lesson_name 
            ORDER BY COUNT(*) DESC LIMIT 1
        ''', (national_code,))
        best_lesson = c.fetchone()
        
        conn.close()
        
        return {
            'total_lessons': total_lessons,
            'max_score': max_score,
            'min_score': min_score,
            'avg_score': avg_score,
            'best_lesson': best_lesson[0] if best_lesson else 'ندارد'
        }
    
    def save_search(self, chat_id, national_code, search_type):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute('INSERT INTO search_history (chat_id, national_code, search_type, search_date) VALUES (?, ?, ?, ?)',
                  (chat_id, national_code, search_type, now))
        conn.commit()
        conn.close()
    
    def get_user_history(self, chat_id):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute('''
            SELECT s.full_name, h.search_type, h.search_date
            FROM search_history h
            JOIN students s ON h.national_code = s.national_code
            WHERE h.chat_id = ?
            ORDER BY h.search_date DESC LIMIT 10
        ''', (chat_id,))
        history = c.fetchall()
        conn.close()
        return history
    
    def show_student_info(self, chat_id, national_code):
        data = self.get_student_info(national_code)
        if not data:
            self.send_message(chat_id, "دانش آموزی با این کد ملی پیدا نشد")
            return
        
        info = data['info']
        text = f"""
اطلاعات دانش آموز
================================
نام و نام خانوادگی: {info[1]}
کد ملی: {info[0]}
کلاس: {info[2]}
رشته تحصیلی: {info[3]}
سال ورود: {info[4]}
تلفن والدین: {info[5]}
آدرس: {info[6]}
================================
"""
        self.send_message(chat_id, text)
    
    def show_grade_report(self, chat_id, national_code):
        data = self.get_student_info(national_code)
        if not data:
            self.send_message(chat_id, "دانش آموزی با این کد ملی پیدا نشد")
            return
        
        info = data['info']
        grades = data['grades']
        attendance = data['attendance']
        
        term1_avg = self.calculate_average(grades, 'نیمسال اول')
        term2_avg = self.calculate_average(grades, 'نیمسال دوم')
        total_avg = self.calculate_average(grades)
        
        ranking, total_students, class_avg = self.get_class_ranking(national_code, info[2])
        
        report = []
        report.append("=" * 45)
        report.append("کارنامه رسمی تحصیلی")
        report.append("=" * 45)
        report.append(f"نام: {info[1]}")
        report.append(f"کد ملی: {info[0]}")
        report.append(f"کلاس: {info[2]}")
        report.append(f"رشته: {info[3]}")
        report.append("-" * 45)
        report.append("نمرات تحصیلی")
        report.append("-" * 45)
        
        for lesson, score, term, teacher in grades:
            report.append(f"{lesson}: {score} - {term}")
        
        report.append("-" * 45)
        report.append(f"میانگین نیمسال اول: {term1_avg:.2f}")
        report.append(f"میانگین نیمسال دوم: {term2_avg:.2f}")
        report.append(f"میانگین کل: {total_avg:.2f}")
        
        if ranking:
            report.append(f"رتبه در کلاس: {ranking} از {total_students}")
            report.append(f"میانگین کلاس: {class_avg:.2f}")
        
        if attendance:
            attendance_rate = (attendance['present'] / attendance['total']) * 100
            report.append("-" * 45)
            report.append("گزارش حضور و غیاب")
            report.append("-" * 45)
            report.append(f"تعداد حضور: {attendance['present']}")
            report.append(f"تعداد غیبت: {attendance['total'] - attendance['present']}")
            report.append(f"درصد حضور: {attendance_rate:.1f} درصد")
        
        if total_avg >= 17:
            report.append("وضعیت: عالی")
        elif total_avg >= 14:
            report.append("وضعیت: خوب")
        elif total_avg >= 10:
            report.append("وضعیت: قابل قبول")
        else:
            report.append("وضعیت: نیاز به تلاش بیشتر")
        
        report.append("=" * 45)
        
        self.send_message(chat_id, "\n".join(report))
    
    def show_term_grades(self, chat_id, national_code, term):
        data = self.get_student_info(national_code)
        if not data:
            self.send_message(chat_id, "دانش آموزی با این کد ملی پیدا نشد")
            return
        
        info = data['info']
        term_grades = [g for g in data['grades'] if g[2] == term]
        
        if not term_grades:
            self.send_message(chat_id, f"نمره ای برای {term} پیدا نشد")
            return
        
        text = f"""
نمرات {term}
دانش آموز: {info[1]}
================================
"""
        for lesson, score, term_name, teacher in term_grades:
            text += f"{lesson}: {score}\n"
        
        avg = self.calculate_average(data['grades'], term)
        text += f"\nمیانگین {term}: {avg:.2f}"
        
        self.send_message(chat_id, text)
    
    def show_attendance(self, chat_id, national_code):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute('SELECT date, status, lesson_name FROM attendance WHERE national_code = ? ORDER BY date DESC LIMIT 10', (national_code,))
        records = c.fetchall()
        conn.close()
        
        if not records:
            self.send_message(chat_id, "گزارش حضور و غیابی یافت نشد")
            return
        
        text = "گزارش حضور و غیاب\n"
        text += "=" * 35 + "\n"
        for date, status, lesson in records:
            status_text = "حاضر" if status == "حاضر" else "غایب" if status == "غایب" else "تاخیر"
            text += f"تاریخ: {date}\n"
            text += f"درس: {lesson}\n"
            text += f"وضعیت: {status_text}\n"
            text += "-" * 35 + "\n"
        
        self.send_message(chat_id, text)
    
    def show_ranking(self, chat_id, national_code):
        data = self.get_student_info(national_code)
        if not data:
            self.send_message(chat_id, "دانش آموزی با این کد ملی پیدا نشد")
            return
        
        ranking, total, avg = self.get_class_ranking(national_code, data['info'][2])
        if ranking:
            text = f"""
رتبه در کلاس
================================
رتبه شما: {ranking} از {total}
میانگین شما: {avg:.2f}
میانگین کل کلاس: {self.get_class_average(data['info'][2]):.2f}
================================
"""
            self.send_message(chat_id, text)
    
    def get_class_average(self, class_name):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute('''
            SELECT AVG(g.score)
            FROM students s
            JOIN grades g ON s.national_code = g.national_code
            WHERE s.class_name = ?
        ''', (class_name,))
        result = c.fetchone()
        conn.close()
        return result[0] if result[0] else 0
    
    def show_lesson_analysis(self, chat_id, national_code):
        data = self.get_student_info(national_code)
        if not data:
            self.send_message(chat_id, "دانش آموزی با این کد ملی پیدا نشد")
            return
        
        analysis = self.get_lesson_analysis(data['grades'])
        
        text = "تحلیل دروس\n"
        text += "=" * 35 + "\n\n"
        text += "درس های ضعیف (نیاز به تقویت)\n"
        text += "-" * 35 + "\n"
        
        weak_lessons = analysis[:3]
        for lesson in weak_lessons:
            text += f"{lesson['name']}: {lesson['average']:.2f} - {lesson['trend']}\n"
        
        text += "\nدرس های قوی\n"
        text += "-" * 35 + "\n"
        
        strong_lessons = analysis[-3:][::-1]
        for lesson in strong_lessons:
            text += f"{lesson['name']}: {lesson['average']:.2f} - {lesson['trend']}\n"
        
        self.send_message(chat_id, text)
    
    def show_progress(self, chat_id, national_code):
        progress = self.get_monthly_progress(national_code)
        
        if not progress:
            self.send_message(chat_id, "اطلاعاتی برای نمایش وجود ندارد")
            return
        
        text = "پیشرفت ماهانه\n"
        text += "=" * 35 + "\n"
        
        for month, avg in progress:
            month_name = f"ماه {month}"
            bar_length = int(avg / 2)
            bar = "#" * bar_length
            text += f"{month_name}: {bar} {avg:.2f}\n"
        
        text += "=" * 35
        self.send_message(chat_id, text)
    
    def show_statistics(self, chat_id, national_code):
        stats = self.get_statistics(national_code)
        data = self.get_student_info(national_code)
        
        if not data:
            self.send_message(chat_id, "دانش آموزی با این کد ملی پیدا نشد")
            return
        
        total_avg = self.calculate_average(data['grades'])
        
        text = f"""
آمار و ارقام تحصیلی
================================
تعداد کل دروس: {stats['total_lessons']}
بیشترین نمره: {stats['max_score']:.2f}
کمترین نمره: {stats['min_score']:.2f}
میانگین کل: {stats['avg_score']:.2f}
بهترین درس: {stats['best_lesson']}
================================
امتیاز عملکرد: {self.get_performance_score(total_avg)}
================================
"""
        self.send_message(chat_id, text)
    
    def get_performance_score(self, avg):
        if avg >= 18:
            return "عالی (A+)"
        elif avg >= 16:
            return "خیلی خوب (A)"
        elif avg >= 14:
            return "خوب (B)"
        elif avg >= 12:
            return "متوسط (C)"
        elif avg >= 10:
            return "قابل قبول (D)"
        else:
            return "نیاز به تلاش (F)"
    
    def show_history(self, chat_id):
        history = self.get_user_history(chat_id)
        if not history:
            self.send_message(chat_id, "تاریخچه جستجویی وجود ندارد")
            return
        
        text = "تاریخچه جستجوهای شما\n"
        text += "=" * 35 + "\n"
        for name, search_type, date in history:
            text += f"دانش آموز: {name}\n"
            text += f"نوع جستجو: {search_type}\n"
            text += f"تاریخ: {date}\n"
            text += "-" * 35 + "\n"
        
        self.send_message(chat_id, text)
    
    def show_help(self, chat_id):
        help_text = """
راهنمای ربات حرفه ای نمرات
================================

قابلیت های ربات:

1. مشاهده اطلاعات دانش آموز - مشاهده مشخصات کامل دانش آموز
2. مشاهده کارنامه - کارنامه کامل با میانگین ها
3. نمرات نیمسال اول - نمایش نمرات نیمسال اول
4. نمرات نیمسال دوم - نمایش نمرات نیمسال دوم
5. وضعیت حضور و غیاب - مشاهده گزارش حضور و غیاب
6. رتبه در کلاس - مقایسه با سایر دانش آموزان
7. درس های ضعیف - شناسایی درس های نیازمند تقویت
8. درس های قوی - مشاهده بهترین درس ها
9. پیشرفت ماهانه - مشاهده روند پیشرفت
10. آمار و ارقام - آمار پیشرفته تحصیلی

نحوه استفاده:
- از دکمه های منو استفاده کنید
- کد ملی 10 رقمی را وارد کنید

کدهای ملی نمونه:
امیر مجتهدی: 0012345678
سعید محمدی: 0023456789
علی بابایی: 0034567890

برای شروع مجدد /start را وارد کنید
"""
        self.send_message(chat_id, help_text)
    
    def run(self):
        print("=" * 40)
        print("ربات حرفه ای نمرات")
        print("نسخه 3.0")
        print("=" * 40)
        print("ربات در حال اجراست...")
        print("در حال انتظار برای پیام ها...")
        print("=" * 40)
        
        while True:
            updates = self.get_updates()
            
            for update in updates:
                global last_update_id
                last_update_id = update.get('update_id')
                message = update.get('message')
                
                if message:
                    chat_id = message.get('chat', {}).get('id')
                    text = message.get('text', '')
                    
                    if text == '/start':
                        self.send_main_menu(chat_id)
                        self.user_sessions[chat_id] = {'state': 'main'}
                    
                    elif text == "مشاهده اطلاعات دانش آموز":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'student_info'}
                    
                    elif text == "مشاهده کارنامه":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'grade_report'}
                    
                    elif text == "نمرات نیمسال اول":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'term1'}
                    
                    elif text == "نمرات نیمسال دوم":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'term2'}
                    
                    elif text == "وضعیت حضور و غیاب":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'attendance'}
                    
                    elif text == "رتبه در کلاس":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'ranking'}
                    
                    elif text == "درس های ضعیف" or text == "درس های قوی":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'lesson_analysis'}
                    
                    elif text == "پیشرفت ماهانه":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'progress'}
                    
                    elif text == "آمار و ارقام":
                        self.send_message(chat_id, "لطفا کد ملی 10 رقمی را وارد کنید:")
                        self.user_sessions[chat_id] = {'state': 'statistics'}
                    
                    elif text == "تاریخچه جستجو":
                        self.show_history(chat_id)
                    
                    elif text == "راهنما":
                        self.show_help(chat_id)
                    
                    elif chat_id in self.user_sessions:
                        state = self.user_sessions[chat_id].get('state')
                        
                        if state and re.match(r'^\d{10}$', text):
                            if state == 'student_info':
                                self.show_student_info(chat_id, text)
                                self.save_search(chat_id, text, 'اطلاعات دانش آموز')
                            
                            elif state == 'grade_report':
                                self.show_grade_report(chat_id, text)
                                self.save_search(chat_id, text, 'کارنامه')
                            
                            elif state == 'term1':
                                self.show_term_grades(chat_id, text, 'نیمسال اول')
                                self.save_search(chat_id, text, 'نیمسال اول')
                            
                            elif state == 'term2':
                                self.show_term_grades(chat_id, text, 'نیمسال دوم')
                                self.save_search(chat_id, text, 'نیمسال دوم')
                            
                            elif state == 'attendance':
                                self.show_attendance(chat_id, text)
                                self.save_search(chat_id, text, 'حضور و غیاب')
                            
                            elif state == 'ranking':
                                self.show_ranking(chat_id, text)
                                self.save_search(chat_id, text, 'رتبه')
                            
                            elif state == 'lesson_analysis':
                                self.show_lesson_analysis(chat_id, text)
                                self.save_search(chat_id, text, 'تحلیل دروس')
                            
                            elif state == 'progress':
                                self.show_progress(chat_id, text)
                                self.save_search(chat_id, text, 'پیشرفت')
                            
                            elif state == 'statistics':
                                self.show_statistics(chat_id, text)
                                self.save_search(chat_id, text, 'آمار')
                            
                            self.user_sessions[chat_id]['state'] = 'main'
                        else:
                            self.send_message(chat_id, "کد ملی نامعتبر. لطفا 10 رقم وارد کنید")
                    
                    elif text:
                        self.send_message(chat_id, "لطفا از دکمه های منو استفاده کنید یا /start را بزنید")
            
            time.sleep(0.5)

if __name__ == "__main__":
    bot = GradeBot()
    bot.run()