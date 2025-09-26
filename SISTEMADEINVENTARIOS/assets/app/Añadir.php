<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Añadir producto</title>
</head>
<body>
    <div class="cont">
        <div class="subcont">
            <nav>
                <ul>
                    <li><a href="Views/adminV.php">Inicio</a></li>
                    <li><a href="Inventario.php">Inventario</a></li>
                </ul>
            </nav>

            <div class="formulario">
                <form action="controller/C_Add.php" method="post">
                    <h2 class="title">Ingresa los datos del producto</h2>
                    <input type="text" class="name" placeholder="Añade el nombre del producto" name="Nombre">
                    <textarea class="descripcion" name="Descripcion" placeholder="Añade la descripcion de tu producto" cols="30" rows="5"></textarea>
                    <input type="text" class="precio" placeholder="Añade el precio" name=Precio>
                    <button class="enviar-datos">Añadir producto al inventario</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>