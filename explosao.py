# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 13:59:06 2025

@author: LAB-13
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de Explosão de Panela", layout="wide")

st.title("Simulador: Quando uma Panela de Pressão Vai Explodir?")





st.sidebar.header("Parâmetros")
initial_pressure = st.sidebar.slider("Pressão Inicial (psi)", 0.0, 10.0, 0.0)
heating_rate = st.sidebar.slider("Taxa de Aquecimento (psi/min)", 0.1, 5.0, 1.0)
max_safe_pressure = st.sidebar.slider("Pressão Máxima Segura (psi)", 10.0, 30.0, 15.0)
simulation_time = st.sidebar.slider("Tempo Máximo (min)", 5, 60, 30)

if st.button("Iniciar Simulação"):
    time_points = np.linspace(0, simulation_time, 100)
    pressure_points = initial_pressure + heating_rate * time_points
    
    explosion_time = None
    for i in range(len(time_points)):
        t = time_points[i]
        p = pressure_points[i]
        if p > max_safe_pressure:
            explosion_time = t
            break
    
    if explosion_time is not None:
        st.error("Explosão em {:.1f} minutos!".format(explosion_time))
    else:
        st.success("Não explode. Pressão final: {:.1f} psi".format(pressure_points[-1]))
    
    
    
    fig, ax = plt.subplots()
    ax.plot(time_points, pressure_points, label='Pressão')
    ax.axhline(y=max_safe_pressure, color='orange', linestyle='--', label='Limite')
    if explosion_time:
         ax.axvline(x=explosion_time, color='red', linestyle=':', label='Explosão')
    ax.set_xlabel('Tempo (min)')
    ax.set_ylabel('Pressão (psi)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
   

