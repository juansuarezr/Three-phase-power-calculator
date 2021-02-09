# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:59:55 2020

@author: Juan Pablo
"""

import numpy as np
import pandas as pd
import sympy as sym
import matplotlib.pyplot as plt


headers_v = ['Harmonic_order','Voltage_A','Phase_A','Voltage_B','Phase_B','Voltage_C','Phase_C']


headers_i = ['Harmonic_order','Current_A','Phase_A','Current_B','Phase_B','Current_C','Phase_C']



def effective_voltages(Voltages_frame,ksi=1):
    """
    

    Parameters
    ----------
    Voltages_frame : TYPE
        DESCRIPTION.
    ksi : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    list_ef_voltages : TYPE
        DESCRIPTION.

    """

    list_ef_voltages = [0,0,0]
    for i in range(len(Voltages_frame)):
        V_a = Voltages_frame['Voltage_A'][i]*np.exp(np.deg2rad(Voltages_frame['Phase_A'][i])*1j)
        V_b = Voltages_frame['Voltage_B'][i]*np.exp(np.deg2rad(Voltages_frame['Phase_B'][i])*1j)
        V_c = Voltages_frame['Voltage_C'][i]*np.exp(np.deg2rad(Voltages_frame['Phase_C'][i])*1j)
        list_ef_voltages[0] += (3*(np.abs(V_a)**2 + np.abs(V_b)**2 + np.abs(V_c)**2)+ ksi*(np.abs(V_a-V_b)**2 + np.abs(V_b-V_c)**2 + np.abs(V_c-V_a)**2))/(9*(ksi+1))
        if i == 0:
            list_ef_voltages[1] += (3*(np.abs(V_a)**2 + np.abs(V_b)**2 + np.abs(V_c)**2)+ ksi*(np.abs(V_a-V_b)**2 + np.abs(V_b-V_c)**2 + np.abs(V_c-V_a)**2))/(9*(ksi+1))
        else:
            list_ef_voltages[2] += (3*(np.abs(V_a)**2 + np.abs(V_b)**2 + np.abs(V_c)**2)+ ksi*(np.abs(V_a-V_b)**2 + np.abs(V_b-V_c)**2 + np.abs(V_c-V_a)**2))/(9*(ksi+1))
        
    for i in range(len(list_ef_voltages)):
        list_ef_voltages[i] = np.sqrt(list_ef_voltages[i])
        
    return list_ef_voltages



def effective_currents(Currents_frame,rho=1):
    """
    

    Parameters
    ----------
    Currents_frame : TYPE
        DESCRIPTION.
    rho : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    list_ef_currents : TYPE
        DESCRIPTION.

    """

    list_ef_currents = [0,0,0]
    for i in range(len(Currents_frame)):
        I_a = Currents_frame['Current_A'][i]*np.exp(np.deg2rad(Currents_frame['Phase_A'][i])*1j)
        I_b = Currents_frame['Current_B'][i]*np.exp(np.deg2rad(Currents_frame['Phase_B'][i])*1j)
        I_c = Currents_frame['Current_C'][i]*np.exp(np.deg2rad(Currents_frame['Phase_C'][i])*1j)
        I_n = I_a + I_b + I_c
        list_ef_currents[0] += (1/3)*(np.abs(I_a)**2 + np.abs(I_b)**2 + np.abs(I_c)**2 + rho*np.abs(I_n)**2)
        if i == 0:
            list_ef_currents[1] += (1/3)*(np.abs(I_a)**2 + np.abs(I_b)**2 + np.abs(I_c)**2 + rho*np.abs(I_n)**2)
        else:
            list_ef_currents[2] += (1/3)*(np.abs(I_a)**2 + np.abs(I_b)**2 + np.abs(I_c)**2 + rho*np.abs(I_n)**2)
    
    for i in range(len(list_ef_currents)):
        list_ef_currents[i] = np.sqrt(list_ef_currents[i])
        
    return list_ef_currents



def Total_Harmonic_Distrotion(Fundamental,Harmonic):
    """
    

    Parameters
    ----------
    Fundamental : TYPE
        DESCRIPTION.
    Harmonic : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return Harmonic/Fundamental

def apparent_power(Voltage,Current):
    """
    

    Parameters
    ----------
    Voltage : TYPE
        DESCRIPTION.
    Current : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return 3*Voltage*Current

def Harmonic_distortion_powers(Voltages_list,Currents_list):
    """
    

    Parameters
    ----------
    Voltages_list : TYPE
        DESCRIPTION.
    Currents_list : TYPE
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """

    #return [Current_dist_power,Voltage_dist_power,harmonic_apparent_power]
    
    return [apparent_power(Voltages_list[1],Currents_list[2]),apparent_power(Voltages_list[2],Currents_list[1]),apparent_power(Voltages_list[2],Currents_list[2])]

def unbalanced_power(harmonic_distortion_powers):
    """
    

    Parameters
    ----------
    harmonic_distortion_powers : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    powers_sum = 0
    for i in harmonic_distortion_powers:
        powers_sum = i**2
    return np.sqrt(powers_sum)


def rms_voltages(Voltages_frame):

    rms_list = [0,0,0]
    order = {0:'Voltage_A',1:'Voltage_B',2:'Voltage_C'}
    for i in range(len(rms_list)):
        for j in Voltages_frame[order[i]]:
            rms_list[i] += (j)**2
            
    for i in range(len(rms_list)):
        rms_list[i] = np.sqrt(rms_list[i])
        
    return rms_list


def rms_currents(Currents_frame):

    rms_list = [0,0,0]
    order = {0:'Current_A',1:'Current_B',2:'Current_C'}
    for i in range(len(rms_list)):
        for j in Currents_frame[order[i]]:
            rms_list[i] += (j)**2
            
    for i in range(len(rms_list)):
        rms_list[i] = np.sqrt(rms_list[i])
        
    return rms_list


def active_powers(Voltages_frame,Currents_frame):

    power_sum = [0,0,0]
    order_v = {0:'Voltage_A',1:'Voltage_B',2:'Voltage_C'}
    order_i = {0:'Current_A',1:'Current_B',2:'Current_C'}
    order_phases = {0:'Phase_A',1:'Phase_B',2:'Phase_C'}

    for i in range(len(power_sum)):
        for j in range(len(Voltages_frame[order_v[i]])):
            power_sum[i] += Voltages_frame[order_v[i]][j]*Currents_frame[order_i[i]][j]*np.cos(np.deg2rad(Currents_frame[order_phases[i]][j]-Voltages_frame[order_phases[i]][j]))
        
    return power_sum
    

def power_factor(Active_power,Apparent_power):
    return Active_power/Apparent_power


def Distorted_voltages(Voltages_frame,f=60):
    t = sym.symbols('t')

    signals = [0,0,0]
    for i in range(len(signals)):
        order_v = {0:'Voltage_A',1:'Voltage_B',2:'Voltage_C'}
        order_phases = {0:'Phase_A',1:'Phase_B',2:'Phase_C'}
        for j in range(len(Voltages_frame[order_v[i]])):
            signals[i] += np.sqrt(2)*Voltages_frame[order_v[i]][j]*sym.cos(Voltages_frame['Harmonic_order'][j]*2*np.pi*f*t + np.deg2rad(Voltages_frame[order_phases[i]][j]))
    for i in range(len(signals)):
        signals[i] = sym.lambdify(t,signals[i],"numpy")
    
    return signals


def Distorted_currents(Currents_frame,f=60):
    t = sym.symbols('t')

    signals = [0,0,0]
    for i in range(len(signals)):
        order_i = {0:'Current_A',1:'Current_B',2:'Current_C'}
        order_phases = {0:'Phase_A',1:'Phase_B',2:'Phase_C'}
        for j in range(len(Currents_frame[order_i[i]])):
            signals[i] += np.sqrt(2)*Currents_frame[order_i[i]][j]*sym.cos(Currents_frame['Harmonic_order'][j]*2*np.pi*f*t + np.deg2rad(Currents_frame[order_phases[i]][j]))
    for i in range(len(signals)):
        signals[i] = sym.lambdify(t,signals[i],"numpy")
    
    return signals


def Arithmetic_power(voltages_list_rms,currents_list_rms):
    Arithmetic_power = 0
    for i in range(len(voltages_list_rms)):
        Arithmetic_power += voltages_list_rms[i]*currents_list_rms[i]
    return Arithmetic_power
        

def reactive_powers(Voltages_frame,Currents_frame):

    power_sum = [0,0,0]
    order_v = {0:'Voltage_A',1:'Voltage_B',2:'Voltage_C'}
    order_i = {0:'Current_A',1:'Current_B',2:'Current_C'}
    order_phases = {0:'Phase_A',1:'Phase_B',2:'Phase_C'}

    for i in range(len(power_sum)):
        for j in range(len(Voltages_frame[order_v[i]])):
            power_sum[i] += Voltages_frame[order_v[i]][j]*Currents_frame[order_i[i]][j]*np.sin(np.deg2rad(Voltages_frame[order_phases[i]][j]-Currents_frame[order_phases[i]][j]))
        
    return power_sum
    

def Distortion_powers(voltages_list_rms,currents_list_rms,active_powers,reactive_powers):
    distortion_powers = [0,0,0]
    for i in range(len(distortion_powers)):
        distortion_powers[i] += np.sqrt((voltages_list_rms[i]*currents_list_rms[i])**2 - active_powers[i]**2 - reactive_powers[i]**2)
    return distortion_powers


def vectorial_power(active_powers,reactive_powers,distortion_powers):
    active = 0
    reactive = 0
    distortion = 0
    for i in active_powers:
        active += i
    for i in reactive_powers:
        reactive += i
    for i in distortion_powers:
        distortion += i
        
    return np.sqrt(active**2 + reactive**2 + distortion**2)

"""
headers_i = ['Harmonic_order','Current_A','Phase_A','Current_B','Phase_B','Current_C','Phase_C']
#Currents_frame = pd.read_csv('Currents.txt',names=headers_i,sep=',')
print(effective_currents(pd.read_csv('Currents.txt',names=headers_i,sep=',')))
"""