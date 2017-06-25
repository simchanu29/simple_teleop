# ros_teleop
Package ros pour la téléopération. Peut publier des messages Twist, Wrench ou Float32 suivant les besoins.

Ce package a été designé pour la commande de multiple actionneurs sur un robot allant d'une commande en force, en vitesse ou encore en position.

### Installation
Déplacez vous au sein d'un workspace ROS et clonez ce repository
`git clone https://github.com/simchanu29/ros_teleop`
Déplacez vous à la racine du workspace
`source devel/setup.bash`

### Test
Pour tester le package après installation
`roslaunch ros_teleop teleop.launch`

### Configuration
L'ensemble du mapping des touches se fait via un fichier de config yaml dans le dossier launcher
Le principe est le suivant : 

1. On définit les topics qui vont être écouté. Ces topics peuvent être de différents types exprimés au dessus. On peut alors spécifier les paramètres de ces topics. 

Par exemple, pour commander le robot turtle avec un message twist, on pourrait créer le topic suivant : 
``` 
twist_turtle:
  type: twist
  range_lin: 20.0
  range_ang: 20.0
  precision : 100.0
```

De maniere générale, range c'est l'échelle par laquelle on multiplie la commande qui est comprise dans [-1,1]. La précision c'est le facteur par lequel on divise la commande issue de la touche (1 ou -1 habituellement) lors de l'incrémentation de la commande du message. Pour une meilleure compréhension, je conseille de regarder les fichiers fill_xxx.py.

2. On définit les touches associées au topic

Par exemple pour avancer ou reculer : 
```
'a':
  topic: 'twist_turtle'
  value: [1,0,0]

'b':
  topic: 'twist_turtle'
  value: [-1,0,0]
```
