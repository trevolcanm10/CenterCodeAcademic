<?php
    //Inicia la sesion
    session_start();
    require('models/conection.php');
    //Obtenemos datos del formulario
    $Email = $_POST['Email'];
    $Contrasena = $_POST['Contrasena'];
    //Instancia de conexion
    $con = new Conection();
    //Llamada de la funcion del login
    $user = $con->loginUser($Email,$Contrasena);

    if($user){
        //Guardamos los datos de la sesión
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['full_name'];
        $_SESSION['role'] = $user['role'];
        //Redireccion de acuerdo al rol
        if($user['role']==='admin'){
            header('Location:Views/adminV.php');//Panel administrador
        }else{
            header('Location:Views/usuarioV.php');//Panel del usuario
        }
        exit;
    }else{
        echo "<h1>Usuario y contraseña son incorrectos</h1>";
    }
?>