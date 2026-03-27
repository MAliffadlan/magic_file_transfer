import os
import uuid
import subprocess
import socket
from flask import Flask, request, jsonify, render_template, send_from_directory, redirect

from werkzeug.utils import secure_filename

app = Flask(__name__)

# Mengatur lokasi penyimpanan ke folder tempat script ini berada
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
STAGING_FOLDER = os.path.join(UPLOAD_FOLDER, '.staging')
os.makedirs(STAGING_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STAGING_FOLDER'] = STAGING_FOLDER

# Menyimpan info file yang sedang "menunggu dilempar"
pending_files = {}

def show_notification(filename):
    """Menampilkan notifikasi desktop di Linux Mint"""
    try:
        subprocess.run(['notify-send', '-i', 'document-save',
                        'Fadlan Send - File Received!',
                        f'File berhasil ditangkap dari HP:\n{filename}'], check=True)
    except Exception as e:
        print(f"[-] Gagal menampilkan notifikasi desktop: {e}")

def open_file(filepath):
    """Membuka file otomatis dengan aplikasi default Linux"""
    try:
        subprocess.Popen(['xdg-open', filepath])
        print(f"[👁️] File dibuka otomatis: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"[-] Gagal membuka file: {e}")

def get_local_ip():
    """Mendapatkan IP Address lokal untuk diakses dari HP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'manifest.json')

@app.route('/icon-192.png')
def serve_icon192():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'icon-192.png')

@app.route('/icon-512.png')
def serve_icon512():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'icon-512.png')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'sw.js')

# ============================================================
# SHARE TARGET: Menangkap file langsung dari Galeri Android
# ============================================================
@app.route('/share-target', methods=['GET', 'POST'])
def share_target():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:
            # Simpan file ke staging area dengan ID unik
            file_id = str(uuid.uuid4())[:8]
            original_name = secure_filename(file.filename)
            staging_path = os.path.join(app.config['STAGING_FOLDER'], f"{file_id}_{original_name}")
            file.save(staging_path)

            # Catat di memori server
            pending_files[file_id] = {
                'original_name': original_name,
                'staging_path': staging_path
            }

            print(f"\n[📥] File dari Galeri ditangkap: {original_name} (ID: {file_id})")
            print(f"[⏳] Menunggu genggaman tangan untuk melempar...")

            # Redirect ke halaman kamera dengan ID file pending
            return redirect(f'/?pending={file_id}')

    # GET fallback
    return redirect('/')

# ============================================================
# API: Cek info file pending (dipanggil oleh JS di halaman)
# ============================================================
@app.route('/pending/<file_id>')
def get_pending_info(file_id):
    if file_id in pending_files:
        return jsonify({
            'found': True,
            'filename': pending_files[file_id]['original_name']
        })
    return jsonify({'found': False})

# ============================================================
# API: Lempar/Konfirmasi file pending -> pindahkan ke folder utama
# ============================================================
@app.route('/throw/<file_id>', methods=['POST'])
def throw_pending(file_id):
    if file_id not in pending_files:
        return jsonify({'error': 'File tidak ditemukan atau sudah dilempar'}), 404

    info = pending_files[file_id]
    staging_path = info['staging_path']
    filename = info['original_name']

    # Tentukan path final (cegah tabrakan nama)
    final_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    base, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(final_path):
        filename = f"{base}_{counter}{extension}"
        final_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        counter += 1

    # Pindahkan dari staging ke folder utama
    os.rename(staging_path, final_path)
    del pending_files[file_id]

    print(f"\n[🚀] FILE BERHASIL DILEMPAR: {filename}")
    show_notification(filename)
    open_file(final_path)

    return jsonify({'message': 'File berhasil mendarat di laptop!', 'filename': filename}), 200

# ============================================================
# API: Upload manual (dari tombol pilih file + gesture)
# ============================================================
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Tidak ada file"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nama file kosong"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    base, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filepath):
        filename = f"{base}_{counter}{extension}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        counter += 1

    file.save(filepath)
    print(f"\n[+] File ditangkap dengan selamat: {filename}")
    show_notification(filename)
    open_file(filepath)

    return jsonify({"message": "File berhasil diluncurkan ke laptop!", "filename": filename}), 200

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 5050

    print("\n" + "="*50)
    print("🚀 FADLAN SEND AKTIF! 🚀")
    print("="*50)
    print(f"Server berjalan di  : http://{local_ip}:{port}")
    print(f"Lokasi penyimpanan  : {UPLOAD_FOLDER}")
    print("="*50)
    print("Menunggu file dilempar dari HP... (Tekan CTRL+C untuk berhenti)\n")

    app.run(host='0.0.0.0', port=port, debug=False)
