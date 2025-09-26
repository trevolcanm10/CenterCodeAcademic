<?php
// Inicia la sesión (para poder destruirla)
session_start();

// Elimina todas las variables de sesión
session_unset();

// Destruye la sesión
session_destroy();

// Redirige al login (o página principal)
header("Location: Views/LoginV.php");
exit;
?>
