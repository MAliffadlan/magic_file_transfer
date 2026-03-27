<div align="center">
  <img src="icon-512.png" width="120" alt="Magic Send Icon" style="border-radius: 20px; box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);" />
  <h1>🪄 Magic Send v2 - *The Seamless Spell*</h1>
  <p><b>Pindahkan file dari Smartphone Android langsung ke Desktop secepat kilat dengan Gerakan Tangan Sihir (AI Hand Gestures).</b></p>

  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
  [![Flask](https://img.shields.io/badge/Flask-Server-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
  [![Google MediaPipe](https://img.shields.io/badge/Google-MediaPipe-orange?style=for-the-badge&logo=google)](https://mediapipe.dev/)
  [![PWA Ready](https://img.shields.io/badge/PWA-Ready-green?style=for-the-badge&logo=pwa)](https://web.dev/progressive-web-apps/)
</div>

---

## ⚡ Fitur Utama yang Gila-gilaan Keren

*   📲 **Integrasi Native PWA Android**: Masuk langsung ke menu "Share" bawaan HP. Ngga pusing mikirin IP/Browser lagi!
*   🤖 **Smart AI Hand Tracking v2**: Mendeteksi 4 jari Anda dengan presisi. Dilengkapi fitur *Anti-False Trigger*, *Cooldown*, dan *Hold Duration*. (Powered by Google MediaPipe)
*   🎶 **Sihir Interaktif (UX Engine)**: Rasakan getaran (Haptic Feedback), suara "ngung-ngung" Synth Wave saat mulai Charge Sihir, dan animasi terbang langsung di browser Anda.
*   💻 **Auto-Open di Desktop**: Lempar foto? Langsung buka otomatis! Lempar video? Langsung play tanpa basa-basi! (Via `xdg-open` di Linux)
*   🔔 **Notifikasi Desktop OS**: PC Anda langsung merespon seketika dari sudut layar.
*   🕵️‍♂️ **Spy Mode UI Terlarang**: Antarmuka *Dark Mode* mewah tapi kameranya *hidden*. Anda dikira lagi pegang remote ajaib, padahal ada AI yang ngintip pergerakan jari Anda.

---

## 🛠️ Persyaratan Tempur

1.  **Laptop / Desktop Linux Mint / Ubuntu (Sebagai Penerima/Server)**
    *   Python 3.8+
    *   Satu Jaringan Wi-Fi (Atau jalankan `cloudflared`)
    *   Fitur `notify-send` & `xdg-open` (Bawaan Linux).
2.  **Smartphone Android (Tongkat Sihirnya)**
    *   Google Chrome versi modern (76+)
    *   Kamera Depan Normal.

---

## 🚀 Instalasi: Semudah Menjentikkan Jari

### Tahap 1: Mantra di Laptop

Unduh (*clone*) kode sihir misterius ini ke Linux Anda:

```bash
git clone https://github.com/MAliffadlan/magic_file_transfer.git
cd magic_file_transfer
```

Install bahan baku ramuan:

```bash
pip install -r requirements.txt
```

Nyalakan mesin penangkap sihir:

```bash
python3 receiver.py
```

### Tahap 2: Buat Lingkaran Sihir Online (HTTPS PWA)
Agar ilmu hitam *(Service Worker)* ini lolos ke HP tanpa diblok keamanan Chrome, sambungkan Laptop ke lorong internet publik pakai [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/downloads/):

Jalankan perintah ini di tab terminal sampingnya:
```bash
cloudflared tunnel --url http://127.0.0.1:5050
```
*(Copy URL `https://xxxx.trycloudflare.com` yang dikasih ya!)*

### Tahap 3: Pemasangan Tongkat di Android
1.  Buka Link Tadi dari HP.
2.  Akan muncul tombol **📲 Install Aplikasi**. Pencet dan tunggu.
3.  Sekarang aplikasi "Magic v2" sudah bertengger gagah di *App Drawer* HP Anda!

---

## 🪄 Kelas Praktik Sihir 101

1. Buka **Galeri** (Foto/Video Favorit) di HP Android Anda.
2. Centang file yang ingin dikirim, tap tombol **Bagikan (Share)**.
3. Cari **Magic v2** dari deretan aplikasi (sebelahan sama WhatsApp/IG).
4. Layar PWA akan menyambut dengan warna Hijau (Tanda file sudah tertangkap rohani-nya).
5. **JURUS RAHASIA: Arahkan layar HP ke muka Anda, lalu pada kamera depan...**
    *   **✊ Charge (Genggam Erat):** Layar merespon, HP bergetar tipis, speaker bunyi *wuzzz*. Tahan 1 detik sampai siap.
    *   **🖐️ Lontarkan Jari (Buka Tangan Mendadak):** Suara mendesing, Animasi file terbang melesat di layar HP Anda!
6. **BAM!** File sukses tertransfer instan ke PC Anda, Notifikasi Desktop muncul, dan filenya langsung terbuka tanpa disentuh! 😱

---

### Momen "Wah" (WOW Factor):
Bukan sembarang file transfer, proyek ini fokus totalitas di *User Experience*. Mulai dari *Micro-animations* (animasi dashed-line berkedip saat siap), *Auditory Feedback* (tanpa file audio sama sekali - murni disintetis oleh Web Audio API `AudioContext`), sampai taktil getar saat jari bergerak. Semuanya bikin sistem transfer sepele jadi terasa hidup.

> Dirakit penuh ambisi dan tanpa tidur oleh **@MAliffadlan (Bos Alif)**. Bintangnya GitHub jangan dilupa Bos! ⭐
