import numpy as np
from stl import mesh
import tkinter as tk
from tkinter import filedialog

class maya():

    def __init__(self):

        self.ruta_stl = filedialog.askopenfilename(title="Selecciona archivo STL",filetypes=[("Archivos STL","*.stl")])
        if not self.ruta_stl:
            raise ValueError("No se seleccionó archivo STL")


    def carga_archivo(self):

        self.ruta_stl = filedialog.askopenfilename(
        title="Selecciona un archivo STL",
        filetypes=[("Archivos STL", "*.stl")]
        )
    def solido(self):
        
        modelo = mesh.Mesh.from_file(self.ruta_stl)
        # np.savetxt("puntos_stl.txt", puntos, fmt="%.6f", delimiter="\t")
        return modelo.vectors
    

