import os
import shutil
import zipfile
from flask import Flask, render_template, request, send_file, redirect, url_for
import yt_dlp

app = Flask(__name__)
UPLOAD_FOLDER = '/app/downloads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        session_dir = os.path.join(UPLOAD_FOLDER, 'session_mp3s')
        if os.path.exists(session_dir):
            shutil.rmtree(session_dir)
        os.makedirs(session_dir)

        links = file.read().decode('utf-8').splitlines()
        clean_links = [line.strip() for line in links if line.strip() and not line.strip().startswith('#')]

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(session_dir, '%(title)s.%(ext)s'),
            'ignoreerrors': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 122.0.0.0 Safari/537.36'
            }
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(clean_links)

        zip_path = os.path.join(UPLOAD_FOLDER, 'youtube_mp3s.zip')
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(session_dir):
                for f in files:
                    if f.endswith('.mp3'):
                        file_path = os.path.join(root, f)
                        zipf.write(file_path, os.path.basename(file_path))

        return send_file(zip_path, as_attachment=True, download_name='youtube_mp3s.zip')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
