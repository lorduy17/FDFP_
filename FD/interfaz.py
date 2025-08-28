

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
from r_t import operations
from objeto import maya



class Interfaz():
    def __init__(self,master,objeto):
        self.master = master
        self.objeto = maya()
        self.opn = operations()

        self.entries = {}
        self.entry_frames = {}
        self.input_mode = tk.StringVar(value="Euler angles")
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Input type
        self.input_type = tk.StringVar(value="Euler angles")
        self.create_mode_selector()
        self.create_entries()

        # Buttons
        self.create_buttons()

        # Wigets
    

    def create_mode_selector(self):
        frame = ttk.Frame(self.master)
        frame.pack(pady = 5)
        tk.Label(frame, text="Select input type:").pack(side=tk.LEFT)
        combo = ttk.Combobox(frame, textvariable=self.input_mode,values=[
            "Euler angles",
            "Aerodynamic angles",
            "Wind vector"
        ],state="readonly")
        combo.pack(side=tk.LEFT)
        combo.bind("<<ComboboxSelected>>", lambda e: self.update_view_input())

    def create_entries(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=5)
        labels = {
            "Euler angles": ["phi(°)", "theta(°)", "psi(°)"],
            "Aerodynamic angles": ["alpha(°)", "beta(°)", "clinb(°)"],
            "Wind vector": ["u m/s", "v m/s", "w m/s"]
        }
        self.entry_frames = {}
        for mode, keys in labels.items():
            f = tk.Frame(frame)
            f.pack(side="top", fill="x", pady=2)
            self.entry_frames[mode] = f
            for key in keys:
                e_frame = tk.Frame(f)
                e_frame.pack(side="left", padx=5)
                tk.Label(e_frame, text=key).pack()
                entry = tk.Entry(e_frame, width=10)
                entry.insert(0, "0")
                entry.pack()
                self.entries[key] = entry
                entry.bind("<Return>", lambda e: self.update.plot())
        self.update_view_input()

    def create_buttons(self):
        tk.Button(self.master, text="Load STL",
                    command=self.load_stl).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.master, text="Update rotation",
                    command=self.update_plot).pack(side=tk.LEFT, padx=5, pady=5)

        ## Functions ##

    def load_stl(self):
        filename = filedialog.askopenfilename(title="Select STL file",
            filetypes=[("STL files", "*.stl")])
        if filename:
            self.objeto.file_load(filename)
            self.update_plot()

    def update_view_input(self):
        mode = self.input_mode.get()
        for m, frame in self.entry_frames.items():
            if m == mode:
                frame.pack(side="top", fill="x", pady=2)
            else:
                frame.pack_forget()
    
    def set_axes_equal(self):
        '''Set 3D plot axes to equal scale.'''
        x_limits = self.ax.get_xlim3d()
        y_limits = self.ax.get_ylim3d()
        z_limits = self.ax.get_zlim3d()

        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = np.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = np.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = np.mean(z_limits)

        plot_radius = 0.5 * max([x_range, y_range, z_range])

        self.ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        self.ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        self.ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
    def update_plot(self):
        if self.objeto.get_normalized_vertices() is None:
            return
        mode = self.input_mode.get()
        vectors = self.objeto.get_normalized_vertices().reshape(-1,3,3)
        try:
                
            if mode == "Euler angles":
                phi = float(self.entries["phi(°)"].get())
                theta = float(self.entries["theta(°)"].get())
                psi = float(self.entries["psi(°)"].get())
                R = self.opn.mult_matrix(
                    self.opn.rot_x(phi),
                    self.opn.rot_y(theta),
                    self.opn.rot_z(psi)
                )
            elif mode == "Aerodynamic angles":
                alpha = float(self.entries["alpha(°)"].get())
                beta = float(self.entries["beta(°)"].get())
                R = self.opn.mult_matrix(
                    self.opn.rot_z(-beta),
                    self.opn.rot_y(alpha)
                )
            elif mode == "Wind vector":
                u = float(self.entries["u m/s"].get())
                v = float(self.entries["v m/s"].get())
                w = float(self.entries["w m/s"].get())
                wind = np.array([u, v, w])
                if np.linalg.norm(wind) != 0:
                    wind_norm = wind / np.linalg.norm(wind)
                    alpha = np.arctan2(wind_norm[2], wind_norm[0])
                    beta = np.arcsin(wind_norm[1])
                    R = self.opn.mult_matrix(
                        self.opn.rot_z((-beta)),
                        self.opn.rot_y((alpha))
                    )
                else:
                    R = np.eye(3)
        except ValueError:
            print("Invalid input")
            return
        
        vectors_rot = vectors.reshape(-1,3) @ R.T
        vectors_rot = vectors_rot.reshape(vectors.shape)

        

        # Draw
        self.ax.clear()
        self.ax.grid(True)
        self.ax.set_axis_off()
        
        poly = Poly3DCollection(vectors_rot, alpha=0.7,
                                facecolor="lightblue",
                                edgecolor="k")
        

        self.ax.add_collection3d(poly)
        self.ax.set_box_aspect([1,1,1])  # Mantiene la proporción en x,y,z
        self.ax.view_init(elev=20, azim=30)
        self.set_axes_equal()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("3D STL Viewer")
    app = Interfaz(root,maya())
    root.mainloop()

        
