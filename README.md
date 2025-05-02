# Clasificador de Perros y Gatos 
Este proyecto es una aplicación web desarrollada con Flask que permite clasificar imágenes de perros y gatos utilizando un modelo de redes neuronales convolucionales (CNN) entrenado previamente.

---

## Características

- Clasificación binaria: perro o gato.
- Interfaz web simple y agradable.
- Carga de imágenes desde el navegador.
- Predicción visual con resultado y vista previa de la imagen.
- Limpieza automática de imágenes temporales tras la predicción.

---

## Estructura del Proyecto

```

clasificador-perros-gatos/
│
├── model/                   # Modelo entrenado (.h5)
│   └── perros-gatos-cnn-ad.h5
│
├── static/                  # Archivos estáticos
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── uploads/             # Carpeta de imágenes temporales
│
├── templates/               # Plantillas HTML
│   ├── index.html
│   └── result.html
│
├── app.py                   # Aplicación principal Flask
├── requirements.txt         # Requisitos del proyecto
└── README.md                # Documentación del proyecto

````

---

## Requisitos

Antes de ejecutar la app, asegúrate de tener Python 3.7+ instalado.

Instala los paquetes necesarios con:

```bash
pip install -r requirements.txt
````

### Contenido de `requirements.txt`

```
absl-py==2.2.2
astunparse==1.6.3
blinker==1.9.0
cachetools==5.5.2
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
Flask==3.1.0
flatbuffers==25.2.10
gast==0.4.0
google-auth==2.39.0
google-auth-oauthlib==1.0.0
google-pasta==0.2.0
grpcio==1.71.0
h5py==3.13.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.6
keras==3.9.2
libclang==18.1.1
Markdown==3.8
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
ml-dtypes==0.4.1
namex==0.0.8
numpy==2.0.2
oauthlib==3.2.2
opt_einsum==3.4.0
optree==0.15.0
packaging==24.2
pillow==11.2.1
protobuf==4.25.6
pyasn1==0.6.1
pyasn1_modules==0.4.2
Pygments==2.19.1
requests==2.32.3
requests-oauthlib==2.0.0
rich==14.0.0
rsa==4.9
six==1.17.0
tensorboard==2.18.0
tensorboard-data-server==0.7.2
tensorflow==2.18.0
tensorflow-estimator==2.13.0
tensorflow-io-gcs-filesystem==0.31.0
tensorflow_intel==2.18.0
termcolor==3.0.1
typing_extensions==4.5.0
urllib3==2.4.0
Werkzeug==3.1.3
wrapt==1.14.1
```

---

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/nicolasPecora/clasificador-perros-gatos.git
cd clasificador-perros-gatos
```

### 2. Crear y activar entorno virtual (recomendado)

```bash
python -m venv venv
.\venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación Flask

```bash
python app.py
```

### 5. Abrir en tu navegador

Visita `http://127.0.0.1:5000/` y ¡empieza a clasificar tus imágenes!

---

## Limpieza automática

Las imágenes cargadas se eliminan automáticamente del servidor después de realizar la predicción. No necesitas borrarlas manualmente.

---

## Subida a GitHub (resumen rápido)

1. Crear `.gitignore` (ignorar entorno virtual y uploads):

   ```bash
   echo venv/ > .gitignore
   echo static/uploads/ >> .gitignore
   ```

2. Inicializar repositorio y subir:

   ```bash
   git init
   git add .
   git commit -m "Primer commit"
   git remote add origin https://github.com/nicolasPecora/clasificador-perros-gatos.git
   git push -u origin master
   ```

---

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo libremente citando al autor.

---

¡Gracias por visitar este proyecto!
por [Nicolás Pécora](https://github.com/nicolasPecora)
