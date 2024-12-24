# Start all services
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down 

# Rebuild images
build:
	docker-compose build

# View logs
logs:
	docker-compose logs -f

# Restart environment
Restart: down up
