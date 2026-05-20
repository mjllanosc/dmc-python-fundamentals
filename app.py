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
    st.title("🏠 DMC Python Fundamentals")
    st.markdown("### Proyecto Aplicado en Streamlit")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👨‍🎓 Información General")
        st.write("**Estudiante:** Merwin Johel Llanos Cueva")
        st.write("**Curso:** Python Fundamentals")
        st.write("**Año:** 2026")
        
    with col2:
        st.markdown("#### 🛠️ Tecnologías Utilizadas")
        st.markdown("- 🐍 Python\n- 🎈 Streamlit\n- 🐼 Pandas\n- 🔢 NumPy")
        
    st.divider()
    
    st.markdown("#### 🎯 Objetivo del trabajo")
    st.info("El objetivo principal de este proyecto es poner en práctica y consolidar los conocimientos adquiridos sobre los fundamentos de la programación con Python. A través de los ejercicios desarrollados, se busca aplicar la lógica de programación, el uso de estructuras de datos, control de flujo y el manejo de librerías para la resolución de problemas de manera interactiva.")

def mostrar_ejercicio_1():
    st.subheader("Ejercicio 1 – Variables y Condicionales (Verificador de Presupuesto)")
    
    st.write("Ingrese su presupuesto y el gasto realizado para verificar si se encuentra dentro del límite.")
    
    # 1. Solicitar presupuesto
    presupuesto = st.number_input("Ingrese el presupuesto ($):", min_value=0.0, step=10.0, format="%.2f")
    
    # 2. Solicitar gasto
    gasto = st.number_input("Ingrese el gasto ($):", min_value=0.0, step=10.0, format="%.2f")
    
    # 3. Botón para evaluar
    if st.button("Evaluar Presupuesto"):
        diferencia = presupuesto - gasto
        
        # 4 y 5. Condición y mensajes
        if gasto <= presupuesto:
            st.success("✅ ¡El gasto está dentro del presupuesto!")
        else:
            st.warning("⚠️ ¡Atención! El presupuesto fue excedido.")
            
        # 6. Mostrar diferencia
        if diferencia >= 0:
            st.write(f"**Diferencia:** Le sobran **${diferencia:.2f}**")
        else:
            st.write(f"**Diferencia:** Se excedió por **${abs(diferencia):.2f}**")

def mostrar_ejercicio_2():
    st.subheader("Ejercicio 2 – Listas y Diccionarios (Registro de Actividades Financieras)")
    
    st.write("Agregue sus actividades financieras. El sistema evaluará el estado del presupuesto para cada una.")
    
    # 1. Crear una lista (usando session_state para que los datos persistan entre recargas)
    if 'actividades' not in st.session_state:
        st.session_state.actividades = []
        
    # 2. Solicitar datos
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre de la actividad:")
        tipo = st.selectbox("Tipo de actividad:", ["Ingreso", "Gasto Fijo", "Gasto Variable", "Inversión"])
    with col2:
        presupuesto = st.number_input("Presupuesto asignado ($):", min_value=0.0, step=10.0, format="%.2f", key="presupuesto_ej2")
        gasto_real = st.number_input("Gasto real ($):", min_value=0.0, step=10.0, format="%.2f", key="gasto_ej2")
        
    # 3. Al presionar "Agregar", guardar como diccionario en la lista
    if st.button("Agregar Actividad"):
        if nombre: # Validación básica para no agregar vacíos
            nueva_actividad = {
                "Nombre": nombre,
                "Tipo": tipo,
                "Presupuesto": presupuesto,
                "Gasto Real": gasto_real
            }
            st.session_state.actividades.append(nueva_actividad)
            st.success(f"Actividad '{nombre}' agregada con éxito.")
        else:
            st.warning("Por favor, ingrese un nombre para la actividad.")

    st.divider()

    # Si hay actividades en la lista
    if st.session_state.actividades:
        st.markdown("### Resumen de Actividades")
        
        # 4. Mostrar la lista en formato tabla usando pandas para una mejor visualización
        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("### Evaluación de Presupuestos")
        
        # 5 y 6. Recorrer la lista y evaluar cada actividad
        for actividad in st.session_state.actividades:
            nombre_act = actividad['Nombre']
            presupuesto_act = actividad['Presupuesto']
            gasto_act = actividad['Gasto Real']
            diferencia = presupuesto_act - gasto_act
            
            if gasto_act <= presupuesto_act:
                st.write(f"✅ **{nombre_act}**: Dentro del presupuesto (Sobra: ${diferencia:.2f})")
            else:
                st.write(f"⚠️ **{nombre_act}**: Presupuesto excedido (Exceso de: ${abs(diferencia):.2f})")
    else:
        st.info("No hay actividades registradas todavía.")

def mostrar_ejercicio_3():
    st.title("Ejercicio 3")
    st.write("Módulo independiente para el Ejercicio 3.")

def mostrar_ejercicio_4():
    st.title("Ejercicio 4")
    st.write("Módulo independiente para el Ejercicio 4.")

if __name__ == "__main__":
    main()
