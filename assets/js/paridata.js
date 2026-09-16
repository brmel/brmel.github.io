(function () {
    var root = document.getElementById('paridata');
    var toggle = document.getElementById('paridata-toggle');
    var stakeField = document.getElementById('paridata-stake-field');
    var stakeInput = document.getElementById('paridata-stake');
    var stakeSymbol = document.getElementById('paridata-stake-symbol');
    if (!root || !toggle || !stakeField || !stakeInput || !stakeSymbol) return;

    var buttons = Array.prototype.slice.call(toggle.querySelectorAll('button'));
    var amounts = root.querySelectorAll('.paridata-amount');
    var state = { mode: buttons[1].dataset.mode, stakes: {} };
    try {
        var saved = JSON.parse(localStorage.getItem('paridata'));
        if (saved && saved.stakes) state = saved;
    } catch (e) {}

    function active() {
        return buttons.filter(function (b) { return b.dataset.mode === state.mode; })[0] || buttons[1];
    }

    function stake(button) {
        var value = state.stakes[button.dataset.mode];
        return value >= 0 ? value : parseFloat(button.dataset.perUnit);
    }

    function format(units, signed, button, compact) {
        var sign = units < 0 ? '−' : (signed ? '+' : '');
        if (!button.dataset.symbol) return sign + Math.abs(units).toFixed(2) + 'u';
        var decimals = parseInt(button.dataset.decimals, 10);
        var value = Math.abs(units * stake(button));
        if (compact && value >= 1000) decimals = 0;
        var n = compact && value >= 10000
            ? value.toLocaleString('en-US', { notation: 'compact', maximumFractionDigits: value >= 100000 ? 0 : 1 })
            : value.toLocaleString('en-US', { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
        return button.hasAttribute('data-after') ? sign + n + ' ' + button.dataset.symbol : sign + button.dataset.symbol + n;
    }

    function paintAmounts() {
        var button = active();
        for (var i = 0; i < amounts.length; i++) {
            amounts[i].textContent = format(parseFloat(amounts[i].dataset.units), amounts[i].hasAttribute('data-signed'), button, !!amounts[i].closest('.paridata-row'));
        }
        try { localStorage.setItem('paridata', JSON.stringify(state)); } catch (e) {}
    }

    function select(button) {
        state.mode = button.dataset.mode;
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b === button)); });
        stakeField.hidden = !button.dataset.symbol;
        stakeSymbol.textContent = button.dataset.symbol || '';
        stakeField.toggleAttribute('data-after', button.hasAttribute('data-after'));
        stakeInput.value = stake(button);
        paintAmounts();
    }

    buttons.forEach(function (b) { b.addEventListener('click', function () { select(b); }); });
    stakeInput.addEventListener('input', function () {
        var value = parseFloat(stakeInput.value);
        if (!isFinite(value) || value < 0) return;
        state.stakes[state.mode] = value;
        paintAmounts();
    });
    stakeInput.addEventListener('change', function () { stakeInput.value = stake(active()); });

    toggle.removeAttribute('hidden');
    select(active());

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
