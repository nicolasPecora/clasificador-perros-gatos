from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Cargar el modelo
model = load_model('model/perros-gatos-cnn-ad.h5')

# Crear una carpeta para almacenar las imágenes subidas
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    try:
        # Guardar la imagen cargada
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Cargar imagen y procesarla
        img = Image.open(filepath).convert('L')  # Convertir a escala de grises
        img = img.resize((100, 100))  # Tamaño que espera el modelo
        img_array = np.array(img) / 255.0  # Normalizar
        img_array = np.expand_dims(img_array, axis=-1)  # Añadir canal (100,100,1)
        img_array = np.expand_dims(img_array, axis=0)   # Añadir batch (1,100,100,1)

        # Predicción
        prediction = model.predict(img_array)
        result = "Perro" if prediction[0][0] > 0.5 else "Gato"

        # Pasar el nombre de la imagen y la predicción a la plantilla de resultados
        return render_template('result.html', prediction=result, image_filename=filename)

    except Exception as e:
        return f"Ocurrió un error procesando la imagen: {str(e)}"

@app.route('/clean_up')
def clean_up():
    # Limpiar los archivos de imagen en el directorio de uploads
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"No se pudo eliminar {filename}: {e}")
    return "Archivos eliminados"

if __name__ == '__main__':
    app.run(debug=True)
