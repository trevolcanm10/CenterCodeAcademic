<?php
include('models/conection.php');
//Extraccion de datos del formulario de registro
$nombre = $_POST['Name'];
$apellido = $_POST['Apellido'];
$full_name = $nombre . ' ' . $apellido;
$email = $_POST['Email'];
$contrasena = $_POST['Contrasena'];
$role = 'user';

//Instancia de la conexión
$con = new Conection();

//Lamada a la función
$validacion=$con->registerUser($full_name,$email,$contrasena,$role);

if($validacion != false){  
        header('Location:Views/LoginV.php');
    }else{
     echo "Error inesperado,no se pudieron guardar los datos";
    }
