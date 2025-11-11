# 🚀 Guía de Despliegue - FUNDECO Chatbot

## Despliegue Local

### Desarrollo
```bash
# 1. Configurar entorno de desarrollo
cp .env.development .env

# 2. Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar en modo desarrollo
python src/api/app.py
```

### Producción Local
```bash
# 1. Configurar variables de producción
cp .env.example .env
# Editar .env con valores reales

# 2. Ejecutar con Gunicorn
gunicorn --bind 0.0.0.0:8000 --chdir src/api app:app
```

## Despliegue en la Nube

### Heroku

1. **Preparar proyecto**
```bash
# Crear Procfile
echo "web: gunicorn --bind 0.0.0.0:$PORT --chdir src/api app:app" > Procfile

# Crear runtime.txt (opcional)
echo "python-3.11.0" > runtime.txt
```

2. **Configurar Heroku**
```bash
# Instalar Heroku CLI y login
heroku login

# Crear aplicación
heroku create fundeco-chatbot

# Configurar variables de entorno
heroku config:set OPENAI_API_KEY=tu_api_key
heroku config:set FLASK_ENV=production

# Desplegar
git push heroku main
```

### Railway

1. **Preparar configuración**
```json
// railway.json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn --bind 0.0.0.0:$PORT --chdir src/api app:app",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100
  }
}
```

2. **Desplegar**
- Conectar repositorio en railway.app
- Configurar variables de entorno
- Desplegar automáticamente

### Render

1. **Configurar build**
```bash
# Build Command
pip install -r requirements.txt

# Start Command
gunicorn --bind 0.0.0.0:$PORT --chdir src/api app:app
```

2. **Variables de entorno**
- `OPENAI_API_KEY`: API key de OpenAI
- `FLASK_ENV`: production

### DigitalOcean App Platform

1. **Configurar app.yaml**
```yaml
name: fundeco-chatbot
services:
- name: web
  source_dir: /
  github:
    repo: tu-usuario/fundeco-chatbot
    branch: main
  run_command: gunicorn --bind 0.0.0.0:$PORT --chdir src/api app:app
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs  envs:
  - key: OPENAI_API_KEY
    value: tu_api_key
    type: SECRET
  - key: FLASK_ENV
    value: production
```

## Docker

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . .

# Crear usuario no-root
RUN useradd -m -u 1000 fundeco && chown -R fundeco:fundeco /app
USER fundeco

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "src/api", "app:app"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  fundeco-chatbot:
    build: .
    ports:
      - "8000:8000"    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - FLASK_ENV=production
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - fundeco-chatbot
    restart: unless-stopped
```

### Comandos Docker
```bash
# Construir imagen
docker build -t fundeco-chatbot .

# Ejecutar contenedor
docker run -p 8000:8000 --env-file .env fundeco-chatbot

# Con docker-compose
docker-compose up -d
```

## Configuración de Nginx

```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    
    # Redirigir a HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name tu-dominio.com;
    
    # Certificados SSL
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    
    # Configuración SSL
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    
    # Configuración del proxy
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Archivos estáticos
    location /static/ {
        alias /app/src/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # Configuración de compresión
    gzip on;
    gzip_vary on;
    gzip_types text/css application/javascript application/json;
}
```

## Variables de Entorno de Producción

### Requeridas
- `FLASK_ENV`: Establecer a `production`
- `FLASK_DEBUG`: Establecer a `False`

### Opcionales
- `OPENAI_API_KEY`: Para habilitar respuestas inteligentes
- `PORT`: Puerto de la aplicación (por defecto 5000)
- `APP_NAME`: Nombre de la aplicación
- `APP_VERSION`: Versión de la aplicación

## Monitoreo y Logs

### Configurar logs
```python
# En producción, configurar logging adecuado
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/fundeco.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
```

### Health Check
La aplicación incluye endpoints para monitoreo:
- `GET /` - Página principal (health check básico)
- `POST /api/chat` - API del chatbot

## Consideraciones de Seguridad

1. **HTTPS**: Siempre usar HTTPS en producción
2. **Variables de entorno**: Nunca commitear claves en el código
3. **CORS**: Configurar CORS apropiadamente
4. **Rate limiting**: Implementar para prevenir abuso
5. **Logs**: No loggear información sensible
6. **Headers de seguridad**: Agregar headers como CSP, HSTS

## Backup y Recuperación

Si se implementa persistencia de datos:
```bash
# Backup automático
0 2 * * * pg_dump fundeco_db > /backups/fundeco_$(date +\%Y\%m\%d).sql

# Restauración
psql fundeco_db < backup.sql
```

## Solución de Problemas

### Problemas Comunes

1. **Error 500**: Verificar logs y variables de entorno
2. **OpenAI timeout**: Verificar conectividad y API key
3. **Archivos estáticos no cargan**: Verificar configuración de Nginx/servidor web
4. **CORS errors**: Configurar flask-cors apropiadamente

### Comandos de diagnóstico
```bash
# Verificar estado de la aplicación
curl -I http://localhost:8000/

# Verificar logs
tail -f logs/fundeco.log

# Verificar variables de entorno
printenv | grep FLASK
```
