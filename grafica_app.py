import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def main ():
    st.title("Grafica de numero polar")
    ALPHA = st.text_input("ingresa el valor de alpha de tu primer fasor: ", "0")
    ANGULO = st.text_input("Ángulo en grados", "0")
    try:
        ALPHA = float(ALPHA)
    except ValueError:
        st.error("Por favor ingresa un número válido para el alpha.")
        return


    try:
        ANGULO = float(ANGULO)
    except ValueError:
        st.error("Por favor ingresa un número válido para el ángulo.")
        return

    def fasor_A (ALPHA, ANGULO):
        FasorA = ALPHA * (np.cos(np.deg2rad(ANGULO)) + 1j*np.sin(np.deg2rad(ANGULO))) #pasamos de forma polar a forma rectangular
        parte_Real = np.real(FasorA) #EJE X
        parte_Imaginaria = np.imag(FasorA) #EJE Y
        return parte_Real, parte_Imaginaria
    
    fasor_a = fasor_A(ALPHA, ANGULO)
    st.write("la parte real del fasor 'A' corresponden a:", fasor_a[0], "la parte imaginaria del fasor 'A' corresponde a:",fasor_a[1] )
    ALPHAB = st.text_input("ingresa el valor de alpha de tu segundo fasor: ", "0")
    ANGULOB = st.text_input("ingresa los grados de tu segundo fasor: ", "0")
    try:
        ALPHAB = float(ALPHAB)
    except ValueError:
        st.error("Por favor ingresa un número válido para el alpha.")
        return
    try:
        ANGULOB = float(ANGULOB)
    except ValueError:
        st.error("Por favor ingresa un número válido para el ángulo.")
        return
    def fasor_B (ALPHAB, ANGULOB):

        FasorB = ALPHAB * (np.cos(np.deg2rad(ANGULOB)) + 1j*np.sin(np.deg2rad(ANGULOB))) #pasa de forma polar a forma rectangular

        parte_Real = np.real(FasorB) #EJE X

        parte_Imaginaria = np.imag(FasorB) #EJE Y

        return parte_Real, parte_Imaginaria
    fasor_b = fasor_B(ALPHAB, ANGULOB) 
    st.write("la parte real del fasor 'B' corresponden a:", fasor_b[0], "la parte imaginaria del fasor 'B' corresponde a:",fasor_b[1] )


    #graficar fasores
    def graficar_fasores(fasor_a, fasor_b):

      fig, ax = plt.subplots()
      #x = np.linspace(0,10,100)
      

      ax.quiver(0, 0, fasor_a[0], fasor_a[1], angles='xy', scale_units='xy', scale=1, color='r', label='Fasor A')

      ax.quiver(fasor_a[0], fasor_a[1], fasor_b[0], fasor_b[1], angles='xy', scale_units='xy', scale=1, color='b', label='Fasor B')

      ax.axis([0, 6, -12 , 12])

      ax.set_xlabel('Parte Real')

      ax.set_ylabel('Parte Imaginaria')

      ax.set_title('Gráfico de Fasores')

      ax.grid(True)
      plt.minorticks_on()
      plt.grid(which='minor', color='blue', linestyle='-', linewidth=0.2)
      

      ax.legend()
      #plt.plot(x)

      plt.show()
      st.pyplot(fig)
    
    st.write("fasor A:", fasor_a[0],"+", fasor_a[1],"j")
    st.write("fasor B:", fasor_b[0],"+", fasor_b[1],"j")
    graficar_fasores(fasor_a, fasor_b)
    

    def sumar_fasores(fasor_a, fasor_b):
      print ("fasor a ",fasor_a)
      print ("fasor b ",fasor_b)
      FasorC = complex(fasor_a[0] + fasor_b[0] , fasor_a[1] + fasor_b[1])
      parte_Real = np.real(FasorC)
      parte_Imaginaria = np.imag(FasorC)
      print("la suma de los fasores nos da un fasor C correspondiente a:", FasorC)
      return parte_Real, parte_Imaginaria
    fasor_c = sumar_fasores(fasor_a, fasor_b)
    st.write(f"los valores del fasor c corresponden a: {fasor_c[0]} y {fasor_c[1]}j ")

    def graficar_todos_los_fasores(fasor_a, fasor_b, fasor_c):
      fig, ax = plt.subplots()
      ax.quiver(0, 0, fasor_a[0], fasor_a[1], angles='xy', scale_units='xy', scale=1, color='r', label='Fasor A')
      ax.quiver(fasor_a[0], fasor_a[1], fasor_b[0], fasor_b[1], angles='xy', scale_units='xy', scale=1, color='b', label='Fasor B')
      ax.quiver(0, 0, fasor_c[0], fasor_c[1],  angles ="xy", scale_units='xy', scale=1, color='g', label='Fasor C')
      if fasor_c[1] <0 :
        ax.axis([0, abs(fasor_c[0]) + 2, abs(fasor_c[1]) - 5,  abs(fasor_c[1]) + 3])
      else:
        ax.axis([0, abs(fasor_c[0]) + 2, abs(fasor_c[1]) + 5,  abs(fasor_c[1]) - 3])
    

      ax.set_xlabel('Parte Real')

      ax.set_ylabel('Parte Imaginaria')

      ax.set_title('Gráfico de Fasores')

      ax.grid(True)

      ax.legend()

      plt.show()
      st.pyplot(fig)
    st.write(f"fasor A: {fasor_a[0]} {fasor_a[1]}j")
    st.write(f"fasor B: {fasor_b[0]} {fasor_b[1]}j")
    st.write("fasor C:", fasor_c [0])
    st.write("fasor C:", fasor_c [1])

    graficar_todos_los_fasores(fasor_a, fasor_b, fasor_c)

if __name__ == "__main__":
    main()