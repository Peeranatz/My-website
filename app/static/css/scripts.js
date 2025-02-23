// เพิ่ม effect สำหรับการโหลดหน้าเว็บ
document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('fade-in');
});

// เพิ่ม effect สำหรับปุ่ม
const buttons = document.querySelectorAll('.btn-hover-effect');
buttons.forEach(button => {
    button.addEventListener('mouseenter', () => {
        button.style.transform = 'scale(1.05)';
    });
    button.addEventListener('mouseleave', () => {
        button.style.transform = 'scale(1)';
    });
});