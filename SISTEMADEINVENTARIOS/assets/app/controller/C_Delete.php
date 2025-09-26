<?php
require('../models/conection.php');

$id = $_GET['id'];

$con = new Conection();

$productos = $con->DeleteProduct($id);

header("Location:../Views/adminV.php");