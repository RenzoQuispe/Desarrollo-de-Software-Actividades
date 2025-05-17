## **Actividad 4:** Introducción a Git - conceptos básicos y operaciones esenciales

### Objetivo de aprendizaje

Familiarizarse con los conceptos básicos de Git y realizar operaciones esenciales, como la configuración inicial, creación de repositorios, preparación y confirmación de cambios, visualización de historial, y gestión de ramas.

### Preguntas

- ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?
Con los comando que tiene es posible visualizar el historial de forma clara "git log --graph --oneline --all" y "git log --oneline" y con "git rebase" podemos organizar los multiples commit que hacemos, ya que combinamos varios commits en uno solo y tenemos el historial mas limpio.
- ¿Qué beneficios ves en el uso de ramas para desarrollar nuevas características o corregir errores?  
Orden en el desarrollo colaborativo, de tal manera que cada uno trabaja en su implementacion, para despues juntar dichas implementaciones. Tambien sirve como un desarrollo de prueba, si en dicha rama desarrollamos correctamente, incluimos los cambios a la rama master.
- Realiza una revisión final del historial de commits para asegurarte de que todos los cambios se han registrado correctamente.  
![](imagenes/ejercicio2_1.PNG)
- Revisa el uso de ramas y merges para ver cómo Git maneja múltiples líneas de desarrollo.
![](imagenes/ejercicio2_5.PNG) 
![](imagenes/ejercicio3_2.PNG)

### Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos
![](imagenes/ejercicio1_1.PNG)
![](imagenes/ejercicio1_2.PNG)
![](imagenes/ejercicio1_3.PNG)
![](imagenes/ejercicio1_4.PNG)
### Ejercicio 2: Exploración y manipulación del historial de commits
![](imagenes/ejercicio2_1.PNG)
![](imagenes/ejercicio2_2.PNG)
![](imagenes/ejercicio2_3.PNG)
![](imagenes/ejercicio2_4.PNG)
![](imagenes/ejercicio2_5.PNG)
### Ejercicio 3: Creación y gestión de ramas desde commits específicos
![](imagenes/ejercicio3_1.PNG)
![](imagenes/ejercicio3_2.PNG)
### Ejercicio 4: Manipulación y restauración de commits con git reset y git restore
![](imagenes/ejercicio4_1.PNG)
![](imagenes/ejercicio4_2.PNG)
### Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests
 - Crear un nuevo repositorio remoto:
  ![](imagenes/ejercicio5_1.png)
  ![](imagenes/ejercicio5_2.png)
 - Crear una nueva rama para desarrollo de una característica:
  ![](imagenes/ejercicio5_3.png)
 - Realizar cambios y enviar la rama al repositorio remoto:
  ![](imagenes/ejercicio5_4.png)
 - Abrir un Pull Request:
  ![](imagenes/ejercicio5_5.png)
 - Revisar y fusionar el Pull Request:
  ![](imagenes/ejercicio5_6.png)
  ![](imagenes/ejercicio5_7.png)
 - Eliminar la rama remota y local:
  ![](imagenes/ejercicio5_8.png)
### Ejercicio 6: Cherry-Picking y Git Stash
 - Hacer cambios en main.py y confirmarlos:
  ![](imagenes/ejercicio6_1.png)
 - Crear una nueva rama y aplicar el commit específico:
  ![](imagenes/ejercicio6_2.png)
 - Guardar temporalmente cambios no confirmados
  ![](imagenes/ejercicio6_3.png)
 - Aplicar los cambios guardados:
  ![](imagenes/ejercicio6_4.png)
 - Revisar el historial y confirmar la correcta aplicación de los cambios:
  ![](imagenes/ejercicio6_5.png)
Presentación PPT:
[Ver ppt de la exposicion](DS_Actividad4.pdf)