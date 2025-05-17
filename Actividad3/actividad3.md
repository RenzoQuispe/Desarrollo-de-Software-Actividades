## **Actividad 3: Computación en la nube**

##### A. Cuestionario

1. **Motivaciones para la nube**  
   - (a) ¿Qué problemas o limitaciones existían antes del surgimiento de la computación en la nube y cómo los solucionó la centralización de servidores en data centers?
    Antes de la computación en la nube las empresas tenian que gastar mucho de dinero en hardware,  y software ademas  de su mantenimiento diario, esto hacia dificil la escalabilidad, con la centralización de servidores en data centers las empresas ahora pueden alquilar recursos y ya no tienen que encargar del hardware, software y su mantenimiento, ni su escalabilidad si es necesario.

<!--   - (b) ¿Por qué se habla de “The Power Wall” y cómo influyó la aparición de procesadores multi-core en la evolución hacia la nube?-->

2. **Clusters y load balancing**  
   - (a) Explica cómo la necesidad de atender grandes volúmenes de tráfico en sitios web condujo a la adopción de clústeres y balanceadores de carga. 
   Un solo servidor no soporta que una pagina web tenga cientos de miles o millones de visitas, para resolver este problema se usa multiples servidores trabajando al mismo tiempo(clusters de servidores). Ademas, para que haya una distribucion correcta del trafico se usa load balancing para llevar parte del trafico a un servidor y las otras partes a otros servidores.
   - (b) Describe un ejemplo práctico de cómo un desarrollador de software puede beneficiarse del uso de load balancers para una aplicación web. 
   Unos desarrolladores puede implementar varias funcionalidades y con load balancig puede distribuir funcionalidad entre servidores del cluster, de tal manera se trabaja ordenadamente y no hay dependencia de funcionamiente entre implementaciones tras desplagar la aplicacion.  


3. **Elastic computing**  
   - (a) Define con tus propias palabras el concepto de Elastic Computing.
   A la capacidad de adaptcion que tienen algunos software a las necesidades de los desarrolladores  
   - (b) ¿Por qué la virtualización es una pieza clave para la elasticidad en la nube?  
   Porque permite crear recursos virtuales sobre hardware de las empresas cloud, de tal manera que hace sencillo su acceso y configuracion a desarrolladores de todo el mundo.
   - (c) Menciona un escenario donde, desde la perspectiva de desarrollo, sería muy difícil escalar la infraestructura sin un entorno elástico.
   Aplicaciones de redes sociales en crecimiento, ya que necesita que el recursos suficientes para soportar la cantidad de usuarios en aumento y las nuevas implementaciones de dicha red social

4. **Modelos de servicio (IaaS, PaaS, SaaS, DaaS)**
  
   - (a) Diferencia cada uno de estos modelos. ¿En qué casos un desarrollador optaría por PaaS en lugar de IaaS?  
   - (b) Enumera tres ejemplos concretos de proveedores o herramientas que correspondan a cada tipo de servicio.
      IaaS
       - Amazon EC2
       - Azure virtual machines
       - Google compute engine
      Paas
       - AWS Fargate 
       - Render
       - Heroku
      SaaS
       - GoogleDrive
       - Word
       - zoom
5. **Tipos de nubes (Pública, Privada, Híbrida, Multi-Cloud)**  
   - (a) ¿Cuáles son las ventajas de implementar una nube privada para una organización grande?
      Una organizacion grande necesita una nube mas personalizada y proteger sus datos, entonces una nube privada en la cual internamente es administrado por personal siguiendo las necesidades de la organizacion es mas adecuado.
   - (b) ¿Por qué una empresa podría verse afectada por el “provider lock-in”?  
      porque queda totalmente dependiente de un solo proveedor de nube, tener mas proveedores da mas libertad. 

Presentación PPT:
[Ver ppt de la exposicion](DS_Actividad3.pdf)