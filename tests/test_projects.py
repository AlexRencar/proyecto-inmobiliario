import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al Sistema de Proyectos Inmobiliarios"}

def test_create_project():
    project_data = {
        "name": "Casa Moderna",
        "location": "Calle Falsa 123",
        "lat": 40.7128,
        "lng": -74.0060,
        "price": 250000.0,
        "description": "Una casa moderna con todas las comodidades",
        "category": "Residencial",
        "image_url": "http://example.com/imagen.jpg"
    }
    response = client.post("/projects/", json=project_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Casa Moderna"
    assert "id" in data
    # Devuelve el id para reutilizarlo en otros tests si fuera necesario
    return data["id"]

def test_search_projects():
    # Primero, crea un proyecto para que haya datos que buscar
    project_data = {
        "name": "Apartamento Central",
        "location": "Avenida Central 456",
        "lat": 40.7130,
        "lng": -74.0070,
        "price": 300000.0,
        "description": "Apartamento en el centro",
        "category": "Residencial",
        "image_url": "http://example.com/apto.jpg"
    }
    client.post("/projects/", json=project_data)
    
    response = client.get("/projects/search", params={"category": "Residencial", "min_price": 200000, "max_price": 350000})
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_update_project():
    # Primero, crea un proyecto para actualizar
    project_data = {
        "name": "Apartamento Original",
        "location": "Avenida Central 456",
        "lat": 40.7130,
        "lng": -74.0070,
        "price": 300000.0,
        "description": "Apartamento en el centro",
        "category": "Residencial",
        "image_url": "http://example.com/apto.jpg"
    }
    create_response = client.post("/projects/", json=project_data)
    assert create_response.status_code == 200
    project_id = create_response.json()["id"]

    # Datos para actualizar el proyecto
    update_data = {
        "name": "Apartamento Actualizado",
        "location": "Avenida Central 456",
        "lat": 40.7130,
        "lng": -74.0070,
        "price": 320000.0,
        "description": "Apartamento actualizado con mejoras",
        "category": "Residencial",
        "image_url": "http://example.com/apto_actualizado.jpg"
    }
    update_response = client.put(f"/projects/{project_id}", json=update_data)
    assert update_response.status_code == 200
    updated_project = update_response.json()
    assert updated_project["name"] == "Apartamento Actualizado"
    assert updated_project["price"] == 320000.0

def test_delete_project():
    # Primero, crea un proyecto que luego eliminaremos
    project_data = {
        "name": "Proyecto a eliminar",
        "location": "Calle Eliminada 789",
        "lat": 40.7140,
        "lng": -74.0080,
        "price": 200000.0,
        "description": "Proyecto que se eliminará",
        "category": "Residencial",
        "image_url": "http://example.com/eliminar.jpg"
    }
    create_response = client.post("/projects/", json=project_data)
    assert create_response.status_code == 200
    project_id = create_response.json()["id"]

    delete_response = client.delete(f"/projects/{project_id}")
    assert delete_response.status_code == 200
    deleted_project = delete_response.json()
    assert deleted_project["id"] == project_id

    # Opcional: Intentar obtener el proyecto eliminado debería resultar en un error (si implementas GET /projects/{id})
    # Por ejemplo:
    # get_response = client.get(f"/projects/{project_id}")
    # assert get_response.status_code == 404
