# app.py
# Flask server: 提供 DZI/.dzi 與 tiles，並包含簡單註解 API 與影像檢測端點。
# 中文註解：保持與你現有 app.py 功能一致，並確保能搭配下方 tile_generator.py 所產生的 DeepZoom 結構。

import os
import sqlite3
from flask import Flask, request, jsonify, send_from_directory, g, render_template
import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TILES_DIR = os.path.join(BASE_DIR, 'tiles_output')
DB_PATH = os.path.join(BASE_DIR, 'annotations.db')

app = Flask(__name__, template_folder='templates')

# ----------------- Database helpers -----------------
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    # 如果你有 db_schema.sql，可在此讀取建立資料表
    schema_path = os.path.join(BASE_DIR, 'db_schema.sql')
    if os.path.exists(schema_path) and not os.path.exists(DB_PATH):
        with app.app_context():
            db = get_db()
            with open(schema_path, 'r', encoding='utf-8') as f:
                db.executescript(f.read())
            db.commit()

# ----------------- Tile serving -----------------
@app.route('/dzi/<path:filename>')
def serve_dzi(filename):
    # 例如 /dzi/image.dzi
    return send_from_directory(TILES_DIR, filename)

@app.route('/tiles/<path:filename>')
def serve_tile_file(filename):
    # Serve from nested "image_files" directory
    image_dir = os.path.join(TILES_DIR, "image_files")
    file_path = os.path.join(image_dir, filename)

    # Debug log (可選)
    print(f"Serving tile from: {file_path}")

    return send_from_directory(image_dir, filename)


# ----------------- Annotation APIs -----------------
@app.route('/annotations', methods=['GET'])
def list_annotations():
    image_id = request.args.get('image_id')
    db = get_db()
    if image_id:
        cur = db.execute('SELECT * FROM annotations WHERE image_id=?', (image_id,))
    else:
        cur = db.execute('SELECT * FROM annotations')
    rows = cur.fetchall()
    items = [dict(r) for r in rows]
    return jsonify(items)

@app.route('/annotations', methods=['POST'])
def create_annotation():
    payload = request.get_json()
    db = get_db()
    keys = ['image_id','type','x','y','width','height','label','zoom_level','metadata']
    vals = [payload.get(k) for k in keys]
    cur = db.execute('INSERT INTO annotations (image_id,type,x,y,width,height,label,zoom_level,metadata) VALUES (?,?,?,?,?,?,?,?,?)', vals)
    db.commit()
    return jsonify({'id': cur.lastrowid}), 201

@app.route('/annotations/<int:ann_id>', methods=['PUT'])
def update_annotation(ann_id):
    payload = request.get_json()
    db = get_db()
    for k, v in payload.items():
        if k in ['type','x','y','width','height','label','zoom_level','metadata']:
            db.execute(f'UPDATE annotations SET {k}=? WHERE id=?', (v, ann_id))
    db.commit()
    return jsonify({'status':'ok'})

@app.route('/annotations/<int:ann_id>', methods=['DELETE'])
def delete_annotation(ann_id):
    db = get_db()
    db.execute('DELETE FROM annotations WHERE id=?', (ann_id,))
    db.commit()
    return jsonify({'status':'deleted'})

# ----------------- Simple CV detection endpoint -----------------
@app.route('/detect_features', methods=['POST'])
def detect_features():
    # 接收小塊影像上傳（file）
    if 'file' not in request.files:
        return jsonify({'error':'no file uploaded'}), 400
    f = request.files['file']
    arr = np.frombuffer(f.read(), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        return jsonify({'error':'invalid image'}), 400
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1) Canny 邊緣
    edges = cv2.Canny(gray, 100, 200)

    # 2) HoughCircles 偵測圓形（坑洞示範）
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20, param1=50, param2=30, minRadius=5, maxRadius=200)
    circles_out = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for c in circles[0, :]:
            circles_out.append({'x': int(c[0]), 'y': int(c[1]), 'r': int(c[2])})

    # 3) Find bright spots (simple blob by threshold)
    _, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bright_spots = []
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if w*h > 9:
            bright_spots.append({'x': x, 'y': y, 'w': w, 'h': h})

    return jsonify({'circles': circles_out, 'bright_spots': bright_spots})

# ----------------- Frontend -----------------
@app.route('/')
def index():
    # 預設載入 tiles_output/image.dzi
    dzi_path = 'image.dzi'
    return render_template('index.html', dzi_url=f'/dzi/{dzi_path}')

if __name__ == '__main__':
    if not os.path.exists(DB_PATH):
        init_db()
    # 若你需要使用 host 0.0.0.0 可調整
    app.run(debug=True, host='0.0.0.0', port=5000)
