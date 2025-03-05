🏡 API de Proyectos Inmobiliarios

Un cliente desea desarrollar un sistema de visualización de proyectos inmobiliarios en un mapa interactivo. El objetivo del sistema es permitir a los usuarios explorar proyectos inmobiliarios en diferentes ubicaciones y obtener información detallada sobre ellos.

Esta API, desarrollada con FastAPI, SQLAlchemy y Docker, permite la gestión de proyectos inmobiliarios, incluyendo la creación, actualización, eliminación y búsqueda de propiedades con filtros avanzados y visualización en mapas.

📌 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

Docker y Docker Compose

Python 3.12+ (si deseas ejecutar sin Docker)

Poetry o pip para manejar dependencias (opcional)

🚀 Instalación y Configuración con Docker

1️⃣ Clonar el Repositorio

git clone https://github.com/tu_usuario/proyecto-inmobiliario.git
cd proyecto-inmobiliario

2️⃣ Configurar Variables de Entorno

Renombra el archivo .env.example a .env y edita los valores:

DATABASE_URL=postgresql://postgres:password@db:5432/proyectosdb
SECRET_KEY=clave_super_secreta

3️⃣ Levantar los Contenedores con Docker

docker-compose up --build

📌 Esto iniciará los servicios:

✅ FastAPI en http://127.0.0.1:8000

✅ PostgreSQL con persistencia de datos

Si deseas correr en segundo plano:

docker-compose up -d

📡 Acceder a la API

API disponible en: http://127.0.0.1:8000

Documentación interactiva en Swagger UI: http://127.0.0.1:8000/docs

🛠 Estructura del Proyecto

📂 proyecto-inmobiliario/
├── 📂 app/
│   ├── 📂 models/         # Modelos de la base de datos (SQLAlchemy)
│   ├── 📂 routes/         # Endpoints de la API
│   ├── 📂 schemas/        # Esquemas de validación con Pydantic
│   ├── 📂 services/       # Lógica de negocio
│   ├── 📂 tests/          # Pruebas unitarias
│   ├── main.py           # Punto de entrada de la aplicación
│   ├── database.py       # Configuración de la base de datos
│   └── config.py         # Variables de configuración
├── .env                  # Variables de entorno
├── docker-compose.yml    # Configuración de Docker
├── Dockerfile            # Imagen de Docker para FastAPI
├── alembic/              # Migraciones de base de datos
├── requirements.txt      # Dependencias del proyecto
└── pytest.ini            # Configuración de pruebas

🔥 Endpoints de la API

Método

Endpoint

Descripción

GET

/proyectos

Listar todos los proyectos

POST

/proyectos

Crear un nuevo proyecto

GET

/proyectos/{id}

Obtener detalles de un proyecto

PUT

/proyectos/{id}

Actualizar un proyecto

DELETE

/proyectos/{id}

Eliminar un proyecto

GET

/buscar?tipo=&precio_max=

Filtrar proyectos

🗺 Visualización en Mapas

📌 Opciones disponibles:

Backend: Generación de mapas con Folium

Frontend: Integración con Leaflet.js

Interactividad: Marcadores con pop-ups mostrando detalles de los proyectos

✅ Pruebas Automatizadas

Ejecuta las pruebas con pytest dentro del contenedor:

pytest -v

📌 Incluye pruebas para: ✔ Validación de datos✔ Endpoints REST✔ Manejo de base de datos

📦 Administración de Base de Datos

Ejecutar migraciones dentro del contenedor:

docker exec -it api alembic upgrade head

Acceder a la base de datos PostgreSQL:

docker exec -it db psql -U postgres -d proyectosdb


