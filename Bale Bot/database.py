import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        national_code TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        class_name TEXT,
        field_of_study TEXT,
        entry_year TEXT,
        parent_phone TEXT,
        address TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        national_code TEXT NOT NULL,
        lesson_name TEXT NOT NULL,
        score REAL NOT NULL,
        term TEXT,
        teacher_name TEXT,
        exam_date TEXT,
        FOREIGN KEY (national_code) REFERENCES students (national_code)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        national_code TEXT NOT NULL,
        date TEXT NOT NULL,
        status TEXT NOT NULL,
        lesson_name TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        national_code TEXT NOT NULL,
        search_type TEXT,
        search_date TEXT NOT NULL
    )
    ''')
    
    students = [
        ('0012345678', 'امیر مجتهدی', 'دوازدهم الف', 'ریاضی فیزیک', '1403', '09123456789', 'تهران'),
        ('0023456789', 'سعید محمدی', 'دوازدهم ب', 'علوم تجربی', '1403', '09123456788', 'مشهد'),
        ('0034567890', 'علی بابایی', 'دوازدهم الف', 'ریاضی فیزیک', '1403', '09123456787', 'اصفهان')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?, ?, ?)', students)
    
    grades = [
        ('0012345678', 'ریاضی', 18.5, 'نیمسال اول', 'احمدی', '1403/08/15'),
        ('0012345678', 'فیزیک', 17.25, 'نیمسال اول', 'کریمی', '1403/08/16'),
        ('0012345678', 'شیمی', 19.0, 'نیمسال اول', 'رضایی', '1403/08/17'),
        ('0012345678', 'ریاضی', 19.0, 'نیمسال دوم', 'احمدی', '1404/01/15'),
        ('0012345678', 'فیزیک', 18.0, 'نیمسال دوم', 'کریمی', '1404/01/16'),
        ('0012345678', 'شیمی', 19.5, 'نیمسال دوم', 'رضایی', '1404/01/17'),
        ('0023456789', 'ریاضی', 15.75, 'نیمسال اول', 'احمدی', '1403/08/15'),
        ('0023456789', 'ادبیات', 18.0, 'نیمسال اول', 'نوری', '1403/08/16'),
        ('0023456789', 'زبان', 16.5, 'نیمسال اول', 'محمدی', '1403/08/17'),
        ('0023456789', 'ریاضی', 16.0, 'نیمسال دوم', 'احمدی', '1404/01/15'),
        ('0023456789', 'ادبیات', 18.5, 'نیمسال دوم', 'نوری', '1404/01/16'),
        ('0023456789', 'زبان', 17.0, 'نیمسال دوم', 'محمدی', '1404/01/17'),
        ('0034567890', 'ریاضی', 20.0, 'نیمسال اول', 'احمدی', '1403/08/15'),
        ('0034567890', 'فیزیک', 19.5, 'نیمسال اول', 'کریمی', '1403/08/16'),
        ('0034567890', 'برنامه نویسی', 20.0, 'نیمسال اول', 'سعادت', '1403/08/17'),
        ('0034567890', 'ریاضی', 20.0, 'نیمسال دوم', 'احمدی', '1404/01/15'),
        ('0034567890', 'فیزیک', 20.0, 'نیمسال دوم', 'کریمی', '1404/01/16'),
        ('0034567890', 'برنامه نویسی', 20.0, 'نیمسال دوم', 'سعادت', '1404/01/17')
    ]
    
    cursor.executemany('INSERT INTO grades (national_code, lesson_name, score, term, teacher_name, exam_date) VALUES (?, ?, ?, ?, ?, ?)', grades)
    
    attendance = [
        ('0012345678', '1403/08/01', 'حاضر', 'ریاضی'),
        ('0012345678', '1403/08/02', 'حاضر', 'فیزیک'),
        ('0012345678', '1403/08/03', 'غایب', 'شیمی'),
        ('0023456789', '1403/08/01', 'حاضر', 'ریاضی'),
        ('0023456789', '1403/08/02', 'تاخیر', 'ادبیات'),
    ]
    
    cursor.executemany('INSERT INTO attendance (national_code, date, status, lesson_name) VALUES (?, ?, ?, ?)', attendance)
    
    conn.commit()
    conn.close()
    print("پایگاه داده با موفقیت ساخته شد")

if __name__ == "__main__":
    create_database()