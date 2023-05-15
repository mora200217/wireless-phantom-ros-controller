# Laboratorio #4 Robótica
Cuarto laboratorio de la asignatura de Robótica de la Universidad Nacional de Colombia 2023-i.


**Integrantes**: 
* Nelson David Ramírez Marín
* Andrés Zuleta 
* Andrés Morales Martínez


## Planteamiento del Problema 
Se busca aplicar cinemática directa en el Phantom X Pincher para obtener una configuración del Robot a partir de sus coordenadas articulares.
 
## Desarrollo 


Se emplea el uso de publishers y de servicios para publicar al tópico `/turtle1/cmd_vel` o llamar los servicios `turtlesim/TeleportRelative` y turtlesim/TeleportAbsolute`

### Estructura del proyecto 

Todo el proyecto está dentro del catkin workspace `turtle_patch`. El paquete central se llama `turtle_control`. Contiene un `.launch` y un nodo ejecutable. 

## Guía de uso
Agrega el pkg a source. 
```
source devel/setup.bash
```

Para correr el proyecto, basta con ejecutar el `example.launch`

```
roslaunch turtle_control example.launch
```

Esto llamará el `tustlesim_node` para vizualizar la tortuga, y el nodo `turtle_teleop_key2` para la GUI de control de movimiento. 

<p align="center">
 <img width="70%" src="https://github.com/mora200217/labrob-3/blob/master/assets/example_launch.png"/>
 </p> 


https://user-images.githubusercontent.com/24869683/235335727-a4c7a3c0-7fd8-4062-9133-6eebed02b2cf.mp4




## Conclusiones

1. Saber la sintaxis que se usan en diferentes lenguajes de programacion, como Python o C++, da una vision y recursividad mas amplia a la hora de elegir en donde se puede programar un codigo.
2. El framework ROS con su metodo de conectar nodos ayuda a realizar diversas operaciones de una manera rápida y sencilla.
3. Los servicios son una herramienta o método bastante util para usar subrutinas de manera mas eficiente.
