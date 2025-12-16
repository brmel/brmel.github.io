---
title: "L'Écosystème Mondial de la Vision Industrielle"
date: 2025-12-14
tags: ["Vision Industrielle", "Analyse de Marché", "Écosystème", "Automatisation"]
summary: "Une exploration interactive du marché mondial de la vision industrielle — des fournisseurs de composants aux utilisateurs finaux."
cover:
    image: "/tech/machine-vision-ecosystem/market_overview.jpg"
    alt: "Vue d'ensemble du marché"
    relative: false
---

Le marché de la vision industrielle n'est pas un bloc monolithique : c'est un **écosystème hautement spécialisé et structuré en niveaux**, conçu pour transformer la lumière brute en données industrielles exploitables.

<style>
    .mv-tab-active {
        border-bottom: 2px solid var(--primary, #2563EB);
        color: var(--content, #1E293B);
        font-weight: 600;
    }
    .mv-tab-inactive {
        color: var(--secondary, #64748B);
        border-bottom: 2px solid transparent;
    }
    .mv-tab-inactive:hover {
        color: var(--content, #334155);
    }

    /* Flow Connector Logic for large screens */
    @media (min-width: 768px) {
        .mv-chain-step::after {
            content: '→';
            position: absolute;
            right: -14px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 24px;
            color: var(--border, #CBD5E1);
            z-index: 10;
        }
        .mv-chain-step:last-child::after {
            display: none;
        }
    }

    .mv-card {
        background: var(--entry, #fff);
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid var(--border, #e2e8f0);
        transition: box-shadow 0.2s;
    }
    .mv-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .mv-chain-step {
        background: var(--entry, #fff);
        border: 1px solid var(--border, #e2e8f0);
        border-radius: 0.5rem;
        padding: 1rem;
        text-align: left;
        cursor: pointer;
        position: relative;
        transition: all 0.2s;
    }
    .mv-chain-step:hover {
        border-color: var(--primary, #2563EB);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .mv-chain-step.active {
        border-color: var(--primary, #2563EB);
        box-shadow: 0 0 0 2px var(--primary, #2563EB);
        background: color-mix(in srgb, var(--primary, #2563EB) 5%, var(--entry, #fff));
    }

    .mv-panel {
        background: var(--entry, #fff);
        border-radius: 0.75rem;
        border: 1px solid var(--border, #e2e8f0);
        padding: 2rem;
        min-height: 300px;
    }

    .mv-grid-3 {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        gap: 1.5rem;
        margin-top: 1.5rem;
    }
    @media (min-width: 768px) {
        .mv-grid-3 {
            grid-template-columns: repeat(3, 1fr);
        }
    }

    .mv-grid-5 {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    @media (min-width: 768px) {
        .mv-grid-5 {
            grid-template-columns: repeat(5, 1fr);
        }
    }

    .mv-icon {
        font-size: 1.5rem;
        margin-bottom: 0.75rem;
    }

    .mv-step-label {
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--secondary, #64748B);
        margin-bottom: 0.25rem;
    }

    .mv-step-title {
        font-weight: 700;
        color: var(--content, #1e293b);
    }

    .mv-step-subtitle {
        font-size: 0.75rem;
        color: var(--secondary, #64748B);
        margin-top: 0.5rem;
    }

    .mv-section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--content, #1e293b);
        margin-bottom: 0.5rem;
        border-left: 4px solid var(--primary, #2563EB);
        padding-left: 1rem;
    }

    .mv-section-subtitle {
        font-size: 0.875rem;
        color: var(--secondary, #64748B);
        margin-bottom: 1.5rem;
    }

    .mv-tab-container {
        display: flex;
        gap: 0.5rem;
        background: var(--code-bg, #f1f5f9);
        padding: 0.25rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }

    .mv-tab-btn {
        padding: 0.5rem 1rem;
        font-size: 0.875rem;
        border-radius: 0.375rem;
        transition: all 0.2s;
        font-weight: 500;
        border: none;
        cursor: pointer;
        background: transparent;
        color: var(--secondary, #64748B);
    }
    .mv-tab-btn:hover {
        background: var(--border, #e2e8f0);
    }
    .mv-tab-btn.active {
        background: var(--primary, #2563EB);
        color: white;
    }

    .mv-table {
        width: 100%;
        text-align: left;
        font-size: 0.875rem;
        border-collapse: collapse;
    }
    .mv-table thead {
        background: var(--code-bg, #f8fafc);
        border-bottom: 1px solid var(--border, #e2e8f0);
    }
    .mv-table th {
        padding: 1rem 1.5rem;
        font-weight: 600;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--secondary, #64748B);
    }
    .mv-table td {
        padding: 1rem 1.5rem;
        border-bottom: 1px solid var(--border, #f1f5f9);
    }
    .mv-table tbody tr:hover {
        background: var(--code-bg, #f8fafc);
    }

    .mv-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
        background: color-mix(in srgb, var(--primary, #2563EB) 15%, transparent);
        color: var(--primary, #2563EB);
    }

    .mv-actors-box {
        background: var(--code-bg, #f8fafc);
        padding: 1.25rem;
        border-radius: 0.5rem;
        border: 1px solid var(--border, #e2e8f0);
    }
    .mv-actors-label {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--secondary, #64748B);
        margin-bottom: 0.5rem;
    }

    .mv-dynamics-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .mv-dynamics-list li {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1rem;
    }
    .mv-dynamics-list .dot {
        color: var(--primary, #2563EB);
        margin-right: 0.75rem;
        margin-top: 0.25rem;
    }

    .mv-content-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    @media (min-width: 768px) {
        .mv-content-grid {
            grid-template-columns: 1fr 1fr;
        }
    }
</style>

## Vue d'ensemble du marché

<div style="margin: 2rem 0; text-align: center;">
    <img src="/tech/machine-vision-ecosystem/market_overview.jpg" alt="Vue d'ensemble du marché" style="max-width: 100%; width: 100%; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
</div>

<div class="mv-grid-3">
    <div class="mv-card">
        <div class="mv-icon">⚗️</div>
        <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Fragmentation et spécialisation</h3>
        <p style="font-size: 0.875rem; color: var(--secondary);">Contrairement à l'électronique grand public, aucune entreprise ne maîtrise l'ensemble de la chaîne. Un expert en optique (ex. Fujinon) fabrique rarement des logiciels, et un spécialiste logiciel (ex. MVTec) construit rarement des robots. Cela nécessite un solide réseau de <strong>partenariats et d'intégration</strong>.</p>
    </div>
    <div class="mv-card">
        <div class="mv-icon">🧩</div>
        <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Le défi de l'intégration</h3>
        <p style="font-size: 0.875rem; color: var(--secondary);">Les systèmes de vision ne sont pas « plug and play » comme une webcam. Ils nécessitent un éclairage précis, une calibration et une programmation logique. Cette complexité crée un marché considérable pour les <strong>intégrateurs de systèmes</strong> qui font le lien entre les fabricants de matériel et les usines.</p>
    </div>
    <div class="mv-card">
        <div class="mv-icon">⚙️</div>
        <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Des pixels aux décisions</h3>
        <p style="font-size: 0.875rem; color: var(--secondary);">La chaîne de valeur suit un flux linéaire : <strong>Composant</strong> (Capture) → <strong>Système</strong> (Traitement) → <strong>Application</strong> (Décision). L'industrie transfère actuellement la valeur de la commoditisation du matériel vers l'intelligence logicielle et l'IA.</p>
    </div>
</div>

---

## La chaîne de valeur : du photon à l'usine

<p class="mv-section-subtitle">Cliquez sur chaque étape pour comprendre sa fonction, sa dynamique de marché et son contexte opérationnel.</p>

<div style="margin: 2rem 0; text-align: center;">
    <img src="/tech/machine-vision-ecosystem/value_chain.jpg" alt="Chaîne de valeur" style="max-width: 100%; width: 100%; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
</div>

<div class="mv-grid-5">
    <button data-stage="components" onclick="mvUpdateChain('components')" class="mv-chain-step">
        <div class="mv-step-label">Niveau 1</div>
        <div class="mv-step-title">Composant</div>
        <div class="mv-step-subtitle">Capteurs et optique</div>
    </button>
    <button data-stage="systems" onclick="mvUpdateChain('systems')" class="mv-chain-step">
        <div class="mv-step-label">Niveau 2</div>
        <div class="mv-step-title">Système de vision</div>
        <div class="mv-step-subtitle">Caméras et logiciels</div>
    </button>
    <button data-stage="distribution" onclick="mvUpdateChain('distribution')" class="mv-chain-step">
        <div class="mv-step-label">Niveau 3</div>
        <div class="mv-step-title">Distribution</div>
        <div class="mv-step-subtitle">Partenaires de distribution</div>
    </button>
    <button data-stage="integrators" onclick="mvUpdateChain('integrators')" class="mv-chain-step">
        <div class="mv-step-label">Niveau 4</div>
        <div class="mv-step-title">Intégrateur</div>
        <div class="mv-step-subtitle">Constructeurs de machines</div>
    </button>
    <button data-stage="endusers" onclick="mvUpdateChain('endusers')" class="mv-chain-step">
        <div class="mv-step-label">Niveau 5</div>
        <div class="mv-step-title">Utilisateur final</div>
        <div class="mv-step-subtitle">Clients industriels</div>
    </button>
</div>

<div id="mv-chain-panel" class="mv-panel">
    <!-- Content injected by JS -->
</div>

---

## Les leaders mondiaux du marché

<p class="mv-section-subtitle">Classement des acteurs dominants dans le matériel, les logiciels et l'intégration de systèmes.</p>

<div style="margin: 2rem 0; text-align: center;">
    <img src="/tech/machine-vision-ecosystem/market_leaders.jpg" alt="Leaders du marché" style="max-width: 100%; width: 100%; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
</div>

<div class="mv-tab-container">
    <button onclick="mvShowLeaders('hardware')" id="mv-tab-hardware" class="mv-tab-btn active">Matériel</button>
    <button onclick="mvShowLeaders('software')" id="mv-tab-software" class="mv-tab-btn">Logiciels</button>
    <button onclick="mvShowLeaders('integrators')" id="mv-tab-integrators" class="mv-tab-btn">Intégrateurs</button>
</div>

<div class="mv-card" style="padding: 0; overflow: hidden;">
    <div style="overflow-x: auto;">
        <table class="mv-table">
            <thead>
                <tr>
                    <th>Entreprise</th>
                    <th>Siège social</th>
                    <th>Expertise principale</th>
                    <th>Marché cible</th>
                </tr>
            </thead>
            <tbody id="mv-leader-table">
                <!-- Rows injected by JS -->
            </tbody>
        </table>
    </div>
</div>

<script>
// Données de l'article Vision Industrielle
const mvChainData = {
    components: {
        title: "1. Fournisseurs de composants (Les matières premières)",
        headline: "La couche fondamentale dominée par l'optique et la physique des semi-conducteurs.",
        desc: "Cette étape se concentre sur la capture physique de l'information. Elle se caractérise par de fortes barrières techniques à l'entrée — fabriquer un capteur d'image de haute qualité ou un objectif télécentrique nécessite une infrastructure de R&D massive. Ces entreprises vendent généralement aux fabricants de 'Systèmes' (Étape 2) plutôt qu'aux usines directement.",
        dynamics: [
            { label: "Structure du marché", text: "Très consolidé pour les capteurs (Sony détient plus de 50% des parts) ; fragmenté pour l'éclairage et les objectifs." },
            { label: "Défi principal", text: "Équilibrer la résolution (Mégapixels), la vitesse (IPS) et la sensibilité." },
            { label: "Pourquoi c'est important", text: "Le logiciel ne peut pas traiter ce que la caméra ne voit pas. La qualité de toute la chaîne dépend de cette première étape." }
        ],
        actors: "Sony, Teledyne e2v, ON Semi (Capteurs) ; Fujinon, Moritex, Tamron (Optique) ; CCS, Smart Vision Lights (Éclairage)."
    },
    systems: {
        title: "2. Systèmes de vision et matériel (Le « cerveau »)",
        headline: "Là où le matériel rencontre la logique. Le secteur le plus compétitif du marché.",
        desc: "Cette étape intègre les composants bruts en un produit utilisable. Elle couvre les 'Caméras intelligentes' (unités tout-en-un avec processeurs intégrés) jusqu'aux caméras PC (GigE/USB) nécessitant des ordinateurs externes. Ces acteurs stimulent l'innovation en facilité d'utilisation et en format.",
        dynamics: [
            { label: "Tendance actuelle", text: "Virage vers la 'Vision embarquée' et le Deep Learning en périphérie (à l'intérieur de la caméra)." },
            { label: "Concurrence", text: "Rivalité féroce entre les entreprises américaines (Zebra/Cognex), japonaises (Keyence/Omron) et européennes (Basler)." },
            { label: "Types de produits", text: "Caméras intelligentes, lecteurs d'identifiants, profileurs 3D, caméras thermiques." }
        ],
        actors: "Zebra, Cognex, Keyence, Basler, Teledyne FLIR, Omron, Hikrobot, TKH Group."
    },
    distribution: {
        title: "3. Distribution et partenaires de distribution (Le pont)",
        headline: "Le ciment logistique et consultatif de l'écosystème.",
        desc: "Parce que le marché est mondial mais la fragmentation élevée, les fabricants s'appuient sur des distributeurs locaux. Ce ne sont pas de simples transporteurs de boîtes ; ce sont des distributeurs à valeur ajoutée (VAD) qui fournissent conseils, calculs d'optique et études de faisabilité aux intégrateurs locaux manquant parfois d'expertise en physique optique.",
        dynamics: [
            { label: "Proposition de valeur", text: "Ils agrègent des composants de plusieurs marques (ex. un capteur Sony dans une caméra Basler avec un objectif Fujinon) pour créer un kit compatible." },
            { label: "Rôle géographique", text: "Crucial pour pénétrer les marchés fragmentés comme l'Europe et l'Asie." }
        ],
        actors: "Stemmer Imaging, Framos, 1stVision, Mid-Atlantic Computer Vision, China Daheng Group."
    },
    integrators: {
        title: "4. Intégrateurs de systèmes et constructeurs de machines (Les bâtisseurs)",
        headline: "L'ingénierie sur mesure pour intégrer la vision dans la ligne de production.",
        desc: "Les usines achètent rarement une caméra pour l'installer elles-mêmes. Elles font appel à des intégrateurs (SI) ou achètent des machines auprès d'équipementiers (OEM). L'intégrateur conçoit le montage mécanique, écrit la logique PLC, intègre le logiciel de vision et garantit le taux de « Conforme/Non-conforme ».",
        dynamics: [
            { label: "Profil de risque", text: "Ils assument le risque opérationnel. Si le système ne détecte pas un défaut, l'intégrateur est responsable." },
            { label: "Spécialisation", text: "Très spécifique par secteur. Un intégrateur automobile fait rarement de l'inspection pharmaceutique." }
        ],
        actors: "ATS Automation, JR Automation, Vanderlande, KUKA, Rockwell Partners, Beckhoff."
    },
    endusers: {
        title: "5. Utilisateurs finaux (La création de valeur)",
        headline: "Les géants de l'industrie et de la logistique qui tirent la demande.",
        desc: "L'étape finale où la technologie génère un retour sur investissement. Les utilisateurs finaux déploient la vision pour trois raisons principales : le contrôle qualité (détection des défauts), la traçabilité (lecture de codes-barres/suivi) et l'automatisation (guidage de robots).",
        dynamics: [
            { label: "Secteurs moteurs", text: "Électronique (miniaturisation), automobile (transition vers l'électrique), logistique (vitesse du e-commerce)." },
            { label: "Frein à l'adoption", text: "Coût initial élevé et complexité de la maintenance." }
        ],
        actors: "Tesla, Apple, TSMC, Amazon, Nestlé, Pfizer, Samsung, Volkswagen."
    }
};

const mvLeadersData = {
    hardware: [
        { rank: 1, name: "Zebra Technologies", hq: "États-Unis", spec: "Scanners industriels fixes", focus: "Logistique et distribution" },
        { rank: 2, name: "Cognex", hq: "États-Unis", spec: "Caméras intelligentes et ID", focus: "Logistique et électronique" },
        { rank: 3, name: "Keyence", hq: "Japon", spec: "Capteurs et mesure", focus: "Automatisation (vente directe)" },
        { rank: 4, name: "Basler", hq: "Allemagne", spec: "Caméras matricielles", focus: "Fabrication de volume et embarqué" },
        { rank: 5, name: "Teledyne Technologies", hq: "États-Unis", spec: "Imagerie thermique et scientifique", focus: "Aérospatiale et industriel" },
        { rank: 6, name: "Omron", hq: "Japon", spec: "Écosystèmes d'automatisation", focus: "Automobile et électronique" },
        { rank: 7, name: "TKH Group", hq: "Pays-Bas", spec: "Vision 3D (LMI/Allied)", focus: "Métrologie et inspection" },
        { rank: 8, name: "Baumer", hq: "Suisse", spec: "Caméras industrielles", focus: "Agroalimentaire et pharma" },
        { rank: 9, name: "Hikrobot", hq: "Chine", spec: "Robots mobiles et vision", focus: "Logistique et fabrication" },
        { rank: 10, name: "Daheng Imaging", hq: "Chine", spec: "Composants et systèmes", focus: "Marché asiatique" }
    ],
    software: [
        { rank: 1, name: "Matrox Imaging (Zebra)", hq: "Canada", spec: "Bibliothèque MIL", focus: "Semi-conducteurs et médical" },
        { rank: 2, name: "MVTec (HALCON)", hq: "Allemagne", spec: "Algorithmes avancés", focus: "Applications PC haut de gamme" },
        { rank: 3, name: "Cognex (VisionPro)", hq: "États-Unis", spec: "Deep Learning et règles", focus: "Intégration usine" },
        { rank: 4, name: "Stemmer (CVB)", hq: "Allemagne", spec: "Common Vision Bloch", focus: "Développement multi-matériel" },
        { rank: 5, name: "Euresys (Open eVision)", hq: "Belgique", spec: "Bibliothèques et IP Cores", focus: "Inspection haute vitesse" },
        { rank: 6, name: "National Instruments", hq: "États-Unis", spec: "LabVIEW Vision", focus: "Test et mesure" },
        { rank: 7, name: "Landing AI", hq: "États-Unis", spec: "Visual Prompting / IA", focus: "Inspection Cloud/Edge" },
        { rank: 8, name: "Scikit-image / OpenCV", hq: "Mondial", spec: "Bibliothèques open source", focus: "R&D et prototypage" },
        { rank: 9, name: "Adaptive Vision", hq: "Pologne", spec: "Logiciel graphique", focus: "Déploiement rapide" },
        { rank: 10, name: "NeuroCheck", hq: "Allemagne", spec: "Logiciel applicatif", focus: "Contrôle qualité automobile" }
    ],
    integrators: [
        { rank: 1, name: "ATS Automation", hq: "Canada", spec: "Intégration complète", focus: "Sciences de la vie et batteries VE" },
        { rank: 2, name: "JR Automation", hq: "États-Unis", spec: "Assemblage robotisé", focus: "Automobile général" },
        { rank: 3, name: "Vanderlande", hq: "Pays-Bas", spec: "Systèmes logistiques", focus: "Aéroports et entrepôts" },
        { rank: 4, name: "KUKA Systems", hq: "Allemagne", spec: "Robotique", focus: "Carrosserie et peinture auto" },
        { rank: 5, name: "Rockwell Automation", hq: "États-Unis", spec: "Systèmes de contrôle", focus: "Industrie nord-américaine" },
        { rank: 6, name: "Siemens", hq: "Allemagne", spec: "Automatisation industrielle", focus: "Industrie 4.0 européenne" },
        { rank: 7, name: "Daifuku", hq: "Japon", spec: "Manutention", focus: "Semi-conducteurs et logistique" },
        { rank: 8, name: "Bastian Solutions", hq: "États-Unis", spec: "Chaîne logistique", focus: "Distribution retail" },
        { rank: 9, name: "Dematic", hq: "États-Unis", spec: "Intralogistique", focus: "Entreposage mondial" },
        { rank: 10, name: "PIA Automation", hq: "Allemagne", spec: "Systèmes d'assemblage", focus: "Mobilité et biens de consommation" }
    ]
};

// Chain Focus Update
function mvUpdateChain(stageKey) {
    const data = mvChainData[stageKey];
    const panel = document.getElementById('mv-chain-panel');
    
    // Reset all buttons
    document.querySelectorAll('.mv-chain-step').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Set active button
    const activeBtn = document.querySelector(`.mv-chain-step[data-stage="${stageKey}"]`);
    if (activeBtn) {
        activeBtn.classList.add('active');
    }

    panel.innerHTML = `
        <div style="border-bottom: 1px solid var(--border, #e2e8f0); padding-bottom: 1rem; margin-bottom: 1.5rem;">
            <h4 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;">${data.title}</h4>
            <p style="color: var(--primary, #2563EB); font-weight: 500; font-style: italic; margin-bottom: 0.75rem;">${data.headline}</p>
            <p style="color: var(--secondary, #64748B); line-height: 1.6;">${data.desc}</p>
        </div>

        <div class="mv-content-grid">
            <div>
                <h5 style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--secondary, #64748B); margin-bottom: 1rem;">Dynamique du marché</h5>
                <ul class="mv-dynamics-list">
                    ${data.dynamics.map(d => `
                        <li>
                            <span class="dot">●</span>
                            <div>
                                <span style="font-weight: 600; display: block; font-size: 0.875rem;">${d.label}</span>
                                <span style="font-size: 0.875rem; color: var(--secondary, #64748B);">${d.text}</span>
                            </div>
                        </li>
                    `).join('')}
                </ul>
            </div>
            
            <div class="mv-actors-box">
                <div class="mv-actors-label">Acteurs mondiaux clés</div>
                <p style="font-size: 0.875rem; font-weight: 500; line-height: 1.6;">${data.actors}</p>
            </div>
        </div>
    `;
}

// Leaders Tab Update
function mvShowLeaders(type) {
    ['hardware', 'software', 'integrators'].forEach(t => {
        const btn = document.getElementById(`mv-tab-${t}`);
        if (t === type) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    const tbody = document.getElementById('mv-leader-table');
    tbody.innerHTML = '';

    mvLeadersData[type].forEach(item => {
        const row = `
            <tr>
                <td style="font-weight: 700;">${item.name}</td>
                <td style="font-size: 0.875rem;">${item.hq}</td>
                <td style="font-size: 0.875rem;">${item.spec}</td>
                <td><span class="mv-badge">${item.focus}</span></td>
            </tr>
        `;
        tbody.insertAdjacentHTML('beforeend', row);
    });
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', function() {
    mvUpdateChain('components');
    mvShowLeaders('hardware');
});

// Also initialize immediately if DOM is already loaded
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(function() {
        mvUpdateChain('components');
        mvShowLeaders('hardware');
    }, 100);
}
</script>
