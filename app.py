
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Conversor de Temperatura",
    page_icon="🌡️",
    layout="centered"
)

# Título
st.title("🌡️ Conversor de Temperatura")
st.write("Convierte temperaturas entre Celsius, Fahrenheit y Kelvin.")

# Entrada de temperatura
temperatura = st.number_input(
    "Ingresa la temperatura:",
    value=25.0,
    step=1.0
)

# Selección de unidades
col1, col2 = st.columns(2)

with col1:
    unidad_origen = st.selectbox(
        "Convertir desde:",
        ["Celsius", "Fahrenheit", "Kelvin"]
    )

with col2:
    unidad_destino = st.selectbox(
        "Convertir a:",
        ["Fahrenheit", "Celsius", "Kelvin"]
    )

# Conversión a Celsius
def a_celsius(valor, unidad):
    if unidad == "Celsius":
        return valor
    elif unidad == "Fahrenheit":
        return (valor - 32) * 5 / 9
    else:
        return valor - 273.15

# Conversión desde Celsius
def desde_celsius(valor, unidad):
    if unidad == "Celsius":
        return valor
    elif unidad == "Fahrenheit":
        return (valor * 9 / 5) + 32
    else:
        return valor + 273.15

# Botón de conversión
if st.button("Convertir temperatura", type="primary"):
    if unidad_origen == "Kelvin" and temperatura < 0:
        st.error("La temperatura en Kelvin no puede ser negativa.")
    elif unidad_origen == "Celsius" and temperatura < -273.15:
        st.error("La temperatura no puede ser inferior al cero absoluto.")
    elif unidad_origen == "Fahrenheit" and temperatura < -459.67:
        st.error("La temperatura no puede ser inferior al cero absoluto.")
    else:
        resultado_celsius = a_celsius(
            temperatura, unidad_origen
        )

        resultado = desde_celsius(
            resultado_celsius, unidad_destino
        )

        st.success("¡Conversión realizada!")
        st.metric(
            label=f"Resultado en {unidad_destino}",
            value=f"{resultado:.2f} °"
        )

        st.caption(
            f"{temperatura:.2f} °{unidad_origen} "
            f"= {resultado:.2f} °{unidad_destino}"
        )
