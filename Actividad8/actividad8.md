### Actividad 8: El patrón Arrange-Act-Assert

Las pruebas unitarias no son nada misteriosas. Son solo código ejecutable escrito en el mismo lenguaje que la aplicación. Cada prueba de unidad constituye el primer uso del código que se desea escribir. Se llama al código tal como se llamará en la aplicación real. 

La prueba ejecuta ese código, captura los resultados que nos interesan y verifica que sean lo que esperábamos. Dado que la prueba usa el código de la misma manera que la aplicación, recibimos comentarios inmediatos sobre qué tan fácil o difícil es usarlo. Esto puede sonar obvio, y lo es, pero es una herramienta poderosa para escribir código limpio y correcto.

#### Objetivos de aprendizaje

- Aplicar el patrón **Arrange-Act-Assert (AAA)** para estructurar pruebas unitarias claras y legibles.
- Escribir pruebas efectivas usando **Pytest**, utilizando buenas prácticas como una sola aserción por prueba.
- Comprender y aplicar los principios **FIRST** para mejorar la calidad de las pruebas.

#### Definición de la estructura de la prueba

Es útil seguir plantillas al hacer pruebas unitarias, y no son una excepción. Kent Beck, el inventor de TDD, descubrió que las pruebas unitarias tenían características en común. Esto se resumió en la estructura llamada **Arrange-Act-Assert (AAA)**.

#### La definición original de AAA

La descripción original de AAA se puede encontrar en el wiki de C2: [Arrange-Act-Assert](http://wiki.c2.com/?ArrangeActAssert).

A continuación, se presenta un ejemplo de una prueba unitaria para asegurarse de que un nombre de usuario se muestre en minúsculas:

##### Ejemplo en Python usando unittest

```python
import unittest

class Username:
    def __init__(self, name):
        self.name = name

    def as_lowercase(self):
        return self.name.lower()

class TestUsername(unittest.TestCase):
    
    def test_converts_to_lowercase(self):
        # Arrange
        username = Username("SirJakington35179")
        
        # Act
        actual = username.as_lowercase()
        
        # Assert
        self.assertEqual(actual, "sirjakington35179")

if __name__ == "__main__":
    unittest.main()
```

El nombre de la clase para la prueba es `TestUsername`, lo que indica el área de comportamiento que estamos probando: nombres de usuario. Este enfoque narrativo ayuda a los lectores a entender qué problema se está resolviendo.

El método de prueba es `test_converts_to_lowercase()`, que describe lo que se espera: convertir un nombre de usuario a minúsculas. La estructura **Arrange-Act-Assert** se utiliza dentro del método de prueba. Primero, en **Arrange**, se crea el objeto `Username` y se almacena en la variable `username`. Luego, en **Act**, se llama al método `as_lowercase()` para realizar la conversión. Finalmente, en **Assert**, se verifica que el resultado sea el esperado con `assertEqual()`.

Las pruebas unitarias en Python, al igual que en Java, son fáciles de escribir, leer y ejecutar rápidamente. Esto las hace ideales para TDD.


#### Definición de una buena prueba

Como todo código, el código de prueba unitaria se puede escribir de mejores o peores maneras. Ya hemos visto cómo **Arrange-Act-Assert (AAA)** nos ayuda a estructurar correctamente una prueba y cómo los nombres descriptivos y precisos cuentan la historia de lo que nuestro código debe hacer. Las pruebas más útiles también siguen los principios **FIRST** y usan una sola aserción por prueba.

##### Aplicando los principios FIRST

Los principios **FIRST** son un conjunto de cinco reglas que hacen que las pruebas unitarias sean más efectivas:

1. **Rápido**: Las pruebas unitarias deben ejecutarse rápidamente, tal como vimos en el ejemplo anterior. Esto es crucial para **TDD** ya que queremos recibir retroalimentación inmediata mientras exploramos nuestro diseño e implementación. Si una prueba tarda demasiado en ejecutarse, es probable que dejemos de ejecutarlas con frecuencia, lo que puede llevarnos a escribir grandes fragmentos de código sin pruebas. Esto va en contra del espíritu de TDD, por lo que debemos trabajar para que nuestras pruebas sean rápidas. Idealmente, las pruebas deben ejecutarse en milisegundos o menos de 2 segundos.

2. **Aislado**: Las pruebas unitarias deben estar completamente aisladas unas de otras. Esto significa que podemos ejecutar cualquier prueba, o cualquier combinación de ellas, en el orden que queramos, obteniendo siempre el mismo resultado. Si una prueba depende del resultado de otra, se generará un falso negativo, lo que hará que la prueba sea inútil. El aislamiento es clave para un flujo de trabajo saludable en **TDD**.

3. **Repetible**: Las pruebas deben ser repetibles. Esto significa que cada vez que ejecutamos una prueba con el mismo código de producción, esa prueba debe devolver siempre el mismo resultado, ya sea éxito o falla. Si las pruebas dependen de factores externos como el tiempo, la red o el estado de una base de datos, puede ser difícil mantener esta repetibilidad. Para abordar estos casos, se suelen utilizar **Stubs** y **Mocks**, que simulan el comportamiento de dependencias externas.

4. **Autoverificable**: Las pruebas deben ser autoverificables. Esto significa que deben incluir toda la lógica necesaria para determinar si el código bajo prueba funciona correctamente. No debemos requerir intervención manual, como revisar una consola o un archivo de registro. La automatización es clave aquí: las pruebas deben ejecutarse y darnos una respuesta inmediata de "aprobado" o "fallado".

5. **Oportuno**: Las pruebas deben escribirse en el momento justo, es decir, antes de escribir el código que hace que la prueba pase. Este es el núcleo del desarrollo impulsado por pruebas (**TDD**). Las pruebas oportunas nos permiten recibir comentarios sobre el diseño del código y evitar errores tempranos.

##### Escribiendo una sola aserción por prueba

Una buena práctica en las pruebas unitarias es escribir una sola aserción por prueba. Esto tiene varias ventajas. En primer lugar, si la prueba falla, sabremos inmediatamente cuál fue el problema, ya que la prueba está probando un único comportamiento. Además, las pruebas con una sola aserción tienden a ser más fáciles de entender y mantener.

Volviendo al ejemplo en Python, la prueba `test_converts_to_lowercase()` contiene una única aserción con `self.assertEqual(actual, "sirjakington35179")`. Si esta aserción falla, sabemos que el método `as_lowercase()` no está funcionando como se esperaba, sin necesidad de inspeccionar múltiples aserciones.


##### Mejorando la retroalimentación en TDD

Al seguir los principios FIRST y la estructura AAA, podemos asegurarnos de que nuestras pruebas unitarias sean útiles, rápidas y confiables. Estas pruebas no solo validan nuestro código, sino que también nos proporcionan una valiosa retroalimentación durante el proceso de diseño y desarrollo. Ver cómo las pruebas fallidas (pruebas rojas) se convierten en pruebas exitosas (pruebas verdes) genera confianza en nuestro código.

Las pruebas unitarias también promueven el código de alta calidad, ya que nos obligan a pensar en cómo se usará el código desde el principio. Este enfoque basado en pruebas es clave para mantener la calidad y robustez de los sistemas de software.

Este patrón ayuda a mantener las pruebas organizadas y fáciles de leer.

#### Ejemplo

A continuación se muestra un ejemplo más complejo del proyecto, donde se amplía la funcionalidad de un carrito de compras. Se agrega manejo de cantidades, eliminación de productos, cálculo de totales y aplicación de descuentos. Cada prueba está claramente separada en las tres fases del patrón **AAA (Arrange, Act, Assert)**, con comentarios que indican cada paso.

Revisa el ejemplo completo en [El patrón AAA](https://github.com/kapumota/DS/tree/main/2025-1/Actividad10-CC3S2/Ejemplo).

##### Estructura de archivos del proyecto

```
Ejemplo/
├── src/
│   ├── __init__.py
|   ├── carrito.py
│   └── factories.py
├── tests/
│   └── test_carrito.py
├── requirements.txt
└── pytest.ini
```


##### 1. Lógica del negocio

En `src/carrito.py` definimos las clases **Producto**, **ItemCarrito** y **Carrito** con funcionalidades ampliadas:

```python
# src/carrito.py

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio})"


class ItemCarrito:
    def __init__(self, producto, cantidad=1):
        self.producto = producto
        self.cantidad = cantidad

    def total(self):
        return self.producto.precio * self.cantidad

    def __repr__(self):
        return f"ItemCarrito({self.producto}, cantidad={self.cantidad})"


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad=1):
        """
        Agrega un producto al carrito. Si el producto ya existe, incrementa la cantidad.
        """
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                item.cantidad += cantidad
                return
        self.items.append(ItemCarrito(producto, cantidad))

    def remover_producto(self, producto, cantidad=1):
        """
        Remueve una cantidad del producto del carrito.
        Si la cantidad llega a 0, elimina el item.
        """
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.cantidad > cantidad:
                    item.cantidad -= cantidad
                elif item.cantidad == cantidad:
                    self.items.remove(item)
                else:
                    raise ValueError("Cantidad a remover es mayor que la cantidad en el carrito")
                return
        raise ValueError("Producto no encontrado en el carrito")

    def actualizar_cantidad(self, producto, nueva_cantidad):
        """
        Actualiza la cantidad de un producto en el carrito.
        Si la nueva cantidad es 0, elimina el item.
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if nueva_cantidad == 0:
                    self.items.remove(item)
                else:
                    item.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado en el carrito")

    def calcular_total(self):
        """
        Calcula el total del carrito sin descuento.
        """
        return sum(item.total() for item in self.items)

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento al total del carrito y retorna el total descontado.
        El porcentaje debe estar entre 0 y 100.
        """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    def contar_items(self):
        """
        Retorna el número total de items (sumando las cantidades) en el carrito.
        """
        return sum(item.cantidad for item in self.items)

    def obtener_items(self):
        """
        Devuelve la lista de items en el carrito.
        """
        return self.items
```

##### 2. Fábricas para datos de prueba

Utilizando **Factory Boy** en `src/factories.py` creamos una fábrica para generar instancias de `Producto`:

```python
# src/factories.py
import factory
from .carrito import Producto

class ProductoFactory(factory.Factory):
    class Meta:
        model = Producto

    nombre = factory.Faker("word")
    precio = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
```


##### 3. Pruebas con Pytest usando el patrón AAA

En `tests/test_carrito.py` se definen múltiples pruebas que validan la funcionalidad del carrito. Cada prueba está organizada en:

- **Arrange**: Preparación del entorno, creación de objetos y configuración inicial.
- **Act**: Ejecución de la acción a probar.
- **Assert**: Verificación del resultado esperado.

```python
# tests/test_carrito.py

import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

def test_agregar_producto_nuevo():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act
    carrito.agregar_producto(producto)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Teclado", precio=75.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.remover_producto(producto, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto, cantidad=2)
    
    # Act
    carrito.remover_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Cargador", precio=25.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 550.00


def test_aplicar_descuento():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=500.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)
```


##### 4. Configuración de dependencias y ejecución

En el archivo `requirements.txt` asegúrate de incluir las dependencias necesarias:

```
pytest==7.1.2          
pytest-cov==3.0.0      
coverage==6.3.2
factory-boy==3.2.1  
pylint==2.14.0
```

Para ejecutar las pruebas y generar el reporte de cobertura, puedes usar:

```bash
pytest --cov=src --cov-report=term-missing
```

O bien, para generar un reporte HTML:

```bash
pytest --cov=src --cov-report=html
```

Y para el análisis estático con pylint:

```bash
pylint src tests
```

En el directorio `Ejemplo`, crea un archivo llamado `pytest.ini` con el siguiente contenido:

```
[pytest]
pythonpath = .
testpaths = tests
```

Este archivo le indica a Pytest que agregue el directorio actual (la raíz del proyecto) al `PYTHONPATH` y que busque las pruebas dentro de la carpeta tests.



---
#### Ejercicios

##### Ejercicio 1: Método para vaciar el carrito
**Objetivo:**  
Implementa en la clase `Carrito` un método llamado `vaciar()` que elimine todos los items del carrito. Luego, escribe pruebas siguiendo el patrón AAA para verificar que, al vaciar el carrito, la lista de items quede vacía y el total sea 0.
**Pistas:**
- Agrega el método `vaciar` en `src/carrito.py` que realice `self.items = []`.
  ![](./imagenes/e1.1.png)
- Crea pruebas en `tests/test_carrito.py` que agreguen varios productos, invoquen `vaciar()` y verifiquen que `obtener_items()` retorne una lista vacía y `calcular_total()` retorne 0.
  ![](./imagenes/e1.2.png)


##### Ejercicio 2: Descuento por compra mínima
**Objetivo:**  
Amplía la lógica del carrito para aplicar un descuento solo si el total supera un monto determinado. Por ejemplo, si el total es mayor a \$500, se aplica un 15% de descuento.
**Pistas:**
- Agrega un nuevo método, por ejemplo, `aplicar_descuento_condicional(porcentaje, minimo)` en la clase `Carrito` que primero verifique si `calcular_total() >= minimo`.  
- Si se cumple la condición, aplica el descuento; de lo contrario, retorna el total sin descuento.
  ![](./imagenes/e2.1.png)
- Escribe pruebas para ambos escenarios (condición cumplida y no cumplida).
![](./imagenes/e2.2.png)


##### Ejercicio 3: Manejo de stock en producto

**Objetivo:**  
Modifica la clase `Producto` para que incluya un atributo `stock` (cantidad disponible). Luego, actualiza el método `agregar_producto` en `Carrito` para que verifique que no se agregue una cantidad mayor a la disponible en stock. Si se intenta agregar más, se debe lanzar una excepción.

**Pistas:**
- Modifica `Producto` en `src/carrito.py` añadiendo `self.stock = stock` en el constructor y actualiza la fábrica en `src/factories.py` para que genere un stock (por ejemplo, entre 1 y 100).
![](./imagenes/e3.0.png)
![](./imagenes/e3.1.png)   
- Escribe pruebas que verifiquen:
  - Se puede agregar un producto dentro del límite de stock.
  - Se lanza una excepción al intentar agregar más unidades de las disponibles.


##### Ejercicio 4: Ordenar items del carrito

**Objetivo:**  
Agrega un método en `Carrito` que devuelva la lista de items ordenados por un criterio (por ejemplo, por precio unitario o por nombre del producto).

**Pistas:**
- Crea un método `obtener_items_ordenados(criterio: str)` donde `criterio` pueda ser `"precio"` o `"nombre"`.
- Utiliza la función `sorted()` con una función lambda para ordenar según el criterio.
![](./imagenes/e4.1.png)
- Escribe pruebas que verifiquen que, al agregar varios productos, la lista devuelta esté ordenada correctamente según el criterio solicitado.
![](./imagenes/e4.2.png)

##### Ejercicio 5: Uso de Pytest Fixtures
**Objetivo:**  
Refactoriza las pruebas para que utilicen **fixtures** de Pytest, de modo que se reutilicen instancias comunes de `Carrito` o de productos.
**Pistas:**
- En el archivo `tests/conftest.py`, crea una fixture para un carrito vacío:
  ![](./imagenes/e5.1.png)

- Actualiza las pruebas existentes para usar estas fixtures en lugar de instanciar los objetos directamente en cada test.
   ![](./imagenes/e5.2.png) 


##### Ejercicio 6: Pruebas parametrizadas
**Objetivo:**  
Utiliza la marca `@pytest.mark.parametrize` para crear pruebas que verifiquen múltiples escenarios de descuento o actualización de cantidades.
**Pistas:**
- Por ejemplo, parametriza pruebas para `aplicar_descuento` usando distintos porcentajes y totales esperados.
- De igual forma, para actualizar cantidades: prueba con diferentes valores (válidos e inválidos) y verifica que se lance la excepción en los casos correspondientes.
![](./imagenes/e6.png) 


##### Ejercicio 7: Calcular impuestos en el carrito

**Objetivo:**  
Implementar un método `calcular_impuestos(porcentaje)` que retorne el valor del impuesto calculado sobre el total del carrito.

##### Red
1. **Escribir la prueba que falla:**  
   Crea un nuevo archivo de pruebas (por ejemplo, `tests/test_impuestos.py`) y escribe una prueba que espere que, dado un carrito con un total de \$1000, al aplicar un 10% de impuestos se retorne \$100.

![](./imagenes/e7.1.png) 
   *En este punto, la prueba fallará porque el método `calcular_impuestos` aún no existe.*

##### Green
2. **Implementar el código mínimo:**  
![](./imagenes/e7.2.png) 
![](./imagenes/e7.3.png) 

##### Refactor
3. **Refactorizar:**  
   - Agrega validaciones para que el porcentaje esté en un rango razonable (por ejemplo, entre 0 y 100).  
   - Añade documentación al método.
![](./imagenes/e7.4.png) 

##### Ejercicio 8: Aplicar cupón de descuento con límite máximo

**Objetivo:**  
Implementar un método `aplicar_cupon(descuento_porcentaje, descuento_maximo)` que aplique un cupón de descuento al total del carrito, pero asegurándose de que el descuento no supere un valor máximo.

##### Red
1. **Escribir la prueba que falla:**  
   Crea un archivo, por ejemplo, `tests/test_cupon.py` y escribe una prueba que verifique que, para un carrito con total \$400 y un cupón del 20% (lo que daría \$80), si el descuento máximo es \$50, el método retorne \$350.

![](./imagenes/e8.1.png) 
##### Green
2. **Implementar el código mínimo:**  
   En `src/carrito.py`, añade un método para aplicar el cupón de descuento de forma básica:

   ```python
   def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
       total = self.calcular_total()
       descuento_calculado = total * (descuento_porcentaje / 100)
       descuento_final = min(descuento_calculado, descuento_maximo)
       return total - descuento_final
   ```
![](./imagenes/e8.2.png) 
##### Refactor
3. **Refactorizar:**  
   - Agrega validaciones para que el porcentaje de descuento y el máximo sean valores positivos.
   - Separa la lógica de cálculo y validación, y documenta el método.

   ![](./imagenes/e8.3.png) 


##### Ejercicio 9: Validación de stock al agregar productos (RGR)

**Objetivo:**  
Asegurarse de que al agregar un producto al carrito, no se exceda la cantidad disponible en stock.  

##### Red
1. **Escribir la prueba que falla:**  
   En un nuevo archivo, por ejemplo, `tests/test_stock.py`, escribe una prueba que verifique que si se intenta agregar más unidades de las disponibles, se lance una excepción.

   ![](./imagenes/e9.1.png) 
##### Green
2. **Implementar el código mínimo:**  
   Modifica el método `agregar_producto` en `Carrito` para que valide el stock:

    ![](./imagenes/e9.2.png) 
##### Refactor
3. **Refactorizar:**  
   - Centraliza la validación del stock en un método privado o en la clase `Producto` si es necesario.
   - Documenta la función y separa la lógica de búsqueda del producto en el carrito.
   ![](./imagenes/e9.3.png) 