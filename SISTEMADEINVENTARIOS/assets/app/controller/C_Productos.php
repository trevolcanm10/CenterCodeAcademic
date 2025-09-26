<?php
//Lamamos la conexion
require('models/conection.php');

//Creacion del objeto para acceder a la clase "Conection"
$con = new Conection();
//Creacion de la variable productos para guardar los datos obtenidos de la funcion "getProducts"
$productos = $con->getProducts();
//Mandamos los datos a la vista
require('Views/ProductosV.php');