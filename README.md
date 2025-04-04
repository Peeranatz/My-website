Music Recommendation 🎵
Music Recommendation เป็นเว็บแอปพลิเคชันที่สร้างด้วย Flask เพื่อให้ผู้ใช้สามารถค้นหาเพลง สร้างเพลย์ลิสต์ บันทึกแนวเพลงที่ชื่นชอบ และรับคำแนะนำเพลงตามแนวที่ชอบ

คุณสมบัติหลัก

ค้นหาเพลง: ค้นหาเพลงโดยใช้ชื่อเพลงหรือชื่อศิลปิน
สร้างเพลย์ลิสต์: สร้างและจัดการเพลย์ลิสต์ส่วนตัว
คำแนะนำเพลง: รับคำแนะนำเพลงตามแนวที่ชอบ
โปรไฟล์ผู้ใช้: อัปเดตข้อมูลส่วนตัวและแนวเพลงที่ชอบ

ทคโนโลยีที่ใช้

Frontend: HTML, CSS, JavaScript, Bootstrap 5.x
Backend: Flask 2.x (Python 3.8+)
Database: SQLite + SQLAlchemy 1.4
Authentication: Flask-Login 0.6+

วิธีติดตั้งและรันโปรเจค

1.ติดตั้ง Python
# ตรวจสอบเวอร์ชัน Python
python --version  # ควรเป็น 3.8 หรือสูงกว่า

2.โคลนโปรเจค
git clone https://github.com/Peeranatz/My-websitesky
cd My-websitesky

3.สร้างและเปิดใช้งาน Virtual Environment
# สร้าง virtual environment
python -m venv venv

# เปิดใช้งาน virtual environment
# สำหรับ macOS/Linux:
source venv/bin/activate
# สำหรับ Windows:
venv\Scripts\activate

4.ติดตั้ง Dependencies
pip install -r requirements.txt

5.ตั้งค่าฐานข้อมูล
# สร้างฐานข้อมูล
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

6.รันโปรเจกต์
flask run
เปิดเบราว์เซอร์ไปที่: http://127.0.0.1:5000/

โครงสร้างโปรเจกต์

```
/My-websitesky/            # โฟลเดอร์หลักของโปรเจค
├── app/               # โฟลเดอร์หลักของแอปพลิเคชัน Flask
│   ├── __init__.py    # ไฟล์เริ่มต้นแอป Flask, กำหนดค่าการเชื่อมต่อ DB และ การตั้งค่าพื้นฐาน
│   ├── routes.py      # จัดการ URL endpoints, การนำทางและการประมวลผลคำขอ
│   ├── models.py      # กำหนดโครงสร้างฐานข้อมูล (User, Song, Playlist models)
│   ├── forms.py       # จัดการฟอร์มต่างๆ (Login, Register, Create Playlist forms)
│   ├── templates/     # โฟลเดอร์เก็บไฟล์ HTML templates
│   │   ├── base.html             # Template หลักที่ใช้เป็นโครงสร้างร่วมกัน
│   │   ├── home.html            # หน้าแรกของเว็บไซต์
│   │   ├── about.html           # หน้าเกี่ยวกับเว็บไซต์
│   │   ├── login.html           # หน้าล็อกอิน
│   │   ├── register.html        # หน้าสมัครสมาชิก
│   │   ├── songs.html           # หน้าแสดงรายการเพลง
│   │   ├── song_detail.html     # หน้าแสดงรายละเอียดเพลง
│   │   ├── playlists.html       # หน้าแสดงเพลย์ลิสต์ทั้งหมด
│   │   ├── create_playlist.html # หน้าสร้างเพลย์ลิสต์ใหม่
│   │   ├── profile.html         # หน้าโปรไฟล์ผู้ใช้
│   │   └── recommendations.html # หน้าแสดงเพลงแนะนำ
│   └── static/        # โฟลเดอร์เก็บไฟล์ static resources
│       ├── css/       # โฟลเดอร์เก็บไฟล์ CSS
│       │   └── styles.css       # ไฟล์ CSS หลักสำหรับการจัดรูปแบบเว็บไซต์
│       └── js/        # โฟลเดอร์เก็บไฟล์ JavaScript
│           └── scripts.js       # ไฟล์ JavaScript สำหรับ interactive features
├── config.py          # ไฟล์กำหนดค่าคอนฟิกของแอปพลิเคชัน (DB URL, Secret Key, etc.)
├── run.py            # ไฟล์หลักสำหรับรันแอปพลิเคชัน (entry point)
├── requirements.txt   # รายการ Python packages ที่จำเป็นต้องติดตั้ง
└── README.md         # เอกสารอธิบายโปรเจค วิธีติดตั้ง และการใช้งาน
```

การใช้งานระบบ

1.สมัครสมาชิก (/register)

-กรอกข้อมูลส่วนตัว
-เลือกแนวเพลงที่ชอบ
-สร้างบัญชีผู้ใช้


2.เข้าสู่ระบบ (/login)

-ใช้อีเมลและรหัสผ่านที่ลงทะเบียนไว้


3.ค้นหาเพลง (/songs)

-ค้นหาโดยชื่อเพลง
-ค้นหาโดยชื่อศิลปิน
-กรองตามแนวเพลง


4.จัดการเพลย์ลิสต์ (/playlists, /create_playlist)

-สร้างเพลย์ลิสต์ใหม่
-เพิ่ม/ลบเพลงในเพลย์ลิสต์
-แชร์เพลย์ลิสต์


5.รับคำแนะนำเพลง (/recommendations)

-ดูเพลงแนะนำตามแนวที่ชอบ
-ค้นพบศิลปินใหม่ๆ


การอธิบายโค้ดสำคัญ
run.py
Entry point หลักของแอปพลิเคชัน ทำหน้าที่:

-นำเข้า Flask application instance
-กำหนดค่า environment variables
-เริ่มต้น development server

app/init.py
ไฟล์กำหนดค่าหลักที่:

-สร้าง Flask application instance
-กำหนดค่าการเชื่อมต่อฐานข้อมูล
-ลงทะเบียน blueprints
-ตั้งค่า Flask-Login

app/models.py
กำหนดโครงสร้างฐานข้อมูลผ่าน SQLAlchemy:

-User: ข้อมูลผู้ใช้และการตั้งค่า
-Song: ข้อมูลเพลงและเมทาดาต้า
-Playlist: การจัดการเพลย์ลิสต์

app/routes.py
จัดการ URL endpoints และ business logic:

-การจัดการผู้ใช้ (สมัคร, ล็อกอิน)
-การค้นหาและแนะนำเพลง
-การจัดการเพลย์ลิสต์


เกี่ยวกับโปรเจค
Music Recommendation System 
เป็นแพลตฟอร์มที่ออกแบบมาเพื่อให้ผู้ใช้ทุกเพศทุกวัย
สามารถค้นพบและเพลิดเพลินกับเพลงที่ชื่นชอบได้อย่างง่ายดาย 
และสุดท้าย เราหวังว่าจะเป็นส่วนหนึ่งในการสร้างประสบการณ์การฟังเพลงที่น่าประทับใจสำหรับผู้ใช้ทุกคน