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

Y se obtuvieron las siguientes poses reales:

Q1(Home)

<p align="center">
<img margin="auto" src= src/px_robot/matlab/HMI/Pose_1_real.PNG width="60%"/> 
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



Y finalmente se acabo de implementar la interfaz de usuario en un modulo de matlab llamado appdesigner que estaba comunicada con matlab en donde se cumplieron los requerimientos:

1. Nombres, logos y datos de los integrantes del grupo.
2. Imagen perspectiva de la posici´on actual del manipulador con la ultima posici´on enviada.
3. Opcion para seleccionar 1 de las 5 poses y enviarlas al manipulador.
4. Valores de los valores articulares reales de cada motor.
5. Imagen perspectiva de la posici´on actual del manipulador con los valores articulares.

Y se denota como resultado que las poses reales del manipulador corresponden a las halladas por el Toolbox de Peter Corke

Video del brazo alcanzando cada posicion solicitada

*

Vıdeo demostracion de uso de la interfase de usuario

*



## Conclusiones

1. Definir de manera correcta la tabla de Denavit-Hartenberg hace que tengan correlacion lo que se hace el robot de forma real con lo que se simula.
2. Matlab ofrece una facilidad para crear una interfaz interactiva en donde puedan ser usadas de manera mas intuitiva cualquier scrpit que se cree previamente.
3. Los servicios son una herramienta o método bastante util para usar subrutinas de manera mas eficiente.
