/* Machine Vision Ecosystem — FR content (DATA layer).
   The translatable article content for the interactive chain panels and
   leader tables. Loaded before the shared machine-vision.js logic via this
   page's customJS front matter, so each language renders in its own words. */
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

const mvLabels = {"dynamics": "Dynamique du marché", "actors": "Acteurs mondiaux clés"};
