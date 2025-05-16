"""
Casos de prueba para el mocking
"""
import os
import json
import pytest
import sys

# Agregar el directorio raíz al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, Mock
from requests import Response
from models import IMDb

# Fixture para cargar los datos de IMDb desde un archivo JSON
@pytest.fixture(scope="session")
def imdb_data():
    """Carga las respuestas de IMDb necesarias para las pruebas"""
    current_dir = os.path.dirname(__file__)
    fixture_path = os.path.join(current_dir, 'fixtures', 'imdb_responses.json')
    with open(fixture_path) as json_data:
        data = json.load(json_data)
        print("Contenido de imdb_data:", data)  # Para depuración
        return data

class TestIMDbDatabase:
    """Casos de prueba para la base de datos de IMDb"""

    @pytest.fixture(autouse=True)
    def setup_class(self, imdb_data):
        """Configuración inicial para cargar los datos de IMDb"""
        self.imdb_data = imdb_data

    ######################################################################
    #  Casos de prueba
    ######################################################################

    @patch('test_imdb.IMDb.search_titles')
    def test_search_by_title(self, imdb_mock): #Paso1
        """Prueba de búsqueda por título"""
        imdb_mock.return_value = self.imdb_data["GOOD_SEARCH"]
        imdb = IMDb("k_12345678")
        resultados = imdb.search_titles("Bambi")
        assert resultados is not None
        assert resultados.get("errorMessage") is None
        assert resultados.get("results") is not None
        assert resultados["results"][0]["id"] == "tt1375666"
    
    @patch('models.imdb.requests.get')
    def test_search_with_no_results(self, imdb_mock): #Paso2
        """Prueba de búsqueda sin resultados"""
        imdb_mock.return_value = Mock(status_code=404)
        imdb = IMDb("k_12345678")
        resultados = imdb.search_titles("Titulo inexistente")
        assert resultados == {}

    @patch('models.imdb.requests.get')
    def test_search_by_title_failed(self, mock_get): #Paso3
        """Prueba de búsqueda por título fallida"""
        # Configurar el mock para devolver una respuesta con API Key inválida
        mock_response = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=self.imdb_data["INVALID_API"])
        )
        mock_get.return_value = mock_response

        imdb = IMDb(apikey="bad-key")
        resultados = imdb.search_titles("Bambi")

        assert resultados is not None
        assert resultados["errorMessage"] == "Invalid API Key"

    @patch('models.imdb.requests.get')
    def test_movie_ratings(self, imdb_mock): #Paso4_
        """Prueba de calificaciones de películas"""
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200, 
            json=Mock(return_value=self.imdb_data["GOOD_RATING"])
        )
        imdb = IMDb("k_12345678")
        resultados = imdb.movie_ratings("tt1375666")
        assert resultados is not None
        assert resultados["title"] == "Bambi"
        assert resultados["filmAffinity"] == 3
        assert resultados["rottenTomatoes"] == 5

    @patch('models.imdb.requests.get')
    def test_search_titles_success(self, mock_get):
        """Prueba que la búsqueda de títulos retorna datos correctamente"""
        # Configurar el mock para devolver una respuesta exitosa
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = self.imdb_data['search_title']
        mock_get.return_value = mock_response

        imdb = IMDb(apikey="fake_api_key")
        resultado = imdb.search_titles("Bambi")

        assert resultado == self.imdb_data['search_title']
        mock_get.assert_called_once_with("https://imdb-api.com/API/SearchTitle/fake_api_key/Bambi")

    @patch('models.imdb.requests.get')
    def test_search_titles_failure(self, mock_get):
        """Prueba que la búsqueda de títulos maneja errores correctamente"""
        # Configurar el mock para devolver una respuesta fallida con json retornando {}
        mock_response = Mock(spec=Response)
        mock_response.status_code = 404
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        imdb = IMDb(apikey="fake_api_key")
        resultado = imdb.search_titles("TituloInexistente")

        assert resultado == {}
        mock_get.assert_called_once_with("https://imdb-api.com/API/SearchTitle/fake_api_key/TituloInexistente")

    @patch('models.imdb.requests.get')
    def test_movie_reviews_success(self, mock_get):
        """Prueba que la obtención de reseñas retorna datos correctamente"""
        # Configurar el mock para devolver una respuesta exitosa
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = self.imdb_data['movie_reviews']
        mock_get.return_value = mock_response

        imdb = IMDb(apikey="fake_api_key")
        resultado = imdb.movie_reviews("tt1375666")

        assert resultado == self.imdb_data['movie_reviews']
        mock_get.assert_called_once_with("https://imdb-api.com/API/Reviews/fake_api_key/tt1375666")

    @patch('models.imdb.requests.get')
    def test_movie_ratings_success(self, mock_get):
        """Prueba que la obtención de calificaciones retorna datos correctamente"""
        # Configurar el mock para devolver una respuesta exitosa
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = self.imdb_data['movie_ratings']
        mock_get.return_value = mock_response

        imdb = IMDb(apikey="fake_api_key")
        resultado = imdb.movie_ratings("tt1375666")

        assert resultado == self.imdb_data['movie_ratings']
        mock_get.assert_called_once_with("https://imdb-api.com/API/Ratings/fake_api_key/tt1375666")

    @patch('models.imdb.requests.get')
    def test_movie_ratings_good(self, mock_get):
        """Prueba de calificaciones de películas con buenas calificaciones"""
        # Configurar el mock para devolver una respuesta exitosa con buenas calificaciones
        mock_response = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=self.imdb_data["movie_ratings"])
        )
        mock_get.return_value = mock_response

        imdb = IMDb(apikey="fake_api_key")
        resultados = imdb.movie_ratings("tt1375666")

        assert resultados is not None
        assert resultados["title"] == "Bambi"
        assert resultados["filmAffinity"] == 3
        assert resultados["rottenTomatoes"] == 5
    
    

