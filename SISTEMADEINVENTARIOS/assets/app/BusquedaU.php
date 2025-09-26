<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="cont">
        <div class="subcont">
            <nav>
                <li><a href="Views/usuarioV.php">Inicio</a></li>
                <li><a href="InventarioU.php">Inventario</a></li>
            </nav>

            <div class="header">
                <header>
                    <div class="sombra">
                        <div class="title">
                            <h1>Busca el producto que quieres editar</h1>
                        </div>

                        <div class="buscador">
                            <form action="controller/C_productoU.php" method="post">
                                <input type="text" name="buscador">
                                <button class="boton">Buscar productos</button>
                            </form>
                        </div>
                    </div>
                </header>
            </div>
        </div>
    </div>
</body>
</html>