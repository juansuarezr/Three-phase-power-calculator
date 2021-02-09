# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:28:02 2020

@author: Juan Pablo
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import TransFortescue as tf

def ThreePhaseSinusoidal():
    #Se definen valores iniciales de voltaje rms, corriente rms y frecuencia
    
    v_rms = 120
    i_rms = 60
    f0 = 60
    fase_voltaje = 0
    fase_corriente = 25.84
    t = np.arange(0.0, 2/f0, 0.0001) #Dominio del tiempo
    axcolor = 'lightgoldenrodyellow'
    
    
    #Se crea la figura principal
    
    fig = plt.figure(figsize = (12,8))
    ax_fondo1 = fig.add_axes([0.027,0.33,0.45,0.53], xticks = [], yticks = [],facecolor = axcolor)
    ax_fondo2 = fig.add_axes([0.52,0.33,0.45,0.53], xticks = [], yticks = [],facecolor = axcolor)
    
    
    #Se grafica el sistema trifásico (voltaje) en el tiempo
    ax_voltaje = fig.add_axes([0.1,0.72,0.21,0.12], ylabel = "$Voltage(V)$", xlabel = "$Time(s)$")
    plt.subplots_adjust(left=0.15, bottom=0.55)
    ax_voltaje.set_ylim(-310,310)
    ax_voltaje.set_xlim(0,2/f0)
    ax_voltaje.set_xticks([])
    s1 = np.sqrt(2) * v_rms * np.cos(2 * np.pi * f0 * t)
    s2 = np.sqrt(2) * v_rms * np.cos(2 * np.pi * f0 * t - 2*np.pi/3)
    s3 = np.sqrt(2) * v_rms * np.cos(2 * np.pi * f0 * t + 2*np.pi/3)
    l1, = plt.plot(t, s1, lw=1, color ="blue", label = "va")
    l2, = plt.plot(t, s2, lw=1, color = "green", label = "vb")
    l3, = plt.plot(t, s3, lw=1, color = "red", label = "vc")
    ax_voltaje.legend(loc='center left', bbox_to_anchor=(-0.45, 1.5))
    ax_voltaje.margins(x=0)
    plt.grid()
    
    
    #Se grafica el sistema trifásico (corriente) en el tiempo
    ax_corriente = fig.add_axes([0.592,0.72,0.21,0.12], ylabel = "$Current(A)$", xlabel = "$Time(s)$")
    plt.subplots_adjust(left=0.15, bottom=0.55)
    ax_corriente.set_ylim(-147,147)
    ax_corriente.set_xlim(0,2/f0)
    ax_corriente.set_xticks([])
    h1 = np.sqrt(2) * i_rms * np.cos(2 * np.pi * f0 * t)
    h2 = np.sqrt(2) * i_rms * np.cos(2 * np.pi * f0 * t -2*np.pi/3)
    h3 = np.sqrt(2) * i_rms * np.cos(2 * np.pi * f0 * t +2*np.pi/3)
    k1, = plt.plot(t, h1, lw=1, color ="blue", label = "ia")
    k2, = plt.plot(t, h2, lw=1, color = "green", label = "ib")
    k3, = plt.plot(t, h3, lw=1, color = "red", label = "ic")
    ax_corriente.legend(loc='center left', bbox_to_anchor=(-0.45, 1.5))
    ax_corriente.margins(x=0)
    plt.grid()
    
    
    """
    A continuación se grafica el sistema desbalanceado para los voltajes en forma fasorial,
    junto con sus respectivas componentes simétricas según el teorema de Fortescue.
    """
    
    #Fasores iniciales
    v1 = v_rms * np.exp(1j*np.deg2rad(fase_voltaje))
    v2 = v_rms * np.exp(1j*(-2*np.pi/3 + np.deg2rad(fase_voltaje)))
    v3 = v_rms * np.exp(1j*(2*np.pi/3 + np.deg2rad(fase_voltaje)))
    
    
    #Sistema desbalanceado
    axpolar_voltajes = fig.add_axes([0.36,0.7,0.08,0.12])
    axpolar_voltajes.set_xlim(-310,310)
    axpolar_voltajes.set_ylim(-310,310)
    axpolar_voltajes.set_title("Phasors", pad = 5)
    #axpolar_voltajes.set_axis_off()
    l1_fasor = axpolar_voltajes.arrow(0,0,np.sqrt(2)*v1.real,np.sqrt(2)*v1.imag, color = "blue", width = 0.01)
    l2_fasor = axpolar_voltajes.arrow(0,0,np.sqrt(2)*v2.real,np.sqrt(2)*v2.imag, color = "green", width = 0.01)
    l3_fasor = axpolar_voltajes.arrow(0,0,np.sqrt(2)*v3.real,np.sqrt(2)*v3.imag, color = "red", width = 0.01)
    
    
    #Grafica de la secuencia positiva
    axpolarv1 = fig.add_axes([0.08,0.51,0.08,0.12])
    axpolarv1.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1)
    axpolarv1.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1)
    axpolarv1.set_title("Positive sequence", pad = 5)
    #axpolarv1.set_axis_off()
    l_pos_1 = axpolarv1.arrow(0,0,np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[0][0].real,np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[0][0].imag, color = "blue", width = 0.01)
    l_pos_2 = axpolarv1.arrow(0,0,np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[1][0].real,np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[1][0].imag, color = "green", width = 0.01)
    l_pos_3 = axpolarv1.arrow(0,0,np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[2][0].real,np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[2][0].imag, color = "red", width = 0.01)
    
    
    #Grafica de la secuencia negativa
    axpolarv2 = fig.add_axes([0.22,0.51,0.08,0.12])
    axpolarv2.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1)
    axpolarv2.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1)
    axpolarv2.set_title("Negative sequence", pad = 5)
    #axpolarv2.set_axis_off()
    l_neg_1 = axpolarv2.arrow(0,0,np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[0][0].real,np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[0][0].imag, color = "blue", width = 0.01)
    l_neg_2 = axpolarv2.arrow(0,0,np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[1][0].real,np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[1][0].imag, color = "green", width = 0.01)
    l_neg_3 = axpolarv2.arrow(0,0,np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[2][0].real,np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[2][0].imag, color = "red", width = 0.01)
    
    
    #Grafica de la secuencia cero
    axpolarv3 = fig.add_axes([0.36,0.51,0.08,0.12])
    axpolarv3.set_title("Zero sequence", pad = 5)
    axpolarv3.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(v1,v2,v3)[0][0])+1)
    axpolarv3.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(v1,v2,v3)[0][0])+1)
    #axpolarv3.set_axis_off()
    l_hom_1 = axpolarv3.arrow(0,0,np.sqrt(2)*tf.sec_homopolar(v1,v2,v3)[0][0].real,np.sqrt(2)*tf.sec_homopolar(v1,v2,v3)[0][0].imag, color = "blue", width = 0.01)
    l_hom_2 = axpolarv3.arrow(((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1)/2,0,tf.sec_homopolar(v1,v2,v3)[1][0].real,tf.sec_homopolar(v1,v2,v3)[1][0].imag, color = "green", width = 0.01)
    l_hom_3 = axpolarv3.arrow(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1)/2,0,tf.sec_homopolar(v1,v2,v3)[2][0].real,tf.sec_homopolar(v1,v2,v3)[2][0].imag, color = "red", width = 0.01)
    
    
    
    """
    A continuación se grafica el sistema desbalanceado para las corrientes en forma fasorial,
    junto con sus respectivas componentes simétricas según el teorema de Fortescue.
    """
    
    #Fasores iniciales
    i1 = i_rms * np.exp(1j*np.deg2rad(fase_corriente))
    i2 = i_rms * np.exp(1j*np.deg2rad(-120 + fase_corriente))
    i3 = i_rms * np.exp(1j*np.deg2rad(120 + fase_corriente))
    
    
    #Sistema desbalanceado
    axpolar_corrientes = fig.add_axes([0.855,0.7,0.08,0.12])
    axpolar_corrientes.set_xlim(-140,140)
    axpolar_corrientes.set_ylim(-140,140)
    axpolar_corrientes.set_title("Phasors", pad = 5)
    #axpolar_corrientes.set_axis_off()
    k1_fasor = axpolar_corrientes.arrow(0,0,np.sqrt(2)*i1.real,np.sqrt(2)*i1.imag, color = "blue", width = 0.01)
    k2_fasor = axpolar_corrientes.arrow(0,0,np.sqrt(2)*i2.real,np.sqrt(2)*i2.imag, color = "green", width = 0.01)
    k3_fasor = axpolar_corrientes.arrow(0,0,np.sqrt(2)*i3.real,np.sqrt(2)*i3.imag, color = "red", width = 0.01)
    
    
    #Grafica de la secuencia positiva
    axpolari1 = fig.add_axes([0.575,0.51,0.08,0.12])
    axpolari1.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1)
    axpolari1.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1)
    axpolari1.set_title("Positive sequence", pad = 5)
    #axpolari1.set_axis_off()
    k_pos_1 = axpolari1.arrow(0,0,np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[0][0].real,np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[0][0].imag, color = "blue", width = 0.01)
    k_pos_2 = axpolari1.arrow(0,0,np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[1][0].real,np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[1][0].imag, color = "green", width = 0.01)
    k_pos_3 = axpolari1.arrow(0,0,np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[2][0].real,np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[2][0].imag, color = "red", width = 0.01)
    
    
    #Grafica de la secuencia negativa
    axpolari2 = fig.add_axes([0.715,0.51,0.08,0.12])
    axpolari2.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1)
    axpolari2.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1)
    axpolari2.set_title("Negative sequence", pad = 5)
    #axpolari2.set_axis_off()
    k_neg_1 = axpolari2.arrow(0,0,np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[0][0].real,np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[0][0].imag, color = "blue", width = 0.01)
    k_neg_2 = axpolari2.arrow(0,0,np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[1][0].real,np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[1][0].imag, color = "green", width = 0.01)
    k_neg_3 = axpolari2.arrow(0,0,np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[2][0].real,np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[2][0].imag, color = "red", width = 0.01)
    
    
    #Grafica de la secuencia cero
    axpolari3 = fig.add_axes([0.855,0.51,0.08,0.12])
    axpolari3.set_title("Zero sequence", pad = 5)
    axpolari3.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0])+1)
    axpolari3.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0])+1)
    #axpolari3.set_axis_off()
    k_hom_1 = axpolari3.arrow(0,0,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0].real,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0].imag, color = "blue", width = 0.01)
    k_hom_2 = axpolari3.arrow(((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1)/2,0,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[1][0].real,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[1][0].imag, color = "green", width = 0.01)
    k_hom_3 = axpolari3.arrow(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1)/2,0,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[2][0].real,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[2][0].imag, color = "red", width = 0.01)
    
    
    
    """
    A continuación se crean los sliders que permitirán variar el valor rms de las señales
    de voltaje.
    """
    
    axphase_v1 = fig.add_axes([0.1, 0.43, 0.28, 0.01], facecolor=axcolor)
    axrms_v1 = fig.add_axes([0.1, 0.45, 0.28, 0.01], facecolor=axcolor)
    
    axphase_v2 = fig.add_axes([0.1, 0.39, 0.28, 0.01], facecolor=axcolor)
    axrms_v2 = fig.add_axes([0.1, 0.41, 0.28, 0.01], facecolor=axcolor)
    
    axphase_v3 = fig.add_axes([0.1, 0.35, 0.28, 0.01], facecolor=axcolor)
    axrms_v3 = fig.add_axes([0.1, 0.37, 0.28, 0.01], facecolor=axcolor)
    
    sphase_v1 = Slider(axphase_v1, 'Phase_va', -180, 180, valinit=fase_voltaje, color ="blue") 
    srms_v1 = Slider(axrms_v1, 'rms_va', 0, 220, valinit=v_rms, color ="blue") 
    
    sphase_v2 = Slider(axphase_v2, 'Phase_vb', -180, 180, valinit=-120 + fase_voltaje, color ="green") 
    srms_v2 = Slider(axrms_v2, 'rms_vb', 0, 220, valinit=v_rms, color = "green") 
    
    sphase_v3 = Slider(axphase_v3, 'Phase_vc', -180, 180, valinit=120 + fase_voltaje, color = "red") 
    srms_v3 = Slider(axrms_v3, 'rms_vc', 0, 220, valinit=v_rms, color = "red") 
    
    
    """
    A continuación se crean los sliders que permitirán variar el valor rms de las señales
    de corriente.
    """
    
    axphase_i1 = fig.add_axes([0.62, 0.43, 0.28, 0.01], facecolor=axcolor)
    axrms_i1 = fig.add_axes([0.62, 0.45, 0.28, 0.01], facecolor=axcolor)
    
    axphase_i2 = fig.add_axes([0.62, 0.39, 0.28, 0.01], facecolor=axcolor)
    axrms_i2 = fig.add_axes([0.62, 0.41, 0.28, 0.01], facecolor=axcolor)
    
    axphase_i3 = fig.add_axes([0.62, 0.35, 0.28, 0.01], facecolor=axcolor)
    axrms_i3 = fig.add_axes([0.62, 0.37, 0.28, 0.01], facecolor=axcolor)
    
    sphase_i1 = Slider(axphase_i1, 'Phase_ia', -180, 180, valinit=fase_corriente, color ="blue") #CAMBIAR POR ANGULO INICIAL
    srms_i1 = Slider(axrms_i1, 'rms_ia', 0, 100, valinit=i_rms, color ="blue") #PONER i_rms en valinit
    
    sphase_i2 = Slider(axphase_i2, 'Phase_ib', -180, 180, valinit=-120 + fase_corriente, color ="green") #CAMBIAR POR ANG INICIAL
    srms_i2 = Slider(axrms_i2, 'rms_ib', 0, 100, valinit=i_rms, color = "green") #PONER i_rms en valinit
    
    sphase_i3 = Slider(axphase_i3, 'Phase_ic', -180, 180, valinit=120 + fase_corriente, color = "red") #CAMBIAR POR ANG INICIAL
    srms_i3 = Slider(axrms_i3, 'rms_ic', 0, 100, valinit=i_rms, color = "red") #PONER i_rms en valinit
    
    
    
    """
    A continuación se crea un diagrama de barras para representar la potencia activa,
    reactiva, aparente aritmética, aparente eficaz y aparente vectorial, según
    la norma IEEE 1459.
    """
    
    potencias = ["Active\nPower\nkW","Reactive\nPower\nkVAR","Apparent\nArithmetic\nPower\nkVA","Apparent\nVector\nPower\nkVA","Apparent\nEffective\nPower\nkVA"]
    valores = [tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[0]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[1]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[2]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[4]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[6]/1000]
    valores_ordenados = valores.copy()
    valores_ordenados.sort()
    valores_ordenados = np.abs(np.array(valores_ordenados))
    ax_bar = fig.add_axes([0.053,0.1,0.39,0.18])
    ax_bar.set_title("Powers")
    ax_bar.set_ylim(-(5/4)*valores_ordenados[-1],(5/4)*valores_ordenados[-1])
    graf_barras = ax_bar.bar(potencias,valores, width=0.4, color = ["orange","black","blue","#2B9B20","#C63729"])
    
    
    #Se insertan textos complementarios
    texto = fig.text(0.6,0.08,"Active power (P): " + str(round(valores[0],3)) + " kW\nReactive power (Q): " + str(round(valores[1],3)) + " kVAR\nArithmetic apparent power (Sa): " + str(round(valores[2],3)) + " kVA\nVector apparent power (Sv): " + str(round(valores[3],3)) + " kVA\nEffective apparent power (Se): " + str(round(valores[4],3))
                     + " kVA\nArithmetic power factor: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[3],3)) + "\nVector power factor: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[5],3))
                     + "\nEffective power factor: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[7],3)) + 
                     "\nUnbalanced power: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[8]/1000,3)) + " kVA")
    texto_corriente = fig.text(0.1,0.88,"Three-phase system (Phase voltages)", fontsize = 15)
    texto_voltajes = fig.text(0.61,0.88,"Three-phase system (Line currents)", fontsize = 15)
    
    
    def update(val):
        """
        Se actualizan los valores rms y de fase para las señales de voltaje y corriente
        según se mueva el slider.
        """
        rms_v1 = srms_v1.val
        phase_v1 = sphase_v1.val
        rms_v2 = srms_v2.val
        phase_v2 = sphase_v2.val
        rms_v3 = srms_v3.val
        phase_v3 = sphase_v3.val
        rms_i1 = srms_i1.val
        phase_i1 = sphase_i1.val
        rms_i2 = srms_i2.val
        phase_i2 = sphase_i2.val
        rms_i3 = srms_i3.val
        phase_i3 = sphase_i3.val
        
        
        """
        Se actualizan las señales de corriente y voltaje en el tiempo con los nuevos
        valores rms y de fase.
        """
        
        #Voltajes
        l1.set_ydata(np.sqrt(2) * rms_v1 * np.cos(2*np.pi*f0*t + np.deg2rad(phase_v1)))
        l2.set_ydata(np.sqrt(2) * rms_v2 * np.cos(2*np.pi*f0*t + np.deg2rad(phase_v2)))
        l3.set_ydata(np.sqrt(2) * rms_v3 * np.cos(2*np.pi*f0*t + np.deg2rad(phase_v3)))
        
        #Corrientes
        k1.set_ydata(np.sqrt(2) * rms_i1 * np.cos(2*np.pi*f0*t + np.deg2rad(phase_i1)))
        k2.set_ydata(np.sqrt(2) * rms_i2 * np.cos(2*np.pi*f0*t + np.deg2rad(phase_i2)))
        k3.set_ydata(np.sqrt(2) * rms_i3 * np.cos(2*np.pi*f0*t + np.deg2rad(phase_i3)))
        
        
        """
        Se actualizan las representaciones fasoriales del sistema desbalanceado y las
        componentes simétricas para los nuevos valores rms y de fase.
        """
        
        #VOLTAJES
        
        v1 = rms_v1*np.exp(1j*np.deg2rad(phase_v1))
        v2 = rms_v2*np.exp(1j*np.deg2rad(phase_v2))
        v3 = rms_v3*np.exp(1j*np.deg2rad(phase_v3))
        
        #Sistema desbalanceado
        l1_fasor = axpolar_voltajes.clear()
        axpolar_voltajes.set_xlim(-310,310)
        axpolar_voltajes.set_ylim(-310,310)
        axpolar_voltajes.set_title("Phasors", pad = 5)
        l1_fasor = axpolar_voltajes.arrow(0,0,v1.real,v1.imag, color = "blue", width = 0.01)
        l2_fasor = axpolar_voltajes.arrow(0,0,v2.real,v2.imag, color = "green", width = 0.01)
        l3_fasor = axpolar_voltajes.arrow(0,0,v3.real,v3.imag, color = "red", width = 0.01)
        
        
        #Grafica de la secuencia positiva
        l_pos_1 = axpolarv1.clear()
        axpolarv1.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1)
        axpolarv1.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(v1,v2,v3)[0][0])+1)
        axpolarv1.set_title("Positive sequence", pad = 5)
        l_pos_1 = axpolarv1.arrow(0,0,tf.sec_positiva_fortescue(v1,v2,v3)[0][0].real,tf.sec_positiva_fortescue(v1,v2,v3)[0][0].imag, color = "blue", width = 0.01)
        l_pos_2 = axpolarv1.arrow(0,0,tf.sec_positiva_fortescue(v1,v2,v3)[1][0].real,tf.sec_positiva_fortescue(v1,v2,v3)[1][0].imag, color = "green", width = 0.01)
        l_pos_3 = axpolarv1.arrow(0,0,tf.sec_positiva_fortescue(v1,v2,v3)[2][0].real,tf.sec_positiva_fortescue(v1,v2,v3)[2][0].imag, color = "red", width = 0.01)
        
        
        #Grafica de la secuencia negativa
        l_neg_1 = axpolarv2.clear()
        axpolarv2.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1)
        axpolarv2.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(v1,v2,v3)[0][0])+1)
        axpolarv2.set_title("Negative sequence", pad = 5)
        l_neg_1 = axpolarv2.arrow(0,0,tf.sec_negativa_fortescue(v1,v2,v3)[0][0].real,tf.sec_negativa_fortescue(v1,v2,v3)[0][0].imag, color = "blue", width = 0.01)
        l_neg_2 = axpolarv2.arrow(0,0,tf.sec_negativa_fortescue(v1,v2,v3)[1][0].real,tf.sec_negativa_fortescue(v1,v2,v3)[1][0].imag, color = "green", width = 0.01)
        l_neg_3 = axpolarv2.arrow(0,0,tf.sec_negativa_fortescue(v1,v2,v3)[2][0].real,tf.sec_negativa_fortescue(v1,v2,v3)[2][0].imag, color = "red", width = 0.01)
        
        
        #Grafica de la secuencia cero
        l_hom_1 = axpolarv3.clear()
        axpolarv3.set_title("Zero sequence", pad = 5)
        axpolarv3.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(v1,v2,v3)[0][0])+1)
        axpolarv3.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(v1,v2,v3)[0][0])+1)
        l_hom_1 = axpolarv3.arrow(0,0,tf.sec_homopolar(v1,v2,v3)[0][0].real,tf.sec_homopolar(v1,v2,v3)[0][0].imag, color = "blue", width = 0.01)
        l_hom_2 = axpolarv3.arrow(((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1)/2,0,tf.sec_homopolar(v1,v2,v3)[1][0].real,tf.sec_homopolar(v1,v2,v3)[1][0].imag, color = "green", width = 0.01)
        l_hom_3 = axpolarv3.arrow(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(v1,v2,v3)[0][0])+1)/2,0,tf.sec_homopolar(v1,v2,v3)[2][0].real,tf.sec_homopolar(v1,v2,v3)[2][0].imag, color = "red", width = 0.01)
            
        
        
        #CORRIENTES
        
        i1 = rms_i1*np.exp(1j*np.deg2rad(phase_i1))
        i2 = rms_i2*np.exp(1j*np.deg2rad(phase_i2))
        i3 = rms_i3*np.exp(1j*np.deg2rad(phase_i3))
        
        #Sistema desbalanceado
        k1_fasor = axpolar_corrientes.clear()
        axpolar_corrientes.set_xlim(-140,140)
        axpolar_corrientes.set_ylim(-140,140)
        axpolar_corrientes.set_title("Phasors", pad = 5)
        k1_fasor = axpolar_corrientes.arrow(0,0,i1.real,i1.imag, color = "blue", width = 0.01)
        k2_fasor = axpolar_corrientes.arrow(0,0,i2.real,i2.imag, color = "green", width = 0.01)
        k3_fasor = axpolar_corrientes.arrow(0,0,i3.real,i3.imag, color = "red", width = 0.01)
        
        
        #Grafica de la secuencia positiva
        k_pos_2 = axpolari1.clear()
        axpolari1.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1)
        axpolari1.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_positiva_fortescue(i1,i2,i3)[0][0])+1)
        axpolari1.set_title("Positive sequence", pad = 5)
        k_pos_1 = axpolari1.arrow(0,0,tf.sec_positiva_fortescue(i1,i2,i3)[0][0].real,tf.sec_positiva_fortescue(i1,i2,i3)[0][0].imag, color = "blue", width = 0.01)
        k_pos_2 = axpolari1.arrow(0,0,tf.sec_positiva_fortescue(i1,i2,i3)[1][0].real,tf.sec_positiva_fortescue(i1,i2,i3)[1][0].imag, color = "green", width = 0.01)
        k_pos_3 = axpolari1.arrow(0,0,tf.sec_positiva_fortescue(i1,i2,i3)[2][0].real,tf.sec_positiva_fortescue(i1,i2,i3)[2][0].imag, color = "red", width = 0.01)
        
        
        #Grafica de la secuencia negativa
        k_neg_1 = axpolari2.clear()
        axpolari2.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1)
        axpolari2.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_negativa_fortescue(i1,i2,i3)[0][0])+1)
        axpolari2.set_title("Negative sequence", pad = 5)
        k_neg_1 = axpolari2.arrow(0,0,tf.sec_negativa_fortescue(i1,i2,i3)[0][0].real,tf.sec_negativa_fortescue(i1,i2,i3)[0][0].imag, color = "blue", width = 0.01)
        k_neg_2 = axpolari2.arrow(0,0,tf.sec_negativa_fortescue(i1,i2,i3)[1][0].real,tf.sec_negativa_fortescue(i1,i2,i3)[1][0].imag, color = "green", width = 0.01)
        k_neg_3 = axpolari2.arrow(0,0,tf.sec_negativa_fortescue(i1,i2,i3)[2][0].real,tf.sec_negativa_fortescue(i1,i2,i3)[2][0].imag, color = "red", width = 0.01)
        
        
        #Grafica de la secuencia cero
        k_hom_1 = axpolari3.clear()
        axpolari3.set_title("Zero sequence", pad = 5)
        axpolari3.set_xlim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0])+1)
        axpolari3.set_ylim(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1),np.abs((5/4)*np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0])+1)
        k_hom_1 = axpolari3.arrow(0,0,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0].real,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[0][0].imag, color = "blue", width = 0.01)
        k_hom_2 = axpolari3.arrow(((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1)/2,0,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[1][0].real,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[1][0].imag, color = "green", width = 0.01)
        k_hom_3 = axpolari3.arrow(-((5/4)*np.sqrt(2)*np.abs(tf.sec_homopolar(i1,i2,i3)[0][0])+1)/2,0,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[2][0].real,np.sqrt(2)*tf.sec_homopolar(i1,i2,i3)[2][0].imag, color = "red", width = 0.01)
        
        
        """
        Se actualiza el gráfico de barras con los nuevos valores de potencia.
        """
    
        graf_barras = ax_bar.clear()
        valores = [tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[0]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[1]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[2]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[4]/1000,tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[6]/1000]
        valores_ordenados = valores.copy()
        valores_ordenados.sort()
        valores_ordenados = np.abs(np.array(valores_ordenados))
        ax_bar.set_title("Powers")
        ax_bar.set_ylim(-(5/4)*valores_ordenados[-1],(5/4)*valores_ordenados[-1])
        graf_barras = ax_bar.bar(potencias,valores, width=0.4, color = ["orange","black","blue","#2B9B20","#C63729"])
        
        #Se actualizan los valores de potencia en el texto
        texto.set_text("Active power (P): " + str(round(valores[0],3)) + " kW\nReactive power (Q): " + str(round(valores[1],3)) + " kVAR\nArithmetic apparent power (Sa): " + str(round(valores[2],3)) + " kVA\nVector apparent power (Sv): " + str(round(valores[3],3)) + " kVA\nEffective apparent power (Se): " + str(round(valores[4],3))
                     + " kVA\nArithmetic power factor: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[3],3)) + "\nVector power factor: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[5],3))
                     + "\nEffective power factor: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[7],3)) + 
                     "\nUnbalanced power: " + str(round(tf.calcula_potencias(v1,v2,v3,i1,i2,i3)[8]/1000,3)) + " kVA")
    
    
    
    """
    Se actualizan los valores rms y de fase moviendo los sliders.
    """
    sphase_v1.on_changed(update)
    srms_v1.on_changed(update)
    sphase_v2.on_changed(update)
    srms_v2.on_changed(update)
    sphase_v3.on_changed(update)
    srms_v3.on_changed(update)
    
    sphase_i1.on_changed(update)
    srms_i1.on_changed(update)
    sphase_i2.on_changed(update)
    srms_i2.on_changed(update)
    sphase_i3.on_changed(update)
    srms_i3.on_changed(update)
    
    
    plt.show()
