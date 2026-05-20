import streamlit as st

def main():
    st.set_page_config(page_title="DMC Python Fundamentals", layout="wide")

    st.sidebar.title("Menú")
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
    st.title("Home")
    st.write("Bienvenido a la aplicación de DMC Python Fundamentals.")
    st.write("Seleccione un ejercicio en el menú lateral para continuar.")

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
