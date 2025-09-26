<?php
require('../models/conection.php');


$id = $_POST['id'];
$Nombre = $_POST['Nombre'];
$Descripcion = $_POST['Descripcion'];
$Precio = $_POST['Precio'];


$con = new Conection();

$productos = $con->UpdateProduct($id,$Nombre,$Descripcion,$Precio);
header("Location:../index.php");