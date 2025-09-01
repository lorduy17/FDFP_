import tkinter as tk
from objeto import maya
from interfaz import Interfaz
import os

if __name__ == "__main__":
    root = tk.Tk()
    root.title("3D STL Viewer")
    app = Interfaz(root)

    root.mainloop()

