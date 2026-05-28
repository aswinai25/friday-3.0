# ✅ Railway Deployment Checklist for "rosey"

## 📋 Before You Start
- [ ] Code is committed to GitHub
- [ ] Have LiveKit credentials ready (URL, API Key, Secret)
- [ ] Have a Railway account (https://railway.app)
- [ ] Have a Vercel account (optional, if deploying frontend there)

---

## 🚀 Deployment Steps

### Step 1: Prepare Your Repository
- [ ] All changes committed and pushed to GitHub
- [ ] `.env` file created with LiveKit credentials (DO NOT commit this file)
- [ ] `.env.example` has been updated with variable names

```bash
# Create .env file locally (DO NOT commit)
LIVEKIT_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your_key
LIVEKIT_API_SECRET=your_secret
```

---

### Step 2: Deploy Backend to Railway

**Manual Steps:**

1. ✅ Go to https://railway.app
2. ✅ Sign in with GitHub
3. ✅ Click **"New Project"** → **"Deploy from GitHub Repo"**
4. ✅ Select your `friday-3.0` repository
5. ✅ Railway auto-detects Python project
6. ✅ Wait for build to complete (~2-3 minutes)

**After Deployment:**
- [ ] Get your backend URL: `https://rosey-backend.up.railway.app` (example)
- [ ] Note this URL for step 3

---

### Step 3: Configure Backend Environment Variables (Railway)

1. ✅ In Railway dashboard, go to your backend service
2. ✅ Click **Settings** → **Variables**
3. ✅ Add these three variables:

```
LIVEKIT_URL = wss://your-livekit-server.com
LIVEKIT_API_KEY = your_api_key
LIVEKIT_API_SECRET = your_api_secret
```

4. ✅ Click **Deploy** to apply changes

---

### Step 4: Deploy Frontend

**Option A: Vercel (Recommended)**

1. ✅ Go to https://vercel.com
2. ✅ Click **"Add New"** → **"Project"**
3. ✅ Select your `friday-3.0` repository
4. ✅ Framework: **Webpack**
5. ✅ Add Environment Variable:
   ```
   REACT_APP_API_URL=https://rosey-backend.up.railway.app
   ```
6. ✅ Click **Deploy**
7. ✅ Get your frontend URL: `https://rosey.vercel.app` (example)

**Option B: Railway**

1. ✅ In your Railway project, click **"New Service"**
2. ✅ Select **"GitHub Repo"** (same repo)
3. ✅ Build Command: `npm run build`
4. ✅ Start Command: `npx serve -s dist -l 3000`
5. ✅ Environment Variable:
   ```
   REACT_APP_API_URL=https://rosey-backend.up.railway.app
   ```
6. ✅ Click **Deploy**

---

### Step 5: Test Your Deployment

1. ✅ Visit your frontend URL
2. ✅ Click **"Start Listening"** button
3. ✅ Check if you see: ✅ Connected to Friday!
4. ✅ Open browser console (F12) → Console tab
5. ✅ Should see: `"Backend config: {...}"`

---

## 📊 Final Deployment Status

After completing all steps, you should have:

| Component | Status | URL |
|-----------|--------|-----|
| Backend | ✅ Running | https://rosey-backend.up.railway.app |
| Frontend | ✅ Running | https://rosey.vercel.app |
| LiveKit | ✅ Connected | wss://your-livekit-server.com |

---

## 🔗 URLs to Save

- **Frontend URL**: https://rosey.vercel.app
- **Backend URL**: https://rosey-backend.up.railway.app
- **Railway Dashboard**: https://railway.app
- **Vercel Dashboard**: https://vercel.com/dashboard

---

## 🐛 Troubleshooting

### Frontend shows "Connection failed"
- Check `REACT_APP_API_URL` in Vercel/Railway settings
- Make sure backend URL is correct
- Check browser console for exact error

### Backend returns 500 error
- Go to Railway backend logs
- Check if LiveKit credentials are correct
- Verify all environment variables are set

### CORS errors
- Already configured in `app.py`
- Make sure frontend URL is pointing to correct backend

### Still having issues?
```bash
# Check local build
npm run build
npm run dev

# Check backend locally
python app.py
```

---

## 📝 Production Notes

- ✅ Both frontend and backend are now live
- ✅ Use production URLs for sharing with users
- ✅ LiveKit handles all video/audio streaming
- ✅ Backend API is protected by CORS
- ✅ Monitor both Railway and Vercel dashboards for logs

**Congratulations! Your "rosey" AI Assistant is deployed! 🎉**
