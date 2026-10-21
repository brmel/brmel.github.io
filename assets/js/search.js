const input = document.getElementById('search-input');
const results = document.getElementById('search-results');
const status = document.getElementById('search-status');
const fold = (s) => s.normalize('NFD').replace(/\p{M}/gu, '').toLowerCase();
let pages = [];

const card = (p) => {
  const item = document.createElement('li');
  item.className = 'post-entry';
  const meta = document.createElement('p');
  meta.className = 'u-eyebrow entry-eyebrow';
  meta.textContent = [p.section, p.date].filter(Boolean).join(' · ');
  const title = document.createElement('h2');
  title.className = 'entry-title';
  title.textContent = p.title;
  title.dir = 'auto';
  const text = document.createElement('p');
  text.className = 'entry-content';
  text.textContent = p.description;
  text.dir = 'auto';
  const link = document.createElement('a');
  link.className = 'entry-link';
  link.href = p.url;
  link.setAttribute('aria-label', p.title);
  item.append(...(meta.textContent ? [meta] : []), title, text, link);
  return item;
};

const search = () => {
  const query = input.value.trim();
  const terms = fold(query).split(/\s+/).filter((t) => t.length > 1);
  const score = (p) => terms.filter((t) => p.titleKey.includes(t)).length;
  const hits = terms.length ? pages.filter((p) => terms.every((t) => p.key.includes(t))) : [];
  results.replaceChildren(...hits.sort((a, b) => score(b) - score(a)).slice(0, 20).map(card));
  status.textContent = terms.length ? status.dataset.count.replace('{n}', hits.length) : '';
  history.replaceState(null, '', query ? `?q=${encodeURIComponent(query)}` : location.pathname);
};

fetch(input.dataset.index).then((r) => r.json()).then((index) => {
  pages = index.map((p) => ({ ...p, titleKey: fold(p.title), key: fold(`${p.title} ${p.description} ${p.content}`) }));
  input.value = new URLSearchParams(location.search).get('q') || input.value;
  search();
});
input.addEventListener('input', search);
