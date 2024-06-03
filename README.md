# Kit Creation API Test Automation. Urban_Grocers 🛠️🔄

## Descripción 📖
Este proyecto automatiza las pruebas para la creación de kits de productos usando una lista de comprobación definida. Se envían solicitudes a una API y se verifican los resultados esperados.

## Archivos 📁
- `configuration.py`: Contiene las configuraciones de la URL base y los endpoints.
- `data.py`: Proporciona los cuerpos de las solicitudes POST.
- `sender_stand_request.py`: Maneja el envío de las solicitudes a la API.
- `create_kit_name_kit_test.py`: Contiene las pruebas automatizadas utilizando pytest.
- `README.md`: Descripción del proyecto.
- `.gitignore`: Archivos y carpetas a ignorar por git.

## Ejecución de Pruebas 🔎
1. Clona el repositorio.
2. Instala las dependencias necesarias.
3. Ejecuta las pruebas con el comando `pytest create_kit_name_kit_test.py`.

## Dependencias 📌
- `requests`
- `pytest`
