import json
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import db
from models.account import Account

ACCOUNT_DATA = {}

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Configura la base de datos antes y después de todas las pruebas"""
    # Se ejecuta antes de todas las pruebas
    db.create_all()
    yield
    # Se ejecuta después de todas las pruebas
    db.session.close()

class TestAccountModel:
    """Modelo de Pruebas de Cuenta"""

    @classmethod
    def setup_class(cls):
        """Conectar y cargar los datos necesarios para las pruebas"""
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)
        print(f"ACCOUNT_DATA cargado: {ACCOUNT_DATA}")

    @classmethod
    def teardown_class(cls):
        """Desconectar de la base de datos"""
        pass  # Agrega cualquier acción de limpieza si es necesario

    def setup_method(self):
        """Truncar las tablas antes de cada prueba"""
        db.session.query(Account).delete()
        db.session.commit()

    def teardown_method(self):
        """Eliminar la sesión después de cada prueba"""
        db.session.remove()

    #  Casos de prueba
    def test_create_an_account(self):
        """Probar la creación de una sola cuenta"""
        data = ACCOUNT_DATA[0]  # obtener la primera cuenta
        account = Account(**data)
        account.create()
        assert len(Account.all()) == 1

    def test_create_all_accounts(self):
        """Probar la creación de múltiples cuentas"""
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        assert len(Account.all()) == len(ACCOUNT_DATA)
        
    # Pruebas para metodos de serializacion/deserializacion    
    def test_a_dict_incluye_todos_los_campos(self):
        """verifica que to_dict incluya todas las columnas incluso si son None"""
        datos = ACCOUNT_DATA[0]
        cuenta = Account(**datos)
        cuenta.create()
        resultado = cuenta.to_dict()
        for columna in cuenta.__table__.columns:
            assert columna.name in resultado
        assert isinstance(resultado['id'], int)
        assert isinstance(resultado['name'], str)
        
    def test_desde_dict_con_datos_incompletos(self):
        cuenta = Account()
        datos_parciales = {"name": "usuario"}
        cuenta.from_dict(datos_parciales)
        assert cuenta.name == "usuario"
        assert cuenta.email is None


    def test_desde_dict_con_claves_inesperadas(self):
        cuenta = Account()
        datos_extra = {"name": "extra", "email": "aeiou@x.com", "inexistente": "valor"}
        cuenta.from_dict(datos_extra)
        assert cuenta.name == "extra"
        assert cuenta.email == "aeiou@x.com"
        assert hasattr(cuenta, "inexistente")

    
    # Pruebas de comportamiento de metodos CRUD

    def test_crear_asigna_id(self):
        """verifica que se asigne un ID al crear una cuenta"""
        cuenta = Account(**ACCOUNT_DATA[0])
        cuenta.create()
        assert cuenta.id is not None

    def test_actualizar_propiedades(self):
        """actualizar propiedades y confirmar que la base de datos refleje esos cambios"""
        cuenta = Account(**ACCOUNT_DATA[0])
        cuenta.create()
        cuenta.name = "Nombre Actualizado"
        cuenta.email = "actualizado@correo.com"
        cuenta.update()

        actualizada = Account.find(cuenta.id)
        assert actualizada.name == "Nombre Actualizado"
        assert actualizada.email == "actualizado@correo.com"

    def test_actualizar_sin_id_lanza_error(self):
        """actualizar sin ID debe lanzar error"""
        cuenta = Account(name="Sin ID")
        with pytest.raises(Exception):
            cuenta.update()

    def test_eliminar_cuenta(self):
        """eliminar una cuenta y verificar que ya no existe"""
        cuenta = Account(**ACCOUNT_DATA[0])
        cuenta.create()
        cuenta_id = cuenta.id
        cuenta.delete()
        assert Account.find(cuenta_id) is None
        assert len(Account.all()) == 0
           
    # Pruebas para metodos de clase

    def test_todas_retornar_lista_vacia_si_no_hay_cuentas(self):
        """probar el comportamiento cuando no hay cuentas en la base de datos"""
        assert Account.all() == []

    def test_buscar_retorna_cuenta_si_existe(self):
        """test para find: retorna una cuenta existente"""
        cuenta = Account(**ACCOUNT_DATA[0])
        cuenta.create()
        encontrada = Account.find(cuenta.id)
        assert encontrada is not None
        assert encontrada.id == cuenta.id

    def test_buscar_retorna_none_si_no_existe(self):
        """test para find: retorna None si no encuentra la cuenta"""
        assert Account.find(999999) is None
        
    # Prueba del metodo especial __repr__    
        
    def test_repr_formato_correcto(self):
        cuenta = Account(name="NombreDePrueba")
        assert repr(cuenta) == "<Account 'NombreDePrueba'>"    