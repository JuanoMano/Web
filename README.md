## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web interactiva utilizando **Streamlit**, cuyo objetivo es realizar un análisis exploratorio de datos sobre anuncios de venta de vehículos usados en Estados Unidos.

A través de esta aplicación se busca explorar las principales características de los vehículos anunciados, identificar patrones en sus precios y analizar la relación entre variables como el kilometraje, el estado del vehículo y su tipo.

## Funcionalidades de la aplicación

La aplicación permite:

- **Visualizar información general:** consultar la cantidad de vehículos y variables disponibles en el conjunto de datos, así como el precio promedio.
- **Analizar la distribución de precios:** construir un histograma interactivo para observar cómo se distribuyen los precios de los vehículos.
- **Explorar la relación entre precio y kilometraje:** utilizar un gráfico de dispersión para identificar posibles patrones entre estas dos variables.
- **Comparar tipos de vehículos:** visualizar los precios promedio según la categoría del vehículo.
- **Analizar la condición de los vehículos:** conocer la cantidad de anuncios según el estado en que se encuentran.
- **Consultar los datos:** mostrar una tabla con los primeros registros del conjunto de datos mediante una casilla de verificación.

## Herramientas utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes herramientas:

- **Python:** lenguaje de programación.
- **Pandas:** lectura, manipulación y análisis de los datos.
- **Plotly Express:** creación de gráficos interactivos.
- **Streamlit:** desarrollo y visualización de la aplicación web.

## Conjunto de datos

Se utiliza el archivo `vehicles_us.csv`, que contiene información de anuncios de vehículos usados en Estados Unidos.

El conjunto de datos cuenta con 51.525 registros y 13 columnas, entre las que se encuentran el precio, año del modelo, condición, kilometraje, combustible, transmisión y tipo de vehículo.

## Ejecución de la aplicación

Para ejecutar la aplicación localmente, sigue estos pasos:

1. Instalar las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

2. Ubicarse en la carpeta `Web`, donde se encuentra el archivo `app.py`.

3. Ejecutar la aplicación con el siguiente comando:

   ```bash
   streamlit run app.py
   ```

La aplicación se abrirá automáticamente en el navegador y permitirá interactuar con las diferentes visualizaciones.

## Objetivo del proyecto

Aplicar conocimientos de análisis exploratorio de datos, manipulación de información y visualización interactiva mediante el desarrollo de una aplicación web que facilite la exploración y comprensión del mercado de vehículos usados.

# Enlace a render
https://web-6v23.onrender.com