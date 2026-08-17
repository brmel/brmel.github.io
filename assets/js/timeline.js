document.addEventListener('DOMContentLoaded', function () {
    const lightbox = document.getElementById('lightbox');
    const lightboxVideo = document.getElementById('lightbox-video');
    const timelineContainer = document.querySelector('.timeline-container');

    if (!lightbox || !lightboxVideo || !timelineContainer) return;

    timelineContainer.querySelectorAll('img.video-thumbnail').forEach(function (img) {
        if (img.parentElement.classList.contains('video-thumb')) return;
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'u-card u-card--interactive video-thumb';
        btn.setAttribute('aria-label', 'Play video: ' + (img.alt || 'video'));
        btn.setAttribute('data-video-src', img.getAttribute('data-video-src') || '');
        img.parentNode.insertBefore(btn, img);
        btn.appendChild(img);
        var badge = document.createElement('span');
        badge.className = 'video-thumb__play';
        badge.setAttribute('aria-hidden', 'true');
        badge.innerHTML = '<svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"/></svg>';
        btn.appendChild(badge);
    });

    timelineContainer.addEventListener('click', function (e) {
        const thumb = e.target.closest('.video-thumb');
        if (!thumb) return;
        const videoSrc = thumb.getAttribute('data-video-src');
        if (!videoSrc) return;
        lightboxVideo.src = videoSrc;
        lightboxVideo.style.display = 'block';
        openLightbox();
    });

    lightbox.addEventListener('click', closeLightbox);

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });

    function openLightbox() {
        lightbox.classList.add('active');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';   // the page must not scroll behind it
    }

    function closeLightbox() {
        lightbox.classList.remove('active');
        lightbox.setAttribute('aria-hidden', 'true');
        lightboxVideo.src = '';                    // stops playback
        document.body.style.overflow = '';
    }
});
