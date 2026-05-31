/* Machine Vision Ecosystem — AR content (DATA layer).
   The translatable article content for the interactive chain panels and
   leader tables. Loaded before the shared machine-vision.js logic via this
   page's customJS front matter, so each language renders in its own words. */
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

const mvLabels = {"dynamics": "ديناميكيات السوق", "actors": "اللاعبون العالميون الرئيسيون"};
