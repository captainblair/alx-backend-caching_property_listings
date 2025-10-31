# ALX Backend Caching Property Listings

Django project with PostgreSQL and Redis caching setup.

## Setup Instructions

1. **Install Docker** (if not already installed)
   - Download and install Docker Desktop from https://www.docker.com/products/docker-desktop

2. **Start Database and Cache Services**
   ```bash
   docker compose up -d
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py migrate
   python manage.py migrate properties
   ```

5. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Django Development Server**
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `properties/models.py` - Property model with required fields
- `alx-backend-caching_property_listings/settings.py` - Django settings with PostgreSQL and Redis configuration
- `docker-compose.yml` - Docker services for PostgreSQL and Redis
- `requirements.txt` - Python dependencies

## Services

- **PostgreSQL**: localhost:5432 (Database: property_listings, User: postgres, Password: postgres)
- **Redis**: localhost:6379 (Cache backend)
- **Django**: localhost:8000 (Development server)