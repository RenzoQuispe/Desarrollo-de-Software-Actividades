## **Actividad 5: Explorando diferentes formas de fusionar en Git**

### **Objetivo de aprendizaje:**  

En esta actividad, exploraremos el proceso de fusionar dos ramas en Git utilizando tres métodos diferentes: fast-forward, no-fast-forward y squash. A través de los ejemplos, comprenderás cómo funcionan y cuándo es recomendable utilizar cada tipo de fusión.

### Fusión Fast-forward (git merge --ff)
- Pasos Practicos - Ejemplo
![](imagenes/actividad5/EjemploFastForward1.PNG)
![](imagenes/actividad5/EjemploFastForward2.PNG)

### Fusión No-fast-forward (git merge --no-ff)
- Pasos Practicos - Ejemplo
![](imagenes/actividad5/EjemploNoFastForward1.PNG)
![](imagenes/actividad5/EjemploNoFastForward2.PNG)
![](imagenes/actividad5/EjemploNoFastForward3.PNG)
![](imagenes/actividad5/EjemploNoFastForward4.PNG)

### Fusión squash (git merge --squash)
- Pasos Practicos - Ejemplo
![](imagenes/actividad5/EjemploSquash1.PNG)
![](imagenes/actividad5/EjemploSquash2.PNG)

### Ejercicios
#### 1. Clona un repositorio Git con múltiples ramas.
![](imagenes/actividad5/e1_1.png)
![](imagenes/actividad5/e1_2.png)
#### 2. Simula un flujo de trabajo de equipo.
![](imagenes/actividad5/e2_1.png)
![](imagenes/actividad5/e2_2.png)
![](imagenes/actividad5/e2_3.png)
![](imagenes/actividad5/e2_4.png)
#### 3. Crea múltiples commits en una rama.
![](imagenes/actividad5/e3_1.png)
![](imagenes/actividad5/e3_2.png)
![](imagenes/actividad5/e3_3.png)
![](imagenes/actividad5/e3_4.png)

### Resolver conflictos en una fusión non-fast-forward

### Ejercicio 1: Comparar los historiales con git log después de diferentes fusiones
![](imagenes/actividad5/ejercicio1_1.PNG)
![](imagenes/actividad5/ejercicio1_2.PNG)
![](imagenes/actividad5/ejercicio1_3.PNG)
![](imagenes/actividad5/ejercicio1_4.PNG)
### Ejercicio 2: Usando fusiones automáticas y revertir fusiones
![](imagenes/actividad5/ejercicio2_1.png)
![](imagenes/actividad5/ejercicio2_2.png)
![](imagenes/actividad5/ejercicio2_3.png)
### Ejercicio 3: Fusión remota en un repositorio colaborativo
![](imagenes/actividad5/ejercicio3_1.png)
![](imagenes/actividad5/ejercicio3_2.png)
### Ejercicio final: flujo de trabajo completo
Crea un proyecto con tres ramas: main, feature1, y feature2.
![](imagenes/actividad5/ef1.png)
Realiza varios cambios en feature1 y feature2 y simula colaboraciones paralelas.
![](imagenes/actividad5/ef2.png)
Realiza fusiones utilizando diferentes métodos:
Fusiona feature1 con main utilizando git merge --ff
![](imagenes/actividad5/ef3.png)
Fusiona feature2 con main utilizando git merge --no-ff
![](imagenes/actividad5/ef4.png)
Haz una rama adicional llamada feature3 y aplasta sus commits utilizando git merge --squash
![](imagenes/actividad5/ef5.png)
![](imagenes/actividad5/ef6.png)
Revisa el historial para entender cómo los diferentes métodos de fusión afectan el árbol de commits.
![](imagenes/actividad5/ef7.png)
- Compara los resultados y discute con tus compañeros de equipo cuál sería la mejor estrategia de fusión para proyectos más grandes.
Para Proyectos grandes es mas util el merge no-ff porque cuando estamos trabajando con varios desarrolladores los conflictos en el codigo son constantes, el merge squash son utiles para mantener el historial de commits mas ordenado y cuando hacemos constantesmente multiples commits. El merge ff por su caracteristica de "desplazar el head" es mas util en proyectos personales o de pocos desarrolladores.