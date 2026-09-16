(function () {
    var root = document.getElementById('paridata');
    var toggle = document.getElementById('paridata-toggle');
    var units = document.getElementById('paridata-units');
    var money = document.getElementById('paridata-money');
    if (!root || !toggle || !units || !money) return;

    function show(mode) {
        root.setAttribute('data-paridata', mode);
        units.setAttribute('aria-pressed', String(mode === 'units'));
        money.setAttribute('aria-pressed', String(mode === 'money'));
        try { localStorage.setItem('paridata-display', mode); } catch (e) {}
    }

    var saved = 'money';
    try { saved = localStorage.getItem('paridata-display') || 'money'; } catch (e) {}
    toggle.removeAttribute('hidden');
    show(saved === 'units' ? 'units' : 'money');
    units.addEventListener('click', function () { show('units'); });
    money.addEventListener('click', function () { show('money'); });

    var PER_PAGE = 10;
    var rows = document.querySelectorAll('.paridata-row');
    var pager = document.getElementById('paridata-pager');
    var prev = document.getElementById('paridata-prev');
    var next = document.getElementById('paridata-next');
    var label = document.getElementById('paridata-pagelabel');
    if (rows.length <= PER_PAGE || !pager || !prev || !next || !label) return;

    var pages = Math.ceil(rows.length / PER_PAGE);
    var page = 0;

    function paint() {
        for (var i = 0; i < rows.length; i++) {
            var visible = Math.floor(i / PER_PAGE) === page;
            rows[i].hidden = !visible;
            if (!visible) rows[i].open = false;
        }
        label.textContent = (page + 1) + ' / ' + pages;
        prev.disabled = page === 0;
        next.disabled = page === pages - 1;
    }

    pager.removeAttribute('hidden');
    prev.addEventListener('click', function () { page--; paint(); });
    next.addEventListener('click', function () { page++; paint(); });
    paint();
})();
