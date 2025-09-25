#!/bin/bash

# BDIAE Production Deployment Script
# This script deploys the BDIAE application to production

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
ENVIRONMENT=${1:-production}
DOCKER_COMPOSE_FILE="docker-compose.yml"
ENV_FILE=".env.production"

echo -e "${GREEN}🚀 Starting BDIAE Production Deployment${NC}"
echo -e "${YELLOW}Environment: ${ENVIRONMENT}${NC}"

# Check if required files exist
if [ ! -f "$DOCKER_COMPOSE_FILE" ]; then
    echo -e "${RED}❌ docker-compose.yml not found!${NC}"
    exit 1
fi

if [ ! -f "$ENV_FILE" ]; then
    echo -e "${RED}❌ .env.production not found!${NC}"
    echo -e "${YELLOW}Please create .env.production file with your configuration${NC}"
    exit 1
fi

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}❌ Docker is not running!${NC}"
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose is not installed!${NC}"
    exit 1
fi

# Create necessary directories
echo -e "${YELLOW}📁 Creating necessary directories...${NC}"
mkdir -p logs uploads ssl prometheus_data grafana_data

# Set proper permissions
echo -e "${YELLOW}🔐 Setting permissions...${NC}"
chmod 755 logs uploads
chmod 600 ssl/* 2>/dev/null || true

# Pull latest images
echo -e "${YELLOW}📥 Pulling latest Docker images...${NC}"
docker-compose -f $DOCKER_COMPOSE_FILE pull

# Build application image
echo -e "${YELLOW}🔨 Building application image...${NC}"
docker-compose -f $DOCKER_COMPOSE_FILE build --no-cache

# Stop existing containers
echo -e "${YELLOW}🛑 Stopping existing containers...${NC}"
docker-compose -f $DOCKER_COMPOSE_FILE down

# Start services
echo -e "${YELLOW}🚀 Starting services...${NC}"
docker-compose -f $DOCKER_COMPOSE_FILE up -d

# Wait for services to be healthy
echo -e "${YELLOW}⏳ Waiting for services to be healthy...${NC}"
sleep 30

# Check service health
echo -e "${YELLOW}🏥 Checking service health...${NC}"

# Check database
if docker-compose -f $DOCKER_COMPOSE_FILE exec -T db pg_isready -U bdiae_user -d bdiae_production > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Database is healthy${NC}"
else
    echo -e "${RED}❌ Database is not healthy${NC}"
    exit 1
fi

# Check Redis
if docker-compose -f $DOCKER_COMPOSE_FILE exec -T redis redis-cli ping > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Redis is healthy${NC}"
else
    echo -e "${RED}❌ Redis is not healthy${NC}"
    exit 1
fi

# Check backend API
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Backend API is healthy${NC}"
else
    echo -e "${RED}❌ Backend API is not healthy${NC}"
    exit 1
fi

# Run database migrations
echo -e "${YELLOW}🗄️ Running database migrations...${NC}"
docker-compose -f $DOCKER_COMPOSE_FILE exec backend alembic upgrade head

# Show running containers
echo -e "${YELLOW}📋 Running containers:${NC}"
docker-compose -f $DOCKER_COMPOSE_FILE ps

# Show service URLs
echo -e "${GREEN}🎉 Deployment completed successfully!${NC}"
echo -e "${YELLOW}Service URLs:${NC}"
echo -e "  Backend API: http://localhost:8000"
echo -e "  API Docs: http://localhost:8000/docs"
echo -e "  Prometheus: http://localhost:9090"
echo -e "  Grafana: http://localhost:3000"
echo -e "  Database: localhost:5432"

# Show logs
echo -e "${YELLOW}📝 Recent logs:${NC}"
docker-compose -f $DOCKER_COMPOSE_FILE logs --tail=20 backend
