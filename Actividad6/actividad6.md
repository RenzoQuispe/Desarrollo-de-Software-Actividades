## **Actividad 6 : Rebase, Cherry-Pick y CI/CD en un entorno ágil**

### Objetivo de aprendizaje:  
Aprender a usar los comandos `git rebase` y `git cherry-pick` para mantener un historial de commits limpio y manejable en proyectos colaborativos.  También explorarás cuándo y por qué utilizar estos comandos en lugar de los merges regulares.

#### **Parte 1: git rebase para mantener un historial lineal**
1. **Introducción a Rebase:**
   El rebase mueve tus commits a una nueva base, dándote un historial lineal y limpio. En lugar de fusionar ramas y mostrar un "commit de merge", el rebase integra los cambios aplicándolos en la parte superior de otra rama.
   - **Caso de uso**: Simplifica la depuración y facilita la comprensión del historial de commits.
2. **Escenario de ejemplo:**
   - Crea un nuevo repositorio Git y dos ramas, main y new-feature:
    ![](/imagenes/actividad6/parte1_2_1.png)
   - Crea y cambia a la rama new-feature:
    ![](/imagenes/actividad6/parte1_2_2.png)
    **Pregunta:** Presenta el historial de ramas obtenida hasta el momento.
    ![](/imagenes/actividad6/parte1_2_3.png)
   Ahora, digamos que se han agregado nuevos commits a main mientras trabajabas en new-feature:
    ![](/imagenes/actividad6/parte1_2_4.png)
   Tu gráfico de commits ahora diverge (comprueba esto)
   > **Tarea**: Realiza el rebase de `new-feature` sobre `main` con los siguientes comandos: 
    ![](/imagenes/actividad6/parte1_2_5.png)
3. **Revisión:**
   Después de realizar el rebase, visualiza el historial de commits con:
   ![](/imagenes/actividad6/parte1_3.png)
4. **Momento de fusionar y completar el proceso de git rebase:**
   ![](/imagenes/actividad6/parte1_4.png)
   Cuando se realiza una fusión *fast-forward*, las HEADs de las ramas main y new-feature serán los commits correspondientes.

#### Parte 2: **git cherry-pick para la integración selectiva de commit**

1. **Introducción a Cherry-pick:**
   `git cherry-pick` te permite seleccionar commits individuales de una rama y aplicarlos en otra. Esto es útil cuando necesitas integrar una característica o corrección sin hacer merge de toda la rama.
   Imagina que tienes dos ramas, main y feature. Te das cuenta de que uno o dos commits de la rama feature deberían moverse a main, pero no estás listo para fusionar toda la rama. El comando `git cherry-pick` te permite hacer precisamente eso.
   Puedes hacer cherry-pick de los cambios de un commit específico en la rama feature y aplicarlos en la rama main.
   Esta acción creará un nuevo commit en la rama main.

2. **Escenario de ejemplo:**
   ![](/imagenes/actividad6/parte2_2_1.png)
    **Pregunta:** Muestra un diagrama de como se ven las ramas en este paso.
    ![](/imagenes/actividad6/parte2_2_2.png)

3. **Tarea: Haz cherry-pick de un commit de add-base-documents a main:**
   ![](/imagenes/actividad6/parte2_3.png)

4. **Revisión:**  
   Revisa el historial nuevamente:
   ![](/imagenes/actividad6/parte2_4.png)
   Después de que hayas realizado con éxito el cherry-pick del commit, se agregará un nuevo commit a tu rama actual (main en este ejemplo) y contendrá los cambios del commit cherry-picked. 

##### **Preguntas de discusión:**

1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?  
2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?  
3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?  
4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

#### **Ejercicios teóricos**

1. **Diferencias entre git merge y git rebase**  
   **Pregunta**: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.

2. **Relación entre git rebase y DevOps**  
   **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.

3. **Impacto del git cherry-pick en un equipo Scrum**  
   **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.

#### **Ejercicios prácticos**

1. **Simulación de un flujo de trabajo Scrum con git rebase y git merge**

   **Contexto:**  
   Tienes una rama `main` y una rama `feature` en la que trabajas. Durante el desarrollo del sprint, se han realizado commits tanto en `main` como en `feature`.  
   Tu objetivo es integrar los cambios de la rama `feature` en `main` manteniendo un historial limpio.
   **Instrucciones:**
   - Crea un repositorio y haz algunos commits en la rama main.
   - Crea una rama feature, agrega nuevos commits, y luego realiza algunos commits adicionales en main.
   - Realiza un rebase de feature sobre main.
   - Finalmente, realiza una fusión fast-forward de feature con main.
![](/imagenes/actividad6/ejerciciospracticos1_1.png)
   **Preguntas:**
   - ¿Qué sucede con el historial de commits después del rebase? 
        ![](/imagenes/actividad6/ejerciciospracticos1_2.png)    
   - ¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?

2. **Cherry-pick para integración selectiva en un pipeline CI/CD**

   **Contexto:**  
   Durante el desarrollo de una funcionalidad, te das cuenta de que solo ciertos cambios deben ser integrados en la rama de producción, ya que el resto aún está en desarrollo. Para evitar fusionar toda la rama, decides hacer cherry-pick de los commits que ya están listos para producción.
   **Instrucciones:**
   - Crea un repositorio con una rama main y una rama feature.
   - Haz varios commits en la rama feature, pero solo selecciona uno o dos commits específicos que consideres listos para producción.
   - Realiza un cherry-pick de esos commits desde feature a main.
   - Verifica que los commits cherry-picked aparezcan en main.

   ![](/imagenes/actividad6/ejerciciospracticos2.png)
   
   **Preguntas:**
   - ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?  
   - ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?

---

#### **Git, Scrum y Sprints**

#### **Fase 1: Planificación del sprint (sprint planning)**
**Ejercicio 1: Crear ramas de funcionalidades (feature branches)**
En esta fase del sprint, los equipos Scrum deciden qué historias de usuario van a trabajar. Cada historia de usuario puede representarse como una rama de funcionalidad.
**Objetivo:** Crear ramas para cada historia de usuario y asegurar que el trabajo se mantenga aislado.
**Instrucciones:**
1. Crea un repositorio en Git.
2. Crea una rama `main` donde estará el código base.
3. Crea una rama por cada historia de usuario asignada al sprint, partiendo de la rama `main`.
![](/imagenes/actividad6/ejercicioScrum1.png)
**Pregunta:** ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?

#### **Fase 2: Desarrollo del sprint (sprint execution)**
**Ejercicio 2: Integración continua con git rebase**
A medida que los desarrolladores trabajan en sus respectivas historias de usuario, pueden ocurrir cambios en main. Para mantener un historial lineal y evitar conflictos más adelante, se usa `git rebase` para integrar los últimos cambios de main en las ramas de funcionalidad antes de finalizar el sprint.
**Objetivo:** Mantener el código de la rama de funcionalidad actualizado con los últimos cambios de main durante el sprint.
**Instrucciones:**
1. Haz algunos commits en main.
2. Realiza un rebase de la rama `feature-user-story-1` para actualizar su base con los últimos cambios de main.
![](/imagenes/actividad6/ejercicioScrum2.png)
**Pregunta:** ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?

#### **Fase 3: Revisión del sprint (sprint review)**
**Ejercicio 3: Integración selectiva con git cherry-pick**
En esta fase, es posible que algunas funcionalidades estén listas para ser mostradas a los stakeholders, pero otras aún no están completamente implementadas. Usar `git cherry-pick` puede permitirte seleccionar commits específicos para mostrar las funcionalidades listas, sin hacer merge de ramas incompletas.
**Objetivo:** Mover commits seleccionados de una rama de funcionalidad (`feature-user-story-2`) a `main` sin integrar todos los cambios.
**Instrucciones:**
1. Realiza algunos commits en `feature-user-story-2`.
2. Haz cherry-pick de los commits que estén listos para mostrarse a los stakeholders durante la revisión del sprint.
![](/imagenes/actividad6/ejercicioScrum3.png)

**Pregunta:** ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?

#### **Fase 4: Retrospectiva del sprint (sprint retrospective)**
**Ejercicio 4: Revisión de conflictos y resolución**
Durante un sprint, pueden surgir conflictos al intentar integrar diferentes ramas de funcionalidades. Es importante aprender cómo resolver estos conflictos y discutirlos en la retrospectiva.
**Objetivo:** Identificar y resolver conflictos de fusión con `git merge` al intentar integrar varias ramas de funcionalidades al final del sprint.
**Instrucciones:**
1. Realiza cambios en `feature-user-story-1` y `feature-user-story-2` que resulten en conflictos.
2. Intenta hacer merge de ambas ramas con main y resuelve los conflictos.
![](/imagenes/actividad6/ejercicioScrum4_1.png)
Conflicto:
![](/imagenes/actividad6/ejercicioScrum4_2.png)
**Pregunta**: ¿Cómo manejas los conflictos de fusión al final de un sprint? ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?

#### **Fase 5: Fase de desarrollo, automatización de integración continua (CI) con git rebase**
**Ejercicio 5: Automatización de rebase con hooks de Git**
En un entorno CI, es común automatizar ciertas operaciones de Git para asegurar que el código se mantenga limpio antes de que pase a la siguiente fase del pipeline. Usa los hooks de Git para automatizar el rebase cada vez que se haga un push a una rama de funcionalidad.
**Objetivo:** Implementar un hook que haga automáticamente un rebase de `main` antes de hacer push en una rama de funcionalidad, asegurando que el historial se mantenga limpio.
**Instrucciones:**
1. Configura un hook `pre-push` que haga un rebase automático de la rama `main` sobre la rama de funcionalidad antes de que el push sea exitoso.
2. Prueba el hook haciendo push de algunos cambios en la rama `feature-user-story-1`.
![](/imagenes/actividad6/ejercicioScrum5.png)

**Pregunta**: ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?

---

### **Navegando conflictos y versionado en un entorno devOps**

**Objetivo:**  
Gestionar conflictos en Git, realizar fusiones complejas, utilizar herramientas para comparar y resolver conflictos, aplicar buenas prácticas en el manejo del historial de versiones  y usar el versionado semántico en un entorno de integración continua (CI).
**Herramientas:**
- Git  
- Un entorno de desarrollo (Visual Studio Code, terminal, etc.)  
- Un repositorio en GitHub o GitLab (opcional, puede ser local)
**Contexto:**  
En un entorno de desarrollo colaborativo, los conflictos son inevitables cuando varios desarrolladores trabajan en la misma base de código. Resolver estos conflictos es crucial para mantener un flujo de trabajo eficiente en DevOps.
Los conflictos ocurren cuando dos ramas modifican la misma línea de un archivo y luego se intenta fusionarlas. Git no puede decidir qué cambio priorizar, por lo que la resolución manual es necesaria.
#### **Cómo fusionar conflictos en Git:**
1. **Identificar conflictos**: Usa `git status` para ver los archivos en conflicto.
2. **Examinar los archivos**: Busca los marcadores de conflicto (`<<<<<<<`, `=======`, `>>>>>>`) en los archivos.
3. **Resolver los conflictos**: Elige qué cambios conservar (rama actual o fusionada) o mezcla ambos.
4. **Commit de los archivos resueltos**: Después de resolver, añade los archivos al staging y realiza el commit.
#### **Comandos para resolver conflictos**
- `git checkout --ours <file-path>`: Conserva los cambios de tu rama.  
- `git checkout --theirs <file-path>`: Conserva los cambios de la rama fusionada.
#### **Herramientas para gestionar fusiones**
- `git diff`: Compara las diferencias entre dos ramas o commits, ayudando a identificar conflictos:
  ```bash
  $ git diff feature-branch..main
  ```
- `git merge --no-commit --no-ff`: Simula una fusión sin realizar el commit para ver los cambios:
  ```bash
  $ git merge --no-commit --no-ff feature-branch
  $ git diff --cached
  ```
  Si no es lo que esperas, puedes abortar la fusión:
  ```bash
  $ git merge --abort
  ```
- `git mergetool`: Usa herramientas gráficas para resolver conflictos de manera visual. Configura tu herramienta preferida:
  ```bash
  $ git config --global merge.tool vimdiff
  $ git mergetool
  ```

##### **Comandos para organizar tu entorno de trabajo**
- **git reset**: Este comando permite retroceder en el historial de commits. Existen tres tipos:
  1. **Soft Reset**: Mueve el HEAD sin cambiar los archivos:
     ```bash
     $ git reset --soft <commit>
     ```
  2. **Mixed Reset**: Mueve el HEAD y quita archivos del staging, pero mantiene los cambios:
     ```bash
     $ git reset --mixed <commit>
     ```
  3. **Hard Reset**: Elimina todos los cambios no guardados y resetea el directorio de trabajo:
     ```bash
     $ git reset --hard <commit>
     ```
- **git revert**: Deshace cambios sin modificar el historial de commits, creando un nuevo commit:
  ```bash
  $ git revert <commit_hash>
  ```
- **git checkout**: Además de cambiar de ramas, este comando te permite restaurar archivos específicos:
  ```bash
  $ git checkout -- <file_name>
  ```

##### **Herramientas para depurar**
- **git blame**: Muestra qué usuario hizo cambios en una línea específica de un archivo:
  ```bash
  $ git blame file.txt
  ```
- **git bisect**: Realiza una búsqueda binaria para encontrar el commit que introdujo un error:
  ```bash
  $ git bisect start
  $ git bisect bad
  $ git bisect good <commit>
  $ git bisect reset
  ```

##### **git clean y stash**
1. `git clean`: Elimina archivos y directorios no rastreados.
   ```bash
   $ git clean -fd
   ```
2. `git stash`: Guarda cambios sin hacer commit, útil para multitasking.
   ```bash
   $ git stash
   $ git stash apply stash@{0}
   ```

##### **.gitignore**
El archivo `.gitignore` te permite especificar qué archivos y carpetas deben ignorarse durante un `git add`, asegurando que permanezcan exclusivos de tu entorno local.
```bash
# Ignorar todos los archivos de log
.log
# Ignorar archivos de configuración personal
config/personal/
```
##### **Versioning en Git**
Usa versioning semántico para gestionar versiones del software de manera clara:
```bash
$ git tag -a v1.0 -m "Initial stable release"
$ git tag v2.4.4 <commit>
```
---

#### **Ejemplo:**

1. **Inicialización del proyecto y creación de ramas**
   - **Paso 1**: Crea un nuevo proyecto en tu máquina local.
     ![](/imagenes/actividad6/ejemplo1_1.png)
   - **Paso 2**: Inicializa Git en tu proyecto.
     ![](/imagenes/actividad6/ejemplo1_2.png)
   - **Paso 3**: Crea un archivo de texto llamado `archivo_colaborativo.txt` y agrega algún contenido inicial.
     ![](/imagenes/actividad6/ejemplo1_3.png)
   - **Paso 4**: Agrega el archivo al área de staging y haz el primer commit.
     ![](/imagenes/actividad6/ejemplo1_4.png)
   - **Paso 5**: Crea dos ramas activas: main y feature-branch.
     ![](/imagenes/actividad6/ejemplo1_5.png)
   - **Paso 6**: Haz checkout a la rama feature-branch y realiza un cambio en el archivo `archivo_colaborativo.txt`.
     ![](/imagenes/actividad6/ejemplo1_6.png)
   - **Paso 7**: Regresa a la rama main y realiza otro cambio en la misma línea del archivo `archivo_colaborativo.txt`.
     ![](/imagenes/actividad6/ejemplo1_7.png)
2. **Fusión y resolución de conflictos**
   - **Paso 1**: Intenta fusionar feature-branch en main. Se espera que surjan conflictos de fusión.
     ![](/imagenes/actividad6/ejemplo2_1.png)
   - **Paso 2**: Usa `git status` para identificar los archivos en conflicto. Examina los archivos afectados y resuelve manualmente los conflictos, conservando las líneas de código más relevantes para el proyecto.
     ![](/imagenes/actividad6/ejemplo2_2.png)
   - **Paso 3**: Una vez resueltos los conflictos, commitea los archivos y termina la fusión
     ![](/imagenes/actividad6/ejemplo2_3.png)
3. **Simulación de fusiones y uso de git diff**
   - **Paso 1**: Simula una fusión usando `git merge --no-commit --no-ff` para ver cómo se comportarían los cambios antes de realizar el commit.
      ![](/imagenes/actividad6/ejemplo3.png)
4. **Uso de git mergetool**
   - **Paso 1**: Configura git mergetool con una herramienta de fusión visual (puedes usar meld, vimdiff, o Visual Studio Code).
     ![](/imagenes/actividad6/ejemplo4_1.png)
   - **Paso 2**: Usa la herramienta gráfica para resolver un conflicto de fusión.
     ![](/imagenes/actividad6/ejemplo4_2.png)
5. **Uso de git revert y git reset**
   - **Paso 1**: Simula la necesidad de revertir un commit en main debido a un error. Usa `git revert` para crear un commit que deshaga los cambios.
      ![](/imagenes/actividad6/ejemplo5_1.png)
   - **Paso 2**: Realiza una prueba con `git reset --mixed` para entender cómo reestructurar el historial de commits sin perder los cambios no commiteados.
      ![](/imagenes/actividad6/ejemplo5_2.png)
6. **Versionado semántico y etiquetado**
   - **Paso 1**: Aplica versionado semántico al proyecto utilizando tags para marcar versiones importantes. 
      ![](/imagenes/actividad6/ejemplo6.png)
7. **Aplicación de git bisect para depuración**
   - **Paso 1**: Usa `git bisect` para identificar el commit que introdujo un error en el código.
      ![](/imagenes/actividad6/ejemplo7.png)
#### **Preguntas**

1. **Ejercicio para git checkout --ours y git checkout --theirs**

   **Contexto**: En un sprint ágil, dos equipos están trabajando en diferentes ramas. Se produce un conflicto de fusión en un archivo de configuración crucial. El equipo A quiere mantener sus cambios mientras el equipo B solo quiere conservar los suyos. El proceso de entrega continua está detenido debido a este conflicto.

   **Pregunta**:  
   ¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en la pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?

2. **Ejercicio para git diff**

   **Contexto**: Durante una revisión de código en un entorno ágil, se observa que un pull request tiene una gran cantidad de cambios, muchos de los cuales no están relacionados con la funcionalidad principal. Estos cambios podrían generar conflictos con otras ramas en la pipeline de CI/CD.

   **Pregunta**:  
   Utilizando el comando `git diff`, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar `git diff feature-branch..main` para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.

3. **Ejercicio para git merge --no-commit --no-ff**

   **Contexto**: En un proyecto ágil con CI/CD, tu equipo quiere simular una fusión entre una rama de desarrollo y la rama principal para ver cómo se comporta el código sin comprometerlo inmediatamente en el repositorio. Esto es útil para identificar posibles problemas antes de completar la fusión.

   **Pregunta**:  
   Describe cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?

4. **Ejercicio para git mergetool**

   **Contexto**: Tu equipo de desarrollo utiliza herramientas gráficas para resolver conflictos de manera colaborativa. Algunos desarrolladores prefieren herramientas como vimdiff o Visual Studio Code. En medio de un sprint, varios archivos están en conflicto y los desarrolladores prefieren trabajar en un entorno visual para resolverlos.

   **Pregunta**:  
   Explica cómo configurarías y utilizarías `git mergetool` en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de `git mergetool` en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?

5. **Ejercicio para git reset**

   **Contexto**: En un proyecto ágil, un desarrollador ha hecho un commit que rompe la pipeline de CI/CD. Se debe revertir el commit, pero se necesita hacerlo de manera que se mantenga el código en el directorio de trabajo sin deshacer los cambios.

   **Pregunta**:  
   Explica las diferencias entre `git reset --soft`, `git reset --mixed` y `git reset --hard`. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías `git reset --mixed` para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.

6. **Ejercicio para git revert**

   **Contexto**: En un entorno de CI/CD, tu equipo ha desplegado una característica a producción, pero se ha detectado un bug crítico. La rama principal debe revertirse para restaurar la estabilidad, pero no puedes modificar el historial de commits debido a las políticas del equipo.

   **Pregunta**:  
   Explica cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial de commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías varios commits consecutivos.

7. **Ejercicio para git stash**

   **Contexto**: En un entorno ágil, tu equipo está trabajando en una corrección de errores urgente mientras tienes cambios no guardados en tu directorio de trabajo que aún no están listos para ser committeados. Sin embargo, necesitas cambiar rápidamente a una rama de hotfix para trabajar en la corrección.

   **Pregunta**:  
   Explica cómo utilizarías `git stash` para guardar temporalmente tus cambios y volver a ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de `git stash` en un flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías automatizar el proceso de *stashing* dentro de una pipeline CI/CD?

8. **Ejercicio para .gitignore**

   **Contexto**: Tu equipo de desarrollo ágil está trabajando en varios entornos locales con configuraciones diferentes (archivos de logs, configuraciones personales). Estos archivos no deberían ser parte del control de versiones para evitar confusiones en la pipeline de CI/CD.

   **Pregunta**:  
   Diseña un archivo `.gitignore` que excluya archivos innecesarios en un entorno ágil de desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en el repositorio.

---

#### **Ejercicios adicionales**

##### **Ejercicio 1: Resolución de conflictos en un entorno ágil**

**Contexto:**  
Estás trabajando en un proyecto ágil donde múltiples desarrolladores están enviando cambios a la rama principal cada día. Durante una integración continua, se detectan conflictos de fusión entre las ramas de dos equipos que están trabajando en dos funcionalidades críticas. Ambos equipos han modificado el mismo archivo de configuración del proyecto.

**Pregunta:**  
- ¿Cómo gestionarías la resolución de este conflicto de manera eficiente utilizando Git y manteniendo la entrega continua sin interrupciones? ¿Qué pasos seguirías para minimizar el impacto en la CI/CD y asegurar que el código final sea estable?


##### **Ejercicio 2: Rebase vs. Merge en integraciones ágiles**

**Contexto:**  
En tu equipo de desarrollo ágil, cada sprint incluye la integración de varias ramas de características. Algunos miembros del equipo prefieren realizar merge para mantener el historial completo de commits, mientras que otros prefieren rebase para mantener un historial lineal.

**Pregunta:**  
- ¿Qué ventajas y desventajas presenta cada enfoque (merge vs. rebase) en el contexto de la metodología ágil? ¿Cómo impacta esto en la revisión de código, CI/CD, y en la identificación rápida de errores?


##### **Ejercicio 3: Git Hooks en un flujo de trabajo CI/CD ágil**

**Contexto:**  
Tu equipo está utilizando Git y una pipeline de CI/CD que incluye tests unitarios, integración continua y despliegues automatizados. Sin embargo, algunos desarrolladores accidentalmente comiten código que no pasa los tests locales o no sigue las convenciones de estilo definidas por el equipo.

**Pregunta:**  
- Diseña un conjunto de Git Hooks que ayudaría a mitigar estos problemas, integrando validaciones de estilo y tests automáticos antes de permitir los commits. Explica qué tipo de validaciones implementarías y cómo se relaciona esto con la calidad del código y la entrega continua en un entorno ágil.

##### **Ejercicio 4: Estrategias de branching en metodologías ágiles**

**Contexto:**  
Tu equipo de desarrollo sigue una metodología ágil y está utilizando Git Flow para gestionar el ciclo de vida de las ramas. Sin embargo, a medida que el equipo ha crecido, la gestión de las ramas se ha vuelto más compleja, lo que ha provocado retrasos en la integración y conflictos de fusión frecuentes.

**Pregunta:**  
- Explica cómo adaptarías o modificarías la estrategia de branching para optimizar el flujo de trabajo del equipo en un entorno ágil y con integración continua. Considera cómo podrías integrar feature branches, release branches y hotfix branches de manera que apoyen la entrega continua y minimicen conflictos.


##### **Ejercicio 5: Automatización de reversiones con git en CI/CD**

**Contexto:**  
Durante una integración continua en tu pipeline de CI/CD, se detecta un bug crítico después de haber fusionado varios commits a la rama principal. El equipo necesita revertir los cambios rápidamente para mantener la estabilidad del sistema.

**Pregunta:**  
- ¿Cómo diseñarías un proceso automatizado con Git y CI/CD que permita revertir cambios de manera eficiente y segura? Describe cómo podrías integrar comandos como `git revert` o `git reset` en la pipeline y cuáles serían los pasos para garantizar que los bugs se reviertan sin afectar el desarrollo en curso.

--- 
**Entrega:**  
- Al finalizar, debes hacer push a su repositorio remoto con los cambios realizados y etiquetar el commit final.

**Evaluación:**  
- El dominio de los comandos Git será evaluado, junto con la correcta resolución de conflictos, uso de herramientas de fusión, y comprensión de versionado semántico.