---
title: "السيرة الذاتية"
layout: "resume"
summary: "مهندس رؤية آلية ومعالجة صور — Zebra Technologies وMatrox Imaging وPolytechnique Montréal."
description: "مطور برمجيات أول متخصص في الرؤية الآلية ومعالجة الصور وأنظمة التحكم."
ShowBreadCrumbs: false
aliases: ["/ar/timeline/", "/ar/about/"]
role: "مطور برمجيات أول — الرؤية الآلية ومعالجة الصور"
location: "مونتريال، كيبك"
availability: "مقيم في مونتريال. البريد الإلكتروني أسرع وسيلة للتواصل."
contact:
  - label: "البريد الإلكتروني"
    url: "mailto:mellah.brahim.redouane@gmail.com"
  - label: "لينكد إن"
    url: "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - label: "غيت هَب"
    url: "https://github.com/brmel"

# المسار المهني، مرحلة بمرحلة. البنية تأتي من
# layouts/partials/career-timeline.html، ولا يتغير بين اللغات سوى النص.
# اجعل `learned` جملة واحدة — فهي السطر الذي يبقى في ذهن القارئ.
experience:
  - period: "2024 — الآن"
    role: "مطور برمجيات أول"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "خوارزميات يبني عليها آخرون منتجاتهم"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "عرض لمكتبة Aurora Imaging داخل Aurora Vision Studio"
        text: >-
          أحد المهندسين المسؤولين عن خوارزميات المكتبة. العمل يتجاوز كتابة
          الكود بكثير: الاتفاق على السلوك مع فرق الواجهة والتوثيق والاختبار قبل
          الإصدار، والدخول في التطبيقات التي يعجز العملاء عن تشغيلها.
      - title: "فحص يجري داخل الكاميرا نفسها"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "الكاميرا الذكية Aurora Focus أثناء فحص القطع"
        text: >-
          نقل مكتبة التصوير إلى داخل الكاميرا نفسها، ليجري الفحص على الجهاز بدل
          حاسوب موصول به.
    built: ["Aurora Imaging Library", "الكاميرا الذكية Aurora Focus"]
    stack: ["C++", "خوارزميات الرؤية الآلية", "التصوير على الأجهزة الطرفية"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA"]
    learned: >-
      لا تصير المكتبة منتجًا إلا حين تقول الخوارزمية والتوثيق والاختبارات الشيء
      نفسه — والاختلاف يظهر في تطبيق العميل قبل أن يظهر في الاختبارات بكثير.

  - period: "2022 — 2024"
    role: "مطور برمجيات II"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "الهندسة التي تقوم عليها وحدات 2D"
        text: >-
          Model Finder وEdge Finder وMeasurement وMetrology وCalibration وBead —
          حل وتنفيذ وتصحيح ما تحتها من هندسة وجبر وتحسين غير خطي، وتوسيع
          الاختبارات التي تحميها. وانتقل Advanced Geometric Matcher من خوارزمية
          داخلية إلى واجهة برمجية عامة، صُممت مع الفريق.
      - title: "إدخال تعلّم الآلة في مكتبة هندسية"
        video: "CS4cs9xVecg"
        videoAlt: "ملاحظات من تخصص التعلم العميق"
        text: >-
          إدخال تعلّم الآلة الكلاسيكي في وحدات كانت هندسية بحتة، ثم توثيق
          الواجهات الجديدة وكتابة أمثلة العملاء التي صدرت معها، والإشراف على
          المتدربين.
    built: ["واجهة Advanced Geometric Matcher", "وحدات 2D في MIL", "أمثلة الواجهات للعملاء"]
    stack: ["C++", "المطابقة الهندسية", "القياس", "التحسين غير الخطي", "التعلم الآلي الكلاسيكي"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA", "Agile"]
    learned: >-
      كتابة التوثيق والأمثلة هي الاختبار الحقيقي لتصميم أي واجهة — فالأسئلة
      التي تعود إليك تدور حول الواجهة، لا حول الخوارزمية.

  - period: "2019 — 2022"
    role: "مطور برمجيات"
    org: "Matrox Imaging"
    url: "https://video.matrox.com/en"
    note: "انضمت Matrox Imaging إلى Zebra Technologies سنة 2022، واستمر العمل دون انقطاع."
    work:
      - title: "تعلّم الصنعة"
        video: "LcoPNbyuhZU"
        videoAlt: "معالجة الصور الصناعية في مكتبة Matrox Imaging"
        text: >-
          أول وظيفة بعد الماجستير، على الوحدات التي تقيس: Calibration
          وMeasurement وMetrology. وتصميم Advanced Geometric Matcher، الخوارزمية
          التي صارت لاحقًا واجهة برمجية عامة.
      - title: "العمل داخل قاعدة كود C++ ضخمة"
        video: "sfLZ7v9gEnc"
        videoAlt: "العمل داخل قاعدة كود مكتبة Matrox Imaging"
        text: >-
          استبدال حلّالات قديمة في وحدات الهندسة بمُحسِّنات غير خطية، منها
          Levenberg–Marquardt، داخل مكتبة تعتمد عليها آلاف التطبيقات المثبّتة.
    built: ["Advanced Geometric Matcher", "MIL Calibration · Measurement · Metrology"]
    stack: ["C++", "التحسين غير الخطي", "Levenberg–Marquardt", "التعلم الآلي الكلاسيكي"]
    tools: ["Visual Studio", "Git", "SVN"]
    learned: >-
      كتابة خوارزمية أفضل هي النصف القصير من العمل؛ أما إدخالها في مكتبة يعتمد
      عليها آخرون دون تغيير نتيجة يبنون عليها فهو النصف الطويل.

  - period: "2017 — 2019"
    role: "ماجستير في هندسة أنظمة التحكم"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "المعدل 3.87/4 · منحة مؤسسة الغرير — 1 من 100 من بين أكثر من 15,000 متقدم."
    work:
      - title: "كيف وصلت إلى كندا"
        video: "BPkj-VETeX0"
        videoAlt: "عن منحة مؤسسة الغرير"
        url: "https://www.alghurairfoundation.org/"
        text: >-
          مُنحت المنحة على أساس الاستحقاق الأكاديمي ومولت الماجستير، وهي سبب
          وقوع بقية هذه الصفحة في مونتريال.
      - title: "أنظمة، لا مقررات فقط"
        video: "UZbmuAs2K2w"
        videoAlt: "الروبوتات والتحكم في الوقت الحقيقي أثناء الماجستير"
        text: >-
          كل مقرر مهم كان ينتهي بشيء يجب أن يعمل: روبوت عليه أن يبلغ نقطته،
          ومتحكم عليه أن يفي بموعده، وكاميرا عليها أن تخبر الذراع بموضع القطعة.
    built: ["مزامنة مسارات الروبوتات بخوارزمية A*", "تحكم آني في الروبوتات على QNX", "نظام رؤية يوجّه روبوت Fanuc"]
    stack: ["C++", "التحكم الرقمي", "الكشف والتقدير", "التحكم العشوائي والمتين", "معالجة الصور"]
    tools: ["QNX", "ROS", "MATLAB / Simulink", "روبوتات Fanuc"]
    learned: >-
      قانون تحكم صحيح على الورق ومتأخر بعشر ميلي ثانية هو قانون خاطئ — فالموعد
      جزء من المواصفات، لا تفصيل في التنفيذ.

  - period: "2012 — 2017"
    role: "مهندس دولة في الهندسة الكهربائية — أنظمة التحكم"
    org: "المدرسة الوطنية المتعددة التقنيات، الجزائر"
    url: "https://www.enp.edu.dz/en/"
    note: "المعدل 17.5/20 · الخامس من بين 1,400 طالب — ضمن أفضل 1% وطنيًا."
    work:
      - title: "سنتان تحضيريتان أولًا"
        video: "VjwIGG7Lbt0"
        videoAlt: "سنوات الأقسام التحضيرية في الجزائر"
        text: >-
          رياضيات وفيزياء وبرمجة، من التاسعة صباحًا إلى السادسة مساءً، ستة أيام
          في الأسبوع، وترتيب في النهاية يحدد المدرسة التي تدخلها. من هناك جاءت
          عادة الاشتغال على المسألة حتى تُحلّ فعلًا.
      - title: "هندسة تخرج من قاعة الدرس"
        video: "eGPbNTXTd1I"
        videoAlt: "مشاريع التحكم والمتحكمات المنطقية أثناء دراسة الهندسة"
        text: >-
          انتهت الدراسة بأنظمة تحكم بُنيت في مواجهة عتاد حقيقي وقيود مصنع
          حقيقية، لا محاكاة لها.
    built: ["مثبّت سرعة تكيّفي لمركبة ذاتية القيادة", "برنامج متحكم منطقي لآلة تجميع صناعية"]
    stack: ["C", "MATLAB", "VHDL", "تصميم أنظمة التحكم", "تعريف الأنظمة", "التحكم الأمثل"]
    tools: ["Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "Simulink", "LabVIEW"]
    learned: >-
      العتاد لا يعنيه جمال النموذج: أول آلة تجميع برمجتها أنفقت أعطالها على
      الحساسات والأسلاك، لا على منطق التحكم الذي قضيت الفصل كله عليه.

skills:
  - group: "لغات البرمجة"
    items: ["C++", "C", "Python", "Dart / Flutter", "TypeScript", "MATLAB", "VHDL", "SQL"]
  - group: "الرؤية الآلية"
    items: ["Aurora Imaging Library", "Matrox Imaging Library", "OpenCV", "المطابقة الهندسية", "المعايرة", "القياس", "قياس الحواف"]
  - group: "الرياضيات والخوارزميات"
    items: ["التحسين غير الخطي", "Levenberg–Marquardt", "نظرية التحكم", "التعلم الآلي الكلاسيكي", "التعلم العميق", "أنظمة الوكلاء المتعددة"]
  - group: "السحابة والخلفية"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "الأنظمة والأدوات"
    items: ["أنظمة الوقت الحقيقي", "QNX", "ROS", "Git / GitHub", "SVN", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "JIRA"]
  - group: "اللغات"
    items: ["الفرنسية", "الإنجليزية", "العربية"]
certifications:
  - year: "2023"
    name: "Neural Networks and Deep Learning · Convolutional Neural Networks"
    issuer: "DeepLearning.AI"
  - year: "2023"
    name: "Machine Learning: Classification"
    issuer: "University of Washington"
---
