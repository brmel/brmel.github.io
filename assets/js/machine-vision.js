/* Machine Vision Ecosystem — interactive behavior (BEHAVIOR layer).
   Language-agnostic. Reads the per-language DATA layer (mvChainData, mvLeadersData,
   mvLabels) that each page loads first via customJS, so this single file serves
   every translation. Loaded per-page via the customJS front-matter hook. */

function mvUpdateChain(stageKey) {
    const data = mvChainData[stageKey];
    const panel = document.getElementById('mv-chain-panel');
    if (!data || !panel) return;

    document.querySelectorAll('.mv-chain-step').forEach(btn => btn.classList.remove('active'));
    const activeBtn = document.querySelector(`.mv-chain-step[data-stage="${stageKey}"]`);
    if (activeBtn) activeBtn.classList.add('active');

    panel.innerHTML = `
        <div class="mv-panel-head">
            <h4 class="mv-panel-title">${data.title}</h4>
            <p class="mv-panel-headline">${data.headline}</p>
            <p class="mv-panel-desc">${data.desc}</p>
        </div>

        <div class="mv-content-grid">
            <div>
                <h5 class="mv-dynamics-heading">${mvLabels.dynamics}</h5>
                <ul class="mv-dynamics-list">
                    ${data.dynamics.map(d => `
                        <li>
                            <span class="dot">●</span>
                            <div>
                                <span class="mv-dyn-label">${d.label}</span>
                                <span class="mv-dyn-text">${d.text}</span>
                            </div>
                        </li>
                    `).join('')}
                </ul>
            </div>

            <div class="mv-actors-box">
                <div class="mv-actors-label">${mvLabels.actors}</div>
                <p class="mv-actors-text">${data.actors}</p>
            </div>
        </div>
    `;
}

function mvShowLeaders(type) {
    ['hardware', 'software', 'integrators'].forEach(t => {
        const btn = document.getElementById(`mv-tab-${t}`);
        if (btn) btn.classList.toggle('active', t === type);
    });
    const tbody = document.getElementById('mv-leader-table');
    if (!tbody || !mvLeadersData[type]) return;
    tbody.innerHTML = mvLeadersData[type].map(item => `
        <tr>
            <td class="mv-td-name">${item.name}</td>
            <td class="mv-td-sm">${item.hq}</td>
            <td class="mv-td-sm">${item.spec}</td>
            <td><span class="mv-badge">${item.focus}</span></td>
        </tr>
    `).join('');
}

function mvInit() {
    if (typeof mvChainData !== 'undefined') mvUpdateChain('components');
    if (typeof mvLeadersData !== 'undefined') mvShowLeaders('hardware');
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mvInit);
} else {
    mvInit();
}
