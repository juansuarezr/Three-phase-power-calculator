# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:05:27 2020

@author: Juan Pablo
"""


import tkinter as tk
from tkinter import filedialog as fd
import Calc_potencia_interfaz as cpi
import Cal_nosin as cn
import pandas as pd


class MainApplication(tk.Frame):
    def __init__(self, parent,*args, **kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        
        self.parent = parent
        self.parent.title("Power calculator")
        
        self.label = tk.Label(parent,text="This program can calculate the power definitions in Standard IEEE 1459 for three-phase four-wire systems. \nChoose the kind of calculation you want to do.\n\n\n\n")
        self.label.pack()
        
        
        self.boton1 = tk.Button(parent,text="Three-phase sinusoidal", command=self.InterfazSinusoidal)
        self.boton1.pack()
        
        
        self.boton2 = tk.Button(parent,text="Three-phase non-sinusoidal", command=self.cargaArchivos)
        self.boton2.pack()
        
    def cargaArchivos(self):
        self.frameCargar = tk.Tk()
        self.VentanaCargar = CargaArchivos(self.frameCargar).pack()
        
    def InterfazSinusoidal(self):
        cpi.ThreePhaseSinusoidal()
        
    
        
        
        

class CargaArchivos(tk.Frame):
    def __init__(self, parent,*args, **kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.file_path1 = ""
        self.file_path2 = ""
        
        self.parent = parent
        self.parent.title("Carga de archivos")
        
        self.boton1 = tk.Button(parent,text="Voltages", command=self.ArchivoVoltages)
        self.boton1.pack()
        
        self.labelVoltage = tk.Label(parent,text="Select the csv file with the voltage data")
        self.labelVoltage.pack()

        self.boton2 = tk.Button(parent,text="Currents", command=self.ArchivoCorrientes)
        self.boton2.pack()
        
        self.labelCurrent = tk.Label(parent,text="Select the csv file with the current data")
        self.labelCurrent.pack()
        
        self.boton3 = tk.Button(parent,text="Continue", command=self.InterfazNoSinusoidal)
        self.boton3.pack()
        self.boton3["state"] = "disabled"
        
        self.labelContinue = tk.Label(parent, text="")
        self.labelContinue.pack()
        

        
    def ArchivoVoltages(self):
        self.file_path1 = fd.askopenfilename()
        self.labelVoltage["text"] = self.file_path1
        if self.file_path1 == "":
                self.labelVoltage["text"] = "Please select a file"
        self.checkLoad()

        
    def ArchivoCorrientes(self):
        self.file_path2 = fd.askopenfilename()
        self.labelCurrent["text"] = self.file_path2
        if self.file_path2 == "":
                self.labelCurrent["text"] = "Please select a file"
        self.checkLoad()

 
    def checkLoad(self):
        
        if (self.file_path1 != "") and (self.file_path2 != ""):
            self.boton3["state"] = "active"
        else:
            
            self.boton3["state"] = "disabled"


    def InterfazNoSinusoidal(self):
        try:
            cn.ThreePhaseNonSinusoidal(self.file_path1,self.file_path2)
            cn.GenerateCSV(self.file_path1,self.file_path2,self.parent)
        except:
            self.file_path1 = ""
            self.file_path2 = ""
            self.labelVoltage["text"] = "Select the csv file with the voltage data"
            self.labelCurrent["text"] = "Select the csv file with the current data"
            self.boton3["state"] = "disabled"
            self.labelContinue["text"] = "An error occurred while processing the data, please make sure the csv files are correct."
    

#class Tabla(tk.Frame):
 #   def __init__(self,origin,df,*args, **kwargs):
  #      tk.Frame.__init__(self,origin,df,*args,**kwargs)
   #     self.Table_interface = tk.Toplevel(origin)
    #    self.table = tk.Text(self.Table_interface)
     #   self.table.insert(tk.INSERT, df.to_string())
      #  self.table.pack()
        
        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack()
    root.mainloop()

