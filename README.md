Music Recommendation 🎵

Music Recommendation เป็นเว็บแอปพลิเคชันที่สร้างด้วย Flask เพื่อให้ผู้ใช้สามารถค้นหาเพลง สร้างเพลย์ลิสต์ 
บันทึกแนวเพลงที่ชื่นชอบ และรับคำแนะนำเพลงตามแนวที่ชอบ

คุณสมบัติหลัก
-ค้นหาเพลง: ค้นหาเพลงโดยใช้ชื่อเพลงหรือชื่อศิลปิน
-สร้างเพลย์ลิสต์: สร้างและจัดการเพลย์ลิสต์ส่วนตัว
-คำแนะนำเพลง: รับคำแนะนำเพลงตามแนวที่ชอบ
-โปรไฟล์ผู้ใช้: อัปเดตข้อมูลส่วนตัวและแนวเพลงที่ชอบ

เทคโนโลยีที่ใช้
-Frontend: HTML, CSS, JavaScript, Bootstrap
-Backend: Flask (Python)
-Database: SQLite (SQLAlchemy)
-Authentication: Flask-Login

วิธีติดตั้งและรันโปรเจค

1.ติดตั้ง Python
ตรวจสอบให้แน่ใจว่าคุณมี Python 3.8 หรือสูงกว่าติดตั้งอยู่บนเครื่องของคุณ  
ดาวน์โหลดได้ที่: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.โคลนโปรเจค
```bash
git clone https://github.com/Peeranatz/My-website
cd My-website

3.สร้างและเปิดใช้งาน Virtual Environment
python -m venv venv
source venv/bin/activate   # สำหรับ macOS/Linux
venv\Scripts\activate      # สำหรับ Windows

4.ติดตั้ง Dependencies
pip install -r requirements.txt

5.รันโปรเจกต์
flask run

จากนั้นเปิดเบราว์เซอร์ไปที่:
http://127.0.0.1:5000/


โครงสร้างโปรเจกต์ 
/My websitesky /
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── songs.html
│   │   ├── song_detail.html
│   │   ├── playlists.html
│   │   ├── create_playlist.html
│   │   ├── profile.html
│   │   ├── recommendations.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── scripts.js
├── config.py
├── run.py
├── requirements.txt
├── README.md

Features
-แนะนำเพลง ตามแนวเพลงที่ชื่นชอบ
-สร้างและจัดการเพลย์ลิสต์
-ระบบ Authentication (สมัครสมาชิก, ล็อกอิน, ล็อกเอาต์)
-UI สวยงามด้วย Bootstrap


ตัวอย่างการใช้งาน
สมัครสมาชิก: ไปที่ /register เพื่อสร้างบัญชีใหม่

เข้าสู่ระบบ: ไปที่ /login เพื่อเข้าสู่ระบบ

ค้นหาเพลง: ใช้ฟังก์ชันค้นหาในหน้า /songs

สร้างเพลย์ลิสต์: ไปที่ /create_playlist เพื่อสร้างเพลย์ลิสต์ใหม่

รับคำแนะนำเพลง: ไปที่ /recommendations เพื่อดูเพลงแนะนำ


***สำหรับเว็บ Music Recommendation System หรือ Music Record เป็นเว็บที่สามารถใช้งานได้ทุกเพศ ทุกวัย และหวังว่า เราจะเป็นส่วนหนึ่งในการสร้างความสุขจากการฟังเพลง และมีความสุขกับบทเพลงต่างๆที่คุณชื่นชอบ ขอบคุณครับ***