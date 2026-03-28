<div align="center">
  <img src="icon-512.png" width="120" alt="Fadlan Send Icon" />
  <h1>🪄 Fadlan Send</h1>
  <p><b>Transfer file dari HP Android ke Laptop dalam sekejap mata — cukup dengan gerakan tangan.</b></p>

  [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![MediaPipe](https://img.shields.io/badge/MediaPipe-AI-FF6F00?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
  [![PWA](https://img.shields.io/badge/PWA-Ready-5A0FC8?style=for-the-badge&logo=pwa&logoColor=white)](https://web.dev/progressive-web-apps/)
</div>

<div align="center">
  <h3>🎬 Demo</h3>
  <p><i>Lihat betapa ajaibnya transfer file hanya dengan gerakan tangan!</i></p>

  <video src="https://github.com/MAliffadlan/magic_file_transfer/raw/main/assets/demo.mp4" controls="controls" muted="muted" style="max-height:640px; min-height: 200px" width="300"></video>
  
  <br><br>
  <blockquote>✊ Genggam → 🖐️ Buka → 💥 File mendarat di laptop!</blockquote>
</div>

---

## ⚡ Kenapa Fadlan Send?

Bosan colok kabel USB? Males buka WhatsApp Web cuma buat kirim satu foto? **Fadlan Send** hadir sebagai solusi transfer file yang *benar-benar* ajaib:

> Pilih foto di Galeri → Share ke Fadlan Send → Kepal tangan ✊ → Buka jari 🖐️ → **BAM!** File langsung muncul di layar laptop.

Tidak ada kabel. Tidak ada login. Tidak ada aplikasi berat. Cukup **tangan kosong**.

---

## 🌟 Fitur

### 🤖 Smart AI Gesture Engine v2
- Deteksi **4 jari sekaligus** (telunjuk, tengah, manis, kelingking) untuk kepalan yang presisi
- **Anti False Trigger** — harus terdeteksi 8 frame berturut-turut
- **Hold Duration** — tangan harus digenggam minimal 1 detik sebelum bisa dilempar
- **Cooldown 3 detik** — mencegah pengiriman ganda yang tidak disengaja
- **Open Validation** — buka tangan harus stabil 5 frame sebelum dianggap sah

### 📲 Native Android Share Integration (PWA)
- Terinstall seperti aplikasi biasa di Home Screen HP
- Muncul langsung di menu **"Bagikan"** bawaan Android (sebelahan sama WhatsApp, Telegram, dll)
- File langsung tertangkap server tanpa perlu pilih ulang

### 🎶 Immersive UX Feedback
- **Sound Effects** — suara synth yang disintesis langsung di browser via Web Audio API (tanpa file audio!)
  - *Wush* saat mulai menggenggam
  - *Tiim* saat genggaman terkunci (armed) 
  - *Ziuung* saat melempar
  - *Ting-ting* saat berhasil mendarat
- **Haptic Vibration** — HP bergetar sesuai tahapan gesture
- **Flying Animation** — ikon 📄 terbang meluncur keluar layar saat file dilempar

### 💻 Auto-Open di Desktop
File yang mendarat di laptop **langsung terbuka otomatis** dengan aplikasi default:

| Jenis File | Dibuka Dengan |
|:---:|:---:|
| 📸 Foto | Image Viewer |
| 🎬 Video | Video Player |
| 📄 PDF | Document Reader |
| 🎵 Audio | Music Player |
| 📝 Teks | Text Editor |

### 🔔 Desktop Notification
Notifikasi OS muncul instan di sudut layar laptop setiap kali file berhasil diterima.

### 🕵️ Hidden Camera Mode
Kamera aktif di latar belakang tapi **tidak terlihat di UI** sama sekali. Tampilannya bersih, hanya kotak instruksi bergaris putus-putus yang elegan.

---

## 🛠️ Kebutuhan Sistem

**Laptop / Desktop (Penerima)**
- Python 3.8+
- Linux (Mint / Ubuntu / Debian) — untuk `notify-send` & `xdg-open`
- Satu jaringan Wi-Fi dengan HP

**Smartphone Android (Pengirim)**
- Google Chrome 76+
- Kamera depan yang berfungsi

---

## 🚀 Instalasi

### 1. Clone & Install

```bash
git clone https://github.com/MAliffadlan/magic_file_transfer.git
cd magic_file_transfer
pip install -r requirements.txt
```

### 2. Jalankan Server

```bash
python3 receiver.py
```

### 3. Buat Tunnel HTTPS (Wajib untuk PWA)

PWA di Android **membutuhkan HTTPS**. Gunakan [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/):

```bash
cloudflared tunnel --url http://127.0.0.1:5050
```

Catat URL `https://xxxx.trycloudflare.com` yang muncul.

### 4. Install di HP Android

1. Buka link Cloudflare di Chrome HP
2. Tap tombol **📲 Install Aplikasi**
3. **Fadlan Send** kini ada di Home Screen!

---

## 🪄 Cara Pakai

```
1. Buka Galeri → Pilih foto/video
2. Tap "Bagikan" → Pilih "Fadlan Send"
3. Layar hijau berkedip = file sudah siap
4. Kepalkan tangan ✊ di depan kamera → Tahan 1 detik
5. Status berubah "SIAP DILEMPAR!" 🔥
6. Buka jari lebar 🖐️ → File terbang ke laptop!
7. File langsung terbuka otomatis di layar laptop 🎉
```

---

## 📁 Struktur Proyek

```
fadlan-send/
├── receiver.py          # Server Flask (penerima file)
├── templates/
│   └── index.html       # Web UI + MediaPipe + Gesture Engine
├── manifest.json        # PWA manifest (Share Target)
├── sw.js                # Service Worker
├── icon-192.png         # App icon 192x192
├── icon-512.png         # App icon 512x512
├── requirements.txt     # Python dependencies
└── .gitignore
```

---

## ⚠️ Catatan Penting

- URL Cloudflare Tunnel bersifat **sementara** — berubah setiap restart. Setelah restart tunnel, **hapus & install ulang** aplikasi di HP.
- Untuk URL permanen, gunakan [Cloudflare Named Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/).
- Jika tampilan tidak berubah setelah update, clear cache browser atau reinstall PWA.

---

<div align="center">
  <sub>Dibuat dengan ☕ dan begadang oleh <a href="https://github.com/MAliffadlan"><b>@MAliffadlan</b></a></sub>
</div>
