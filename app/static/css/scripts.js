// 🎵 เพิ่ม effect สำหรับการโหลดหน้าเว็บ
document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('fade-in');
});

// 🎵 เพิ่ม effect สำหรับปุ่ม
const buttons = document.querySelectorAll('.btn-hover-effect');
buttons.forEach(button => {
    button.addEventListener('mouseenter', () => {
        button.style.transform = 'scale(1.05)';
    });
    button.addEventListener('mouseleave', () => {
        button.style.transform = 'scale(1)';
    });
});

// 🎵 ตรวจสอบฟอร์มก่อนส่ง
document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            let isValid = true;
            const inputs = form.querySelectorAll('input, textarea');
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('is-invalid');
                } else {
                    input.classList.remove('is-invalid');
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    });
});

// 🎵 บันทึกข้อมูลใน Local Storage
document.addEventListener('DOMContentLoaded', function () {
    const saveButtons = document.querySelectorAll('.btn-save');
    saveButtons.forEach(button => {
        button.addEventListener('click', function () {
            const input = button.previousElementSibling;
            if (input && input.value.trim()) {
                localStorage.setItem(input.name, input.value);
                alert('Data saved successfully!');
            }
        });
    });
});

// 🎵 โหลดข้อมูลจาก Local Storage
document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        const savedValue = localStorage.getItem(input.name);
        if (savedValue) {
            input.value = savedValue;
        }
    });
});