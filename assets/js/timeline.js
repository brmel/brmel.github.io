document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.timeline-body img');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    if (!lightbox || !lightboxImg) return;

    images.forEach(img => {
        img.addEventListener('click', function () {
            lightboxImg.src = this.src;
            lightbox.classList.add('active');
        });
    });

    lightbox.addEventListener('click', function () {
        lightbox.classList.remove('active');
    });
});
