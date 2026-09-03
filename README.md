# NASA Ultra High Resolution Imagery Cloud Interactive Platform 🌌🛰️

An interactive cloud platform designed for real-time visualization, processing, and analysis of NASA's ultra-high-resolution satellite imagery and spatial datasets.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/AuroraShiao/NASA-Ultra-High-Resolution-Imagery-Cloud-Interactive-Platform)
![Python Version](https://img.shields.io/badge/Python-3.9+-green?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-18+-61DAFB?logo=react)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 專案簡介 (Overview)

**NASA Ultra High Resolution Imagery Cloud Interactive Platform** 是一個結合雲端原生地理資訊技術（Cloud-Native Geospatial Technologies）與 Web 互動圖台的平台。本專案旨在提供高效、流暢的超高解析度衛星影像（如 Cloud Optimized GeoTIFF, COG）動態切片與即時視覺化服務，讓使用者無需下載動輒數十 GB 的原始檔即可線上進行空間資料探索與波段分析。

---

## ✨ 核心功能 (Key Features)

- 🗺️ **動態瓦片切片 (Dynamic Tile Rendering)**：基於 COG 與 TiTiler，實現巨幅衛星影像的即時動態金字塔切片與隨選渲染。
- ☁️ **雲端串流整合 (Cloud Streaming Integration)**：直接讀取 AWS S3 或 NASA Earthdata 雲端儲存的地理空間數據。
- 📊 **多波段與假色合成 (Multispectral Analysis)**：支援動態調整波段組合（如真彩色、假色紅外線）與 NDVI 等指標運算。
- 🔍 **互動式 Web 圖台 (Interactive Web Map UI)**：使用 React 與 MapLibre GL 打造，支援快速平移、平滑縮放與空間 ROI 獲取。
- 🚀 **OpenAPI / Swagger 介面**：完整後端 RESTful API 規範，方便整合第三方 GIS 工具與數據串流。

---

## 🛠️ 技術棧 (Tech Stack)

| 領域 | 技術 / 套件 |
| :--- | :--- |
| **前端 (Frontend)** | React, MapLibre GL, Leaflet, Axios, Vite |
| **後端 (Backend)** | Python 3.9+, FastAPI, Uvicorn, Pydantic |
| **空間資料處理 (Geospatial)** | TiTiler, Rasterio, GDAL, Cloud Optimized GeoTIFF (COG) |
| **部署與開發 (DevOps)** | Docker, Docker-Compose, Git |

---

## 📁 專案目錄結構 (Directory Structure)

```text
NASA-Ultra-High-Resolution-Imagery-Cloud-Interactive-Platform/
├── backend/            # Python FastAPI 後端服務與 TiTiler 圖資切片 API
│   ├── main.py         # 後端進入點
│   └── requirements.txt# 後端套件依賴清單
├── frontend/           # React 互動式地圖前端應用
│   ├── src/            # 前端原始碼與地圖組件
│   ├── package.json    # 前端依賴項與腳本設定
│   └── vite.config.js  # Vite 建置組態
├── docs/               # 專案架構文件與 API 規格說明
└── README.md           # 專案說明文件
