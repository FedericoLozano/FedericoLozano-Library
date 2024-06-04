# Proyecto Web Django con Patrón MVT

## Instrucciones para probar la funcionalidad

1. Clonar el repositorio y navegar al directorio del proyecto.
2. Instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecutar las migraciones:
    ```bash
    python manage.py migrate
    ```
4. Iniciar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
5. Acceder a las siguientes URLs para interactuar con la aplicación:

    - Crear un autor: [http://localhost:8000/crear_autor/](http://localhost:8000/crear_autor/)
    - Crear un libro: [http://localhost:8000/crear_libro/](http://localhost:8000/crear_libro/)
    - Crear una editorial: [http://localhost:8000/crear_editorial/](http://localhost:8000/crear_editorial/)
    - Buscar un libro: [http://localhost:8000/buscar_libro/](http://localhost:8000/buscar_libro/)

## Funcionalidades

- **Herencia de HTML**: Las plantillas utilizan herencia de HTML a partir de `base.html`.
- **Modelos**: Tres modelos (`Autor`, `Libro`, `Editorial`) definidos en `mi_app/models.py`.
- **Formularios de inserción**: Formularios para insertar datos en los modelos, definidos en `mi_app/forms.py` y manejados en `mi_app/views.py`.
- **Formulario de búsqueda**: Formulario para buscar libros en la base de datos, definido en `mi_app/views.py`.

