<?php

require('../models/conection.php');
$con = new Conection();

$productos = $con->Product($_POST['buscador']);
require('../Views/ProductV.php');