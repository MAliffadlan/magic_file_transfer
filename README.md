<div align="center">
  <h1>🪄 Magic Send v2</h1>
  <p>Transfer file dari Smartphone Android langsung ke Desktop dengan menggunakan Gerakan Tangan (Hand Gestures) bak seorang penyihir.</p>
</div>

---

## 🌟 Fitur Unggulan

- **Native Share Integration**: Terintegrasi seketika dengan menu "Bagikan / Share Target" sistem operasional mutlak OS Android sebagai Aplikasi *Progressive Web App (PWA)* mandiri.
- **AI Hand Tracking**: Menangkap gerakan genggaman (Tarik) ✊ dan lemparan (Dorong) 🖐️ secara *real-time* dan responsif menggunakan **Google MediaPipe AI**.
- **Dark Mode UI**: Antarmuka premium yang modern nan "gaib" *(kamera tersembunyi)*. 
- **No-Install Desktop (Backend)**: Laptop Anda murni hanya menjalankan *script* Python tunggal (Flask server), tanpa *driver* aneh-aneh.
- **Desktop Notifications**: File mendarat dan laptop Anda merespon instan dengan kotak dialog OS (*`notify-send`* untuk Linux).

---

## ⚙️ Persyaratan Kebutuhan

1. **Laptop / Desktop (Sebagai Penerima)**
   - Punya **Python 3.8+**
   - Jaringan area lokal / Wi-Fi bersama.
   - OS Linux / Ubuntu / Mint (Untuk fitur native *Pop-up notify-send* yang *out-of-the-box*).
2. **Smartphone Android (Sebagai Tongkat Sihir/Pengirim)**
   - Aplikasi peramban Google Chrome minimum versi modern (76+).
   - Kamera Selfie yang berfungsi untuk deteksi wajah AI!

---

## 🚀 Instalasi Sistem

### 1. Menyiapkan Penangkap (Server)

Unduh (*clone*) kode ini ke mesin Linux Anda:

```bash
git clone https://github.com/MAliffadlan/magic_file_transfer.git
cd magic_file_transfer
```

Instalasi obat ketergantungannya (Dependencies):

```bash
pip install -r requirements.txt
```

Nyalakan mesin penangkap sihir:

```bash
python3 receiver.py
```

### 2. Rahasia Jalur Aman (PWA Butuh HTTPS!)
Sistem Android masa kini sangat ketat; dilarang keras meng-install `PWA` penangkap file ke dalam HP dari IP address lokal `http://192.168.x.x`. Solusi mujarabnya? Gunakan sambungan VPN/Tunnel ajaib dari internet resmi:

**Cara Jitu Cloudflare Tunnel:**
Buka *terminal* satu lagi bersebelahan dengan server, lalu jalankan terowongan `cloudflared`:
```bash
cloudflared tunnel --url http://127.0.0.1:5050
```
Ambil tautan (URL) ujung-nya yang mengandung ekstensi `.trycloudflare.com`.

### 3. Eksekusi Pengunduhan Pada Handphone
1. Buka URL rahasia `.trycloudflare.com` itu langsung dari Google Chrome Handphone.
2. Di layar akan tertulis dengan menakjubkan **"📲 Install Aplikasi"**. Tinggal sentuh!
3. Aplikasi akan tercatat sebagai **"Magic v2"** di jajaran ikon menu layar beranda (Home Screen) layaknya aplikasi Play Store.

---

## 🪄 Merapal Mantra dan Sihir
1. Jelajahi laci kenangan (Galeri Fotografi) dalam Handphone Anda.
2. Temukan foto, video langka yang mau disalurkan, sentuh fitur/tombol **Bagikan (Share)** milik ponsel.
3. Di dalam roda deretan Aplikasi (seperti saat akan share ke WhatsApp/Tiktok), cari satria pahlawan kita: Aplikasi Bernama **Magic v2**.
4. Terhantam masuk langsung ke Aplikasi Kamera Terselubung, dan Spanduk Hijau Berkedip siap menantang kemampuan Lemparan Batin Anda.
5. Sorot Tangan Ke Depan Posisi Kamera HP Sembarang (Kamera Depan menyala tanpa nampak di mata):
   - **Tarik & Genggam Mengepal Penuh ✊:** Sistem bersiap melakukan inisialisasi dorongan sihir.
   - **Buka Kelima Jari Lebar Mendadak Ke Depan 🖐️:** Lempar secara reflek dengan satu gerakan spontan!
6. Wushhh... Layar mengatakan SIAP, tak lama kemudian Linux PC anda akan bergetar girang menyambut kedatangan *File* Anda di kandang `Documents/share_file`.

### 💡 Fakta Unik
Ketika Anda terlalu bosan menggunakan lemparan sulap atau ada gangguan jaringan (Cache Google Chrome macet di awang-awang), File yang dibagikan dari Web Share akan otomatis disemprotkan terbang "By-Pass" ke Laptop Anda langsung tanpa basa-basi (Fallback Server Feature Terbaru!)

---
*Ditenun sepenuh hati siang & malam dengan bangga mendalam oleh Sang Arsitek (Bos Alif).*
