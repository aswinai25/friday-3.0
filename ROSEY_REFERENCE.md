# 🚀 ROSEY - Quick Deployment Reference

## Project Name: **rosey**

---

## 📋 Quick Links

| Resource | Link |
|----------|------|
| Railway Dashboard | https://railway.app |
| Vercel Dashboard | https://vercel.com/dashboard |
| GitHub Repository | [Your GitHub Link] |
| LiveKit Console | [Your LiveKit Link] |

---

## 🔧 Quick Commands

### Local Development
```bash
# Terminal 1: Backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Frontend
npm run dev
```

### Local Testing
```bash
# Build frontend
npm run build

# Test production build
npm run start
```

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d

# Access
# Frontend: http://localhost
# Backend: http://localhost:8000
```

---

## 📤 Deployment URLs (After Railway Setup)

### Backend Service
```
Name: rosey-backend
URL: https://rosey-backend.up.railway.app
Environment:
  - LIVEKIT_URL=wss://your-livekit.com
  - LIVEKIT_API_KEY=your_key
  - LIVEKIT_API_SECRET=your_secret
```

### Frontend Service (Vercel)
```
Name: rosey
URL: https://rosey.vercel.app
Environment:
  - REACT_APP_API_URL=https://rosey-backend.up.railway.app
```

---

## 🔐 Environment Variables

### Backend (.env)
```
LIVEKIT_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
```

### Frontend (.env or Vercel Settings)
```
REACT_APP_API_URL=https://rosey-backend.up.railway.app
```

---

## ✅ Health Checks

### Backend Health
```
GET https://rosey-backend.up.railway.app/health
GET https://rosey-backend.up.railway.app/config
```

### Frontend Test
```
Visit: https://rosey.vercel.app
Click: "Start Listening" button
Expected: ✅ Connected to Friday!
```

---

## 📊 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serve HTML |
| `/health` | GET | Health check |
| `/config` | GET | Get LiveKit config |
| `/token` | POST | Generate access token |
| `/clear/{session_id}` | DELETE | Clear session |

---

## 🎯 Next Steps

1. **Backend Ready?**
   - Visit: `https://rosey-backend.up.railway.app/config`
   - Should return JSON with `livekit_url` and `has_credentials`

2. **Frontend Ready?**
   - Visit: `https://rosey.vercel.app`
   - Click "Start Listening"
   - Should show ✅ Connected

3. **Share With Users**
   - Give them: `https://rosey.vercel.app`
   - They can start using Friday immediately

---

## 🆘 Support

| Issue | Check | Fix |
|-------|-------|-----|
| Backend 502 | Railway logs | Restart service |
| Frontend 404 | Vercel logs | Check build logs |
| CORS error | App.py | Already configured |
| Token error | LiveKit credentials | Update .env |

---

## 📱 Mobile Access

```
iOS:  https://rosey.vercel.app
Android: https://rosey.vercel.app
Desktop: https://rosey.vercel.app
```

All devices can access the live application through the Vercel URL.

---

**🎉 Congratulations! ROSEY is deployed and ready to use!**
