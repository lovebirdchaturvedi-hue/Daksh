// APD Global Trade - Service Worker (PWA)
const CACHE_NAME = 'apd-trade-v2.1';
const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/public-rfqs.html',
  '/supplier-login.html',
  '/membership.html',
  '/manifest.json',
  '/assets/icons/icon-192.png',
  '/assets/icons/icon-512.png',
  '/assets/js/mobile-pwa.js'
];

// Install: Cache critical assets
self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_ASSETS).catch((err) => {
        console.warn('Pre-caching partial failure (assets may be loaded dynamically):', err);
      });
    })
  );
});

// Activate: Clean up old caches & take control immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: Network-first for dynamic HTML & API, cache-first for static media/icons
self.addEventListener('fetch', (event) => {
  const req = event.request;
  const url = new URL(req.url);

  // Skip non-GET requests and external APIs (Firebase, Razorpay, etc.)
  if (req.method !== 'GET' || !url.origin.includes(self.location.origin)) {
    return;
  }

  // Static assets (images, icons, css, js) -> Cache First with Network Fallback
  if (
    url.pathname.match(/\.(png|jpg|jpeg|svg|webp|ico|css|woff2?)$/) ||
    url.pathname.includes('/assets/icons/')
  ) {
    event.respondWith(
      caches.match(req).then((cached) => {
        if (cached) return cached;
        return fetch(req).then((res) => {
          if (res.status === 200) {
            const clone = res.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(req, clone));
          }
          return res;
        });
      })
    );
    return;
  }

  // HTML Pages -> Network First with Cache Fallback for offline reading
  if (req.headers.get('accept') && req.headers.get('accept').includes('text/html')) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          if (res.status === 200) {
            const clone = res.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(req, clone));
          }
          return res;
        })
        .catch(() => {
          return caches.match(req).then((cached) => {
            if (cached) return cached;
            return caches.match('/public-rfqs.html');
          });
        })
    );
    return;
  }

  // Default: Network with cache fallback
  event.respondWith(
    fetch(req).catch(() => caches.match(req))
  );
});
