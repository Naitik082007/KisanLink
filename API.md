# API overview

## Auth
`POST /api/auth/login`
```json
{"email":"farmer@example.com","role":"farmer"}
```

## Markets
`GET /api/mandis`

## Demo prices
`GET /api/crops`

## Listings
`POST /api/listings` — JWT required
`GET /api/listings`

## Live events
Socket.IO:
- client emits `bid:create`
- server broadcasts `bid:update`

## Analytics
FastAPI:
- `POST /forecast`
- `GET /health`
