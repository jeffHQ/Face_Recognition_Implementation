import tkinter as tk
from tkinter import ttk, filedialog
import face_recognition
import numpy as np
import heapq
from PIL import Image, ImageTk
from rtree import index
from scipy.spatial import KDTree
import time

# Variable global para el frame de la cuadrícula de imágenes
frame_grid = None

def obtener_vector(file_path):
    # Obtener el vector característico de la foto
    vector_foto = face_recognition.face_encodings(face_recognition.load_image_file(file_path))
    return vector_foto

def choose_file():
    # Función llamada al presionar el botón "Seleccionar Foto"
    file_path = filedialog.askopenfilename()
    start_time = time.time()
    process_file(file_path)
    end_time = time.time()
    print("Tiempo de ejecución: %.2f segundos" % (end_time - start_time))

def process_file(file_path):
    # Procesar el archivo seleccionado
    # Cargar los datos guardados
    datos_cargados = np.load("C:/Users/JEFF QUINTANA/Desktop/database/binarios/vectoresFinal.npy", allow_pickle=True).item()
    vector_foto1 = obtener_vector(file_path)
    vectores = np.array(datos_cargados["vectores"])
    nombres = np.array(datos_cargados["nombres"])
    cola_prioridad = []
    
    # Calcular la distancia entre el vector de la foto y los vectores cargados
    for i in range(len(vectores)):
        distancia = face_recognition.face_distance(vectores[i], vector_foto1)
        heapq.heappush(cola_prioridad, (nombres[i], distancia[0]))
    
    # Ordenar los resultados por distancia
    data = sorted(cola_prioridad, key=lambda x: x[1])

    # Agregar la ruta base a los nombres de las fotos en data
    ruta_base = "C:/Users/JEFF QUINTANA/Desktop/database/prueba1/"
    data_con_ruta = [(ruta_base + nombre, distancia) for nombre, distancia in data]

    # Crear una lista de rutas de las imágenes más similares
    rutas = [ruta for ruta, _ in data_con_ruta]

    # Mostrar vista previa de la imagen seleccionada
    image = Image.open(file_path)
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo

    # Mostrar las imágenes en una cuadrícula
    for i, ruta in enumerate(rutas[:8]):
        image = Image.open(ruta)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame_grid, image=photo)
        label.image = photo
        label.grid(row=i // 3, column=i % 3)

def choose_file_rtree():
    # Función llamada al presionar el botón "Seleccionar Foto" en la pestaña "KNN - Rtree"
    file_path = filedialog.askopenfilename()
    start_time = time.time()
    process_file_rtree(file_path)
    end_time = time.time()
    print("Tiempo de ejecución: %.2f segundos" % (end_time - start_time))

# Variable global para el índice Rtree
idxx = None
def process_file_rtree(file_path):
    # Procesar el archivo seleccionado en la pestaña "KNN - Rtree"
    global idxx
    # Cargar los datos guardados
    datos_cargados = np.load("C:/Users/JEFF QUINTANA/Desktop/database/binarios/vectoresFinal.npy", allow_pickle=True).item()
    vector_foto1 = face_recognition.face_encodings(face_recognition.load_image_file(file_path))[0]
    vectores = np.array(datos_cargados["vectores"])
    nombres = np.array(datos_cargados["nombres"])
    
    # Crear una lista de tuplas con nombres y vectores
    data = list(zip(nombres, vectores))
    
    # Mostrar vista previa de la imagen seleccionada
    image = Image.open(file_path)
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    image_label3.configure(image=photo)
    image_label3.image = photo

    if idxx is None:
        # Crear el índice Rtree si no existe
        p = index.Property()
        p.fill_factor = 0.7
        p.index_capacity = 100
        p.dimension = 128
        
        idxx = index.Index(properties=p)
        
        for i, (nombre, vector) in enumerate(data):
            # Insertar la tupla en el índice
            idxx.insert(i, tuple(vector), nombre)
    
    # Obtener los vecinos más cercanos usando el índice Rtree
    nearest_neighbors = list(idxx.nearest(tuple(vector_foto1), 8))
    ruta_base = "C:/Users/JEFF QUINTANA/Desktop/database/prueba1/"
    rutas = [ruta_base + data[nearest_neighbor][0] for nearest_neighbor in nearest_neighbors[:8]]

    for i, ruta in enumerate(rutas[:8]):
        image = Image.open(ruta)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label3 = tk.Label(frame_grid3, image=photo)
        label3.image = photo
        label3.grid(row=i // 3, column=i % 3)

def choose_file_kdtree():
    # Función llamada al presionar el botón "Seleccionar Foto" en la pestaña "KNN - HighD"
    file_path = filedialog.askopenfilename()
    start_time = time.time()
    process_file_kdtree(file_path)
    end_time = time.time()
    print("Tiempo de ejecución: %.2f segundos" % (end_time - start_time))

def process_file_kdtree(file_path):
    # Procesar el archivo seleccionado en la pestaña "KNN - HighD"
    # Cargar los datos guardados
    datos_cargados = np.load("C:/Users/JEFF QUINTANA/Desktop/database/binarios/vectoresFinal.npy", allow_pickle=True).item()
    vector_foto1 = face_recognition.face_encodings(face_recognition.load_image_file(file_path))[0]
    vectores = np.array(datos_cargados["vectores"])
    nombres = np.array(datos_cargados["nombres"])

    # Mostrar vista previa de la imagen seleccionada
    image = Image.open(file_path)
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    image_label4.configure(image=photo)
    image_label4.image = photo

    # Crear las tuplas (nombre, vector) a partir de los datos
    tuplas = list(zip(nombres, vectores))

    # Crear el KDTree con las tuplas
    kdtree = KDTree(vectores)
    distancias, indices = kdtree.query(vector_foto1, k=8)

    # Obtener las tuplas (nombre, vector) correspondientes a los índices obtenidos
    tuplas_similares = [tuplas[i] for i in indices]

    # Imprimir los nombres similares encontrados
    nombres_similares = [nombre for nombre, _ in tuplas_similares]
    
    ruta_base = "C:/Users/JEFF QUINTANA/Desktop/database/prueba1/"
    rutas = [ruta_base + nombre for nombre in nombres_similares]

    for i, ruta in enumerate(rutas[:8]):
        image = Image.open(ruta)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label3 = tk.Label(frame_grid4, image=photo)
        label3.image = photo
        label3.grid(row=i // 3, column=i % 3)

# Crear la ventana principal
root = tk.Tk()

# Configurar la ventana
root.title("Aplicación con Menús")

# Crear un notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear las pestañas
tab1 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

# Agregar las pestañas al notebook
notebook.add(tab1, text="Búsqueda KNN")
notebook.add(tab3, text="KNN - Rtree")
notebook.add(tab4, text="KNN - HighD")

# Agregar contenido a cada pestaña

# Pestaña "Búsqueda KNN"
button1 = tk.Button(tab1, text="Seleccionar Foto", command=choose_file)
button1.pack(pady=20)

# Agregar un Label para mostrar la vista previa de la imagen
image_label = tk.Label(tab1)
image_label.pack()

# Crear un frame para la cuadrícula de imágenes
frame_grid = tk.Frame(tab1)
frame_grid.pack()

# Pestaña "KNN - Rtree"
button3 = tk.Button(tab3, text="Seleccionar Foto", command=choose_file_rtree)
button3.pack(pady=20)

# Agregar un Label para mostrar la vista previa de la imagen
image_label3 = tk.Label(tab3)
image_label3.pack()

# Crear un frame para la cuadrícula de imágenes
frame_grid3 = tk.Frame(tab3)
frame_grid3.pack()

# Pestaña "KNN - HighD"
button4 = tk.Button(tab4, text="Seleccionar Foto", command=choose_file_kdtree)
button4.pack(pady=20)

# Agregar un Label para mostrar la vista previa de la imagen
image_label4 = tk.Label(tab4)
image_label4.pack()

# Crear un frame para la cuadrícula de imágenes
frame_grid4 = tk.Frame(tab4)
frame_grid4.pack()

# Empacar el notebook
notebook.pack(expand=True, fill=tk.BOTH)

# Iniciar el bucle principal de la aplicación
root.mainloop()
