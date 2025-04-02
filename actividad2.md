### **Actividad 2: Del código a la producción: Infraestructura, contenedores, despliegue y observabilidad**

#### Tareas Teóricas

##### - Investigar una herramienta de IaC (p. ej. Terraform) y describir cómo organiza sus módulos.
Terraform: Es una herramienta que sirve para automatizar, configurar y administrar nuestra infraestructura de manera sencilla. Organiza dicha configuración mediante módulos. Es de codigo abierto y es desarrollado por HashiCorp
Los modulos sirven para enpaquetar y reutilizar configuraciones de recursos.
##### - Proponer la estructura de archivos y directorios para un proyecto hipotético que incluya tres módulos: network, database y application. Justificar la jerarquía elegida.
-
##### - Describir un flujo simple de despliegue donde un desarrollador hace un cambio en el código, se construye una nueva imagen Docker y se actualiza un Deployment de Kubernetes.
-
##### - Explicar las ventajas de usar Kubernetes para escalar una aplicación en un evento de alto tráfico.
- Reparte el trafico de manera eficiente.
- Permite agregar mas recursos cuando sea necesario  
- Permite escalar la aplicacion automaticamente cuando hay mas trafico.
##### - Investigar y describir cómo Prometheus y Grafana se integran con Kubernetes para monitorear los contenedores y el cluster.

##### - Proponer un set de métricas y alertas mínimas para una aplicación web (por ejemplo, latencia de peticiones, uso de CPU/memoria, tasa de errores).

##### - Explicar la diferencia entre entrega continua (continuous delivery) y despliegue continuo (continuous deployment).
En entrega continua, el software se prepara automaticamente para produccion, pero el despliegue no es automatico, hay mas control de las nuevas versiones del software. En cambio en el despliegue continuo las pruebas y el despliegue es automatico.
##### - Describir la relevancia de implementar pruebas automáticas (unitarias, de integración, de seguridad) dentro del pipeline.

#### Evaluación de la teoría
##### - Cada estudiante deberá redactar un informe sobre la importancia de IaC, contenedores, Kubernetes, observabilidad y CI/CD para la entrega ágil y confiable de software.
##### - Identificar riesgos y desafíos (p.e. sobrecarga cognitiva, necesidad de capacitación, configuración de seguridad).    
#### Discusión en grupo
##### - Debatir cómo la adopción de estas prácticas puede acelerar el “time to market” de un producto.
##### - Comentar ejemplos reales de cómo las grandes empresas usan estas herramientas para manejar volúmenes altos de tráfico y cambios frecuentes en sus aplicaciones.
#### Trabajo colaborativo
##### - En grupos, diseñar un flujo teórico que combine IaC (para crear recursos en la nube), despliegue de contenedores en Kubernetes y monitoreo con Prometheus/Grafana.
##### - Presentar el flujo en un diagrama que incluya cada paso desde el commit hasta la visualización de métricas en tiempo real.