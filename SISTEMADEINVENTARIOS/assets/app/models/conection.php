<?php

class Conection{
    //Conexion privada
    private $conect;

    //Constructor que guarda la conexion
    public function __construct(){
        //Variable de acceso y se crea la conexion
        $this ->conect = new mysqli('localhost','root','','inventario');
    }

    //Gestion de usuarios
    public function loginUser($email,$password){
        $validacion = $this->conect->query("SELECT * FROM usuarios WHERE email = '$email' AND password = '$password'");

        if($validacion->num_rows !=1){
            return false; //Usuario o contraseña incorrectos
        }else{
            return $validacion->fetch_assoc();
        }
    }

    //Registro de Usuarios
    public function registerUser($full_name,$email,$password,$role='user'){
        $registro = "INSERT INTO usuarios(full_name,email,password,role) VALUES ('$full_name','$email','$password','$role')";
        return $this->conect->query($registro);
    }
    //Obtención de los productos generales
    public function getProducts(){
        //Peticion de los datos en la base de datos
        $peticion = $this->conect->query('SELECT * FROM productos');
        $datos = [];
        $i = 0;

        //Ejecutamos el ciclo para almacenar los datos obtenidos desde la base de datos
        while($fila = $peticion->fetch_assoc()){
            $datos[$i] = $fila;
            $i++;
        }
        //Retornamos los registros obtenidos de la base de datos
        return $datos;
    }

    // Solicitud de productos generales
    public function Product($Nombre){
        //Consulta a la base de datos con la coincidencia del nombre
        //Si coincide el nombre me regresará todo el contenido
        $peticion = $this->conect->query("SELECT * FROM productos WHERE Nombre = '$Nombre'");
        $datos=[];
        $i=0;
        
        //Recorremos todos los datos y los guardamos en un arreglo seguro
        while($fila = $peticion->fetch_assoc()){
            $datos[$i] = $fila;
            $i++;
        }
        return $datos;
    }

    public function EditProduct($id){
        //Se realiza la peticion a la base de datos
        //Comparacion del id_producos, si encuentra el id entonces regresará el registro obtenido
        $peticion = $this->conect->query("SELECT * FROM productos WHERE id_productos = '$id'");
        $datos=[];
        $i=0;

        while($fila = $peticion->fetch_assoc()){
            $datos[$i] = $fila;
            $i++;
        }
        return $datos;
    }

    //Funcion de actualizacion de datos
    public function UpdateProduct($id,$Nombre,$Descripcion,$Precio){
        $peticion = $this->conect->query("UPDATE productos SET Nombre = '$Nombre', Descripcion='$Descripcion',Precio='$Precio' WHERE id_productos='$id'");
    }

    //Funcion insertar productos

    public function InsertProduct($Nombre,$Descripcion,$Precio){
        $peticion = $this->conect->query("INSERT INTO productos(Nombre,Descripcion,Precio)VALUES('$Nombre','$Descripcion','$Precio')");
    }

    public function DeleteProduct($id){
        $peticion = $this->conect->query("DELETE FROM productos WHERE id_productos ='$id'");
    }
}