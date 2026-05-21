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
    st.image("logo_dmc_institute.png", width=300)
    
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
    st.title("Ejercicio 1")
    st.write("Módulo independiente para el Ejercicio 1.")

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
