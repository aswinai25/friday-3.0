# Production Deployment Checklist

## Pre-Deployment

- [ ] All tests passing locally
- [ ] No hardcoded secrets or credentials
- [ ] Environment variables configured
- [ ] Database migrations run
- [ ] Logging configured
- [ ] Error handling implemented
- [ ] Performance optimized
- [ ] Code reviewed
- [ ] Dependencies audited for vulnerabilities

## Frontend Checklist

- [ ] React build succeeds: `npm run build`
- [ ] Production environment variables set
- [ ] API URL points to production backend
- [ ] Error boundaries implemented
- [ ] 404 page exists
- [ ] Favicon configured
- [ ] Meta tags set (title, description, og:image)
- [ ] Analytics tracking configured
- [ ] Console warnings/errors resolved
- [ ] Performance metrics checked (Lighthouse score > 80)

## Backend Checklist

- [ ] All FastAPI routes tested
- [ ] Error handling on all endpoints
- [ ] CORS configured correctly
- [ ] Rate limiting enabled
- [ ] Input validation on all endpoints
- [ ] Logging configured
- [ ] Health check endpoint working
- [ ] Database connection pooling configured
- [ ] Timeout values set appropriately
- [ ] Security headers configured

## LiveKit Configuration

- [ ] LIVEKIT_URL set to production server
- [ ] API keys rotated
- [ ] API secrets stored securely
- [ ] Access control policies configured
- [ ] Recording/transcription settings configured

## Infrastructure

- [ ] SSL/HTTPS certificate installed
- [ ] HTTPS redirects configured
- [ ] Firewall rules configured
- [ ] Backup strategy implemented
- [ ] Monitoring alerts set up
- [ ] Log aggregation configured
- [ ] CDN configured (if needed)

## Security

- [ ] No secrets in version control
- [ ] Environment variables encrypted
- [ ] Database passwords rotated
- [ ] API keys rotated
- [ ] HTTPS enforced
- [ ] CORS properly restricted
- [ ] SQL injection prevention verified
- [ ] XSS prevention verified
- [ ] CSRF tokens implemented
- [ ] Rate limiting enabled

## Monitoring & Logging

- [ ] Error tracking (Sentry/Rollbar)
- [ ] Performance monitoring
- [ ] Uptime monitoring
- [ ] Application metrics
- [ ] User analytics
- [ ] API call logging
- [ ] Error notifications setup
- [ ] Performance alerts setup

## Deployment Steps

### Using Docker Compose (Recommended)

```bash
# 1. Build images
docker-compose build

# 2. Start services
docker-compose up -d

# 3. Check logs
docker-compose logs -f

# 4. Scale if needed
docker-compose up -d --scale backend=3

# 5. Update (with zero downtime)
docker-compose pull
docker-compose up -d
```

### Using Railway.app (Easiest)

```bash
# 1. Push to GitHub
git push origin main

# 2. Railway auto-deploys
# 3. Check deployment status in dashboard
# 4. Get public URLs
```

### Using Vercel (Frontend) + Railway (Backend)

```bash
# Frontend
1. Push to GitHub
2. Vercel auto-deploys
3. Add environment variables in Vercel dashboard

# Backend
1. Create new service on Railway.app
2. Connect GitHub repo
3. Configure environment variables
4. Deploy
```

## Post-Deployment Testing

- [ ] Frontend loads without errors
- [ ] All pages accessible
- [ ] API endpoints respond correctly
- [ ] WebSocket connection works
- [ ] Error pages display correctly
- [ ] Redirects work properly
- [ ] Performance acceptable (< 2s load time)
- [ ] Mobile responsive
- [ ] Form submissions work
- [ ] File uploads work
- [ ] Cookies/sessions work
- [ ] Authentication flows work

## Performance Optimization

- [ ] Minify JavaScript/CSS
- [ ] Compress images
- [ ] Enable gzip compression
- [ ] Implement caching strategy
- [ ] Use CDN for static assets
- [ ] Database query optimization
- [ ] Connection pooling
- [ ] Load balancing configured

## Backup & Disaster Recovery

- [ ] Daily backups configured
- [ ] Backup verification tested
- [ ] Restoration procedure documented
- [ ] Disaster recovery plan written
- [ ] Team trained on recovery process

## Maintenance Windows

- [ ] Scheduled maintenance time defined
- [ ] Users notified of maintenance
- [ ] Rollback procedure documented
- [ ] Team on-call for issues

## Documentation

- [ ] Deployment guide written
- [ ] API documentation updated
- [ ] Runbook for common issues
- [ ] Architecture documentation
- [ ] Environment setup guide

## Sign-Off

- [ ] QA approval
- [ ] Stakeholder approval
- [ ] Deployment lead approval
- [ ] Post-deployment support plan confirmed

---

## Monitoring Commands

```bash
# Docker
docker-compose ps          # Check service status
docker-compose logs -f     # View logs
docker stats              # Check resource usage
docker-compose exec backend curl http://localhost:8000/health

# Railway
railway logs              # View logs
railway status            # Check deployment status

# Performance
curl -I https://yourdomain.com  # Check response headers
ab -n 1000 -c 10 https://yourdomain.com  # Load test
```

---

## Incident Response

1. **Monitor alerts** - Set up notifications
2. **Check logs** - Identify the issue
3. **Scale horizontally** - If traffic spike
4. **Rollback** - If recent deployment caused issue
5. **Communicate** - Notify users if extended downtime
6. **Root cause analysis** - After resolution
7. **Document** - Update runbooks

---

**Ready for production? Use this checklist before every deployment!** ✅
