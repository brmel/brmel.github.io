document.addEventListener('DOMContentLoaded', function () {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxVideo = document.getElementById('lightbox-video');
    const timelineContainer = document.querySelector('.timeline-container');

    if (!lightbox || !lightboxImg || !lightboxVideo || !timelineContainer) return;

    // Event Delegation: Handle clicks on images and video thumbnails
    timelineContainer.addEventListener('click', function (e) {
        const target = e.target;

        // Handle Video Thumbnails
        if (target.classList.contains('video-thumbnail')) {
            const videoSrc = target.getAttribute('data-video-src');
            if (videoSrc) {
                lightboxVideo.src = videoSrc;
                lightboxVideo.style.display = 'block';
                lightboxImg.style.display = 'none';
                openLightbox();
            }
            return;
        }

        // Handle Regular Images
        if (target.tagName === 'IMG' && target.closest('.timeline-body')) {
            lightboxImg.src = target.src;
            lightboxImg.style.display = 'block';
            lightboxVideo.style.display = 'none';
            lightboxVideo.src = ''; // Stop video if playing
            openLightbox();
        }
    });

    // Close Lightbox
    lightbox.addEventListener('click', closeLightbox);

    // Keyboard Support (Escape key)
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });

    function openLightbox() {
        lightbox.classList.add('active');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden'; // Prevent scrolling
    }

    function closeLightbox() {
        lightbox.classList.remove('active');
        lightbox.setAttribute('aria-hidden', 'true');
        lightboxVideo.src = ''; // Stop video
        document.body.style.overflow = ''; // Restore scrolling
    }
});
