# Coordinate Frames and transformation

This project is a Python app with a GUI that allows viewing a 3D model in STL format and applying transformations.
The tool aims to represent the body in an aeronautical reference system and display wind vectors, NED axes, and aerodynamic angles.

## Characteristics
* Loads STL files and normalizes their vertices
* 3D viewer using Matplotlib and Tkinter.

### Input:
* Euler angles: φ, θ, ψ.
* Aerodynamics angles: α (attack of angle), β (slipside angle), γ (clim angle).
* Body velocities: u, v, w.
* Wind across component.
* Angular rates: p, q, r

### Graphic view:
* Rotate model STL.
* Body axes.
* Fix axes (NED).
* Wind relative vector.
* Dynamic updates for modify values in the interface.


### Estructure:
```
├── main.py         # Start point of app.
├── interfaz.py     # Management of GUI and 3D view.
├── objeto.py       # Class 'maya' for load y normalized STL models.
├── r_t.py          # Class 'operations' for rotations and state control
```
# Requirements:
The following libreries must be installed:
* numpy
* matplotlib
* numpy-stl

To check if the libs are installed, run in the terminal:
```
pip list
```
If the not installed, run:
```
pip install numpy matplotlib numpy-stl
```

# Usage:
#### 1. Ejecute program with:
   python main.py
#### 2. The interfaz:
   * Load an STL file using **Load STL**.
   * Enter values of angles o body velocities.
   * Click **Upadate rotation** to apply the transforamtion.

# NOTES
* The program print in the terminal the actual state of aircraft.
* The option **Gamma is input** allows choosing whether γ is calculated automatically or entered manually.
* The program load the stl in the original CAD axis. It is recommended in CAD that the aircraft’s nose points along the X-axis. _For e.x load the file `aeronave_fd.stl`._
