document.addEventListener('DOMContentLoaded', function () {
    const lightbox = document.getElementById('lightbox');
    const lightboxVideo = document.getElementById('lightbox-video');
    const lightboxClose = document.getElementById('lightbox-close');
    const timelineContainer = document.querySelector('.timeline-container');

    if (!lightbox || !lightboxVideo || !timelineContainer) return;

    const playLabel = timelineContainer.getAttribute('data-play-label') || 'Play video';
    let lastFocused = null;

    timelineContainer.querySelectorAll('img.video-thumbnail').forEach(function (img) {
        if (img.parentElement.classList.contains('video-thumb')) return;
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'u-card u-card--interactive video-thumb';
        btn.setAttribute('aria-label', playLabel + ': ' + (img.alt || ''));
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
        lastFocused = thumb;
        lightboxVideo.src = videoSrc;
        lightboxVideo.style.display = 'block';
        openLightbox();
    });

    lightbox.addEventListener('click', function (e) {
        if (e.target === lightbox) closeLightbox();
    });
    lightboxClose && lightboxClose.addEventListener('click', closeLightbox);

    document.addEventListener('keydown', function (e) {
        if (!lightbox.classList.contains('active')) return;
        if (e.key === 'Escape') { closeLightbox(); return; }
        if (e.key === 'Tab' && lightboxClose) { e.preventDefault(); lightboxClose.focus(); }
    });

    function openLightbox() {
        lightbox.classList.add('active');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        lightboxClose && lightboxClose.focus();
    }

    function closeLightbox() {
        lightbox.classList.remove('active');
        lightbox.setAttribute('aria-hidden', 'true');
        lightboxVideo.removeAttribute('src');
        lightboxVideo.style.display = 'none';
        document.body.style.overflow = '';
        if (lastFocused) { lastFocused.focus(); lastFocused = null; }
    }
});
