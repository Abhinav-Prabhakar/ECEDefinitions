/* one·liners — offline app shell */
const CACHE = 'oneliners-v10';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './data/curriculum.json',
  './data/sources.json',
  './assets/icon.svg',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './assets/icon-maskable-512.png',
  './assets/apple-touch-icon.png',
  './assets/favicon-32.png',
  './assets/diagrams.svg',
  './assets/katex/katex.min.css',
  './assets/katex/katex.min.js',
  './assets/fonts/inter-latin-var.woff2',
  './assets/katex/fonts/KaTeX_AMS-Regular.woff2',
  './assets/katex/fonts/KaTeX_Caligraphic-Bold.woff2',
  './assets/katex/fonts/KaTeX_Caligraphic-Regular.woff2',
  './assets/katex/fonts/KaTeX_Fraktur-Bold.woff2',
  './assets/katex/fonts/KaTeX_Fraktur-Regular.woff2',
  './assets/katex/fonts/KaTeX_Main-Bold.woff2',
  './assets/katex/fonts/KaTeX_Main-BoldItalic.woff2',
  './assets/katex/fonts/KaTeX_Main-Italic.woff2',
  './assets/katex/fonts/KaTeX_Main-Regular.woff2',
  './assets/katex/fonts/KaTeX_Math-BoldItalic.woff2',
  './assets/katex/fonts/KaTeX_Math-Italic.woff2',
  './assets/katex/fonts/KaTeX_SansSerif-Bold.woff2',
  './assets/katex/fonts/KaTeX_SansSerif-Italic.woff2',
  './assets/katex/fonts/KaTeX_SansSerif-Regular.woff2',
  './assets/katex/fonts/KaTeX_Script-Regular.woff2',
  './assets/katex/fonts/KaTeX_Size1-Regular.woff2',
  './assets/katex/fonts/KaTeX_Size2-Regular.woff2',
  './assets/katex/fonts/KaTeX_Size3-Regular.woff2',
  './assets/katex/fonts/KaTeX_Size4-Regular.woff2',
  './assets/katex/fonts/KaTeX_Typewriter-Regular.woff2'
];

async function precacheCurriculum(cache) {
  try {
    const url = new URL('./data/curriculum.json', self.location.href).href;
    const response = await fetch(url, { cache: 'no-cache' });
    if (!response || !response.ok) return;

    const index = await response.clone().json();
    await cache.put(url, response.clone());

    const files = [];
    for (const semester of index.semesters || []) {
      for (const subject of semester.subjects || []) {
        if (subject && subject.data) {
          files.push(new URL(subject.data, self.location.href).href);
        }
      }
    }
    await Promise.all(files.map(file => cache.add(file).catch(() => {})));
  } catch (e) {
    // The shell still installs; data will be cached on first online use.
  }
}

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE)
      .then(async cache => {
        await cache.addAll(ASSETS);
        await precacheCurriculum(cache);
      })
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        // Sibling one·liners apps share this origin; only clear this app's caches.
        keys.filter(k => /^oneliners-v\d+$/.test(k) && k !== CACHE)
            .map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE);
      try {
        const fresh = await fetch(request);
        if (fresh && fresh.ok) cache.put(request, fresh.clone());
        return fresh;
      } catch (e) {
        return (await cache.match(request)) || (await cache.match('./index.html')) || (await cache.match('./'));
      }
    })());
    return;
  }

  // Curriculum data changes with each batch, so prefer the network while
  // online and fall back to the cached copy offline.
  if (url.pathname.includes('/data/') && url.pathname.endsWith('.json')) {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE);
      try {
        const fresh = await fetch(request);
        if (fresh && fresh.ok) cache.put(request, fresh.clone());
        return fresh;
      } catch (e) {
        const cached = await cache.match(request);
        if (cached) return cached;
        throw e;
      }
    })());
    return;
  }

  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    const cached = await cache.match(request);
    const network = fetch(request).then(response => {
      if (response && response.ok) cache.put(request, response.clone());
      return response;
    }).catch(() => null);

    return cached || network || Response.error();
  })());
});
