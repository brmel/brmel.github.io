(function () {
    var root = document.getElementById('paridata');
    var toggle = document.getElementById('paridata-toggle');
    var stakeField = document.getElementById('paridata-stake-field');
    var stakeInput = document.getElementById('paridata-stake');
    var stakeSymbol = document.getElementById('paridata-stake-symbol');
    if (!root || !toggle || !stakeField || !stakeInput || !stakeSymbol) return;

    var phone = window.matchMedia('(max-width: 600px)');
    var buttons = Array.prototype.slice.call(toggle.querySelectorAll('button'));
    var defaultButton = buttons[1];
    var amounts = Array.prototype.map.call(root.querySelectorAll('.paridata-amount'), function (el) {
        return { el: el, units: parseFloat(el.dataset.units), signed: el.hasAttribute('data-signed'), inCell: !!el.closest('.paridata-row') };
    });
    var state = { mode: defaultButton.dataset.mode, stakes: {} };
    try {
        var saved = JSON.parse(localStorage.getItem('paridata'));
        if (saved && saved.stakes) state = saved;
    } catch (e) {}

    function active() {
        return buttons.filter(function (b) { return b.dataset.mode === state.mode; })[0] || defaultButton;
    }

    function stake(button) {
        var value = state.stakes[button.dataset.mode];
        return value >= 0 ? value : parseFloat(button.dataset.perUnit);
    }

    function money(sign, value, options, button) {
        var n = value.toLocaleString(root.dataset.locale, options);
        var pattern = button.hasAttribute('data-after') ? '{sign}{n}\u00a0{symbol}' : root.dataset.pattern;
        return pattern.replace('{sign}', sign).replace('{symbol}', button.dataset.symbol).replace('{n}', n);
    }

    function format(amount, button) {
        var sign = amount.units < 0 ? '−' : (amount.signed ? '+' : '');
        if (!button.dataset.symbol) return sign + Math.abs(amount.units).toLocaleString(root.dataset.locale, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + 'u';
        var value = Math.abs(amount.units * stake(button));
        var decimals = parseInt(button.dataset.decimals, 10);
        var fits = [
            { minimumFractionDigits: decimals, maximumFractionDigits: decimals },
            { maximumFractionDigits: 0 },
            { notation: 'compact', maximumFractionDigits: 1 },
            { notation: 'compact', maximumFractionDigits: 0 }
        ];
        var text = money(sign, value, fits[0], button);
        var cellChars = phone.matches ? 9 : 11;
        for (var i = 1; amount.inCell && text.length > cellChars && i < fits.length; i++) {
            text = money(sign, value, fits[i], button);
        }
        return text;
    }

    function paintAmounts() {
        var button = active();
        amounts.forEach(function (amount) { amount.el.textContent = format(amount, button); });
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

    phone.addEventListener('change', paintAmounts);
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
