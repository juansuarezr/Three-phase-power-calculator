# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:03:16 2020

@author: Juan Pablo
"""


import numpy as np


"""
TRANSFORMADA DE FORTESCUE
"""

op_alpha = np.exp(1j*np.deg2rad(120)) #rota un fasor 120°

matriz_fortescue = (1/3)*np.array([[1,1,1],[1,op_alpha,op_alpha**2],[1,op_alpha**2,op_alpha]])


def sec_positiva_fortescue(fasor_1,fasor_2,fasor_3):
    """
    

    Parameters
    ----------
    f1 : TYPE. complex
        
    f2 : TYPE. complex
        
    f3 : TYPE. complex
    
        LOS PARAMETROS CORRESPONDEN A LOS TRES FASORES DE UN SISTEMA TRIFASICO
        
    Returns
    -------
    list
        DESCRIPTION. RETORNA UNA LISTA CON LOS TRES FASORES DE LA SECUENCIA POSITIVA 
        DE LA TRANSFORMADA DE FORTESCUE.

    """
    vec_tensiones = np.array([[fasor_1],[fasor_2],[fasor_3]])
    
    vec_resultante = matriz_fortescue@vec_tensiones
    
    va1 = vec_resultante[1][0]
    vb1 = va1*op_alpha**2
    vc1 = va1*op_alpha
    
    return np.array([[va1],[vb1],[vc1]])


def sec_negativa_fortescue(fasor_1,fasor_2,fasor_3):
    """
    

    Parameters
    ----------
    f1 : TYPE. complex
        
    f2 : TYPE. complex
        
    f3 : TYPE. complex
    
        LOS PARAMETROS CORRESPONDEN A LOS TRES FASORES DE UN SISTEMA TRIFASICO
        
    Returns
    -------
    list
        DESCRIPTION. RETORNA UNA LISTA CON LOS TRES FASORES DE LA SECUENCIA NEGATIVA
        DE LA TRANSFORMADA DE FORTESCUE.

    """
    vec_tensiones = np.array([[fasor_1],[fasor_2],[fasor_3]])
    
    vec_resultante = matriz_fortescue@vec_tensiones
    
    va2 = vec_resultante[2][0]
    vb2 = va2*op_alpha
    vc2 = va2*op_alpha**2
    
    return np.array([[va2],[vb2],[vc2]])

def sec_homopolar(fasor_1,fasor_2,fasor_3):
    """
    

    Parameters
    ----------
    f1 : TYPE. complex
        
    f2 : TYPE. complex
        
    f3 : TYPE. complex
    
        LOS PARAMETROS CORRESPONDEN A LOS TRES FASORES DE UN SISTEMA TRIFASICO
        
    Returns
    -------
    list
        DESCRIPTION. RETORNA UNA LISTA CON LOS TRES FASORES DE LA SECUENCIA CERO
        DE LA TRANSFORMADA DE FORTESCUE.

    """
    
    vec_tensiones = np.array([[fasor_1],[fasor_2],[fasor_3]])
    
    vec_resultante = matriz_fortescue@vec_tensiones
    
    va0 = vec_resultante[0][0]
    vb0 = va0
    vc0 = va0
    
    return np.array([[va0],[vb0],[vc0]])


def corriente_eficaz(i1,i2,i3,rho=1):
    """
    

    Parameters
    ----------
    i1 : TYPE. complex
        
    i2 : TYPE. complex
        
    i3 : TYPE. complex
    
    rho : TYPE. float
        según la norma 1459 de la IEEE numeral 3.2.2.8 rho se define como el cociente entre
        la resistencia del neutro y la resistencia de linea.
        (de no ser conocido el valor exacto de rho se recomienda usar rho=1)
        
        LOS PARAMETROS CORRESPONDEN A LAS FORMAS FASORIALES DE LAS CORRIENTES DE UN SISTEMA TRIFÁSICO
         
    Returns
    -------
    complex
    
        RETORNA EL VALOR DE LA CORRIENTE EFICAZ MEDIANTE LA DEFINICIÓN DADA EN LA NORMA 1459
        DE LA IEEE NUMERAL 3.2.2.8
        

    """    
    
    return np.sqrt(np.abs(sec_positiva_fortescue(i1,i2,i3)[0][0])**2 + np.abs(sec_negativa_fortescue(i1,i2,i3)[0][0])**2 + (1+3*rho)*(np.abs(sec_homopolar(i1,i2,i3)[0][0])**2))

def voltage_eficaz(v1,v2,v3,ksi=1):
    
    """
    

    Parameters
    ----------
    v1 : TYPE. complex
        
    v2 : TYPE. complex
        
    v3 : TYPE. complex
    
    ksi : TYPE. float
        el valor de ksi se calcula según la norma 1459 de la IEEE numeral 3.2.2.8
        (de no ser conocido el valor exacto de ksi se recomienda usar ksi=1)
        
        LOS PARAMETROS CORRESPONDEN A LAS FORMAS FASORIALES DE LOS VOLTAJES DE UN SISTEMA TRIFÁSICO
         
    Returns
    -------
    complex
    
        RETORNA EL VALOR DEL VOLTAJE EFICAZ MEDIANTE LA DEFINICIÓN DADA EN LA NORMA 1459
        DE LA IEEE NUMERAL 3.2.2.8
        

    """      
    return np.sqrt(np.abs(sec_positiva_fortescue(v1,v2,v3)[0][0])**2 + np.abs(sec_negativa_fortescue(v1,v2,v3)[0][0])**2 + (np.abs(sec_homopolar(v1,v2,v3)[0][0])**2)/(1+ksi))

def calcula_potencias(v1,v2,v3,i1,i2,i3):
    
    '''
        Parameters
    ----------
    v1 : TYPE. complex
        
    v2 : TYPE. complex
        
    v3 : TYPE. complex
    
    i1 : TYPE. complex
    
    i2 : TYPE. complex
    
    i3 : TYPE. complex
    
        LOS PARAMETROS CORRESPONDEN A LOS SEIS FASORES (CORRIENTES Y VOLTAJES) DE UN SISTEMA TRIFÁSICO
        CUALQUIERA
        
    Returns
    -------
    list
        DESCRIPTION. RETORNA UNA LISTA CON LOS VALORES DE LAS DIFERENTES POTENCIAS ASOCIADAS AL SISTEMA
        TRIFÁSICO QUE LA FUNCIÓN TOMA COMO ARGUMENTO, DICHAS POTENCIAS SE ENCUENTRAN EN EL SIGUIENTE ORDEN
        
        [potencia_activa_total, potencia_reactiva_total, potencia_aparente_aritmetica...
        ..., factor_potencia_aritmetica, potencia_aparente_vectorial, factor_potencia_vectorial...
        ..., potencia_aparente_eficaz, factor_potencia_eficaz]
    '''
    
    voltajes_positiva = sec_positiva_fortescue(v1,v2,v3)
    corrientes_positiva = sec_positiva_fortescue(i1,i2,i3)
    potencia_positiva_activa = 3*np.abs(voltajes_positiva[0][0])*np.abs(corrientes_positiva[0][0])*np.cos(np.angle(voltajes_positiva[0][0])-np.angle(corrientes_positiva[0][0]))
    potencia_positiva_reactiva = 3*np.abs(voltajes_positiva[0][0])*np.abs(corrientes_positiva[0][0])*np.sin(np.angle(voltajes_positiva[0][0])-np.angle(corrientes_positiva[0][0]))
  
    voltajes_negativa = sec_negativa_fortescue(v1,v2,v3)
    corrientes_negativa = sec_negativa_fortescue(i1,i2,i3)
    potencia_negativa_activa = 3*np.abs(voltajes_negativa[0][0])*np.abs(corrientes_negativa[0][0])*np.cos(np.angle(voltajes_negativa[0][0])-np.angle(corrientes_negativa[0][0]))
    potencia_negativa_reactiva = 3*np.abs(voltajes_negativa[0][0])*np.abs(corrientes_negativa[0][0])*np.sin(np.angle(voltajes_negativa[0][0])-np.angle(corrientes_negativa[0][0]))

    voltajes_cero = sec_homopolar(v1,v2,v3)
    corrientes_cero = sec_homopolar(i1,i2,i3)
    potencia_cero_activa = 3*np.abs(voltajes_cero[0][0])*np.abs(corrientes_cero[0][0])*np.cos(np.angle(voltajes_cero[0][0])-np.angle(corrientes_cero[0][0]))
    potencia_cero_reactiva = 3*np.abs(voltajes_cero[0][0])*np.abs(corrientes_cero[0][0])*np.sin(np.angle(voltajes_cero[0][0])-np.angle(corrientes_cero[0][0]))

    # CALCULA LA POTENCIA ACTIVA TOTAL SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.2.1
    potencia_activa_total = potencia_positiva_activa + potencia_negativa_activa + potencia_cero_activa
    
    # CALCULA LA POTENCIA REACTIVA TOTAL SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.3.1
    potencia_reactiva_total = potencia_positiva_reactiva + potencia_negativa_reactiva + potencia_cero_reactiva

    # CALCULA LA POTENCIA APARENTE VECTORIAL SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.6
    potencia_aparente_vectorial = np.sqrt(potencia_activa_total**2+potencia_reactiva_total**2)
    
    # CALCULA EL FACTOR DE POTENCIA VECTORIAL SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.7
    factor_potencia_vectorial = potencia_activa_total/potencia_aparente_vectorial
    
    # CALCULA LA POTENCIA APARENTE ARITMÉTICA SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.6.1
    potencia_aparente_aritmetica = np.abs(v1)*np.abs(i1) + np.abs(v2)*np.abs(i2) + np.abs(v3)*np.abs(i3)
    
    # CALCULA EL FACTOR DE POTENCIA ARITMÉTICO SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.7
    factor_potencia_aritmetica = potencia_activa_total/potencia_aparente_aritmetica
    
    # CALCULA LA POTENCIA APARENTE EFICAZ SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.8
    potencia_aparente_eficaz = 3*voltage_eficaz(v1,v2,v3)*corriente_eficaz(i1,i2,i3)
    
    # CALCULA EL FACTOR DE POTENCIA EFICAZ SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.9
    factor_potencia_eficaz = potencia_activa_total/potencia_aparente_eficaz
    
    #CALCULA LA POTENCIA APARENTE DE SECUENCIA POSITIVA SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.11
    potencia_aparente_eficaz_sec_positiva = np.sqrt(potencia_positiva_activa**2 + potencia_positiva_reactiva**2)
    
    #CALCULA LA POTENCIA DE DESEQUILIBRIO SEGÚN LA NORMA 1459 DE LA IEEE NUMERAL 3.2.2.11
    potencia_desequilibrio = np.sqrt(potencia_aparente_eficaz**2 - potencia_aparente_eficaz_sec_positiva**2)
    
    return [potencia_activa_total,potencia_reactiva_total,potencia_aparente_aritmetica,factor_potencia_aritmetica,potencia_aparente_vectorial,factor_potencia_vectorial,potencia_aparente_eficaz,factor_potencia_eficaz,potencia_desequilibrio]