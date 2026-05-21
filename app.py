import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="DMC Python Fundamentals", layout="wide")

    st.sidebar.title("DMC Python Fundamentals")
    opciones = ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    seleccion = st.sidebar.radio("Selecciona un módulo:", opciones)

    if seleccion == "Home":
        mostrar_home()
    elif seleccion == "Ejercicio 1":
        mostrar_ejercicio_1()
    elif seleccion == "Ejercicio 2":
        mostrar_ejercicio_2()
    elif seleccion == "Ejercicio 3":
        mostrar_ejercicio_3()
    elif seleccion == "Ejercicio 4":
        mostrar_ejercicio_4()

def mostrar_home():
    st.title("Proyecto Aplicado: DMC Python Fundamentals")
    
    # Logo
    st.image("resources/logo_dmc_institute.png", width=300)
    
    st.divider()
    
    st.markdown("### 👨‍🎓 Información del Estudiante")
    
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        st.image("resources/mjllanos.png", width=200)
        
    with col_info:
        st.write("**Nombre Completo:** Merwin Johel Llanos Cueva")
        st.write("**Módulo:** Python Fundamentals")
        st.write("**Año:** 2026")
        
        st.markdown("#### Sobre mí")
        st.write("Soy una persona muy curiosa en la tecnología y las novedades, siempre dispuesta a explorar nuevas herramientas y enfoques.\nMe apasiona aprender continuamente y aplicar estos conocimientos en proyectos prácticos e innovadores.")
    
    st.divider()
    
    st.markdown("### 🎯 Breve descripción del proyecto")
    st.info("El objetivo principal de este proyecto es poner en práctica y consolidar los conocimientos adquiridos sobre los fundamentos de la programación con Python. A través de los ejercicios desarrollados, se busca aplicar la lógica de programación, el uso de estructuras de datos, control de flujo y el manejo de librerías para la resolución de problemas de manera interactiva.")
    
    st.markdown("### 🛠️ Tecnologías Utilizadas")
    st.markdown("- 🐍 Python\n- 🎈 Streamlit\n- 🐼 Pandas\n- 🔢 NumPy")

def mostrar_ejercicio_1():
    st.subheader("Ejercicio 1 – Flujo de caja con listas")
    
    st.markdown("""
    **Descripción del ejercicio:**
    En este módulo puedes registrar movimientos financieros. Ingresa el concepto, 
    selecciona el tipo de movimiento (Ingreso o Gasto) y define el valor. 
    Todos los registros se irán almacenando en una lista, permitiendo calcular 
    los totales y evaluar si el flujo de caja está a favor o en contra.
    """)
    
    st.divider()
    
    # Inicializar la lista en session_state para persistencia
    if 'flujo_caja' not in st.session_state:
        st.session_state.flujo_caja = []
        
    st.markdown("### Registrar Nuevo Movimiento")
    
    # Widgets para ingresar los datos
    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto del movimiento:")
    with col2:
        tipo_movimiento = st.selectbox("Tipo de movimiento:", ["Ingreso", "Gasto"])
    with col3:
        valor = st.number_input("Valor ($):", min_value=0.0, step=10.0, format="%.2f")
        
    # Botón para agregar movimientos
    if st.button("Agregar Movimiento"):
        if concepto.strip() == "":
            st.warning("Por favor, ingresa un concepto válido.")
        elif valor <= 0:
            st.warning("Por favor, ingresa un valor mayor a 0.")
        else:
            movimiento = {
                "Concepto": concepto,
                "Tipo": tipo_movimiento,
                "Valor": valor
            }
            st.session_state.flujo_caja.append(movimiento)
            st.success(f"Movimiento '{concepto}' agregado correctamente.")
            
    st.divider()
    
    # Si hay movimientos registrados
    if st.session_state.flujo_caja:
        st.markdown("### Registro de Movimientos")
        
        # Mostrar la tabla de movimientos
        df_flujo = pd.DataFrame(st.session_state.flujo_caja)
        st.dataframe(df_flujo, use_container_width=True)
        
        # Cálculos de ingresos, gastos y saldo
        total_ingresos = sum(item["Valor"] for item in st.session_state.flujo_caja if item["Tipo"] == "Ingreso")
        total_gastos = sum(item["Valor"] for item in st.session_state.flujo_caja if item["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos
        
        st.markdown("### Resumen Financiero")
        col_ing, col_gas, col_sal = st.columns(3)
        
        with col_ing:
            st.metric(label="Total Ingresos", value=f"${total_ingresos:.2f}")
        with col_gas:
            st.metric(label="Total Gastos", value=f"${total_gastos:.2f}")
        with col_sal:
            st.metric(label="Saldo Final", value=f"${saldo_final:.2f}")
            
        st.write("") # Espaciador
        
        # Resultado final del flujo de caja
        if saldo_final > 0:
            st.success("✅ El flujo de caja está a favor.")
        elif saldo_final < 0:
            st.error("❌ El flujo de caja está en contra.")
        else:
            st.info("⚖️ El flujo de caja está balanceado (Saldo 0).")
    else:
        st.info("No hay movimientos registrados. Agrega uno para comenzar.")

def mostrar_ejercicio_2():
    st.title("Ejercicio 2")
    st.write("Módulo independiente para el Ejercicio 2.")

def mostrar_ejercicio_3():
    st.title("Ejercicio 3")
    st.write("Módulo independiente para el Ejercicio 3.")

def mostrar_ejercicio_4():
    st.title("Ejercicio 4")
    st.write("Módulo independiente para el Ejercicio 4.")

if __name__ == "__main__":
    main()
