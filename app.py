import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Calculadora de Rendimiento",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Calculadora de Rendimiento")
st.subheader("Fondos de inversión de deuda")

st.markdown("""
### Metodología utilizada

Base anual de 360 días con metodología simple:

Rendimiento anualizado =
((Precio Final / Precio Inicial) - 1) × (360 / días)
""")

st.divider()

# Inputs
precio_inicial = st.number_input(
    "Precio inicial",
    min_value=0.000001,
    format="%.6f"
)

fecha_inicial = st.date_input(
    "Fecha inicial",
    value=datetime.today()
)

precio_final = st.number_input(
    "Precio final",
    min_value=0.000001,
    format="%.6f"
)

fecha_final = st.date_input(
    "Fecha final",
    value=datetime.today()
)

# Calcular
if st.button("Calcular rendimiento"):

    dias = (fecha_final - fecha_inicial).days

    if dias <= 0:
        st.error("La fecha final debe ser posterior a la fecha inicial.")

    else:

        rendimiento_periodo = (
            (precio_final / precio_inicial) - 1
        )

        rendimiento_anualizado = (
            rendimiento_periodo * (360 / dias)
        )

        st.success("Cálculo realizado correctamente")

        st.markdown("## Resultados")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Días transcurridos",
            f"{dias}"
        )

        col2.metric(
            "Rendimiento periodo",
            f"{rendimiento_periodo:.4%}"
        )

        col3.metric(
            "Rendimiento anualizado",
            f"{rendimiento_anualizado:.4%}"
        )

        st.divider()

        st.markdown("### Detalle del cálculo")

        st.code(f"""
Rendimiento periodo:
(({precio_final:.6f} / {precio_inicial:.6f}) - 1)

= {rendimiento_periodo:.6%}

Rendimiento anualizado simple:
({rendimiento_periodo:.6%}) × (360 / {dias})

= {rendimiento_anualizado:.6%}
""")
