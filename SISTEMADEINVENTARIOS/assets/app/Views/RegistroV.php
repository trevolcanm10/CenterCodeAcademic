<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de datos</title>
</head>
<body>
    <div class="contenedor">
        <div class="subcontenedor">
            <nav class="menu">
                <h2 class="academy">Academy</h2>
            </nav>
            <header>
                <div class="sombra1">
                    <h1>Has tu cuenta y disfruta de todo el contenido que ofrecemos</h1>
                    <h3 class="sublogo">Es facil y rapido</h3>
                </div>
                <div class="formulario">
                    <form action="../Registro.php" method="post">
                        <h2 class="titulo_formulario">Registro</h2>
                        <br>
                        <input type="text" name="Name" placeholder="Ingrese su primer Nombre" class="P_Nombre" required>
                        <input type="text" name="Apellido" placeholder="Ingrese su Apellido" class="Apellido" required>
                        <br>
                        <input type="email" name="Email" placeholder="Ingrese su correo electronico" class="P_Nombre" required>
                        <br>
                        <input type="text" name="Contrasena" placeholder="Ingrese su contraseña" class="contra" required>
                        <button class="finalizar">Registrarse</button>
                    </form>   
                </div>
                <div class="banner">
                    <div class="sombra2">
                        <h2 class="alucivo">Aprende con la mejor academia de cursos</h2>
                    </div>
                </div>
            </header>
        </div>
    </div>
</body>
</html>