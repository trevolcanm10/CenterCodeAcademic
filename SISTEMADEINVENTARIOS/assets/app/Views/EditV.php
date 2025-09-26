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
                <ul>
                    <li><a href=""></a>Inicio</li>
                    <li><a href=""></a>Inventario</li>
                    <li><a href=""></a>Añadir producto</li>
                </ul>
            </nav>

            <div class="table">
                <table>
                    <thead>
                        <tr>
                            <td>Id</td>
                            <td>Nombre</td>
                            <td>Descripcion</td>
                            <td>Precio</td>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        foreach($productos as $pro){
                        ?>
                        <form action="../controller/C_Update.php" method="post">
                            <tr>
                                <td><input type="hidden" value="<?php echo $pro['id_productos']?>" name="id"></td>
                                <td><input type="text" value="<?php echo $pro['Nombre']?>" name="Nombre"></td>
                                <td><textarea value="<?php echo $pro['Descripcion']?>" name="Descripcion" cols="20" rows="5" ></textarea></td>
                                <td><input type="text" value="<?php echo $pro['Precio']?>" name="Precio"></td>
                                <td><button class="actualizar">Actualizar producto</button></td>
                            </tr>

                        </form>
                        <?php }?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>