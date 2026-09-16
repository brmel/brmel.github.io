(function () {
    var root = document.getElementById('paridata');
    var toggle = document.getElementById('paridata-toggle');
    var units = document.getElementById('paridata-units');
    var money = document.getElementById('paridata-money');
    if (!root || !toggle || !units || !money) return;

    // The toggle is inert without this script, so it ships hidden and is revealed here.
    toggle.removeAttribute('hidden');

    function show(mode) {
        root.setAttribute('data-paridata', mode);
        units.setAttribute('aria-pressed', mode === 'units' ? 'true' : 'false');
        money.setAttribute('aria-pressed', mode === 'money' ? 'true' : 'false');
        try { localStorage.setItem('paridata-display', mode); } catch (e) {}
    }

    var saved = 'money';
    try { saved = localStorage.getItem('paridata-display') || 'money'; } catch (e) {}
    show(saved === 'units' ? 'units' : 'money');

    units.addEventListener('click', function () { show('units'); });
    money.addEventListener('click', function () { show('money'); });

    // Pagination is an enhancement: with scripts off every row is already on the
    // page, which is the right failure — a ledger should never hide its evidence.
    var PER_PAGE = 10;
    var rows = document.querySelectorAll('.paridata-row');
    var pager = document.getElementById('paridata-pager');
    var prev = document.getElementById('paridata-prev');
    var next = document.getElementById('paridata-next');
    var label = document.getElementById('paridata-pagelabel');

    if (rows.length > PER_PAGE && pager && prev && next && label) {
        var pages = Math.ceil(rows.length / PER_PAGE);
        var page = 0;

        function paint() {
            for (var i = 0; i < rows.length; i++) {
                var on = i >= page * PER_PAGE && i < (page + 1) * PER_PAGE;
                rows[i].hidden = !on;
                if (!on) rows[i].open = false;
            }
            label.textContent = (page + 1) + ' / ' + pages;
            prev.disabled = page === 0;
            next.disabled = page === pages - 1;
        }

        pager.removeAttribute('hidden');
        prev.addEventListener('click', function () { if (page > 0) { page--; paint(); } });
        next.addEventListener('click', function () { if (page < pages - 1) { page++; paint(); } });
        paint();
    }
})();
