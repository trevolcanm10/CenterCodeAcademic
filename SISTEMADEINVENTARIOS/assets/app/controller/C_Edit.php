<?php

require('../models/conection.php');

$id = $_GET['id'];

$con = new Conection();

$productos = $con->EditProduct($id);

require('../Views/EditV.php');