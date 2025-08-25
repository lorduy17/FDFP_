import numpy as np
from stl import mesh

class operaciones:

    def __init__(self):
        self.z = np.eye(3)
        self.y = np.eye(3)
        self.x = np.eye(3)

    def rot_z(self, phi):
        self.z = np.array([
            [np.cos(phi), -np.sin(phi), 0],
            [np.sin(phi),  np.cos(phi), 0],
            [0,            0,           1]
        ])

    def rot_y(self, theta):
        self.y = np.array([
            [np.cos(theta), 0, np.sin(theta)],
            [0,             1, 0],
            [-np.sin(theta), 0, np.cos(theta)]
        ])

    def rot_x(self, psi):
        self.x = np.array([
            [1, 0, 0],
            [0, np.cos(psi), -np.sin(psi)],
            [0, np.sin(psi),  np.cos(psi)]
        ])

    def m_multiply(self):
        matrices = [self.z, self.y, self.x]
        return np.linalg.multi_dot(matrices)
    
    def rotacion(self, matriz_rotacional, objeto):
        pass


if __name__ == "__main__":

    # phi = np.pi / 2
    # theta = np.pi / 4
    # gamma = np.pi / 16

    # opn = operaciones()
    # opn.rot_z(phi)
    # opn.rot_y(theta)
    # opn.rot_x(gamma)

    # x = opn.m_multiply()
    # np.savetxt("matriz_rotacion.txt",x,fmt="%.6f",delimiter="\t")
    # print(x)
    None
    