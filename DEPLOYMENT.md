# Friday AI Assistant - Deployment Guide

## Deployment Options

### Quick Options (Recommended for Beginners)

#### Option 1: Vercel (Frontend) + Railway (Backend)
**Cost**: Free tier available
**Ease**: Easiest

#### Option 2: Netlify (Frontend) + Heroku (Backend)
**Cost**: Free tier available
**Ease**: Very Easy

#### Option 3: Docker Compose (Full Stack - Local/Server)
**Cost**: Depends on server
**Ease**: Moderate

#### Option 4: AWS/Google Cloud (Production)
**Cost**: Pay-as-you-go
**Ease**: Advanced

---

## Option 1: Vercel + Railway (RECOMMENDED - Easiest)

### Step 1: Deploy Frontend to Vercel

1. **Create Vercel Account**
   - Go to https://vercel.com
   - Sign up with GitHub

2. **Prepare Frontend**
   ```bash
   # Add vercel.json to project root
   ```

3. **Deploy**
   - Push code to GitHub
   - Connect GitHub repo to Vercel
   - Vercel auto-deploys on push

4. **Set Environment Variables**
   - Go to Settings → Environment Variables
   - Add: `REACT_APP_API_URL=https://your-backend-url.com`

### Step 2: Deploy Backend to Railway

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Create new project → GitHub repo
   - Select `friday 3.0` folder
   - Set root directory to project folder

3. **Configure Environment Variables**
   ```
   LIVEKIT_URL=wss://your-livekit-server.com
   LIVEKIT_API_KEY=your_key
   LIVEKIT_API_SECRET=your_secret
   ```

4. **Get Backend URL**
   - Railway provides: `https://xxx.railway.app`
   - Use this in Vercel `REACT_APP_API_URL`

---

## Option 2: Netlify + Heroku

### Frontend (Netlify)

1. **Create Netlify Account**
   - https://netlify.com
   - Sign up with GitHub

2. **Connect Repository**
   - New site from Git → Select repo
   - Build command: `npm run build`
   - Publish directory: `dist`

3. **Environment Variables**
   - Site settings → Build & deploy → Environment
   - Add: `REACT_APP_API_URL`

### Backend (Heroku)

1. **Create Heroku Account**
   - https://heroku.com

2. **Deploy from CLI**
   ```bash
   # Install Heroku CLI
   npm install -g heroku
   
   # Login
   heroku login
   
   # Create app
   heroku create your-app-name
   
   # Deploy
   git push heroku main
   ```

3. **Add Configuration Variables**
   ```bash
   heroku config:set LIVEKIT_URL="your_livekit_url"
   heroku config:set LIVEKIT_API_KEY="your_key"
   heroku config:set LIVEKIT_API_SECRET="your_secret"
   ```

---

## Option 3: Docker Compose (Full Stack)

### Create Docker Files

**Dockerfile (Backend)**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Dockerfile (Frontend)**
```dockerfile
FROM node:18 as builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**docker-compose.yml**
```yaml
version: '3.8'

services:
  backend:
    build: ./
    ports:
      - "8000:8000"
    environment:
      LIVEKIT_URL: ${LIVEKIT_URL}
      LIVEKIT_API_KEY: ${LIVEKIT_API_KEY}
      LIVEKIT_API_SECRET: ${LIVEKIT_API_SECRET}
    networks:
      - friday-network

  frontend:
    build:
      context: ./
      dockerfile: Dockerfile.frontend
    ports:
      - "3000:80"
    environment:
      REACT_APP_API_URL: http://backend:8000
    depends_on:
      - backend
    networks:
      - friday-network

networks:
  friday-network:
    driver: bridge
```

### Deploy with Docker Compose
```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## Option 4: Production Setup (Recommended)

### 1. Use Render or Railway for Full Stack
- Render.com supports Docker
- Railway supports both Node and Python

### 2. Add a Reverse Proxy (Nginx)
```nginx
upstream backend {
    server backend:8000;
}

upstream frontend {
    server frontend:3000;
}

server {
    listen 80;
    server_name yourdomain.com;

    location /api {
        proxy_pass http://backend;
    }

    location / {
        proxy_pass http://frontend;
    }
}
```

### 3. Enable SSL/HTTPS
- Use Let's Encrypt (free)
- Certbot for auto-renewal

---

## Environment Configuration

### Create `.env` Files

**Backend (.env)**
```
LIVEKIT_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
```

**Frontend (.env.production)**
```
REACT_APP_API_URL=https://api.yourdomain.com
```

---

## Step-by-Step: Vercel + Railway (Quick Start)

### Frontend (5 minutes)
1. Push to GitHub
2. Go to Vercel.com
3. Import project
4. Add env variable: `REACT_APP_API_URL`
5. Deploy (automatic on push)

### Backend (5 minutes)
1. Go to Railway.app
2. Create new project
3. Connect GitHub
4. Set environment variables
5. Deploy

### Connect Them
1. Get Railway URL (looks like: `xxx.railway.app`)
2. Add to Vercel env: `REACT_APP_API_URL=https://xxx.railway.app`
3. Done! They communicate

---

## Production Checklist

- [ ] Remove hardcoded LiveKit credentials
- [ ] Use environment variables
- [ ] Enable CORS properly
- [ ] Add error logging (Sentry)
- [ ] Set up monitoring (Uptime monitoring)
- [ ] Configure backups
- [ ] Use production databases
- [ ] Enable HTTPS
- [ ] Add rate limiting
- [ ] Set up CI/CD pipeline
- [ ] Add authentication
- [ ] Monitor performance

---

## Cost Estimates (Monthly)

| Option | Frontend | Backend | Total |
|--------|----------|---------|-------|
| Vercel + Railway | $0-20 | $5-50 | $5-70 |
| Netlify + Heroku | $0-19 | $0-50 | $0-69 |
| DigitalOcean Droplet | Included | Included | $4-12 |
| AWS/Google Cloud | Pay per use | Pay per use | $10-100+ |

---

## Troubleshooting

### CORS Errors
- Ensure backend has CORS enabled
- Check `REACT_APP_API_URL` is correct
- Verify frontend can reach backend URL

### Deploy Fails
- Check logs: `railway logs` or `heroku logs`
- Verify environment variables are set
- Check Python/Node versions match

### Connection Timeout
- Ensure backend is running
- Check firewall rules
- Verify port 8000 is exposed

---

## Next Steps

1. Choose deployment option
2. Follow step-by-step guide below
3. Test in production
4. Set up monitoring
5. Configure auto-backups
