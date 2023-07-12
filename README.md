# Aplicación de Búsqueda KNN en Imágenes

Esta es una aplicación de búsqueda KNN (K-Nearest Neighbors) que utiliza la biblioteca `face_recognition` para calcular la similitud entre imágenes faciales. La aplicación muestra una imagen de entrada y busca las imágenes más similares en una base de datos de imágenes faciales.

## Requisitos

Para ejecutar la aplicación, se requiere tener instaladas las siguientes bibliotecas de Python:

- `tkinter`: Para la interfaz gráfica de usuario.
- `Pillow`: Para el manejo de imágenes.
- `face_recognition`: Para el reconocimiento facial.
- `numpy`: Para el manejo de matrices y vectores.
- `heapq`: Para la creación de una cola de prioridad.
- `rtree`: Para la indexación de datos utilizando el algoritmo R-tree.
- `scipy`: Para el manejo de estructuras de datos espaciales, como KDTree.
  
Puedes instalar estas bibliotecas utilizando el administrador de paquetes `pip`. Por ejemplo:

pip install tkinter
pip install Pillow
pip install face_recognition
pip install numpy
pip install heapq
pip install Rtree
pip install scipy

## Uso

1. Ejecuta el archivo `app.py` para iniciar la aplicación.
2. Aparecerá una ventana con pestañas.
3. En la pestaña "Búsqueda KNN", presiona el botón "Seleccionar Foto" para elegir una imagen.
4. La aplicación calculará la similitud entre la imagen seleccionada y las imágenes de la base de datos.
5. Se mostrará una vista previa de la imagen seleccionada y las imágenes más similares en una cuadrícula.
6. Puedes cambiar a las pestañas "KNN - Rtree" y "KNN - HighD" para probar otros métodos de búsqueda KNN utilizando R-tree y KDTree, respectivamente.

## Estructura del Código

El código se organiza de la siguiente manera:

- `app.py`: El archivo principal que contiene la interfaz gráfica de usuario y la lógica de la aplicación.

El archivo `app.py` contiene las siguientes funciones principales:

### `obtener_vector(file_path)`

Esta función recibe la ruta de un archivo de imagen y utiliza la biblioteca `face_recognition` para extraer el vector característico de la imagen facial. Devuelve el vector característico.

### `choose_file()`

Esta función se ejecuta cuando se presiona el botón "Seleccionar Foto" en la pestaña "Búsqueda KNN". Abre un cuadro de diálogo para seleccionar una imagen y luego llama a la función `process_file()` para procesar la imagen seleccionada.

### `process_file(file_path)`

Esta función carga los datos de vectores característicos y nombres de la base de datos. Luego, calcula la similitud entre la imagen seleccionada y las imágenes de la base de datos utilizando la distancia euclidiana en el espacio de características. Ordena los resultados por similitud y muestra las imágenes más similares en una cuadrícula junto con la vista previa de la imagen seleccionada.

### `choose_file_rtree()`

Esta función se ejecuta cuando se presiona el botón "Seleccionar Foto" en la pestaña "KNN - Rtree". Abre un cuadro de diálogo para seleccionar una imagen y luego llama a la función `process_file_rtree()` para procesar la imagen seleccionada.

### `process_file_rtree(file_path)`

Esta función carga los datos de vectores característicos y nombres de la base de datos. Luego, crea un índice R-tree utilizando la biblioteca `rtree` si el índice no se ha creado previamente. Utiliza el índice para encontrar los vecinos más cercanos de la imagen seleccionada y muestra las imágenes correspondientes en una cuadrícula junto con la vista previa de la imagen seleccionada.

### `choose_file_kdtree()`

Esta función se ejecuta cuando se presiona el botón "Seleccionar Foto" en la pestaña "KNN - HighD". Abre un cuadro de diálogo para seleccionar una imagen y luego llama a la función `process_file_kdtree()` para procesar la imagen seleccionada.

### `process_file_kdtree(file_path)`

Esta función carga los datos de vectores característicos y nombres de la base de datos. Luego, crea un KDTree utilizando la biblioteca `scipy` y utiliza el árbol para encontrar los vecinos más cercanos de la imagen seleccionada. Muestra las imágenes correspondientes en una cuadrícula junto con la vista previa de la imagen seleccionada.

## Contribución

Si deseas contribuir a este proyecto, puedes hacerlo de las siguientes maneras:

- Reportando problemas o errores.
- Sugiriendo nuevas características o mejoras.
- Enviando solicitudes de extracción para corregir problemas o agregar funcionalidades.

¡Espero que esta aplicación sea útil y te diviertas explorando las imágenes similares!
