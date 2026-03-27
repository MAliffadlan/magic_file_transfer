import os
import subprocess
import socket
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Mengatur lokasi penyimpanan ke folder tempat script ini berada
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def show_notification(filename):
    """Menampilkan notifikasi desktop di Linux Mint"""
    try:
        # Menjalankan command `notify-send`
        subprocess.run(['notify-send', '-i', 'document-save', 'Magic File Received!', f'File berhasil ditangkap dari HP:\\n{filename}'], check=True)
    except Exception as e:
        print(f"[-] Gagal menampilkan notifikasi desktop: {e}")

def get_local_ip():
    """Mendapatkan IP Address lokal untuk diakses dari HP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Coba koneksi ke IP yang acak untuk memancing IP lokal kita keluar
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

@app.route('/upload', methods=['POST'])
def upload_file():
    # Memeriksa apakah ada file di request
    if 'file' not in request.files:
        return jsonify({"error": "Tidak ada file yang terlampir di pengiriman"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Nama file kosong"}), 400
        
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Mencegah file tertimpa jika namanya sama
        base, extension = os.path.splitext(filename)
        counter = 1
        while os.path.exists(filepath):
            filename = f"{base}_{counter}{extension}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            counter += 1

        # Menyimpan file ke Linux Mint
        file.save(filepath)
        print(f"\\n[+] File ditangkap dengan selamat: {filename}")
        
        # Memunculkan notifikasi keren
        show_notification(filename)
        
        return jsonify({"message": "File berhasil diluncurkan ke laptop!", "filename": filename}), 200

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 5050
    
    print("\\n" + "="*50)
    print("🚀 MAGIC RECEIVER AKTIF! 🚀")
    print("="*50)
    print(f"Server berjalan di  : http://{local_ip}:{port}")
    print(f"Lokasi penyimpanan: {UPLOAD_FOLDER}")
    print("="*50)
    print("Menunggu file dilempar dari HP... (Tekan CTRL+C untuk berhenti)\\n")
    
    # Menjalankan server di 0.0.0.0 agar bisa diakses alat lain dalam WiFi lokal
    app.run(host='0.0.0.0', port=port, debug=False)
