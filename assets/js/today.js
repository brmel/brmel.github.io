/*
 * Today — daily glance dashboard
 *
 * Renders a live, single-source-of-truth view of the day:
 *  - live wall clock (second tick)
 *  - NOW card  (current slot · action · progress · next)
 *  - training session card (auto-selected per weekday)
 *  - day grid: every slot as a card; each card doubles as a
 *    check-off button persisted in localStorage per calendar day
 *    (so the checklist resets at midnight without ceremony)
 *
 * No build step, no framework — vanilla DOM + a single IIFE.
 */
(function () {
  'use strict';

  // ──────────────────────────────────────────────────────────────
  // Icons — geometric SVG glyphs drawn with currentColor (32×32)
  // ──────────────────────────────────────────────────────────────
  var ICONS = {
    wake:    '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="16" cy="20" r="6"/><line x1="16" y1="6" x2="16" y2="10"/><line x1="6" y1="20" x2="2" y2="20"/><line x1="30" y1="20" x2="26" y2="20"/><line x1="9" y1="12" x2="6" y2="9"/><line x1="23" y1="12" x2="26" y2="9"/><line x1="2" y1="28" x2="30" y2="28"/></svg>',
    meal:    '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="16" cy="18" r="10"/><path d="M9 18 Q16 11 23 18"/><circle cx="16" cy="6" r="1.5" fill="currentColor"/></svg>',
    work:    '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="8" width="24" height="16" rx="1"/><line x1="2" y1="26" x2="30" y2="26"/><line x1="10" y1="14" x2="22" y2="14"/><line x1="10" y1="18" x2="18" y2="18"/></svg>',
    ocular:  '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 16 Q16 6 30 16 Q16 26 2 16Z"/><circle cx="16" cy="16" r="4"/><circle cx="16" cy="16" r="1.5" fill="currentColor"/></svg>',
    posture: '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="16" cy="8" r="3"/><line x1="16" y1="11" x2="16" y2="22"/><line x1="10" y1="16" x2="22" y2="16"/><line x1="16" y1="22" x2="12" y2="28"/><line x1="16" y1="22" x2="20" y2="28"/></svg>',
    tendon:  '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="6" y="12" width="20" height="8" rx="4"/><line x1="16" y1="12" x2="16" y2="20"/><circle cx="11" cy="16" r="1" fill="currentColor"/><circle cx="21" cy="16" r="1" fill="currentColor"/></svg>',
    train:   '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="6" y1="16" x2="26" y2="16"/><rect x="3" y="11" width="3" height="10"/><rect x="26" y="11" width="3" height="10"/><rect x="8" y="13" width="2" height="6"/><rect x="22" y="13" width="2" height="6"/></svg>',
    cut:     '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="16" cy="16" r="11"/><line x1="9" y1="9" x2="23" y2="23"/></svg>',
    moon:    '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 6 A12 12 0 1 0 26 22 A9 9 0 0 1 22 6 Z"/></svg>'
  };

  var CHECK_SVG =
    '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M3 8 L7 12 L13 4"/>' +
    '</svg>';

  // ──────────────────────────────────────────────────────────────
  // Schedule — the canonical day. Times are minutes-since-midnight
  // (06:00 = 360, 22:00 = 1320). Each entry surfaces a one-line
  // `action` (what to do) and a denser `detail` (why / mechanism).
  // ──────────────────────────────────────────────────────────────
  var SCHEDULE = [
    { id: 'wake',       start: 360,  end: 420,  label: 'Wake',           tag: 'Anchor',    icon: 'wake',    cutoff: false,
      action: 'No snooze. Eyes open. Daylight in.',
      detail: 'Reinforces the circadian anchor; prevents sleep inertia from a fragmented secondary onset.' },

    { id: 'breakfast',  start: 420,  end: 540,  label: 'Breakfast',      tag: 'Fuel',      icon: 'meal',    cutoff: false,
      action: '3–4 organic eggs · oatmeal with berries · 5–7 mL/kg water.',
      detail: 'Initiates morning protein synthesis; rehydrates after the 8 h fast.' },

    { id: 'work-am',    start: 540,  end: 720,  label: 'Deep work',      tag: 'Focus',     icon: 'work',    cutoff: false,
      action: 'Cognitive prime time. The hardest engineering problem of the day.',
      detail: 'Frontal-cortex peak from late morning catecholamines — protect it from meetings and Slack.' },

    { id: 'lunch',      start: 720,  end: 780,  label: 'Lunch + Ocular', tag: 'Stack',     icon: 'ocular',  cutoff: true,
      action: 'WeCook Spicy Peanut Chicken or Piri Piri Bowl. Astaxanthin 4–12 mg · Lutein 10 mg · Zeaxanthin 2 mg. Caffeine cutoff.',
      detail: 'Carotenoids are fat-soluble — take with the meal. Caffeine half-life ≈ 5 h; cutoff now protects the sleep window.' },

    { id: 'posture',    start: 780,  end: 840,  label: 'Posture',        tag: 'Reset',     icon: 'posture', cutoff: false,
      action: 'SMR · cervical stretch · face pulls · chin tucks · hip-flexor · dead bugs · glute bridges. 12 min.',
      detail: 'Resets UCS and APT compensations imposed by the morning desk block.' },

    { id: 'work-pm',    start: 840,  end: 960,  label: 'Deep work',      tag: 'Focus',     icon: 'work',    cutoff: false,
      action: 'Second block. Code review, communication, lighter cognitive load.',
      detail: 'Post-prandial dip. Lower-load tasks; save cognition for the morning block tomorrow.' },

    { id: 'tendon',     start: 960,  end: 990,  label: 'Tendon prep',    tag: 'Prime',     icon: 'tendon',  cutoff: false,
      action: '15 g hydrolyzed collagen + 100 mg vitamin C in 300 mL water.',
      detail: 'Peaks serum amino acids ~45 min before mechanical loading (Baar protocol).' },

    { id: 'pre-wo',     start: 990,  end: 1020, label: 'Pre-workout',    tag: 'Fuel',      icon: 'meal',    cutoff: false,
      action: 'Banana or rice cakes if the session is high-demand. No heavy fat.',
      detail: 'Rapid glycogen availability without slowing gastric emptying.' },

    { id: 'train',      start: 1020, end: 1140, label: 'Train',          tag: 'Load',      icon: 'train',   cutoff: false, isTrain: true,
      action: '', // populated per weekday
      detail: 'Mechanical loading forces nutrients into the avascular tendon matrix; concurrent stimulus for hypertrophy.' },

    { id: 'dinner',     start: 1140, end: 1200, label: 'Dinner',         tag: 'Refuel',    icon: 'meal',    cutoff: true,
      action: 'WeCook Grilled Beef Steak + rice — or home-cooked sirloin (Bovins Charlevoix) with sweet potato. Food cutoff.',
      detail: 'Tissue repair · glycogen resynthesis · iron + bioavailable protein. Final caloric intake.' },

    { id: 'work-cut',   start: 1200, end: 1260, label: 'Work cutoff',    tag: 'Wind down', icon: 'cut',     cutoff: true,
      action: 'Close the IDE. Cortisol drop.',
      detail: 'Lets systemic cortisol and adrenaline fall into parasympathetic dominance.' },

    { id: 'screen-cut', start: 1260, end: 1320, label: 'Screens off',    tag: 'Melatonin', icon: 'cut',     cutoff: true,
      action: 'All blue-light sources dark.',
      detail: 'Releases the pineal gland from melatonin inhibition by removing 400–500 nm exposure.' },

    { id: 'sleep',      start: 1320, end: 1800, label: 'Sleep',          tag: 'Recover',   icon: 'moon',    cutoff: false,
      action: 'Eight continuous hours. Cool, dark room.',
      detail: 'Primary sleep cycle: deep-stage consolidation, growth hormone pulse, glymphatic clearance.' }
  ];

  // ──────────────────────────────────────────────────────────────
  // Weekly training split — 0 = Sunday … 6 = Saturday
  // ──────────────────────────────────────────────────────────────
  var TRAINING_BY_DAY = {
    0: { title: 'Total Recovery',         tag: 'Glycogen restoration', rest: true,
         note: 'Zero strenuous activity. Postural correction only.', items: [] },
    1: { title: 'Lower Body Hypertrophy', tag: 'Mechanical tension',
         items: [
           { name: 'Back Squat',            reps: '4 × 8–10' },
           { name: 'Romanian Deadlift',     reps: '3 × 8–12' },
           { name: 'Bulgarian Split Squat', reps: '3 × 10 / leg' },
           { name: 'Leg Extension',         reps: '3 × 12–15' },
           { name: 'Calf Raise',            reps: '4 × 15' }
         ] },
    2: { title: 'Upper Body Hypertrophy', tag: 'Pull-volume bias',
         items: [
           { name: 'Bench Press',           reps: '4 × 8–10' },
           { name: 'Weighted Pull-up',      reps: '3 × 8–10' },
           { name: 'Seated Cable Row',      reps: '4 × 10–12' },
           { name: 'Overhead Press',        reps: '3 × 8–10' },
           { name: 'Face Pull',             reps: '3 × 15' }
         ] },
    3: { title: 'Active Recovery',        tag: 'CNS regeneration', rest: true,
         note: 'Mobility, walking, full postural correction routine.', items: [] },
    4: { title: 'Speed & Power',          tag: 'Rate of force',
         items: [
           { name: 'Power Clean',           reps: '4 × 3–5' },
           { name: 'Box Jump',              reps: '3 × 5' },
           { name: 'MB Rotational Throw',   reps: '3 × 8 / side' },
           { name: '10 m COD drills',       reps: '5 sets' }
         ] },
    5: { title: 'Full Body Accessory',    tag: 'Volume top-up',
         items: [
           { name: 'Clean Pull',            reps: '3 × 5' },
           { name: 'Hip Thrust',            reps: '3 × 10–12' },
           { name: 'Leg Curl',              reps: '3 × 12' },
           { name: 'Lateral Raise',         reps: '3 × 15' }
         ] },
    6: { title: 'Field Conditioning',     tag: 'FIFA 11+ → sprints',
         items: [
           { name: 'FIFA 11+ warm-up',      reps: '20 min' },
           { name: 'Continuous run',        reps: '2 sets' },
           { name: '50 m sprint / 50 m jog',reps: '2 sets' },
           { name: '10 s on / 10 s off',    reps: '2 sets' }
         ] }
  };

  var TRAIN_ACTION_BY_DAY = {
    0: 'Recovery day. Walk. Mobility. Sleep early.',
    1: 'Squat heavy. 3-second eccentrics. Mechanical tension.',
    2: 'Push and pull. High pulling volume to undo the desk.',
    3: 'Active recovery. Mobility + walk. No barbell.',
    4: 'Move fast. Maximal velocity, explosive intent.',
    5: 'Accessory volume. Smaller groups. Leave CNS fresh.',
    6: 'Field. FIFA 11+ first. Then sprint intervals.'
  };

  var DAY_NAMES   = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  var MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  // ──────────────────────────────────────────────────────────────
  // Pure helpers
  // ──────────────────────────────────────────────────────────────
  var pad        = function (n) { return n < 10 ? '0' + n : '' + n; };
  var formatTime = function (mins) { return pad(Math.floor(mins / 60) % 24) + ':' + pad(mins % 60); };

  var nowState = function () {
    var d = new Date();
    return { d: d, mins: d.getHours() * 60 + d.getMinutes(), weekday: d.getDay() };
  };

  var currentSlotIndex = function (mins) {
    // Pre-wake (00:00 → 06:00) is still inside the Sleep slot.
    if (mins < SCHEDULE[0].start) return SCHEDULE.length - 1;
    for (var i = 0; i < SCHEDULE.length; i++) {
      if (mins >= SCHEDULE[i].start && mins < SCHEDULE[i].end) return i;
    }
    return SCHEDULE.length - 1;
  };

  var nextSlotIndex = function (idx) { return (idx + 1) % SCHEDULE.length; };

  // Compute the localStorage key fresh on every access so a tab left
  // open across midnight rolls over to the new day's bucket.
  var todayKey   = function () {
    var d = new Date();
    return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
  };
  var storageKey = function () { return 'protocol-day-' + todayKey(); };

  // ──────────────────────────────────────────────────────────────
  // Persistence — per-day check state, namespaced by date
  // ──────────────────────────────────────────────────────────────
  var loadDone = function () {
    try {
      var raw = localStorage.getItem(storageKey());
      return raw ? (JSON.parse(raw) || {}) : {};
    } catch (e) { return {}; }
  };
  var saveDone = function (state) {
    try { localStorage.setItem(storageKey(), JSON.stringify(state)); } catch (e) {}
  };

  // ──────────────────────────────────────────────────────────────
  // Mutations — patch the per-day training slot in place
  // ──────────────────────────────────────────────────────────────
  function patchScheduleForToday(weekday) {
    for (var i = 0; i < SCHEDULE.length; i++) {
      if (!SCHEDULE[i].isTrain) continue;
      var t = TRAINING_BY_DAY[weekday];
      SCHEDULE[i].action = TRAIN_ACTION_BY_DAY[weekday] || '';
      SCHEDULE[i].label  = t && t.rest ? t.title : 'Train';
      SCHEDULE[i].tag    = t ? t.tag : 'Load';
      break;
    }
  }

  // ──────────────────────────────────────────────────────────────
  // DOM references — resolved once on init
  // ──────────────────────────────────────────────────────────────
  var els = {
    clock:      document.querySelector('[data-clock]'),
    day:        document.querySelector('[data-day]'),
    date:       document.querySelector('[data-date]'),
    trainBadge: document.querySelector('[data-train-badge]'),
    nowSlot:    document.querySelector('[data-now-slot]'),
    nowTitle:   document.querySelector('[data-now-title]'),
    nowAction:  document.querySelector('[data-now-action]'),
    nowBar:     document.querySelector('[data-now-bar]'),
    nowRemain:  document.querySelector('[data-now-remain]'),
    nowNext:    document.querySelector('[data-now-next]'),
    dayGrid:    document.querySelector('[data-day-grid]'),
    dayCount:   document.querySelector('[data-day-count]'),
    session:    document.querySelector('[data-session]')
  };

  // ──────────────────────────────────────────────────────────────
  // Render — header, NOW, session, day grid, counter
  // ──────────────────────────────────────────────────────────────
  function renderHeader(d, weekday) {
    if (els.day)  els.day.innerHTML  = DAY_NAMES[weekday].replace(/(day)$/, '<em>$1</em>');
    if (els.date) els.date.textContent = pad(d.getDate()) + ' ' + MONTH_NAMES[d.getMonth()].toUpperCase() + ' ' + d.getFullYear();
    if (els.trainBadge) {
      var t = TRAINING_BY_DAY[weekday];
      els.trainBadge.textContent = t ? t.title : '';
    }
  }

  function renderClock(d) {
    if (!els.clock) return;
    els.clock.innerHTML = pad(d.getHours()) + ':' + pad(d.getMinutes()) +
      '<span class="sec">:' + pad(d.getSeconds()) + '</span>';
  }

  function renderNow(mins) {
    var idx = currentSlotIndex(mins);
    var s   = SCHEDULE[idx];
    var nxt = SCHEDULE[nextSlotIndex(idx)];

    if (els.nowSlot)   els.nowSlot.textContent  = formatTime(s.start) + ' → ' + formatTime(s.end % 1440);
    if (els.nowTitle)  els.nowTitle.textContent = s.label;
    if (els.nowAction) els.nowAction.textContent = s.action || '—';

    var into  = mins - s.start;        if (into < 0) into += 1440;
    var total = s.end - s.start;
    var pct   = Math.max(0, Math.min(100, (into / total) * 100));
    if (els.nowBar) els.nowBar.style.width = pct.toFixed(1) + '%';

    if (els.nowRemain) {
      var remain = total - into;
      var rh = Math.floor(remain / 60), rm = remain % 60;
      els.nowRemain.textContent = (rh > 0 ? rh + 'h ' : '') + rm + 'm remaining';
    }
    if (els.nowNext) {
      var until = nxt.start - mins; if (until <= 0) until += 1440;
      var uh = Math.floor(until / 60), um = until % 60;
      els.nowNext.innerHTML =
        '<strong>Next</strong> · in ' + (uh > 0 ? uh + 'h ' : '') + um + 'm' +
        ' &nbsp;·&nbsp; <span class="next-action">' + formatTime(nxt.start) + ' — ' + nxt.label + '</span>';
    }
    return idx;
  }

  function renderSession(weekday) {
    if (!els.session) return;
    var t = TRAINING_BY_DAY[weekday]; if (!t) return;
    var html = '';
    html += '<div>';
    html +=   '<div class="session__label">Today · 17:00 → 19:00</div>';
    html +=   '<div class="session__title">' + t.title + '</div>';
    html +=   '<div class="session__tag">' + t.tag + '</div>';
    html += '</div>';
    if (t.rest) {
      html += '<ul class="session__list is-single"><li>' + t.note + '</li></ul>';
    } else {
      html += '<ul class="session__list">';
      for (var i = 0; i < t.items.length; i++) {
        html += '<li><span>' + t.items[i].name + '</span><span class="reps">' + t.items[i].reps + '</span></li>';
      }
      html += '</ul>';
    }
    els.session.innerHTML = html;
    els.session.classList.toggle('is-rest', !!t.rest);
  }

  function renderDayGrid(currentIdx) {
    if (!els.dayGrid) return;
    var state = loadDone();
    var html  = '';
    for (var i = 0; i < SCHEDULE.length; i++) {
      var s     = SCHEDULE[i];
      var done  = !!state[s.id];
      var isNow = i === currentIdx;
      var cls   = ['day-card'];
      if (isNow)             cls.push('is-now');
      else if (i < currentIdx) cls.push('is-past');
      if (s.cutoff) cls.push('is-cut');
      if (done)     cls.push('is-done');

      // Chip row — every card shows time; conditional chips for cutoff + NOW.
      // Inline chips replace the older absolute-positioned badges so they
      // never collide with the time or the icon.
      var chips =
        '<span class="day-card__chip day-card__chip--time">' + formatTime(s.start) + '</span>' +
        (s.cutoff ? '<span class="day-card__chip day-card__chip--cut" title="Hard cutoff">✕ Cutoff</span>' : '') +
        (isNow    ? '<span class="day-card__chip day-card__chip--now">Now</span>' : '');

      html +=
        '<li class="' + cls.join(' ') + '" data-id="' + s.id + '" role="button" tabindex="0" ' +
            'aria-pressed="' + done + '" aria-label="' + s.label + ' at ' + formatTime(s.start) + '. Click to mark done.">' +
          '<div class="day-card__head">' +
            '<span class="day-card__icon" aria-hidden="true">' + (ICONS[s.icon] || '') + '</span>' +
            '<div class="day-card__chips">' + chips + '</div>' +
          '</div>' +
          '<div class="day-card__cat">' + s.tag + '</div>' +
          '<div class="day-card__label">' + s.label + '</div>' +
          (s.action ? '<div class="day-card__action">' + s.action + '</div>' : '') +
          (s.detail ? '<div class="day-card__detail">' + s.detail + '</div>' : '') +
          '<span class="day-card__check" aria-hidden="true">' + CHECK_SVG + '</span>' +
        '</li>';
    }
    els.dayGrid.innerHTML = html;
    updateDoneCount(state);
  }

  function updateDoneCount(state) {
    if (!els.dayCount) return;
    var done = 0;
    for (var i = 0; i < SCHEDULE.length; i++) if (state[SCHEDULE[i].id]) done++;
    els.dayCount.innerHTML = '<strong>' + done + '</strong>&nbsp;/&nbsp;' + SCHEDULE.length + '&nbsp;done';
  }

  // ──────────────────────────────────────────────────────────────
  // Interaction — toggle done state on a card (click + keyboard)
  // ──────────────────────────────────────────────────────────────
  function toggleCard(card) {
    var id = card.getAttribute('data-id'); if (!id) return;
    var state = loadDone();
    state[id] = !state[id];
    saveDone(state);
    card.classList.toggle('is-done', !!state[id]);
    card.setAttribute('aria-pressed', !!state[id]);
    updateDoneCount(state);
  }

  function wireDayGrid() {
    if (!els.dayGrid) return;
    els.dayGrid.addEventListener('click', function (e) {
      var card = e.target.closest('.day-card');
      if (card) toggleCard(card);
    });
    els.dayGrid.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      var card = e.target.closest('.day-card');
      if (card) { e.preventDefault(); toggleCard(card); }
    });
  }

  // ──────────────────────────────────────────────────────────────
  // Tick loop — full render on minute change, clock-only between
  // ──────────────────────────────────────────────────────────────
  function fullRender() {
    var n = nowState();
    patchScheduleForToday(n.weekday);
    renderHeader(n.d, n.weekday);
    renderClock(n.d);
    var idx = renderNow(n.mins);
    renderSession(n.weekday);
    renderDayGrid(idx);
  }

  function startTickLoop() {
    var lastMinute = -1;
    var lastDayKey = todayKey();
    setInterval(function () {
      var n = nowState();
      renderClock(n.d);
      if (n.mins === lastMinute) return;
      lastMinute = n.mins;
      fullRender();
      // Midnight rollover — re-render against the new day's bucket.
      var k = todayKey();
      if (k !== lastDayKey) { lastDayKey = k; renderDayGrid(currentSlotIndex(n.mins)); }
    }, 1000);
  }

  // ──────────────────────────────────────────────────────────────
  // Bootstrap
  // ──────────────────────────────────────────────────────────────
  fullRender();
  wireDayGrid();
  startTickLoop();
})();
