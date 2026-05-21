import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_ratio_endeudamiento
from libreria_clases_proyecto1 import ProyectoInversion

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
        st.write("**Repositorio:** [GitHub - dmc-python-fundamentals](https://github.com/mjllanosc/dmc-python-fundamentals)")
        
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
    st.subheader("Ejercicio 2 – Registro con NumPy, arrays y DataFrame")
    
    st.markdown("""
    **Descripción del ejercicio:**
    En este formulario puedes registrar productos o ventas. La información ingresada 
    se almacena temporalmente y se procesa utilizando arreglos de **NumPy** para luego 
    convertirse en un **DataFrame** de Pandas.
    """)
    
    st.divider()
    
    # Inicializar la lista en session_state para recolectar los datos antes de convertirlos a array
    if 'registro_productos' not in st.session_state:
        st.session_state.registro_productos = []
        
    st.markdown("### Formulario de Registro")
    
    # Widgets para ingresar los datos
    col1, col2 = st.columns(2)
    with col1:
        nombre_producto = st.text_input("Nombre del producto:")
        categoria = st.selectbox("Categoría:", ["Electrónica", "Ropa", "Alimentos", "Hogar", "Otros"])
    with col2:
        precio = st.number_input("Precio ($):", min_value=0.0, step=1.0, format="%.2f")
        cantidad = st.number_input("Cantidad:", min_value=1, step=1)
        
    # Botón para agregar registro
    if st.button("Agregar Registro"):
        if nombre_producto.strip() == "":
            st.warning("Por favor, ingresa el nombre del producto.")
        elif precio <= 0:
            st.warning("Por favor, ingresa un precio mayor a 0.")
        else:
            total = precio * cantidad
            
            # Se guarda el registro en la lista
            nuevo_registro = [nombre_producto, categoria, precio, cantidad, total]
            st.session_state.registro_productos.append(nuevo_registro)
            st.success(f"Producto '{nombre_producto}' agregado exitosamente.")
            
    st.divider()
    
    # Si hay registros, los mostramos
    if st.session_state.registro_productos:
        st.markdown("### Tabla de Productos Registrados")
        
        # 1. Almacenar la información en un array de NumPy (dtype=object permite mezclar strings y números)
        arreglo_numpy = np.array(st.session_state.registro_productos, dtype=object)
        
        # 2. Convertir el array de NumPy en un DataFrame actualizado
        columnas = ["Producto", "Categoría", "Precio ($)", "Cantidad", "Total ($)"]
        df_productos = pd.DataFrame(arreglo_numpy, columns=columnas)
        
        # 3. Mostrar la tabla en DataFrame
        st.dataframe(df_productos, use_container_width=True)
    else:
        st.info("Aún no hay registros. Agrega un producto para ver la tabla.")

def mostrar_ejercicio_3():
    st.subheader("Ejercicio 3 – Uso de funciones desde una librería externa")
    
    st.markdown("""
    **Descripción del ejercicio:**
    En esta sección nos conectamos con la función `calcular_ratio_endeudamiento` del módulo de Finanzas 
    incluido en `libreria_funciones_proyecto1.py`. Ingresa los parámetros correspondientes para ejecutar 
    el cálculo y mantén un registro histórico de los resultados obtenidos.
    """)
    
    st.divider()
    
    # 1. Selector de función (tal como se solicitó para contextualizar, aunque se usará específicamente una)
    st.markdown("### Selección y Ejecución de Función")
    funcion_seleccionada = st.selectbox("Seleccione la función a ejecutar:", ["5) FINANZAS - calcular_ratio_endeudamiento"])
    
    # Inicializar la lista histórica en session_state
    if 'historico_resultados' not in st.session_state:
        st.session_state.historico_resultados = []
        
    # 2 y 3. Widgets para ingresar parámetros
    col1, col2 = st.columns(2)
    with col1:
        empresa = st.text_input("Nombre de la Empresa / Contexto:")
        pasivo_total = st.number_input("Pasivo Total ($):", min_value=0.0, step=1000.0, format="%.2f")
    with col2:
        activo_total = st.number_input("Activo Total ($):", min_value=0.01, step=1000.0, format="%.2f")
        
    # 4. Botón para ejecutar
    if st.button("Ejecutar Cálculo"):
        if not empresa.strip():
            st.warning("Por favor, ingresa el nombre de la empresa.")
        else:
            try:
                # 5. Ejecutar la función y mostrar el resultado en pantalla
                resultado = calcular_ratio_endeudamiento(pasivo_total, activo_total)
                ratio_pct = resultado["ratio_endeudamiento_pct"]
                
                st.success(f"Cálculo exitoso para **{empresa}**.")
                st.write(f"**Ratio de Endeudamiento:** {ratio_pct}%")
                
                # 6. Guardar en histórico de resultados
                nuevo_registro = {
                    "Empresa": empresa,
                    "Pasivo Total ($)": pasivo_total,
                    "Activo Total ($)": activo_total,
                    "Ratio de Endeudamiento (%)": ratio_pct
                }
                st.session_state.historico_resultados.append(nuevo_registro)
                
            except ValueError as e:
                st.error(f"Error en el cálculo: {e}")
                
    st.divider()
    
    # Mostrar tabla histórica
    if st.session_state.historico_resultados:
        st.markdown("### Histórico de Resultados")
        df_historico = pd.DataFrame(st.session_state.historico_resultados)
        st.dataframe(df_historico, use_container_width=True)
    else:
        st.info("Aún no hay cálculos realizados. Ejecuta la función para ver el histórico.")

def mostrar_ejercicio_4():
    st.subheader("Ejercicio 4 – Uso de clases desde una librería externa con CRUD")
    
    st.markdown("""
    **Descripción del ejercicio:**
    En este ejercicio utilizamos la clase `ProyectoInversion` del módulo de Finanzas. 
    Se implementan operaciones básicas CRUD (Crear, Leer, Actualizar, Eliminar) 
    para gestionar una lista de proyectos de inversión.
    """)
    
    st.divider()
    
    # Inicializar la lista de proyectos en session_state (diccionario para facilitar búsqueda y actualización)
    if 'proyectos_inversion' not in st.session_state:
        st.session_state.proyectos_inversion = {}
        
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])
    
    # --- C: CREAR ---
    with tab_crear:
        st.markdown("### Crear Nuevo Proyecto")
        with st.form("form_crear_proyecto"):
            nombre_proyecto = st.text_input("Nombre del Proyecto:")
            inversion_inicial = st.number_input("Inversión Inicial ($):", min_value=1.0, step=1000.0, format="%.2f")
            flujos_str = st.text_input("Flujos de Caja (separados por coma, ej: 1000, 2000, 3000):")
            tasa_descuento_pct = st.number_input("Tasa de Descuento (%):", min_value=0.0, max_value=100.0, step=1.0, format="%.2f")
            
            submit_crear = st.form_submit_button("Crear Proyecto")
            
            if submit_crear:
                if not nombre_proyecto.strip():
                    st.warning("Por favor, ingresa el nombre del proyecto.")
                elif nombre_proyecto in st.session_state.proyectos_inversion:
                    st.warning("Ya existe un proyecto con este nombre.")
                else:
                    try:
                        # Procesar flujos
                        flujos = [float(f.strip()) for f in flujos_str.split(',') if f.strip()]
                        if not flujos:
                            st.warning("Por favor, ingresa al menos un flujo de caja.")
                        else:
                            # Instanciar la clase y guardar en session_state
                            nuevo_proyecto = ProyectoInversion(nombre_proyecto, inversion_inicial, flujos, tasa_descuento_pct)
                            st.session_state.proyectos_inversion[nombre_proyecto] = nuevo_proyecto
                            st.success(f"Proyecto '{nombre_proyecto}' creado exitosamente.")
                    except ValueError as e:
                        st.error(f"Error en los datos ingresados: {e}")

    # --- R: LEER ---
    with tab_leer:
        st.markdown("### Listado de Proyectos Registrados")
        if st.session_state.proyectos_inversion:
            datos_proyectos = []
            for nombre, proyecto in st.session_state.proyectos_inversion.items():
                resumen = proyecto.resumen()
                # Añadimos los datos de entrada al resumen para tener la vista completa
                resumen["inversion_inicial"] = proyecto.inversion_inicial
                resumen["flujos"] = str(proyecto.flujos)
                resumen["tasa_descuento_pct"] = proyecto.tasa_descuento_pct
                
                # Reorganizar el diccionario para una mejor visualización en el DataFrame
                fila = {
                    "Proyecto": resumen["proyecto"],
                    "Inversión Inicial ($)": resumen["inversion_inicial"],
                    "Flujos": resumen["flujos"],
                    "Tasa Desc. (%)": resumen["tasa_descuento_pct"],
                    "VPN ($)": resumen["vpn"],
                    "ROI (%)": resumen["roi_pct"],
                    "Payback (Años)": resumen["payback_anios"],
                    "Decisión": resumen["decision"]
                }
                datos_proyectos.append(fila)
                
            df_proyectos = pd.DataFrame(datos_proyectos)
            st.dataframe(df_proyectos, use_container_width=True)
        else:
            st.info("No hay proyectos registrados. Ve a la pestaña 'Crear' para agregar uno.")

    # --- U: ACTUALIZAR ---
    with tab_actualizar:
        st.markdown("### Actualizar Proyecto Existente")
        if st.session_state.proyectos_inversion:
            nombres_proyectos = list(st.session_state.proyectos_inversion.keys())
            proyecto_seleccionado = st.selectbox("Selecciona un proyecto para actualizar:", nombres_proyectos)
            
            # Cargar datos actuales del proyecto
            proyecto_actual = st.session_state.proyectos_inversion[proyecto_seleccionado]
            
            with st.form("form_actualizar_proyecto"):
                nueva_inversion_inicial = st.number_input(
                    "Nueva Inversión Inicial ($):", 
                    min_value=1.0, 
                    value=float(proyecto_actual.inversion_inicial), 
                    step=1000.0, 
                    format="%.2f"
                )
                
                nuevos_flujos_str = st.text_input(
                    "Nuevos Flujos de Caja (separados por coma):", 
                    value=", ".join(map(str, proyecto_actual.flujos))
                )
                
                nueva_tasa_descuento_pct = st.number_input(
                    "Nueva Tasa de Descuento (%):", 
                    min_value=0.0, 
                    max_value=100.0, 
                    value=float(proyecto_actual.tasa_descuento_pct), 
                    step=1.0, 
                    format="%.2f"
                )
                
                submit_actualizar = st.form_submit_button("Actualizar Proyecto")
                
                if submit_actualizar:
                    try:
                        nuevos_flujos = [float(f.strip()) for f in nuevos_flujos_str.split(',') if f.strip()]
                        if not nuevos_flujos:
                            st.warning("Por favor, ingresa al menos un flujo de caja.")
                        else:
                            # Sobrescribir la instancia con los nuevos valores
                            proyecto_actualizado = ProyectoInversion(
                                proyecto_seleccionado, 
                                nueva_inversion_inicial, 
                                nuevos_flujos, 
                                nueva_tasa_descuento_pct
                            )
                            st.session_state.proyectos_inversion[proyecto_seleccionado] = proyecto_actualizado
                            st.success(f"Proyecto '{proyecto_seleccionado}' actualizado exitosamente.")
                            st.rerun() # Recargar la página para actualizar las otras pestañas
                    except ValueError as e:
                        st.error(f"Error en los datos ingresados: {e}")
        else:
            st.info("No hay proyectos para actualizar.")

    # --- D: ELIMINAR ---
    with tab_eliminar:
        st.markdown("### Eliminar Proyecto")
        if st.session_state.proyectos_inversion:
            nombres_proyectos_eliminar = list(st.session_state.proyectos_inversion.keys())
            proyecto_a_eliminar = st.selectbox("Selecciona un proyecto para eliminar:", nombres_proyectos_eliminar)
            
            if st.button("Eliminar Proyecto", type="primary"):
                del st.session_state.proyectos_inversion[proyecto_a_eliminar]
                st.success(f"Proyecto '{proyecto_a_eliminar}' eliminado exitosamente.")
                st.rerun() # Recargar para actualizar los selectores y tablas
        else:
            st.info("No hay proyectos para eliminar.")

if __name__ == "__main__":
    main()
