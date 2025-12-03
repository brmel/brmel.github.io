document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.timeline-body img');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    if (!lightbox || !lightboxImg) return;

    const videoThumbnails = document.querySelectorAll('.video-thumbnail');
    const lightboxVideo = document.getElementById('lightbox-video');

    if (!lightbox || !lightboxImg || !lightboxVideo) return;

    // Handle Images
    images.forEach(img => {
        if (img.classList.contains('video-thumbnail')) return; // Skip video thumbnails
        img.addEventListener('click', function () {
            lightboxImg.src = this.src;
            lightboxImg.style.display = 'block';
            lightboxVideo.style.display = 'none';
            lightboxVideo.src = ''; // Stop video if playing
            lightbox.classList.add('active');
        });
    });

    // Handle Videos
    videoThumbnails.forEach(img => {
        img.addEventListener('click', function () {
            const videoSrc = this.getAttribute('data-video-src');
            if (videoSrc) {
                lightboxVideo.src = videoSrc;
                lightboxVideo.style.display = 'block';
                lightboxImg.style.display = 'none';
                lightbox.classList.add('active');
            }
        });
    });

    lightbox.addEventListener('click', function () {
        lightbox.classList.remove('active');
        lightboxVideo.src = ''; // Stop video
    });
});
