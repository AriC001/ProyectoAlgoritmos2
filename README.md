# Proyecto Algoritmos y Estructura de datos 2


## **Seguimiento de navegación.**
### Descripción:
Una flota naviera está compuesta por varias embarcaciones y cada mes se recibe un informe de configuración (posición en el plano) de los barcos que conforman la flota. Dicho informe contiene dos componentes fundamentales:
 - Fecha
 - Información sobre los barcos

La **Información sobre los barcos** indica por cada embarcación 4 elementos fundamentales:

1.  Nombre de Embarcación
2.  Posición en X
3.  Posición en Y
4.  Dirección en la que se dirige

El proyecto a realizar se constituye de la siguiente manera:


### Indicaciones

Dada la configuración inicial de la flota y sabiendo que cada día que pasa, un barco avanza 1 valor en su posición de acuerdo a la dirección que lleva. Implementar las siguientes funcionalidades:

1.  Dado un día, devolver que posición tiene un barco en particular.
2.  Dado un día, devolver cuales son los dos barcos más cercanos entre sí (distancia euclidiana). Si hay más de un barco con la misma distancia indicar cada uno de estos.
3.  Conocer si dentro del mes existe un día de riesgo de colisión (dos o más barcos a distancia 1) e indicar la fecha y el nombre de los barcos involucrados en los riesgos de colisión.
4.  (Opcional) Brindar la funcionalidad de dado un día del mes mostrar un ranking de los 10 barcos más cercanos entre sí.

### Requerimientos:

Para lograr la navegación de los elementos es necesario la creación de la flota y para ello se utilizará el siguiente comando: `python sistema_navegacion.py -create <local_path>`
    
Una vez cargados los elementos que componen la flota en la aplicación, permitir realizar consultas sobre las embarcaciones y su interacción entre sí.
    
-   Para la generación de consultas se utilizará el siguiente comando:
    1.  `python navigation_system.py -search <date> <nombre_embarcacion>` Devuelve la posición (X, Y) dado una fecha (<date>) y un nombre de embarcación (<nombre_embarcacion>)
    2.  `python navigation_system.py -closer` Devuelve el nombre de las dos embarcaciones más cercanas entre sí (menor distancia euclidiana).
    3.  `python navigation_system.py -collision` Devuelve el día del mes (date) y los barcos que están involucrados en un riesgo de colisión. En caso que no exista ningún riesgo de colisión en el mes se devuelve False
    4.  `python navigation_system.py -collision_ranking <date>` Devuelve un ranking (10) de las embarcaciones más cercanas entre sí.

Además se deberá garantizar la persistencia de los datos. Esto significa que la estructura que compone el índice de los elementos de la flota tiene que ser recuperable a través de consultas en todo momento.