<h1 align="center">El dolar hoy</h1>

Script para consultar el tipo de cambio del dolar, mediante el uso de la libreria Beautifulsoup4

* pip install beautifulsoup4

Consulta la tabla expuesta en la pagina:

* https://www.eldolar.info/es-MX/mexico/dia/hoy

Expone únicamente las fila donde se encuentra el Diario Oficial de la Federación.

Genera 2 archivos en la carpeta del Script:

* Historico_DOF.txt: Archiva el valor del dolar de manera incremental cuantas veces se ejecute el Script.
* DOF_Hoy.txt: Muestra únicamente el valor del dolar de acuerdo al DOF.

Notas:

    1.- Cuando la tabla del portal cambia, el valor almacenado puede no ser el del DOF. Se tiene que ajustar manualmente.
    2.- Es necesario crear una tarea para ejecutar el Script de manera automatica, si así se requiere.
    3.- Si se eliminan los archivos .txt, estos se vuelven a generar pero comenzara de cero el historico.
