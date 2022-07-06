# Entrega de Proyecto Final de Python - Comisión 36945

# Ante la falta de respuesta de los compañeros asignados, el tutor a cargo me autorizó a desarrollar a solas el proyecto final.

# Descarga

    Git Repository: https://github.com/Gonedar/Python_PF.git
    Video presentación: https://drive.google.com/file/d/1jkTuoTOtZdoX5S9eChPjsxnin4YJBG00/view?usp=sharing

# Pasos

    Se crea proyecto
    Se agrega archivo .gitignore
    Se crea carpeta "templates" y archivo index.html
    Se crea app "products" y se crean tres clases en "models" (Tortas, PetitFours y Box)
    Se crea super usuario "adminuser" con la contraseña "admin123" y mail admin@admin.com
    Se agregan urls necesarias en urls.py de la app
    Se crean templates para cada clase generada y se realizan las herencias HTML necesarias desde base.html, generando templates para cargar, editar y eliminar el producto "tortas". 

    En el link http://127.0.0.1:8000/products/cargar-torta/ se puede acceder a un formulario de carga de productos.
    Se crea template de búsqueda de productos, relacionándolo con la función "buscar_producto_view" en views.py, que le da funcionalidad al campo de búsqueda en la navbar del proyecto.
Se crea app "users" y el modelo "User_profile" para permitirá registro de usuario, loggeos y diferentes permisos al validar el acceso adecuado, así como la edición de dichos usuarios y los productos creados. 
Se incorpora la posibilidad de cargar imagenes de perfil para los usuarios y para los productos.
Se agregan las templates requeridas "contacto" y "about".
