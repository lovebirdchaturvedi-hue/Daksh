const CACHE_NAME = 'apd-trade-v1';

// We won't aggressively cache everything yet, just the basics to allow installation.
const urlsToCache = [
  '/',
  '/supplier-login.html',
  '/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request).catch(() => {
        return caches.match(event.request);
    })
  );
});
