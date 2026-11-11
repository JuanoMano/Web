import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("data/vehicles_us.csv")


st.set_page_config(
    page_title="Análisis de vehículos usados",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Análisis del mercado de vehículos usados")
st.write(
    "Esta aplicación explora un conjunto de datos "
    "sobre anuncios de venta de vehículos en Estados Unidos."
)


st.header("Información general del conjunto de datos")

col1, col2, col3 = st.columns(3)

col1.metric("Total de vehículos", f"{len(car_data):,}")
col2.metric("Número de columnas", len(car_data.columns))
col3.metric(
    "Precio promedio",
    f"${car_data['price'].mean():,.0f}"
)


st.header("1. Distribución de precios")

st.write(
    "Este histograma permite observar cómo se distribuyen "
    "los precios de los vehículos anunciados."
)

hist_button = st.button("Construir histograma")

if hist_button:

    fig = px.histogram(
        car_data,
        x="price",
        nbins=50,
        title="Distribución de precios de vehículos",
        labels={
            "price": "Precio (USD)",
            "count": "Cantidad de vehículos"
        },
        color_discrete_sequence=["#3498DB"]
    )

    st.plotly_chart(fig, use_container_width=True)



st.header("2. Precio vs. kilometraje")

st.write(
    "Analizamos si existe una relación entre el kilometraje "
    "de un vehículo y su precio de venta."
)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:

    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        title="Relación entre precio y kilometraje",
        labels={
            "odometer": "Kilometraje (millas)",
            "price": "Precio (USD)",
            "condition": "Condición"
        },
        opacity=0.6
    )

    st.plotly_chart(fig_scatter, use_container_width=True)


st.header("3. Análisis por tipo de vehículo")

st.write(
    "Comparamos el precio promedio de los diferentes "
    "tipos de vehículos disponibles."
)

price_by_type = (
    car_data.groupby("type")["price"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig_bar = px.bar(
    price_by_type,
    x="type",
    y="price",
    title="Precio promedio según tipo de vehículo",
    labels={
        "type": "Tipo de vehículo",
        "price": "Precio promedio (USD)"
    },
    color="price",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_bar, use_container_width=True)


st.header("4. Estado de los vehículos")

condition_data = (
    car_data["condition"]
    .value_counts()
    .reset_index()
)

condition_data.columns = ["condition", "quantity"]

fig_condition = px.bar(
    condition_data,
    x="condition",
    y="quantity",
    title="Cantidad de vehículos según su condición",
    labels={
        "condition": "Condición",
        "quantity": "Cantidad de vehículos"
    },
    color="condition"
)

st.plotly_chart(fig_condition, use_container_width=True)


st.header("5. Explorar los datos")

show_data = st.checkbox("Mostrar tabla de vehículos")

if show_data:
    st.write("Primeros 20 registros del conjunto de datos:")
    st.dataframe(car_data.head(20), use_container_width=True)

