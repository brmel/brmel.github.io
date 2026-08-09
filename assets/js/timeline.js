document.addEventListener('DOMContentLoaded', function () {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxVideo = document.getElementById('lightbox-video');
    const timelineContainer = document.querySelector('.timeline-container');

    if (!lightbox || !lightboxImg || !lightboxVideo || !timelineContainer) return;

    /* Give every video thumbnail a real button wrapper.

       The markdown only carries a bare <img class="video-thumbnail">, so there
       is nowhere to hang a play badge or a focus ring. Wrapping at runtime
       keeps the content files simple and makes the thumbnails keyboard
       reachable — they open a video, so they have to be buttons, not images. */
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

    // Event Delegation: Handle clicks on images and video thumbnails
    timelineContainer.addEventListener('click', function (e) {
        const target = e.target;

        // Handle Video Thumbnails (click lands on the wrapper, the img or the badge)
        const thumb = target.closest('.video-thumb');
        if (thumb) {
            const videoSrc = thumb.getAttribute('data-video-src');
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
