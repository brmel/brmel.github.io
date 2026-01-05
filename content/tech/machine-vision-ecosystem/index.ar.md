---
title: "المنظومة العالمية للرؤية الآلية"
date: 2025-12-14
tags: ["الرؤية الآلية", "تحليل السوق", "منظومة الصناعة", "الأتمتة"]
summary: "استكشاف تفاعلي لسوق الرؤية الآلية العالمي — من مصنعي المكونات إلى المستخدمين النهائيين."
cover:
    image: "/tech/machine-vision-ecosystem/market_overview.jpg"
    alt: "نظرة عامة على السوق"
    relative: false
---

سوق الرؤية الآلية ليس كتلة واحدة متجانسة، بل هو **منظومة متخصصة للغاية ومُهيكلة على مستويات**، صُمّمت لتحويل الضوء الخام إلى بيانات صناعية قابلة للتنفيذ.

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

    /* Flow Connector Logic for large screens - RTL */
    @media (min-width: 768px) {
        .mv-chain-step::after {
            content: '←';
            position: absolute;
            left: -14px;
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
        text-align: right;
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
        border-right: 4px solid var(--primary, #2563EB);
        padding-right: 1rem;
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
        table-layout: auto;
        text-align: right;
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
        white-space: nowrap;
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
        margin-left: 0.75rem;
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

## نظرة عامة على هيكل السوق

<div style="margin: 2rem 0; text-align: center;">
    <img src="/tech/machine-vision-ecosystem/market_overview.jpg" alt="نظرة عامة على السوق" style="max-width: 100%; width: 100%; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
</div>

<div class="mv-grid-3">
    <div class="mv-card">
        <div class="mv-icon">⚗️</div>
        <h3 style="font-weight: 700; margin-bottom: 0.5rem;">التجزئة والتخصص</h3>
        <p style="font-size: 0.875rem; color: var(--secondary);">على عكس الإلكترونيات الاستهلاكية، لا توجد شركة واحدة تمتلك سلسلة القيمة بأكملها. خبير العدسات (مثل Fujinon) نادراً ما يصنع البرمجيات، وخبير البرمجيات (مثل MVTec) نادراً ما يبني الروبوتات. هذا يستلزم شبكة قوية من <strong>الشراكات والتكامل</strong>.</p>
    </div>
    <div class="mv-card">
        <div class="mv-icon">🧩</div>
        <h3 style="font-weight: 700; margin-bottom: 0.5rem;">تحدي التكامل</h3>
        <p style="font-size: 0.875rem; color: var(--secondary);">أنظمة الرؤية ليست "وصّل وشغّل" مثل كاميرا الويب. تتطلب إضاءة دقيقة، ومعايرة، وبرمجة منطقية. هذا التعقيد يخلق سوقاً ضخماً <strong>لمتكاملي الأنظمة</strong> الذين يربطون بين مصنعي المعدات والمصانع.</p>
    </div>
    <div class="mv-card">
        <div class="mv-icon">⚙️</div>
        <h3 style="font-weight: 700; margin-bottom: 0.5rem;">من البكسل إلى القرار</h3>
        <p style="font-size: 0.875rem; color: var(--secondary);">تتحرك سلسلة القيمة بشكل خطي: <strong>المكوّن</strong> (الالتقاط) ← <strong>النظام</strong> (المعالجة) ← <strong>التطبيق</strong> (القرار). تنتقل الصناعة حالياً من تسليع الأجهزة نحو ذكاء البرمجيات والذكاء الاصطناعي.</p>
    </div>
</div>

---

## سلسلة القيمة: من الفوتون إلى المصنع

<p class="mv-section-subtitle">انقر على أي مرحلة لفهم وظيفتها وديناميكياتها السوقية وسياقها التشغيلي.</p>

<div class="mv-grid-5">
    <button data-stage="components" onclick="mvUpdateChain('components')" class="mv-chain-step">
        <div class="mv-step-label">المستوى ١</div>
        <div class="mv-step-title">المكوّن</div>
        <div class="mv-step-subtitle">المستشعرات والبصريات</div>
    </button>
    <button data-stage="systems" onclick="mvUpdateChain('systems')" class="mv-chain-step">
        <div class="mv-step-label">المستوى ٢</div>
        <div class="mv-step-title">نظام الرؤية</div>
        <div class="mv-step-subtitle">الكاميرات والبرمجيات</div>
    </button>
    <button data-stage="distribution" onclick="mvUpdateChain('distribution')" class="mv-chain-step">
        <div class="mv-step-label">المستوى ٣</div>
        <div class="mv-step-title">التوزيع</div>
        <div class="mv-step-subtitle">شركاء التوزيع</div>
    </button>
    <button data-stage="integrators" onclick="mvUpdateChain('integrators')" class="mv-chain-step">
        <div class="mv-step-label">المستوى ٤</div>
        <div class="mv-step-title">المتكامل</div>
        <div class="mv-step-subtitle">بناة الآلات</div>
    </button>
    <button data-stage="endusers" onclick="mvUpdateChain('endusers')" class="mv-chain-step">
        <div class="mv-step-label">المستوى ٥</div>
        <div class="mv-step-title">المستخدم النهائي</div>
        <div class="mv-step-subtitle">العملاء الصناعيون</div>
    </button>
</div>

<div id="mv-chain-panel" class="mv-panel">
    <!-- Content injected by JS -->
</div>

---

## الرواد العالميون في السوق

<p class="mv-section-subtitle">تصنيف اللاعبين الرئيسيين في المعدات والبرمجيات وتكامل الأنظمة.</p>

<div class="mv-tab-container">
    <button onclick="mvShowLeaders('hardware')" id="mv-tab-hardware" class="mv-tab-btn active">المعدات</button>
    <button onclick="mvShowLeaders('software')" id="mv-tab-software" class="mv-tab-btn">البرمجيات</button>
    <button onclick="mvShowLeaders('integrators')" id="mv-tab-integrators" class="mv-tab-btn">المتكاملون</button>
</div>

<div class="mv-card" style="padding: 0; overflow: hidden;">
    <div style="overflow-x: auto;">
        <table class="mv-table" style="min-width: 100%;">
            <colgroup>
                <col style="width: 25%;">
                <col style="width: 15%;">
                <col style="width: 25%;">
                <col style="width: 35%;">
            </colgroup>
            <thead>
                <tr>
                    <th>الشركة</th>
                    <th>المقر الرئيسي</th>
                    <th>التخصص الرئيسي</th>
                    <th>السوق المستهدف</th>
                </tr>
            </thead>
            <tbody id="mv-leader-table">
                <!-- Rows injected by JS -->
            </tbody>
        </table>
    </div>
</div>

<script>
// بيانات مقال الرؤية الآلية
const mvChainData = {
    components: {
        title: "١. موردو المكونات (المواد الخام)",
        headline: "الطبقة الأساسية التي تهيمن عليها البصريات وفيزياء أشباه الموصلات.",
        desc: "تركز هذه المرحلة على الالتقاط المادي للمعلومات. تتميز بحواجز تقنية عالية للدخول — تصنيع مستشعر صور عالي الجودة أو عدسة تيليسنتريك يتطلب بنية تحتية ضخمة للبحث والتطوير. تبيع هذه الشركات عادةً لصانعي 'الأنظمة' (المرحلة ٢) وليس مباشرة للمصانع.",
        dynamics: [
            { label: "هيكل السوق", text: "شديد التركيز للمستشعرات (Sony تمتلك أكثر من ٥٠٪) ؛ مجزأ للإضاءة والعدسات." },
            { label: "التحدي الرئيسي", text: "الموازنة بين الدقة (ميغابكسل)، السرعة (إطار/ثانية)، والحساسية." },
            { label: "لماذا هذا مهم", text: "لا يمكن للبرنامج معالجة ما لا تستطيع الكاميرا رؤيته. جودة السلسلة بأكملها تعتمد على هذه الخطوة الأولى." }
        ],
        actors: "Sony, Teledyne e2v, ON Semi (المستشعرات) ؛ Fujinon, Moritex, Tamron (البصريات) ؛ CCS, Smart Vision Lights (الإضاءة)."
    },
    systems: {
        title: "٢. أنظمة الرؤية والمعدات (الدماغ)",
        headline: "حيث تلتقي المعدات بالمنطق. القطاع الأكثر تنافسية في السوق.",
        desc: "تدمج هذه المرحلة المكونات الخام في منتج قابل للاستخدام. تشمل 'الكاميرات الذكية' (وحدات متكاملة مع معالجات مدمجة) إلى كاميرات PC (GigE/USB) التي تتطلب حواسيب خارجية. يقود هؤلاء اللاعبون الابتكار في سهولة الاستخدام وعامل الشكل.",
        dynamics: [
            { label: "الاتجاه الحالي", text: "التحول نحو 'الرؤية المدمجة' والتعلم العميق على الحافة (داخل الكاميرا)." },
            { label: "المنافسة", text: "منافسة شرسة بين الشركات الأمريكية (Zebra/Cognex)، اليابانية (Keyence/Omron)، والأوروبية (Basler)." },
            { label: "أنواع المنتجات", text: "الكاميرات الذكية، قارئات الهوية، ماسحات ثلاثية الأبعاد، الكاميرات الحرارية." }
        ],
        actors: "Zebra, Cognex, Keyence, Basler, Teledyne FLIR, Omron, Hikrobot, TKH Group."
    },
    distribution: {
        title: "٣. التوزيع وشركاء القنوات (الجسر)",
        headline: "الصمغ اللوجستي والاستشاري للمنظومة.",
        desc: "لأن السوق عالمي لكن التجزئة عالية، يعتمد المصنعون على الموزعين المحليين. هؤلاء ليسوا مجرد ناقلي صناديق؛ هم موزعون ذوو قيمة مضافة (VAD) يقدمون الاستشارات، وحسابات العدسات، ودراسات الجدوى للمتكاملين المحليين الذين قد يفتقرون للخبرة في فيزياء البصريات.",
        dynamics: [
            { label: "القيمة المقدمة", text: "يجمعون مكونات من علامات متعددة (مثل مستشعر Sony في كاميرا Basler مع عدسة Fujinon) لإنشاء مجموعة متوافقة." },
            { label: "الدور الجغرافي", text: "حاسم لاختراق الأسواق المجزأة مثل أوروبا وآسيا." }
        ],
        actors: "Stemmer Imaging, Framos, 1stVision, Mid-Atlantic Computer Vision, China Daheng Group."
    },
    integrators: {
        title: "٤. متكاملو الأنظمة وبناة الآلات (البناؤون)",
        headline: "الهندسة المخصصة لدمج الرؤية في خط الإنتاج.",
        desc: "نادراً ما تشتري المصانع كاميرا وتركبها بنفسها. تستأجر متكاملين (SI) أو تشتري آلات من مصنعي المعدات الأصلية (OEM). يصمم المتكامل التركيب الميكانيكي، ويكتب منطق PLC، ويدمج برنامج الرؤية، ويضمن معدل 'مطابق/غير مطابق'.",
        dynamics: [
            { label: "ملف المخاطر", text: "يتحملون المخاطر التشغيلية. إذا فشل النظام في اكتشاف عيب، يكون المتكامل مسؤولاً." },
            { label: "التخصص", text: "متخصص جداً حسب القطاع. متكامل السيارات نادراً ما يقوم بفحص الأدوية." }
        ],
        actors: "ATS Automation, JR Automation, Vanderlande, KUKA, Rockwell Partners, Beckhoff."
    },
    endusers: {
        title: "٥. المستخدمون النهائيون (تحقيق القيمة)",
        headline: "عمالقة التصنيع والخدمات اللوجستية الذين يدفعون الطلب.",
        desc: "الخطوة النهائية حيث تولد التكنولوجيا عائداً على الاستثمار. ينشر المستخدمون النهائيون الرؤية لثلاثة أسباب رئيسية: مراقبة الجودة (اكتشاف العيوب)، التتبع (قراءة الباركود/التتبع)، والأتمتة (توجيه الروبوتات).",
        dynamics: [
            { label: "محركات الصناعة", text: "الإلكترونيات (التصغير)، السيارات (التحول للكهرباء)، الخدمات اللوجستية (سرعة التجارة الإلكترونية)." },
            { label: "عائق التبني", text: "التكلفة الأولية العالية وتعقيد الصيانة." }
        ],
        actors: "Tesla, Apple, TSMC, Amazon, Nestlé, Pfizer, Samsung, Volkswagen."
    }
};

const mvLeadersData = {
    hardware: [
        { rank: 1, name: "Zebra Technologies", hq: "الولايات المتحدة", spec: "الماسحات الصناعية الثابتة", focus: "الخدمات اللوجستية والتوزيع" },
        { rank: 2, name: "Cognex", hq: "الولايات المتحدة", spec: "الكاميرات الذكية والهوية", focus: "الخدمات اللوجستية والإلكترونيات" },
        { rank: 3, name: "Keyence", hq: "اليابان", spec: "المستشعرات والقياس", focus: "أتمتة المصانع (مبيعات مباشرة)" },
        { rank: 4, name: "Basler", hq: "ألمانيا", spec: "كاميرات المسح المصفوفي", focus: "التصنيع بالجملة والمدمج" },
        { rank: 5, name: "Teledyne Technologies", hq: "الولايات المتحدة", spec: "التصوير الحراري والعلمي", focus: "الفضاء والصناعة" },
        { rank: 6, name: "Omron", hq: "اليابان", spec: "منظومات الأتمتة", focus: "السيارات والإلكترونيات" },
        { rank: 7, name: "TKH Group", hq: "هولندا", spec: "الرؤية ثلاثية الأبعاد (LMI/Allied)", focus: "القياس والفحص" },
        { rank: 8, name: "Baumer", hq: "سويسرا", spec: "الكاميرات الصناعية", focus: "الأغذية والأدوية" },
        { rank: 9, name: "Hikrobot", hq: "الصين", spec: "الروبوتات المتنقلة والرؤية", focus: "الخدمات اللوجستية والتصنيع" },
        { rank: 10, name: "Daheng Imaging", hq: "الصين", spec: "المكونات والأنظمة", focus: "السوق الآسيوي" }
    ],
    software: [
        { rank: 1, name: "Matrox Imaging (Zebra)", hq: "كندا", spec: "مكتبة MIL", focus: "أشباه الموصلات والطب" },
        { rank: 2, name: "MVTec (HALCON)", hq: "ألمانيا", spec: "خوارزميات متقدمة", focus: "تطبيقات PC المتطورة" },
        { rank: 3, name: "Cognex (VisionPro)", hq: "الولايات المتحدة", spec: "التعلم العميق والقواعد", focus: "تكامل المصانع" },
        { rank: 4, name: "Stemmer (CVB)", hq: "ألمانيا", spec: "Common Vision Bloch", focus: "تطوير متعدد المعدات" },
        { rank: 5, name: "Euresys (Open eVision)", hq: "بلجيكا", spec: "المكتبات وIP Cores", focus: "الفحص عالي السرعة" },
        { rank: 6, name: "National Instruments", hq: "الولايات المتحدة", spec: "LabVIEW Vision", focus: "الاختبار والقياس" },
        { rank: 7, name: "Landing AI", hq: "الولايات المتحدة", spec: "Visual Prompting / AI", focus: "فحص السحابة/الحافة" },
        { rank: 8, name: "Scikit-image / OpenCV", hq: "عالمي", spec: "مكتبات مفتوحة المصدر", focus: "البحث والتطوير والنماذج" },
        { rank: 9, name: "Adaptive Vision", hq: "بولندا", spec: "برمجيات رسومية", focus: "النشر السريع" },
        { rank: 10, name: "NeuroCheck", hq: "ألمانيا", spec: "برمجيات تطبيقية", focus: "مراقبة جودة السيارات" }
    ],
    integrators: [
        { rank: 1, name: "ATS Automation", hq: "كندا", spec: "التكامل الكامل", focus: "علوم الحياة وبطاريات السيارات الكهربائية" },
        { rank: 2, name: "JR Automation", hq: "الولايات المتحدة", spec: "التجميع الروبوتي", focus: "السيارات العام" },
        { rank: 3, name: "Vanderlande", hq: "هولندا", spec: "الأنظمة اللوجستية", focus: "المطارات والمستودعات" },
        { rank: 4, name: "KUKA Systems", hq: "ألمانيا", spec: "الروبوتات", focus: "هياكل السيارات والطلاء" },
        { rank: 5, name: "Rockwell Automation", hq: "الولايات المتحدة", spec: "أنظمة التحكم", focus: "الصناعة الأمريكية الشمالية" },
        { rank: 6, name: "Siemens", hq: "ألمانيا", spec: "الأتمتة الصناعية", focus: "الصناعة 4.0 الأوروبية" },
        { rank: 7, name: "Daifuku", hq: "اليابان", spec: "مناولة المواد", focus: "أشباه الموصلات والخدمات اللوجستية" },
        { rank: 8, name: "Bastian Solutions", hq: "الولايات المتحدة", spec: "سلسلة التوريد", focus: "توزيع التجزئة" },
        { rank: 9, name: "Dematic", hq: "الولايات المتحدة", spec: "الخدمات اللوجستية الداخلية", focus: "التخزين العالمي" },
        { rank: 10, name: "PIA Automation", hq: "ألمانيا", spec: "أنظمة التجميع", focus: "التنقل والسلع الاستهلاكية" }
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
                <h5 style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--secondary, #64748B); margin-bottom: 1rem;">ديناميكيات السوق</h5>
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
                <div class="mv-actors-label">اللاعبون العالميون الرئيسيون</div>
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
