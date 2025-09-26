<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
require('../models/conection.php');
$con = new Conection();

$productos = $con->Product($_POST['buscador']);
require('../Views/ProductU.php');