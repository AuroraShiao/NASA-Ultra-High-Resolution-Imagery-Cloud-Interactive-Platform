<h1>NASA Ultra High Resolution Imagery Cloud Interactive Platform 🌌🛰️</h1>

<p>An interactive cloud platform designed for real-time visualization, processing, and analysis of NASA's ultra-high-resolution satellite imagery and spatial datasets.</p>

**[ 💻 Python 3.9+ ]** **[ ⚡ FastAPI ]** **[ ⚛️ React ]** **[ 📜 MIT License ]**

<hr>

<h2>📌 專案簡介 (Overview)</h2>
<p><b>NASA Ultra High Resolution Imagery Cloud Interactive Platform</b> 是一個結合雲端原生地理資訊技術（Cloud-Native Geospatial Technologies）與 Web 互動圖台的平台。本專案旨在提供高效、流暢的超高解析度衛星影像（如 Cloud Optimized GeoTIFF, COG）動態切片與即時視覺化服務，讓使用者無需下載動輒數十 GB 的原始檔即可線上進行空間資料探索與波段分析。</p>

<hr>

<h2>✨ 核心功能 (Key Features)</h2>
<ul>
  <li>🗺️ <b>動態瓦片切片 (Dynamic Tile Rendering)</b>：基於 COG 與 TiTiler，實現巨幅衛星影像的即時動態金字塔切片與隨選渲染。</li>
  <li>☁️ <b>雲端串流整合 (Cloud Streaming Integration)</b>：直接讀取 AWS S3 或 NASA Earthdata 雲端儲存的地理空間數據。</li>
  <li>📊 <b>多波段與假色合成 (Multispectral Analysis)</b>：支援動態調整波段組合（如真彩色、假色紅外線）與 NDVI 等指標運算。</li>
  <li>🔍 <b>互動式 Web 圖台 (Interactive Web Map UI)</b>：使用 React 與 MapLibre GL 打造，支援快速平移、平滑縮放與空間 ROI 獲取。</li>
  <li>🚀 <b>OpenAPI / Swagger 介面</b>：完整後端 RESTful API 規範，方便整合第三方 GIS 工具與數據串流。</li>
</ul>

<hr>

<h2>🛠️ 技術棧 (Tech Stack)</h2>

<table border="1">
  <thead>
    <tr>
      <th>領域</th>
      <th>技術 / 套件</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>前端 (Frontend)</b></td>
      <td>React, MapLibre GL, Leaflet, Axios, Vite</td>
    </tr>
    <tr>
      <td><b>後端 (Backend)</b></td>
      <td>Python 3.9+, FastAPI, Uvicorn, Pydantic</td>
    </tr>
    <tr>
      <td><b>空間資料處理 (Geospatial)</b></td>
      <td>TiTiler, Rasterio, GDAL, Cloud Optimized GeoTIFF (COG)</td>
    </tr>
    <tr>
      <td><b>部署與開發 (DevOps)</b></td>
      <td>Docker, Docker-Compose, Git</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>📁 專案目錄結構 (Directory Structure)</h2>

<pre><code>NASA-Ultra-High-Resolution-Imagery-Cloud-Interactive-Platform/
├── backend/            # Python FastAPI 後端服務與 TiTiler 圖資切片 API
│   ├── main.py         # 後端進入點
│   └── requirements.txt# 後端套件依賴清單
├── frontend/           # React 互動式地圖前端應用
│   ├── src/            # 前端原始碼與地圖組件
│   ├── package.json    # 前端依賴項與腳本設定
│   └── vite.config.js  # Vite 建置組態
├── docs/               # 專案架構文件與 API 規格說明
└── README.md           # 專案說明文件</code></pre>

<hr>

<h2>🚀 快速開始 (Quick Start)</h2>

<h3>前置需求 (Prerequisites)</h3>
<ul>
  <li><a href="[https://git-scm.com/](https://git-scm.com/)">Git</a></li>
  <li><a href="[https://www.python.org/](https://www.python.org/)">Python 3.9+</a></li>
  <li><a href="[https://nodejs.org/](https://nodejs.org/)">Node.js 16+</a></li>
</ul>

<h3>1. 克隆儲存庫 (Clone Repository)</h3>
<pre><code>git clone [https://github.com/AuroraShiao/NASA-Ultra-High-Resolution-Imagery-Cloud-Interactive-Platform.git](https://github.com/AuroraShiao/NASA-Ultra-High-Resolution-Imagery-Cloud-Interactive-Platform.git)
cd NASA-Ultra-High-Resolution-Imagery-Cloud-Interactive-Platform</code></pre>

<h3>2. 後端環境設定 (Backend Setup)</h3>
<pre><code>cd backend
python -m venv venv

# Windows 啟動虛擬環境：
# venv\Scripts\activate

# macOS / Linux 啟動虛擬環境：
source venv/bin/activate

pip install -r requirements.txt
python main.py</code></pre>
<p>💡 後端啟動後，可造訪 API 互動文件：<code>http://localhost:8000/docs</code></p>

<h3>3. 前端環境設定 (Frontend Setup)</h3>
<pre><code>cd ../frontend
npm install
npm run dev</code></pre>
<p>💡 開啟瀏覽器訪問 <code>http://localhost:5173</code> 即可體驗互動式地圖平台。</p>

<hr>

<h2>🤝 貢獻指南 (Contributing)</h2>
<p>歡迎提交 Pull Request 或開立 Issues 提出建議與改善方案！</p>
<ol>
  <li>Fork 本專案</li>
  <li>建立功能分支 (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li>提交變更 (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
  <li>推送至分支 (<code>git push origin feature/AmazingFeature</code>)</li>
  <li>開啟 Pull Request</li>
</ol>

<hr>

<h2>📜 授權條款 (License)</h2>
<p>本專案採用 <a href="LICENSE">MIT License</a> 授權條款。</p>
