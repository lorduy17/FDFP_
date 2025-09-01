# Coordinate Frames and transformation

This project is a app developed in Python with a GUI the permmit a view model 3D in STL format, applied transformation.
The tool have like objective the body representation in aeronautical systeme reference. Showed wind vector, NED axis and aerodynamic angles

# Characteristics
Files STL load and normalized them vertices.
3D viwer with Matplotlib and Tkinder

# Input:
Euler angles: φ, θ, ψ.
Aerodynamics angles: α (ángulo de ataque), β (ángulo de resbale), γ (ángulo de ascenso).
Body velocities: u, v, w.
Wind across component.

# Graphic view:
Roteta model STL.
NED axes
Ejes fijos (NED).
Wind relative vector.
Dynamic updates for modify values in the interface


# Estructure:
├── main.py         # Start point of app.
├── interfaz.py     # Management of GUI and 3D view.
├── objeto.py       # Class 'maya' for load y normalized STL models.
├── r_t.py          # Class 'operations' for rotations and state control

# Requirements:
pip install numpy matplotlib numpy-stl

Paste this comand in the terminal

# Used mode:
1. Ejecute program with:
   python main.py
2. The interfaz:
   Load STL file with Load STL.
   Join values of angles o body velocities.
   Click update rotation for applie transforamtion

# NOTES:
The program print in the terminal the actual state of aircraft
The option " Gamma is input " allow chose if gamma was calc automatic or join manual the value.
