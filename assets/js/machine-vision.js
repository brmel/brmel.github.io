// Machine Vision Ecosystem — interactive tab switching.
// Layer: behavior. Loaded per-page via the customJS front-matter hook
// (layouts/partials/extend_footer.html).

// Machine Vision Article Data
const mvChainData = {
    components: {
        title: "1. Component Providers (The Raw Materials)",
        headline: "The foundational layer dominated by optics and semiconductor physics.",
        desc: "This stage focuses on the physical capture of information. It is characterized by high technical barriers to entry—manufacturing a high-quality image sensor or a telecentric lens requires massive R&D infrastructure. These companies generally sell to the 'System' makers (Stage 2) rather than directly to factories.",
        dynamics: [
            { label: "Market Structure", text: "Highly consolidated for sensors (Sony holds >50% share); fragmented for lighting and lenses." },
            { label: "Key Challenge", text: "Balancing resolution (Megapixels) with speed (FPS) and sensitivity." },
            { label: "Why it matters", text: "Software cannot process what the camera cannot see. The quality of the entire chain depends on this first step." }
        ],
        actors: "Sony, Teledyne e2v, ON Semi (Sensors); Fujinon, Moritex, Tamron (Optics); CCS, Smart Vision Lights (Illumination)."
    },
    systems: {
        title: "2. Vision Systems & Hardware (The 'Brain')",
        headline: "Where hardware meets logic. The most competitive sector of the market.",
        desc: "This stage integrates the raw components into a usable product. It spans from 'Smart Cameras' (all-in-one units with embedded processors) to PC-based cameras (GigE/USB) that require external computers. These players drive innovation in ease-of-use and form factor.",
        dynamics: [
            { label: "Current Trend", text: "Shift toward 'Embedded Vision' and Deep Learning on the edge (inside the camera)." },
            { label: "Competition", text: "Fierce rivalry between American (Zebra/Cognex), Japanese (Keyence/Omron), and European (Basler) firms." },
            { label: "Product Types", text: "Smart Cameras, ID Readers, 3D Profilers, Thermal Cameras." }
        ],
        actors: "Zebra, Cognex, Keyence, Basler, Teledyne FLIR, Omron, Hikrobot, TKH Group."
    },
    distribution: {
        title: "3. Distribution & Channel Partners (The Bridge)",
        headline: "The logistical and consultative glue of the ecosystem.",
        desc: "Because the market is global but fragmentation is high, manufacturers rely on local distributors. These are not just box-movers; they are Value-Added Distributors (VADs) who provide consulting, lens calculation, and feasibility studies to local integrators who may lack deep optical physics knowledge.",
        dynamics: [
            { label: "Value Proposition", text: "They aggregate components from multiple brands (e.g., a Sony sensor inside a Basler camera with a Fujinon lens) to create a compatible kit." },
            { label: "Geographic Role", text: "Crucial for penetrating fragmented markets like Europe and Asia." }
        ],
        actors: "Stemmer Imaging, Framos, 1stVision, Mid-Atlantic Computer Vision, China Daheng Group."
    },
    integrators: {
        title: "4. System Integrators & Machine Builders (The Builders)",
        headline: "Custom engineering to fit vision into the production line.",
        desc: "Factories rarely buy a camera and install it themselves. They hire Integrators (SIs) or buy machines from OEMs (Original Equipment Manufacturers). The SI designs the mechanical mounting, writes the PLC logic, integrates the vision software, and guarantees the 'Pass/Fail' rate.",
        dynamics: [
            { label: "Risk Profile", text: "They bear the operational risk. If the system fails to detect a defect, the Integrator is liable." },
            { label: "Specialization", text: "Highly vertical-specific. An automotive integrator rarely does pharmaceutical inspection." }
        ],
        actors: "ATS Automation, JR Automation, Vanderlande, KUKA, Rockwell Partners, Beckhoff."
    },
    endusers: {
        title: "5. End Users (The Value Realization)",
        headline: "The manufacturing and logistics giants driving demand.",
        desc: "The final step where the technology generates ROI. End users implement vision for three main reasons: Quality Control (detecting defects), Traceability (reading barcodes/Tracking), and Automation (robot guidance).",
        dynamics: [
            { label: "Industry Drivers", text: "Electronics (Miniaturization), Automotive (EV transition), Logistics (E-commerce speed)." },
            { label: "Adoption Hurdle", text: "High initial cost and complexity of maintenance." }
        ],
        actors: "Tesla, Apple, TSMC, Amazon, Nestlé, Pfizer, Samsung, Volkswagen."
    }
};

const mvLeadersData = {
    hardware: [
        { rank: 1, name: "Zebra Technologies", hq: "USA", spec: "Fixed Industrial Scanning", focus: "Logistics & Retail Supply Chain" },
        { rank: 2, name: "Cognex", hq: "USA", spec: "Smart Cameras & ID", focus: "Logistics & Electronics" },
        { rank: 3, name: "Keyence", hq: "Japan", spec: "Sensors & Measurement", focus: "Factory Automation (Direct Sales)" },
        { rank: 4, name: "Basler", hq: "Germany", spec: "Area Scan Cameras", focus: "Volume Manufacturing & Embedded" },
        { rank: 5, name: "Teledyne Technologies", hq: "USA", spec: "Thermal & Scientific Imaging", focus: "Aerospace & Industrial" },
        { rank: 6, name: "Omron", hq: "Japan", spec: "Automation Ecosystems", focus: "Automotive & Electronics" },
        { rank: 7, name: "TKH Group", hq: "Netherlands", spec: "3D Vision (LMI/Allied)", focus: "Metrology & inspection" },
        { rank: 8, name: "Baumer", hq: "Switzerland", spec: "Industrial Cameras", focus: "Food, Bev & Pharma" },
        { rank: 9, name: "Hikrobot", hq: "China", spec: "Mobile Robots & Vision", focus: "Logistics & Manufacturing" },
        { rank: 10, name: "Daheng Imaging", hq: "China", spec: "Components & Systems", focus: "Asian Domestic Market" }
    ],
    software: [
        { rank: 1, name: "Matrox Imaging (Zebra)", hq: "Canada", spec: "MIL Library", focus: "Semiconductor & Medical" },
        { rank: 2, name: "MVTec (HALCON)", hq: "Germany", spec: "Advanced Algorithms", focus: "High-end PC Vision Applications" },
        { rank: 3, name: "Cognex (VisionPro)", hq: "USA", spec: "Deep Learning & Rules", focus: "Factory Integration" },
        { rank: 4, name: "Stemmer (CVB)", hq: "Germany", spec: "Common Vision Bloch", focus: "Hardware-agnostic Development" },
        { rank: 5, name: "Euresys (Open eVision)", hq: "Belgium", spec: "Libraries & IP Cores", focus: "High-speed inspection" },
        { rank: 6, name: "National Instruments", hq: "USA", spec: "LabVIEW Vision", focus: "Test & Measurement" },
        { rank: 7, name: "Landing AI", hq: "USA", spec: "Visual Prompting / AI", focus: "Cloud/Edge AI Inspection" },
        { rank: 8, name: "Scikit-image / OpenCV", hq: "Global", spec: "Open Source Libraries", focus: "R&D and Prototyping" },
        { rank: 9, name: "Adaptive Vision", hq: "Poland", spec: "Graphical Software", focus: "Rapid Deployment" },
        { rank: 10, name: "NeuroCheck", hq: "Germany", spec: "Application Software", focus: "Automotive Quality Control" }
    ],
    integrators: [
        { rank: 1, name: "ATS Automation", hq: "Canada", spec: "Full Line Integration", focus: "Life Sciences & EV Battery" },
        { rank: 2, name: "JR Automation", hq: "USA", spec: "Robotic Assembly", focus: "General Automotive" },
        { rank: 3, name: "Vanderlande", hq: "Netherlands", spec: "Logistics Systems", focus: "Airports & Warehousing" },
        { rank: 4, name: "KUKA Systems", hq: "Germany", spec: "Robotics", focus: "Automotive Body & Paint" },
        { rank: 5, name: "Rockwell Automation", hq: "USA", spec: "Control Systems", focus: "North American Manufacturing" },
        { rank: 6, name: "Siemens", hq: "Germany", spec: "Factory Automation", focus: "European Industry 4.0" },
        { rank: 7, name: "Daifuku", hq: "Japan", spec: "Material Handling", focus: "Semiconductor & Logistics" },
        { rank: 8, name: "Bastian Solutions", hq: "USA", spec: "Supply Chain", focus: "Retail Distribution" },
        { rank: 9, name: "Dematic", hq: "USA", spec: "Intralogistics", focus: "Global Warehousing" },
        { rank: 10, name: "PIA Automation", hq: "Germany", spec: "Assembly Systems", focus: "Mobility & Consumer Goods" }
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
                <h5 style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--secondary, #64748B); margin-bottom: 1rem;">Market Dynamics</h5>
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
                <div class="mv-actors-label">Key Global Actors</div>
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
