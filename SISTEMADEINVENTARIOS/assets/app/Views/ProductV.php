<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Producto</title>
</head>
<body>
    <div class="cont">
        <div class="subcont">
            <nav>
                <ul>
                    <li><a href="../index.php">Inicio</a></li>
                    <li><a href="Inventario.php"></a>Inventario</li>
                    <li><a href=""></a>Añadir Producto</li>
                </ul>
            </nav>

            <div class="table">
                <table>
                    <thead>
                        <tr>
                            <td>Nombre</td>
                            <td>Descripcion</td>
                            <td>Precio</td>
                            <td>Editar</td>
                            <td>ELiminar</td>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        foreach($productos as $pro){
                        ?>
                        <tr>
                            <td><?php echo $pro['Nombre']?></td>
                            <td><?php echo $pro['Descripcion']?></td>
                            <td><?php echo $pro['Precio']?></td>
                            <td><a href="../controller/C_Edit.php?id=<?php echo $pro["id_productos"];?>">Editar producto</a></td>
                            <td><a href="../controller/C_Delete.php?id=<?php echo $pro["id_productos"];?>">Eliminar producto</a></td>
                        </tr>
                        <?php } ?>        
                    </tbody>
                </table>

            </div>
        </div>
    </div>
</body>
</html>