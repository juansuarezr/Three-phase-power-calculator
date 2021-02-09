# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:29:40 2020

@author: Juan Pablo
"""


import matplotlib.pyplot as plt
import numpy as np
import Modulo_calculos as mc
import pandas as pd

def ThreePhaseNonSinusoidal(VoltageFile,CurrentFile):
    headers_v = ['Harmonic_order','Voltage_A','Phase_A','Voltage_B','Phase_B','Voltage_C','Phase_C']
    Voltages_frame = pd.read_csv(VoltageFile,names=headers_v,sep=',')
    
    
    headers_i = ['Harmonic_order','Current_A','Phase_A','Current_B','Phase_B','Current_C','Phase_C']
    Currents_frame = pd.read_csv(CurrentFile,names=headers_i,sep=',')
    
    f0 = 60
    tiempo = np.linspace(0,2/f0,1000)
    fig = plt.figure(figsize = (12,8))
    
    
    #Voltages in the time domain
    ax_voltages_time = fig.add_axes([0.1,0.7,0.35,0.19], ylabel = "$Voltage (V)$", xlabel = "$Time (s)$")
    Va = mc.Distorted_voltages(Voltages_frame)[0]
    Vb = mc.Distorted_voltages(Voltages_frame)[1]
    Vc = mc.Distorted_voltages(Voltages_frame)[2]
    ax_voltages_time.plot(tiempo,Va(tiempo), color = "#05077C", label = "va")
    ax_voltages_time.plot(tiempo,Vb(tiempo), color = "#DC3929", label = "vb")
    ax_voltages_time.plot(tiempo,Vc(tiempo), color = "#0C9540", label = "vc")
    ax_voltages_time.legend(loc='upper right')
    ax_voltages_time.set_title("Phase Voltages")
    
    
    #Currents in the time domain
    ax_currents_time = fig.add_axes([0.55,0.7,0.35,0.19], ylabel = "$Current(A)$", xlabel = "$Time(s)$")
    Ia = mc.Distorted_currents(Currents_frame)[0]
    Ib = mc.Distorted_currents(Currents_frame)[1]
    Ic = mc.Distorted_currents(Currents_frame)[2]
    ax_currents_time.plot(tiempo,Ia(tiempo), color = "#05077C",label = "ia")
    ax_currents_time.plot(tiempo,Ib(tiempo), color = "#DC3929", label = "ib")
    ax_currents_time.plot(tiempo,Ic(tiempo), color = "#0C9540", label = "ic")
    ax_currents_time.legend(loc='upper right')
    ax_currents_time.set_title("Line Currents")
    
    
    
    #Frequency spectrum for the voltages
    ax_voltage_frequency = fig.add_axes([0.1,0.4,0.8,0.19], ylabel = "$RMS\:voltage(V)$", xlabel = "$Harmonic$")
    bar_V = []
    harmonics_v = list(range(Voltages_frame['Harmonic_order'][0],Voltages_frame['Harmonic_order'][len(Voltages_frame['Harmonic_order'])-1]+1))
        
    for i in range(3):
        order_v = {0:'Voltage_A',1:'Voltage_B',2:'Voltage_C'}
        lista = []
        for j in harmonics_v:
            if j in list(Voltages_frame['Harmonic_order']):
                lista.append(list(Voltages_frame[order_v[i]])[list(Voltages_frame['Harmonic_order']).index(j)])
            else:
                lista.append(0)
        bar_V.append(lista)
    
    barWidth = 0.25
    
    r1 = np.arange(len(bar_V[0][1:]))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    ax_voltage_frequency.bar(r1, bar_V[0][1:], color='#05077C', width=barWidth, edgecolor='white', label='va')
    ax_voltage_frequency.bar(r2, bar_V[1][1:], color='#DC3929', width=barWidth, edgecolor='white', label='vb')
    ax_voltage_frequency.bar(r3, bar_V[2][1:], color='#0C9540', width=barWidth, edgecolor='white', label='vc')
    ax_voltage_frequency.legend(loc='upper right')
    ax_voltage_frequency.set_title("Frequency spectrum (Voltages)")
    plt.xticks([r + barWidth for r in range(len(bar_V[0][1:]))], harmonics_v[1:])
    
    #Frequency spectrum for the currents
    
    ax_current_frequency = fig.add_axes([0.1,0.1,0.8,0.19], ylabel = "$RMS\:Current(A)$", xlabel = "$Harmonic$")
    bar_I = []
    harmonics_i = list(range(Currents_frame['Harmonic_order'][0],Currents_frame['Harmonic_order'][len(Currents_frame['Harmonic_order'])-1]+1))
        
    for i in range(3):
        order_i = {0:'Current_A',1:'Current_B',2:'Current_C'}
        lista = []
        for j in harmonics_i:
            if j in list(Currents_frame['Harmonic_order']):
                lista.append(list(Currents_frame[order_i[i]])[list(Currents_frame['Harmonic_order']).index(j)])
            else:
                lista.append(0)
        bar_I.append(lista)
    
    barWidth = 0.25
    
    r1 = np.arange(len(bar_V[0][1:]))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    ax_current_frequency.bar(r1, bar_I[0][1:], color='#05077C', width=barWidth, edgecolor='white', label='ia')
    ax_current_frequency.bar(r2, bar_I[1][1:], color='#DC3929', width=barWidth, edgecolor='white', label='ib')
    ax_current_frequency.bar(r3, bar_I[2][1:], color='#0C9540', width=barWidth, edgecolor='white', label='ic')
    ax_current_frequency.legend(loc='upper right')
    ax_current_frequency.set_title("Frequency spectrum (Currents)")
    plt.xticks([r + barWidth for r in range(len(bar_I[0][1:]))], harmonics_i[1:])
    
    
    
    plt.show()
    
def GenerateCSV(VoltageFile,CurrentFile):
    headers_v = ['Harmonic_order','Voltage_A','Phase_A','Voltage_B','Phase_B','Voltage_C','Phase_C']
    Voltages_frame = pd.read_csv(VoltageFile,names=headers_v,sep=',')
    
    
    headers_i = ['Harmonic_order','Current_A','Phase_A','Current_B','Phase_B','Current_C','Phase_C']
    Currents_frame = pd.read_csv(CurrentFile,names=headers_i,sep=',')
    effective_voltage = mc.effective_voltages(Voltages_frame)[0]
    effective_current = mc.effective_currents(Currents_frame)[0]
    fundamental_voltage = mc.effective_voltages(Voltages_frame)[1]
    fundamental_current = mc.effective_currents(Currents_frame)[1]
    harmonic_voltage = mc.effective_voltages(Voltages_frame)[2]
    harmonic_current = mc.effective_currents(Currents_frame)[2]
    total_harmonic_distortion_v = harmonic_voltage/fundamental_voltage
    total_harmonic_distortion_i = harmonic_current/fundamental_current
    active_power_a = mc.active_powers(Voltages_frame,Currents_frame)[0]
    active_power_b = mc.active_powers(Voltages_frame,Currents_frame)[1]
    active_power_c = mc.active_powers(Voltages_frame,Currents_frame)[2]
    total_active_power = active_power_a+active_power_b+active_power_c
    reactive_power_a = mc.reactive_powers(Voltages_frame,Currents_frame)[0]
    reactive_power_b = mc.reactive_powers(Voltages_frame,Currents_frame)[1]
    reactive_power_c = mc.reactive_powers(Voltages_frame,Currents_frame)[2]
    total_reactive_power = reactive_power_a+reactive_power_b+reactive_power_c    
    fundamental_apparent_power = mc.apparent_power(fundamental_voltage,fundamental_current)
    current_distortion_power = mc.Harmonic_distortion_powers(mc.effective_voltages(Voltages_frame),mc.effective_currents(Currents_frame))[0]
    voltage_distortion_power = mc.Harmonic_distortion_powers(mc.effective_voltages(Voltages_frame),mc.effective_currents(Currents_frame))[1]
    harmonic_apparent_power = mc.Harmonic_distortion_powers(mc.effective_voltages(Voltages_frame),mc.effective_currents(Currents_frame))[2]
    unbalanced_power = mc.unbalanced_power(mc.Harmonic_distortion_powers(mc.effective_voltages(Voltages_frame),mc.effective_currents(Currents_frame)))
    effective_apparent_power = 3*effective_voltage*effective_current
    arithmetic_apparent_power = mc.Arithmetic_power(mc.rms_voltages(Voltages_frame),mc.rms_currents(Currents_frame))
    vector_apparent_power = mc.vectorial_power(mc.active_powers(Voltages_frame,Currents_frame),mc.reactive_powers(Voltages_frame,Currents_frame),mc.Distortion_powers(mc.rms_voltages(Voltages_frame),mc.rms_currents(Currents_frame),mc.active_powers(Voltages_frame,Currents_frame),mc.reactive_powers(Voltages_frame,Currents_frame)))
    effective_power_factor = total_active_power/effective_apparent_power
    arithmetic_power_factor = total_active_power/arithmetic_apparent_power
    vector_power_factor = total_active_power/vector_apparent_power
    
    Calculations = {'Variable':['Effective voltage',
                                'Effective current',
                                'Total Harmonic Distortion (V)',
                                'Total Harmonic Distortion (I)',
                                'Active power', 
                                'Reactive power',
                                'Fundamental effective apparent power',
                                'Current distortion power',
                                'Voltage distortion power',
                                'Harmonic apparent power',
                                'Unbalanced power',
                                'Effective apparent power',
                                'Arithmetic apparent power',
                                'Vector apparent power',
                                'Effective power factor',
                                'Arithmetic power factor',
                                'Vector power factor'],
                    'Value':[effective_voltage,
                             effective_current,
                             total_harmonic_distortion_v,
                             total_harmonic_distortion_i,
                             total_active_power,
                             total_reactive_power,
                             fundamental_apparent_power,
                             current_distortion_power,
                             voltage_distortion_power,
                             harmonic_apparent_power,
                             unbalanced_power,
                             effective_apparent_power,
                             arithmetic_apparent_power,
                             vector_apparent_power,
                             effective_power_factor,
                             arithmetic_power_factor,
                             vector_power_factor]}
    
    df = pd.DataFrame(Calculations, columns = ['Variable', 'Value'])
    df.to_csv('archivo.csv')
    return df


