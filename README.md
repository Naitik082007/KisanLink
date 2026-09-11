# SIH26 Farmer Market Linkage App — Prototype

A prototype implementation of the workflow described in the supplied SIH-2026 concept note.

## Key idea
Connect farmers and buyers through a transparent agricultural marketplace, with:
- nearest mandi/market discovery
- crop listing and bid workflow
- live bid/price updates
- farm-gate vs retail price/profit calculator
- logistics estimation
- price-history and simple price forecasting
- role-based authentication
- GIS-ready market routing
- research dashboard with government/RBI evidence

## Architecture
- `frontend`: React + Vite + Tailwind CSS + Leaflet
- `backend`: Node.js + Express + Socket.IO + JWT + Mongoose
- `analytics`: FastAPI + Pandas + scikit-learn
- MongoDB is optional for the first demo; the backend falls back to an in-memory store.

## Run

### 1. Frontend
```bash
cd frontend
npm install
npm run dev
```

### 2. Backend
```bash
cd backend
npm install
npm run dev
```

### 3. Analytics service
```bash
cd analytics
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The frontend expects the API at `http://localhost:5000` and analytics at `http://localhost:8000`.

## Prototype data
The included mandi/crop values are clearly marked as DEMO data. They are not presented as live government prices. For production, connect the price service to e-NAM/Agmarknet or another authorized data source.

## Research note
The research report in `docs/` verifies the core market-linkage claims against NITI Aayog, MoSPI, RBI, NABARD and Ministry of Agriculture sources. It specifically avoids claiming that every agricultural supply chain has the same intermediary margin.
