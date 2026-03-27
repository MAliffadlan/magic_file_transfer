const CACHE_NAME = 'magic-cache-v5';

self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

// Tidak perlu intercept share-target lagi!
// Server Python langsung menangkap file dari Galeri Android.
// SW ini hanya ada agar Chrome mau menginstall PWA.
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
