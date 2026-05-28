# Friday AI Assistant - Quick Deployment Guide

## 🚀 Fastest Deployment Option (5-10 Minutes)

### Option A: Railway (Easiest - Free Tier Available)

**Deploy Both Frontend & Backend in One Platform:**

1. **Go to Railway.app**
   - Sign up with GitHub account

2. **New Project → GitHub Repo**
   - Select your `friday 3.0` repository

3. **Configure Environment Variables**
   ```
   LIVEKIT_URL=wss://your-livekit.com
   LIVEKIT_API_KEY=your_key
   LIVEKIT_API_SECRET=your_secret
   ```

4. **Set Build Command**
   - Node service: `npm run build`
   - Python service: Auto-detected from Procfile

5. **Get Your URLs**
   - Backend: `https://xxx.railway.app`
   - Frontend: `https://yyy.railway.app`

---

### Option B: Docker Compose (Local Server / VPS)

**Deploy Everything on Your Own Server:**

1. **Install Docker & Docker Compose**
   ```bash
   # On Ubuntu/Linux
   curl -fsSL https://get.docker.com -o get-docker.sh
   sh get-docker.sh
   ```

2. **Create `.env` File**
   ```bash
   LIVEKIT_URL=wss://your-livekit.com
   LIVEKIT_API_KEY=your_key
   LIVEKIT_API_SECRET=your_secret
   ```

3. **Deploy**
   ```bash
   docker-compose up -d
   ```

4. **Access**
   - Frontend: http://your-server-ip
   - Backend: http://your-server-ip:8000

---

### Option C: Vercel (Frontend) + Railway/Render (Backend)

**Best for Production:**

1. **Deploy Frontend to Vercel**
   - Go to vercel.com
   - Import your GitHub repo
   - Set `REACT_APP_API_URL` environment variable
   - Deploy (automatic on git push)

2. **Deploy Backend to Railway**
   - Create Python service on railway.app
   - Set environment variables
   - Deploy

3. **Connect Them**
   - Get Railway backend URL
   - Add to Vercel env: `REACT_APP_API_URL=https://backend-url.railway.app`

---

## 📋 Pre-Deployment Checklist

- [ ] Update LiveKit credentials in `.env`
- [ ] Update API URLs for production
- [ ] Test locally with `npm start` + `python app.py`
- [ ] Push all code to GitHub
- [ ] Create `.env` file with production secrets
- [ ] Run `npm run build` to test build process

---

## 🔧 Building for Production

```bash
# Build React frontend
npm run build

# Output: dist/ folder with optimized bundle

# Backend: Already production-ready (app.py)
```

---

## 💾 Storage & Database

For future enhancements:
- **Messages**: Store in MongoDB or PostgreSQL
- **User Data**: Encrypt and store securely
- **Logs**: Use centralized logging (ELK, Sentry)

---

## 🔒 Security Tips

1. **Never commit secrets** - Use environment variables
2. **Enable HTTPS** - Use Let's Encrypt (free)
3. **Add Rate Limiting** - Prevent API abuse
4. **Validate Inputs** - Server-side validation
5. **Use CORS Properly** - Only allow trusted origins
6. **Keep Dependencies Updated** - Regular `npm update` and `pip install -U`

---

## 🆘 Troubleshooting Deployments

### Frontend won't load
- Check `REACT_APP_API_URL` is correct
- Verify build command: `npm run build`
- Check build output in `dist/` folder

### Backend connection fails
- Ensure backend port 8000 is exposed
- Check environment variables are set
- Verify LIVEKIT credentials are correct
- Check CORS is enabled

### Docker build fails
- Ensure `requirements.txt` exists
- Check `package.json` in root
- Verify Python/Node versions

---

## 📞 Support Platforms

- **Railway**: https://railway.app (Recommended)
- **Render**: https://render.com
- **Heroku**: https://heroku.com (Limited free tier)
- **Vercel**: https://vercel.com (Frontend only)
- **AWS**: https://aws.amazon.com (Advanced)

---

**Your app is ready to deploy! Choose any option above and you'll be live in minutes.** 🎉
