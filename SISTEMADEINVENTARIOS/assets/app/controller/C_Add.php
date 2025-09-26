<?php
require('../models/conection.php');


$Nombre = $_POST['Nombre'];
$Descripcion = $_POST['Descripcion'];
$Precio = $_POST['Precio'];
$con = new Conection();

$productos = $con->InsertProduct($Nombre,$Descripcion,$Precio);

header('Location:../Views/adminV.php');