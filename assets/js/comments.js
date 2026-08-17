document.addEventListener('DOMContentLoaded', function () {
    var mount = document.querySelector('.comments__mount');
    if (!mount) return;

    var light = mount.dataset.themeLight;
    var dark = mount.dataset.themeDark;

    function current() {
        return document.body.classList.contains('dark') ? dark : light;
    }

    /* Built here rather than in the template: the theme is a runtime fact. A
       static data-theme would load the widget in light, then flip it a beat
       later for every reader who prefers dark. */
    var s = document.createElement('script');
    s.src = 'https://giscus.app/client.js';
    s.crossOrigin = 'anonymous';
    s.async = true;
    var attrs = {
        'data-repo': mount.dataset.repo,
        'data-repo-id': mount.dataset.repoId,
        'data-category': mount.dataset.category,
        'data-category-id': mount.dataset.categoryId,
        'data-mapping': 'pathname',
        'data-strict': '1',
        'data-reactions-enabled': '1',
        'data-emit-metadata': '0',
        'data-input-position': 'top',
        'data-lang': mount.dataset.lang,
        'data-loading': 'lazy',
        'data-theme': current()
    };
    Object.keys(attrs).forEach(function (k) { s.setAttribute(k, attrs[k]); });
    mount.appendChild(s);

    function send(theme) {
        var frame = document.querySelector('iframe.giscus-frame');
        if (!frame) return;
        frame.contentWindow.postMessage(
            { giscus: { setConfig: { theme: theme } } },
            'https://giscus.app'
        );
    }

    new MutationObserver(function () { send(current()); })
        .observe(document.body, { attributes: true, attributeFilter: ['class'] });
});
