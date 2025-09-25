# BDIAE Production Deployment Guide

This guide covers deploying the BDIAE (Blockchain-based Tender & Auction System) to production.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Nginx         │    │   Backend API   │
│   (Next.js)     │◄───┤   (Reverse      │◄───┤   (FastAPI)     │
│                 │    │    Proxy)       │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                       │
                                │                       │
                       ┌─────────────────┐    ┌─────────────────┐
                       │   PostgreSQL    │    │   Redis         │
                       │   (Database)    │    │   (Cache)       │
                       └─────────────────┘    └─────────────────┘
                                │
                       ┌─────────────────┐
                       │   Monitoring    │
                       │   (Prometheus   │
                       │   + Grafana)    │
                       └─────────────────┘
```

## 📋 Prerequisites

- Docker and Docker Compose
- Domain name (for production)
- SSL certificates (for HTTPS)
- Polygon mainnet RPC URL
- Deployed smart contracts

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone <repository-url>
cd bdiae-hack
```

### 2. Configure Environment

```bash
# Copy production environment template
cp backend/env.production .env.production

# Edit with your production values
nano .env.production
```

### 3. Deploy with Docker Compose

```bash
# Make deployment script executable
chmod +x deploy.sh

# Deploy to production
./deploy.sh production
```

## ⚙️ Configuration

### Environment Variables

Create `.env.production` with the following:

```env
# Environment
ENVIRONMENT=production
DEBUG=false

# Blockchain (Polygon Mainnet)
RPC_URL=https://polygon-rpc.com
CHAIN_ID=137
PRIVATE_KEY=your_private_key
PUBLIC_ADDRESS=your_wallet_address

# Contract Addresses
INR_TOKEN_ADDRESS=0x...
AUCTION_ESCROW_ADDRESS=0x...

# Security
JWT_SECRET=your_very_strong_jwt_secret_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Database
DATABASE_URL=postgresql://bdiae_user:password@db:5432/bdiae_production

# CORS
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Rate Limiting
RATE_LIMIT_PER_MINUTE=100

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# Monitoring
ENABLE_METRICS=true
METRICS_PORT=9090

# Email (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

### Smart Contract Deployment

1. **Deploy INRToken.sol** on Polygon mainnet
2. **Deploy AuctionEscrow.sol** with INRToken address
3. **Update contract addresses** in `.env.production`

## 🐳 Docker Services

### Core Services

- **backend**: FastAPI application
- **db**: PostgreSQL database
- **redis**: Redis cache
- **nginx**: Reverse proxy

### Monitoring Services

- **prometheus**: Metrics collection
- **grafana**: Metrics visualization

## 📊 Monitoring

### Access Points

- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)

### Key Metrics

- HTTP request rate and duration
- Database connection pool
- Redis cache hit rate
- Blockchain transaction success rate

## 🔒 Security

### Implemented Security Features

- JWT-based authentication
- Rate limiting
- CORS protection
- Security headers
- Input validation
- SQL injection prevention
- XSS protection

### Security Checklist

- [ ] Change default JWT secret
- [ ] Use strong database passwords
- [ ] Enable HTTPS with valid certificates
- [ ] Configure firewall rules
- [ ] Regular security updates
- [ ] Monitor logs for suspicious activity

## 📈 Scaling

### Horizontal Scaling

```yaml
# docker-compose.override.yml
services:
  backend:
    deploy:
      replicas: 3
  nginx:
    depends_on:
      - backend
```

### Database Scaling

- Use read replicas for read-heavy workloads
- Implement connection pooling
- Consider database sharding for large datasets

## 🔧 Maintenance

### Backup

```bash
# Database backup
docker-compose exec db pg_dump -U bdiae_user bdiae_production > backup.sql

# Restore
docker-compose exec -T db psql -U bdiae_user bdiae_production < backup.sql
```

### Updates

```bash
# Pull latest changes
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Logs

```bash
# View logs
docker-compose logs -f backend

# View specific service logs
docker-compose logs -f db
```

## 🚨 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check database credentials
   - Verify database is running
   - Check network connectivity

2. **JWT Token Invalid**
   - Verify JWT_SECRET is set
   - Check token expiration
   - Ensure consistent secret across instances

3. **Blockchain Connection Failed**
   - Verify RPC_URL is correct
   - Check network connectivity
   - Verify contract addresses

### Health Checks

```bash
# Check service health
curl http://localhost:8000/health

# Check metrics
curl http://localhost:8000/metrics

# Check database
docker-compose exec db pg_isready -U bdiae_user
```

## 📞 Support

For production support:

1. Check logs: `docker-compose logs -f`
2. Monitor metrics: http://localhost:9090
3. Review documentation: `/docs` endpoint
4. Contact development team

## 🔄 CI/CD

### GitHub Actions Example

```yaml
name: Deploy to Production
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy
        run: |
          ./deploy.sh production
```

## 📝 License

This project is licensed under the MIT License.
