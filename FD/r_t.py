import numpy as np


class operations:
    @staticmethod
    def rot_x(phi):
        c = np.cos(np.radians(phi))
        s = np.sin(np.radians(phi))
        return np.array([[1, 0, 0],
                         [0, c, -s],
                         [0, s, c]])
    
    @staticmethod
    def rot_y(theta):
        c = np.cos(np.radians(theta))
        s = np.sin(np.radians(theta))
        return np.array([[c, 0, s],
                         [0, 1, 0],
                         [-s, 0, c]])
    
    @staticmethod
    def rot_z(psi):
        c = np.cos(np.radians(psi))
        s = np.sin(np.radians(psi))
        return np.array([[c, -s, 0],
                         [s, c, 0],
                         [0, 0, 1]])
    
    @staticmethod
    def mult_matrix(*matrices):
        result = np.eye(3)
        for matrix in matrices:
            result = result @ matrix
        return result
    
    @staticmethod
    def normalized(v):
        v_min = np.min(v)
        v_max = np.max(v)
        if v_max - v_min == 0:
            return v
        return (v - v_min) / (v_max - v_min)
    
    
