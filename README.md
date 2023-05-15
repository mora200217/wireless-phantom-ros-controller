# Laboratorio #4 Robótica
Cuarto laboratorio de la asignatura de Robótica de la Universidad Nacional de Colombia 2023-i.


**Integrantes**: 
* Nelson David Ramírez Marín
* Andrés Zuleta 
* Andrés Morales Martínez


## Planteamiento del Problema 
Se busca aplicar cinemática directa en el Phantom X Pincher para obtener una configuración del Robot a partir de sus coordenadas articulares.
 
## Desarrollo 


Se hizo en primer lugar la asignacion de los sistemas de coordenadas para el diagrama del robot, lo que resulto de la siguiente manera

<p align="center">
<img margin="auto" src="https://github.com/mora200217/labrob-1/blob/master/design/sketch.jpeg" width="60%"/> 
</p> 

Y de acuerdo a lo anterior se hizo la tabla Denavit-Hartenberg, que se presenta a continuacion

<p align="center">
<img margin="auto" src="https://github.com/mora200217/labrob-1/blob/master/design/sketch.jpeg" width="60%"/> 
</p> 

Seguidamente, se creo toda la representacion del robot usando la libreria de Peter corke, para 5 posiciones asignadas dando las siguientes representaciones

Q1(Home)

<p align="center">
<img margin="auto" src="https://github.com/mora200217/labrob-1/blob/master/design/sketch.jpeg" width="60%"/> 
</p> 

Q2

<p align="center">
<img margin="auto" src="https://github.com/mora200217/labrob-1/blob/master/design/sketch.jpeg" width="60%"/> 
</p> 

Q3

<p align="center">
<img margin="auto" src="https://github.com/mora200217/labrob-1/blob/master/design/sketch.jpeg" width="60%"/> 
</p> 

Q4

<p align="center">
<img margin="auto" src="https://github.com/mora200217/labrob-1/blob/master/design/sketch.jpeg" width="60%"/> 
</p> 

Q5


<p align="center">
<img margin="auto" src="https://github.com/mora200217/labrob-1/blob/master/design/sketch.jpeg" width="60%"/> 
</p> 

Seguidamente se desarrollo en matlab la interfaz de usuario asi como la comunicacion entre Matlab y el PhantomX por medio de Ros en donde se creo una funcion 





Y finalmente se acabo de implementar la interfaz de usuario en un modulo de matlab llamado appdesigner que estaba comunicada con matlab en donde se cumplieron los requerimientos:





## Conclusiones

1. Saber la sintaxis que se usan en diferentes lenguajes de programacion, como Python o C++, da una vision y recursividad mas amplia a la hora de elegir en donde se puede programar un codigo.
2. El framework ROS con su metodo de conectar nodos ayuda a realizar diversas operaciones de una manera rápida y sencilla.
3. Los servicios son una herramienta o método bastante util para usar subrutinas de manera mas eficiente.
