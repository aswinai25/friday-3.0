# Railway Deployment Guide for "rosey" Project

## 🚀 Deploy to Railway with Project Name: **rosey**

### Prerequisites
- GitHub account (repo must be pushed)
- Railway account (https://railway.app)
- LiveKit credentials

---

## Step 1: Deploy Backend to Railway

### 1.1 Create Railway Project
1. Go to **https://railway.app**
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select your `friday-3.0` repository
4. Railway will auto-detect it's a Python project

### 1.2 Configure Backend Service
1. Railway creates a service automatically
2. Rename it to: **rosey-backend**
3. In Settings → Variables, add these environment variables:

```
LIVEKIT_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
```

4. Click **Deploy** → Railway builds and deploys
5. You'll get a URL like: `https://rosey-backend.up.railway.app`

---

## Step 2: Deploy Frontend to Railway (or Vercel)

### Option A: Deploy Frontend on Railway (Same Project)

1. In your Railway project, click **"New Service"**
2. Select **"GitHub Repo"** → Same repo
3. In settings, set:
   - **Root Directory**: `/` (or leave blank)
   - **Build Command**: `npm run build`
   - **Start Command**: `npm run start` or `npx serve -s dist -l 3000`
   - **Port**: `3000`

4. Add Environment Variables:
```
REACT_APP_API_URL=https://rosey-backend.up.railway.app
```

5. Deploy → Get URL like: `https://rosey-frontend.up.railway.app`

### Option B: Deploy Frontend on Vercel (Recommended)

1. Go to **https://vercel.com**
2. Click **"Add New"** → **"Project"**
3. Import your GitHub repo
4. Select the framework: **Webpack (Other)**
5. Add Environment Variable:
   ```
   REACT_APP_API_URL=https://rosey-backend.up.railway.app
   ```
6. Click **Deploy**
7. You'll get a URL like: `https://rosey.vercel.app`

---

## Step 3: Connect Frontend to Backend

After deployment, update the frontend with your backend URL:

### If using Railway for both:
- Backend URL: `https://rosey-backend.up.railway.app`
- Frontend URL: `https://rosey-frontend.up.railway.app`

### If using Vercel + Railway:
- Backend URL: `https://rosey-backend.up.railway.app`
- Frontend URL: `https://rosey.vercel.app`

Set `REACT_APP_API_URL` in your frontend deploy settings to point to the backend.

---

## Step 4: Verify Deployment

1. Visit your frontend URL
2. Click **"Start Listening"** button
3. Check browser console for any errors
4. Should see: ✅ Connected to Friday!

---

## 📝 Your Deployment Details

| Component | Service Name | URL |
|-----------|------------|-----|
| Backend | rosey-backend | https://rosey-backend.up.railway.app |
| Frontend | rosey-frontend (or rosey on Vercel) | https://rosey.vercel.app or https://rosey-frontend.up.railway.app |

---

## 🔐 Environment Variables Summary

**Backend (Railway) - Environment Variables:**
```
LIVEKIT_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your_key
LIVEKIT_API_SECRET=your_secret
```

**Frontend (Vercel/Railway) - Environment Variables:**
```
REACT_APP_API_URL=https://rosey-backend.up.railway.app
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| CORS errors | Backend CORS is already configured in app.py |
| Token endpoint 404 | Make sure backend service is running |
| Connection timeout | Check LiveKit URL and credentials |
| Frontend can't find backend | Verify REACT_APP_API_URL env variable |

---

## After Deployment

Once deployed:
- ✅ Share your frontend URL with users
- ✅ Backend is internal only (accessed from frontend)
- ✅ LiveKit handles voice/video communication
- ✅ Monitor logs in Railway dashboard

**Live Application is Ready! 🎉**
