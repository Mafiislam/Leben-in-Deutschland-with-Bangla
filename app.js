/* Leben in Deutschland: Deutsch, English, বাংলা
 * Plain JavaScript, no dependencies. Data: data/questions.json */
(function () {
  'use strict';

  const LANGS = ['de', 'en', 'bn'];
  const LANG_NAME = { de: 'Deutsch', en: 'English', bn: 'বাংলা' };
  const PASS_MARK = 17, EXAM_TOTAL = 33, EXAM_GENERAL = 30, EXAM_STATE = 3, EXAM_MINUTES = 60;

  /* ---------- interface text ---------- */
  const T = {
    title: { de: 'Leben in Deutschland Test', en: 'Life in Germany Test', bn: 'লেবেন ইন ডয়চল্যান্ড টেস্ট' },
    lede: {
      de: 'Übe alle Fragen des Einbürgerungstests auf Deutsch, Englisch und Bengalisch.',
      en: 'Practise every question of the German citizenship test in German, English and Bangla.',
      bn: 'জার্মান নাগরিকত্ব পরীক্ষার সব প্রশ্ন জার্মান, ইংরেজি ও বাংলায় অনুশীলন করুন।'
    },
    showLangs: { de: 'Sprachen', en: 'Languages', bn: 'ভাষা' },
    study: { de: 'Lernen', en: 'Study', bn: 'পড়াশোনা' },
    studyD: { de: 'Alle Fragen mit Antworten und Erklärungen', en: 'All questions with answers and explanations', bn: 'উত্তর ও ব্যাখ্যাসহ সব প্রশ্ন' },
    quiz: { de: 'Übungsquiz', en: 'Practice quiz', bn: 'অনুশীলন কুইজ' },
    quizD: { de: 'Frage für Frage mit sofortigem Feedback', en: 'Question by question with instant feedback', bn: 'প্রতিটি প্রশ্নের সাথে সাথে ফলাফল' },
    exam: { de: 'Prüfungssimulation', en: 'Exam simulation', bn: 'পরীক্ষার মহড়া' },
    examD: { de: '33 Fragen, 60 Minuten, 17 richtige zum Bestehen', en: '33 questions, 60 minutes, 17 correct to pass', bn: '৩৩টি প্রশ্ন, ৬০ মিনিট, পাস করতে ১৭টি সঠিক' },
    mistakes: { de: 'Meine Fehler', en: 'My mistakes', bn: 'আমার ভুলগুলো' },
    mistakesD: { de: 'Falsch beantwortete Fragen wiederholen', en: 'Repeat questions you got wrong', bn: 'যেগুলো ভুল হয়েছে সেগুলো আবার করুন' },
    progress: { de: 'Dein Fortschritt', en: 'Your progress', bn: 'আপনার অগ্রগতি' },
    learnedOf: { de: 'gelernt', en: 'learned', bn: 'শেখা হয়েছে' },
    general: { de: 'Allgemeine Fragen', en: 'General questions', bn: 'সাধারণ প্রশ্ন' },
    stateQs: { de: 'Fragen zu deinem Bundesland', en: 'Questions for your state', bn: 'আপনার রাজ্যের প্রশ্ন' },
    state: { de: 'Bundesland', en: 'State (Bundesland)', bn: 'রাজ্য (বুন্দেসল্যান্ড)' },
    all: { de: 'Alle', en: 'All', bn: 'সব' },
    search: { de: 'Fragen suchen…', en: 'Search questions…', bn: 'প্রশ্ন খুঁজুন…' },
    noResult: { de: 'Keine Treffer.', en: 'No results.', bn: 'কিছু পাওয়া যায়নি।' },
    question: { de: 'Frage', en: 'Question', bn: 'প্রশ্ন' },
    explanation: { de: 'Erklärung', en: 'Explanation', bn: 'ব্যাখ্যা' },
    learnedBtn: { de: '✓ Gelernt', en: '✓ Learned', bn: '✓ শেখা হয়েছে' },
    markBtn: { de: '＋ Als gelernt markieren', en: '＋ Mark as learned', bn: '＋ শেখা হয়েছে চিহ্নিত করুন' },
    unlearned: { de: 'Noch nicht gelernt', en: 'Not learned yet', bn: 'এখনও শেখা হয়নি' },
    hideAns: { de: 'Antworten verbergen', en: 'Hide answers', bn: 'উত্তর লুকান' },
    showAns: { de: 'Antworten zeigen', en: 'Show answers', bn: 'উত্তর দেখান' },
    source: { de: 'Fragenset', en: 'Question set', bn: 'প্রশ্নের সেট' },
    count: { de: 'Anzahl', en: 'Number of questions', bn: 'প্রশ্নের সংখ্যা' },
    start: { de: 'Starten', en: 'Start', bn: 'শুরু করুন' },
    next: { de: 'Weiter', en: 'Next', bn: 'পরবর্তী' },
    prev: { de: 'Zurück', en: 'Back', bn: 'পূর্ববর্তী' },
    finish: { de: 'Abgeben', en: 'Finish', bn: 'শেষ করুন' },
    quit: { de: 'Beenden', en: 'Quit', bn: 'বন্ধ করুন' },
    quitAsk: { de: 'Wirklich beenden? Der Fortschritt dieser Runde geht verloren.', en: 'Quit now? Progress in this round will be lost.', bn: 'সত্যিই বন্ধ করবেন? এই রাউন্ডের অগ্রগতি হারিয়ে যাবে।' },
    correctT: { de: 'Richtig!', en: 'Correct!', bn: 'সঠিক!' },
    wrongT: { de: 'Falsch.', en: 'Wrong.', bn: 'ভুল।' },
    result: { de: 'Ergebnis', en: 'Result', bn: 'ফলাফল' },
    passed: { de: 'Bestanden', en: 'Passed', bn: 'উত্তীর্ণ' },
    failed: { de: 'Nicht bestanden', en: 'Not passed', bn: 'অনুত্তীর্ণ' },
    of: { de: 'von', en: 'of', bn: 'এর মধ্যে' },
    review: { de: 'Falsche Antworten', en: 'Wrong answers', bn: 'ভুল উত্তরগুলো' },
    allRight: { de: 'Alles richtig. Sehr gut!', en: 'All correct. Well done!', bn: 'সব সঠিক। চমৎকার!' },
    again: { de: 'Nochmal', en: 'Try again', bn: 'আবার চেষ্টা করুন' },
    home: { de: 'Startseite', en: 'Home', bn: 'শুরুর পাতা' },
    timeLeft: { de: 'Restzeit', en: 'Time left', bn: 'বাকি সময়' },
    examNote: {
      de: 'Wie in der echten Prüfung: 30 allgemeine Fragen und 3 Fragen zu deinem Bundesland. Mit 17 richtigen Antworten hast du bestanden.',
      en: 'Like the real test: 30 general questions and 3 questions about your state. You pass with 17 correct answers.',
      bn: 'আসল পরীক্ষার মতোই: ৩০টি সাধারণ প্রশ্ন ও আপনার রাজ্যের ৩টি প্রশ্ন। ১৭টি সঠিক উত্তর দিলে উত্তীর্ণ।'
    },
    unanswered: { de: 'Unbeantwortet', en: 'Unanswered', bn: 'উত্তর দেওয়া হয়নি' },
    empty: { de: 'In diesem Set gibt es noch keine Fragen.', en: 'There are no questions in this set yet.', bn: 'এই সেটে এখনও কোনো প্রশ্ন নেই।' },
    resetProg: { de: 'Fortschritt zurücksetzen', en: 'Reset progress', bn: 'অগ্রগতি মুছে ফেলুন' },
    resetAsk: { de: 'Gelernt-Markierungen und Fehlerliste löschen?', en: 'Delete learned marks and the mistakes list?', bn: '"শেখা হয়েছে" চিহ্ন ও ভুলের তালিকা মুছবেন?' },
    disclaimer: {
      de: 'Nur zum Lernen. Fragen zu Amtsträgern ändern sich nach Wahlen. Prüfe aktuelle Angaben beim BAMF.',
      en: 'For study only. Answers about office holders change after elections. Check current facts with BAMF.',
      bn: 'শুধু পড়াশোনার জন্য। নির্বাচনের পর পদাধিকারীদের বিষয়ে উত্তর বদলায়। হালনাগাদ তথ্য BAMF-এ দেখে নিন।'
    },
    credits: {
      de: 'Fragen: BAMF. Deutsche und englische Texte aus dem Projekt von Abdullah Butt (CC BY-NC 4.0). Bengalische Übersetzung: dieses Projekt.',
      en: 'Questions: BAMF. German and English text from the project by Abdullah Butt (CC BY-NC 4.0). Bangla translation: this project.',
      bn: 'প্রশ্ন: BAMF। জার্মান ও ইংরেজি পাঠ আবদুল্লাহ বাটের প্রকল্প থেকে (CC BY-NC 4.0)। বাংলা অনুবাদ: এই প্রকল্প।'
    },
    loadFail: { de: 'Die Daten konnten nicht geladen werden.', en: 'The data could not be loaded.', bn: 'তথ্য লোড করা যায়নি।' },
    shown: { de: 'angezeigt', en: 'shown', bn: 'দেখানো হচ্ছে' },
    img: { de: 'Bild zur Frage', en: 'Picture for the question', bn: 'প্রশ্নের ছবি' }
  };

  /* ---------- storage ---------- */
  const store = {
    get(k, d) { try { const v = localStorage.getItem('lid.' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem('lid.' + k, JSON.stringify(v)); } catch (e) { /* storage blocked */ } },
    raw(k, v) { try { localStorage.setItem('lid.' + k, v); } catch (e) { /* ignore */ } }
  };
  const prefs = {
    ui: store.get('ui', 'en'),
    langs: store.get('langs', ['de', 'en', 'bn']),
    state: store.get('state', ''),
    learned: new Set(store.get('learned', [])),
    mistakes: new Set(store.get('mistakes', [])),
    showAns: store.get('showAns', true)
  };
  if (!LANGS.includes(prefs.ui)) prefs.ui = 'en';
  prefs.langs = LANGS.filter(l => prefs.langs.includes(l));
  if (!prefs.langs.length) prefs.langs = ['en'];
  const saveSets = () => { store.set('learned', [...prefs.learned]); store.set('mistakes', [...prefs.mistakes]); };

  /* ---------- helpers ---------- */
  const $ = (s, r) => (r || document).querySelector(s);
  const app = () => $('#app');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const t = k => (T[k] && (T[k][prefs.ui] || T[k].en)) || k;
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const fmt = n => prefs.ui === 'bn' ? String(n).replace(/\d/g, d => '০১২৩৪৫৬৭৮৯'[d]) : String(n);

  let DATA = null, BY_ID = {}, STATES = [];
  const stateName = s => s['name_' + prefs.ui] || s.name_en;

  /** Text of a field in every active language, main language first. */
  function texts(obj, base) {
    const out = [];
    prefs.langs.forEach(l => {
      const v = obj[base ? base + '_' + l : l];
      if (v) out.push({ l, v });
    });
    return out;
  }
  function textBlock(obj, base, cls) {
    return texts(obj, base).map((x, i) =>
      `<p class="t ${i === 0 ? 'main' : 'alt'} ${cls || ''}" lang="${x.l}">${esc(x.v)}</p>`).join('');
  }
  function optBlock(o) {
    return LANGS.filter(l => prefs.langs.includes(l) && o[l]).map((l, i) =>
      `<p class="t ${i === 0 ? 'main' : 'alt'}" lang="${l}">${esc(o[l])}</p>`).join('');
  }

  /* ---------- question card ---------- */
  function qCard(q, opt) {
    opt = opt || {};
    const reveal = opt.reveal !== false;
    const letters = 'ABCD';
    const label = q.state ? `${t('question')} ${fmt(q.n)} · ${esc(stateName(STATES.find(s => s.slug === q.state)))}` : `${t('question')} ${fmt(q.n)}`;
    const learnedBtn = opt.noLearn ? '' :
      `<button class="learned ${prefs.learned.has(q.id) ? 'on' : ''}" data-learn="${esc(q.id)}">${prefs.learned.has(q.id) ? t('learnedBtn') : t('markBtn')}</button>`;
    let h = `<article class="q" id="q-${esc(q.id)}"><div class="q-head"><span>${label}</span>${learnedBtn}</div>`;
    if (q.image) h += `<img class="qimg" src="${esc(q.image)}" alt="${esc(t('img'))}" loading="lazy">`;
    h += `<div class="q-text">${textBlock(q)}</div><ul class="opts">`;
    q.opts.forEach((o, i) => {
      let cls = '';
      if (opt.picked != null) {
        if (opt.feedback) { if (i === q.correct) cls = 'correct'; else if (i === opt.picked) cls = 'wrong'; }
        else if (i === opt.picked) cls = 'picked';
      } else if (reveal && !opt.selectable && i === q.correct) cls = 'correct';
      if (opt.reviewMode) { if (i === q.correct) cls = 'correct'; else if (i === opt.picked) cls = 'wrong'; }
      const tag = opt.selectable && !opt.locked ? 'button' : 'div';
      h += `<li><${tag} class="opt ${cls}" ${tag === 'button' ? `data-opt="${i}" type="button"` : ''}><span class="k">${letters[i]}</span><span>${optBlock(o)}</span></${tag}></li>`;
    });
    h += '</ul>';
    if (opt.showExp !== false && (reveal || opt.feedback || opt.reviewMode)) {
      const ex = texts(q, 'exp');
      if (ex.length) h += `<div class="exp"><div class="exp-title">💡 ${t('explanation')}</div>${textBlock(q, 'exp')}</div>`;
    }
    return h + '</article>';
  }

  /* ---------- header / chrome ---------- */
  function paintChrome() {
    document.documentElement.lang = prefs.ui;
    document.title = T.title[prefs.ui] + ' · DE EN বাংলা';
    document.querySelectorAll('#uiLang button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.ui === prefs.ui)));
    $('#brand').textContent = T.title[prefs.ui];
    $('#foot').innerHTML = `<p>${esc(t('disclaimer'))}</p><p>${esc(t('credits'))} ` +
      `<a href="https://github.com/abdullahbutt/leben-in-deutschland-test" rel="noopener">Source</a> · ` +
      `<a href="https://www.bamf.de/SharedDocs/Anlagen/DE/Integration/Einbuergerung/gesamtfragenkatalog-lebenindeutschland.html" rel="noopener">BAMF</a></p>`;
  }
  function langChips() {
    return `<div class="chips"><span class="lbl">${t('showLangs')}:</span>` + LANGS.map(l =>
      `<button class="chip" data-lang="${l}" aria-pressed="${prefs.langs.includes(l)}">${LANG_NAME[l]}</button>`).join('') + '</div>';
  }
  function stateSelect(id) {
    return `<label class="field">${t('state')}<select id="${id}"><option value="">—</option>` +
      STATES.map(s => `<option value="${s.slug}" ${prefs.state === s.slug ? 'selected' : ''}>${esc(stateName(s))}</option>`).join('') + '</select></label>';
  }

  /* ---------- sets ---------- */
  const RANGES = [[1, 50], [51, 100], [101, 150], [151, 200], [201, 250], [251, 300]];
  const general = () => DATA.questions.filter(q => !q.state);
  function getSet(key) {
    if (key === 'general') return general();
    if (key === 'unlearned') return DATA.questions.filter(q => !prefs.learned.has(q.id));
    if (key === 'mistakes') return DATA.questions.filter(q => prefs.mistakes.has(q.id));
    if (key === 'all') return DATA.questions;
    if (key.startsWith('r:')) { const [a, b] = key.slice(2).split('-').map(Number); return general().filter(q => q.n >= a && q.n <= b); }
    if (key.startsWith('s:')) return DATA.questions.filter(q => q.state === key.slice(2));
    return [];
  }
  function setOptions(sel) {
    let h = `<option value="general" ${sel === 'general' ? 'selected' : ''}>${t('general')} (1–300)</option>`;
    RANGES.forEach(([a, b]) => { const k = `r:${a}-${b}`; h += `<option value="${k}" ${sel === k ? 'selected' : ''}>${t('question')} ${fmt(a)}–${fmt(b)}</option>`; });
    h += `<option disabled>──────</option>`;
    STATES.forEach(s => { const k = 's:' + s.slug; h += `<option value="${k}" ${sel === k ? 'selected' : ''}>${esc(stateName(s))} (301–310)</option>`; });
    h += `<option disabled>──────</option><option value="unlearned" ${sel === 'unlearned' ? 'selected' : ''}>${t('unlearned')}</option>`;
    h += `<option value="mistakes" ${sel === 'mistakes' ? 'selected' : ''}>${t('mistakes')} (${fmt(prefs.mistakes.size)})</option>`;
    h += `<option value="all" ${sel === 'all' ? 'selected' : ''}>${t('all')} (${fmt(DATA.questions.length)})</option>`;
    return h;
  }

  /* ---------- views ---------- */
  function viewHome() {
    const done = prefs.learned.size, total = DATA.questions.length;
    app().innerHTML = `
      <h1>${esc(t('title'))}</h1><p class="lede">${esc(t('lede'))}</p>
      ${langChips()}
      <div class="grid">
        <a class="tile primary" href="#/study"><b>📖 ${t('study')}</b><span>${t('studyD')}</span></a>
        <a class="tile" href="#/quiz"><b>🎯 ${t('quiz')}</b><span>${t('quizD')}</span></a>
        <a class="tile" href="#/exam"><b>⏱️ ${t('exam')}</b><span>${t('examD')}</span></a>
        <a class="tile" href="#/study/mistakes"><b>🔁 ${t('mistakes')} (${fmt(prefs.mistakes.size)})</b><span>${t('mistakesD')}</span></a>
      </div>
      <div class="card" style="margin-top:1rem"><b>${t('progress')}</b>
        <div class="bar"><i style="width:${(done / total * 100).toFixed(1)}%"></i></div>
        <div class="row between"><span class="count">${fmt(done)} / ${fmt(total)} ${t('learnedOf')}</span>
        <button class="btn ghost small" id="reset">${t('resetProg')}</button></div></div>`;
  }

  let studyState = { set: 'r:1-50', q: '' };
  function viewStudy(setKey) {
    if (setKey) studyState.set = decodeURIComponent(setKey);
    app().innerHTML = `
      <h1>📖 ${t('study')}</h1>
      ${langChips()}
      <div class="row"><label class="field" style="margin:0">${t('source')}<select id="setSel">${setOptions(studyState.set)}</select></label>
      <button class="btn ghost small" id="ansBtn">${prefs.showAns ? t('hideAns') : t('showAns')}</button></div>
      <p></p><input type="search" id="search" placeholder="${esc(t('search'))}" value="${esc(studyState.q)}" aria-label="${esc(t('search'))}">
      <p class="count" id="cnt"></p><div id="list"></div>`;
    paintStudyList();
  }
  function paintStudyList() {
    let list = getSet(studyState.set);
    const needle = studyState.q.trim().toLowerCase();
    let capped = false;
    if (needle) {
      list = DATA.questions.filter(q => (q._s || (q._s = [q.de, q.en, q.bn, ...q.opts.flatMap(o => [o.de, o.en, o.bn])].filter(Boolean).join(' ').toLowerCase())).includes(needle));
      if (list.length > 100) { list = list.slice(0, 100); capped = true; }
    }
    $('#cnt').textContent = `${fmt(list.length)}${capped ? '+' : ''} ${t('shown')}`;
    $('#list').innerHTML = list.length ? list.map(q => qCard(q, { reveal: prefs.showAns })).join('') : `<p class="lede">${needle ? t('noResult') : t('empty')}</p>`;
  }

  /* ---------- quiz & exam engine ---------- */
  let run = null, timerId = null;
  const stopTimer = () => { if (timerId) { clearInterval(timerId); timerId = null; } };

  function viewQuizSetup() {
    stopTimer(); run = null;
    app().innerHTML = `
      <h1>🎯 ${t('quiz')}</h1>${langChips()}
      <div class="card">
        <label class="field">${t('source')}<select id="qSet">${setOptions(store.get('quizSet', 'general'))}</select></label>
        <label class="field">${t('count')}<select id="qCount">${[10, 20, 33, 50, 0].map(n => `<option value="${n}" ${store.get('quizCount', 20) === n ? 'selected' : ''}>${n ? fmt(n) : t('all')}</option>`).join('')}</select></label>
        <p><button class="btn" id="qStart">${t('start')}</button></p>
      </div>`;
  }
  function startQuiz() {
    const key = $('#qSet').value, n = +$('#qCount').value;
    store.set('quizSet', key); store.set('quizCount', n);
    let list = shuffle(getSet(key));
    if (n) list = list.slice(0, n);
    if (!list.length) { alert(t('empty')); return; }
    run = { mode: 'quiz', list, i: 0, picks: {}, done: false };
    viewRun();
  }

  function viewExamSetup() {
    stopTimer(); run = null;
    app().innerHTML = `
      <h1>⏱️ ${t('exam')}</h1>${langChips()}
      <div class="card"><p>${t('examNote')}</p>${stateSelect('eState')}
      <p><button class="btn" id="eStart">${t('start')}</button></p></div>`;
  }
  function startExam() {
    const st = $('#eState').value;
    if (!st) { $('#eState').focus(); return; }
    prefs.state = st; store.set('state', st);
    const list = shuffle(general()).slice(0, EXAM_GENERAL).concat(shuffle(getSet('s:' + st)).slice(0, EXAM_STATE));
    run = { mode: 'exam', list, i: 0, picks: {}, done: false, end: Date.now() + EXAM_MINUTES * 60000 };
    viewRun();
    stopTimer(); timerId = setInterval(tick, 1000);
  }
  function tick() {
    if (!run || run.mode !== 'exam' || run.done) { stopTimer(); return; }
    const left = Math.max(0, run.end - Date.now()), el = $('#timer');
    if (el) { const m = Math.floor(left / 60000), s = Math.floor(left % 60000 / 1000); el.textContent = `${fmt(String(m).padStart(2, '0'))}:${fmt(String(s).padStart(2, '0'))}`; el.classList.toggle('low', left < 5 * 60000); }
    if (left <= 0) finishRun();
  }

  function viewRun() {
    if (!run) return viewHome();
    if (run.done) return viewResult();
    const q = run.list[run.i], total = run.list.length, picked = run.picks[q.id];
    const quiz = run.mode === 'quiz', answered = picked != null;
    const last = run.i === total - 1;
    app().innerHTML = `
      <div class="row between"><span class="count">${fmt(run.i + 1)} / ${fmt(total)}</span>
        ${quiz ? '' : `<span class="timer" id="timer"></span>`}
        <button class="btn ghost small" id="quit">${t('quit')}</button></div>
      <div class="bar"><i style="width:${(run.i + (answered ? 1 : 0)) / total * 100}%"></i></div>
      ${qCard(q, { selectable: true, locked: quiz && answered, picked, feedback: quiz && answered, noLearn: true, reveal: false, showExp: quiz && answered })}
      ${quiz && answered ? `<p><b class="${picked === q.correct ? 'pass' : 'fail'}">${picked === q.correct ? t('correctT') : t('wrongT')}</b></p>` : ''}
      <div class="row between">
        ${quiz ? '<span></span>' : `<button class="btn ghost" id="prev" ${run.i === 0 ? 'disabled' : ''}>${t('prev')}</button>`}
        ${last ? `<button class="btn" id="finish" ${quiz && !answered ? 'disabled' : ''}>${t('finish')}</button>`
               : `<button class="btn" id="next" ${quiz && !answered ? 'disabled' : ''}>${t('next')}</button>`}
      </div>`;
    if (!quiz) tick();
  }
  function pick(i) {
    const q = run.list[run.i];
    if (run.mode === 'quiz' && run.picks[q.id] != null) return;
    run.picks[q.id] = i;
    if (run.mode === 'quiz') {
      if (i === q.correct) prefs.mistakes.delete(q.id); else prefs.mistakes.add(q.id);
      saveSets();
    }
    viewRun();
  }
  function finishRun() {
    if (!run || run.done) return;
    run.done = true; stopTimer();
    run.list.forEach(q => {
      const p = run.picks[q.id];
      if (p == null) return;
      if (p === q.correct) prefs.mistakes.delete(q.id); else prefs.mistakes.add(q.id);
    });
    saveSets(); viewResult();
  }
  function viewResult() {
    const total = run.list.length;
    const right = run.list.filter(q => run.picks[q.id] === q.correct).length;
    const wrong = run.list.filter(q => run.picks[q.id] !== q.correct);
    const exam = run.mode === 'exam';
    const pass = exam ? right >= PASS_MARK : null;
    app().innerHTML = `
      <h1>${t('result')}</h1>
      <div class="card"><div class="score ${exam ? (pass ? 'pass' : 'fail') : ''}">${fmt(right)} ${t('of')} ${fmt(total)}</div>
        ${exam ? `<p><b class="${pass ? 'pass' : 'fail'}">${pass ? t('passed') : t('failed')}</b> <span class="small">(${fmt(PASS_MARK)}/${fmt(EXAM_TOTAL)})</span></p>` : ''}
        <div class="row"><button class="btn" id="again">${t('again')}</button><a class="btn ghost" href="#/">${t('home')}</a></div></div>
      <h2>${t('review')}</h2>
      ${wrong.length ? wrong.map(q => qCard(q, { reviewMode: true, picked: run.picks[q.id], noLearn: true })).join('') : `<p class="lede">${t('allRight')}</p>`}`;
    window.scrollTo(0, 0);
  }

  /* ---------- routing ---------- */
  function route() {
    if (!DATA) return;
    const h = location.hash.replace(/^#\/?/, '');
    const [name, arg] = h.split('/');
    if (name !== 'exam' && name !== 'quiz') stopTimer();
    paintChrome();
    if (name === 'study') viewStudy(arg);
    else if (name === 'quiz') run && run.mode === 'quiz' && !run.done ? viewRun() : viewQuizSetup();
    else if (name === 'exam') run && run.mode === 'exam' && !run.done ? viewRun() : viewExamSetup();
    else viewHome();
    window.scrollTo(0, 0);
  }

  /* ---------- events ---------- */
  document.addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) return;
    if (b.dataset.ui) { prefs.ui = b.dataset.ui; store.raw('ui', JSON.stringify(prefs.ui)); const keep = studyState; route(); studyState = keep; return; }
    if (b.id === 'themeBtn') {
      const cur = document.documentElement.getAttribute('data-theme') ||
        (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      const next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next); store.raw('theme', next); return;
    }
    if (b.dataset.lang) {
      const l = b.dataset.lang, on = prefs.langs.includes(l);
      if (on && prefs.langs.length === 1) return;
      prefs.langs = LANGS.filter(x => (x === l ? !on : prefs.langs.includes(x)));
      store.set('langs', prefs.langs);
      const y = window.scrollY; (run && !run.done) ? viewRun() : (location.hash.startsWith('#/study') ? (viewStudy(), 0) : route()); window.scrollTo(0, y); return;
    }
    if (b.dataset.learn) {
      const id = b.dataset.learn;
      prefs.learned.has(id) ? prefs.learned.delete(id) : prefs.learned.add(id);
      saveSets(); const on = prefs.learned.has(id);
      b.classList.toggle('on', on); b.textContent = on ? t('learnedBtn') : t('markBtn'); return;
    }
    if (b.dataset.opt != null) return pick(+b.dataset.opt);
    if (b.closest('.opt')) return;
    switch (b.id) {
      case 'ansBtn': prefs.showAns = !prefs.showAns; store.set('showAns', prefs.showAns); b.textContent = prefs.showAns ? t('hideAns') : t('showAns'); paintStudyList(); break;
      case 'qStart': startQuiz(); break;
      case 'eStart': startExam(); break;
      case 'next': run.i++; viewRun(); window.scrollTo(0, 0); break;
      case 'prev': run.i--; viewRun(); window.scrollTo(0, 0); break;
      case 'finish': finishRun(); break;
      case 'quit': if (confirm(t('quitAsk'))) { stopTimer(); const m = run.mode; run = null; location.hash = '#/' + (m === 'exam' ? 'exam' : 'quiz'); route(); } break;
      case 'again': { const m = run.mode; run = null; m === 'exam' ? viewExamSetup() : viewQuizSetup(); break; }
      case 'reset': if (confirm(t('resetAsk'))) { prefs.learned.clear(); prefs.mistakes.clear(); saveSets(); viewHome(); } break;
    }
  });
  document.addEventListener('change', e => {
    if (e.target.id === 'setSel') { studyState.set = e.target.value; studyState.q = ''; paintStudyList(); $('#search').value = ''; }
    if (e.target.id === 'eState') { prefs.state = e.target.value; store.set('state', prefs.state); }
  });
  let st;
  document.addEventListener('input', e => {
    if (e.target.id === 'search') { clearTimeout(st); st = setTimeout(() => { studyState.q = e.target.value; paintStudyList(); }, 150); }
  });
  window.addEventListener('hashchange', route);

  /* ---------- boot ---------- */
  fetch('data/questions.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }).then(d => {
    DATA = d; STATES = d.states; BY_ID = Object.fromEntries(d.questions.map(q => [q.id, q]));
    route();
  }).catch(() => { app().innerHTML = `<p class="loading">${esc(T.loadFail[prefs.ui])}</p>`; });
  paintChrome();

  if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
    window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
  }
})();
