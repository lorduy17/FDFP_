import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import matplotlib.pyplot as plt
import numpy as np
from r_t import operaciones
from objeto import maya



class Interfaz():
    def __init__(self,master,objeto):
        self.master = master
        self.objeto = objeto
        self.opn = operaciones()

        self.sld_original = self.objeto.solido()

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111,projection='3d')

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=True)
        
        # sliders
        self.slider_x = tk.Scale(master, from_=0, to=360, orient=tk.HORIZONTAL, label="Rot X", command=self.update_plot)
        self.slider_x.pack(fill="x")
        self.slider_y = tk.Scale(master, from_=0, to=360, orient=tk.HORIZONTAL, label="Rot Y", command=self.update_plot)
        self.slider_y.pack(fill="x")
        self.slider_z = tk.Scale(master, from_=0, to=360, orient=tk.HORIZONTAL, label="Rot Z", command=self.update_plot)
        self.slider_z.pack(fill="x")
        
        self.update_plot(0)  # Dibuja inicial
        self.ax.clear()

    def update_plot(self, _):
        ang_x = np.radians(self.slider_x.get())
        ang_y = np.radians(self.slider_y.get())
        ang_z = np.radians(self.slider_z.get())

        self.opn.rot_x(ang_x)
        self.opn.rot_y(ang_y)
        self.opn.rot_z(ang_z)

        matriz_rot = self.opn.m_multiply()

        sld_r = matriz_rot@self.sld_original

        n_tri = self.sld_original.shape[0]
        sld_flat = self.sld_original.reshape(-1,3).T
        sld_r = matriz_rot@sld_flat
        sld_r = sld_r.T.reshape(n_tri,3,3)
        # Redibujar
        self.ax.clear()

        # puntos = sld_r.T.reshape(-1,3,3)
        coleccion = Poly3DCollection(sld_r, alpha=0.7, facecolor="lightblue", edgecolor="k")
        # self.ax.scatter(sld_r[0,:], sld_r[1,:], sld_r[aforme
        # self.canvas.draw()
        self.ax.add_collection3d(coleccion)
        self.ax.set_box_aspect([1,1,1])
        self.canvas.draw()

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Rotación STL con sliders")

#     obj = maya()  # Esto abrirá el diálogo para cargar el STL
#     app = Interfaz(root, obj)

#     root.mainloop()

