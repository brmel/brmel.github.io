const lightbox = document.getElementById('lightbox');
const video = document.getElementById('lightbox-video');

document.querySelectorAll('.video-thumb').forEach((thumb) => thumb.addEventListener('click', () => {
    video.src = `https://www.youtube.com/embed/${thumb.dataset.video}?autoplay=1`;
    lightbox.showModal();
}));
lightbox.addEventListener('click', (event) => { if (event.target === lightbox) lightbox.close(); });
lightbox.addEventListener('close', () => video.removeAttribute('src'));
