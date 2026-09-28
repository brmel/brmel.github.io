(() => {
    const root = document.getElementById('paridata');
    const toggle = document.getElementById('paridata-toggle');
    const stakeField = document.getElementById('paridata-stake-field');
    const stakeInput = document.getElementById('paridata-stake');
    const stakeSymbol = document.getElementById('paridata-stake-symbol');
    if (!root || !toggle || !stakeField || !stakeInput || !stakeSymbol) return;

    const phone = window.matchMedia('(max-width: 600px)');
    const buttons = [...toggle.querySelectorAll('button')];
    const defaultButton = buttons[1];
    const amounts = [...root.querySelectorAll('.paridata-amount')].map(el => ({
        el, units: parseFloat(el.dataset.units), signed: el.hasAttribute('data-signed'), inCell: !!el.closest('.paridata-row')
    }));

    let state = { mode: defaultButton.dataset.mode, stakes: {} };
    try {
        const saved = JSON.parse(localStorage.getItem('paridata'));
        if (saved?.stakes) state = saved;
    } catch {}

    const active = () => buttons.find(b => b.dataset.mode === state.mode) || defaultButton;
    const stake = b => state.stakes[b.dataset.mode] >= 0 ? state.stakes[b.dataset.mode] : parseFloat(b.dataset.perUnit);

    const money = (sign, val, opts, btn) => {
        const n = val.toLocaleString(root.dataset.locale, opts);
        const pat = btn.hasAttribute('data-after') ? '{sign}{n}\u00a0{symbol}' : root.dataset.pattern;
        return pat.replace('{sign}', sign).replace('{symbol}', btn.dataset.symbol).replace('{n}', n);
    };

    const format = (amt, btn) => {
        const sign = amt.units < 0 ? '−' : (amt.signed ? '+' : '');
        if (!btn.dataset.symbol) return `${sign}${Math.abs(amt.units).toLocaleString(root.dataset.locale, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}u`;
        const val = Math.abs(amt.units * stake(btn));
        const dec = parseInt(btn.dataset.decimals, 10);
        const fits = [
            { minimumFractionDigits: dec, maximumFractionDigits: dec },
            { maximumFractionDigits: 0 },
            { notation: 'compact', maximumFractionDigits: 1 },
            { notation: 'compact', maximumFractionDigits: 0 }
        ];
        let text = money(sign, val, fits[0], btn);
        const maxLen = phone.matches ? 9 : 11;
        for (let i = 1; amt.inCell && text.length > maxLen && i < fits.length; i++) {
            text = money(sign, val, fits[i], btn);
        }
        return text;
    };

    const paintAmounts = () => {
        const btn = active();
        amounts.forEach(a => { a.el.textContent = format(a, btn); });
        try { localStorage.setItem('paridata', JSON.stringify(state)); } catch {}
    };

    const select = btn => {
        state.mode = btn.dataset.mode;
        buttons.forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
        stakeField.hidden = !btn.dataset.symbol;
        stakeSymbol.textContent = btn.dataset.symbol || '';
        stakeField.toggleAttribute('data-after', btn.hasAttribute('data-after'));
        stakeInput.value = stake(btn);
        paintAmounts();
    };

    buttons.forEach(b => b.addEventListener('click', () => select(b)));
    stakeInput.addEventListener('input', () => {
        const val = parseFloat(stakeInput.value);
        if (Number.isFinite(val) && val >= 0) {
            state.stakes[state.mode] = val;
            paintAmounts();
        }
    });
    stakeInput.addEventListener('change', () => { stakeInput.value = stake(active()); });
    phone.addEventListener('change', paintAmounts);

    toggle.removeAttribute('hidden');
    select(active());

    const PER_PAGE = 10;
    const rows = document.querySelectorAll('.paridata-row');
    const pager = document.getElementById('paridata-pager');
    const prev = document.getElementById('paridata-prev');
    const next = document.getElementById('paridata-next');
    const label = document.getElementById('paridata-pagelabel');
    if (rows.length <= PER_PAGE || !pager || !prev || !next || !label) return;

    const totalPages = Math.ceil(rows.length / PER_PAGE);
    let currentPage = 0;

    const paintPager = () => {
        rows.forEach((row, i) => {
            const visible = Math.floor(i / PER_PAGE) === currentPage;
            row.hidden = !visible;
            if (!visible) row.open = false;
        });
        label.textContent = `${currentPage + 1} / ${totalPages}`;
        prev.disabled = currentPage === 0;
        next.disabled = currentPage === totalPages - 1;
    };

    pager.removeAttribute('hidden');
    prev.addEventListener('click', () => { currentPage--; paintPager(); });
    next.addEventListener('click', () => { currentPage++; paintPager(); });
    paintPager();
})();
