import numpy as np


class operations:

    def __init__(self):
        self.phi = 0
        self.theta = 0
        self.psi = 0
        self.alpha = 0
        self.beta = 0
        self.gamma = 0
        self.wind = np.array([0,0,0])
        
    def rot_x(self,phi):
        self.phi = phi
        c = np.cos(np.radians(phi))
        s = np.sin(np.radians(phi))
        return np.array([[1, 0, 0],
                         [0, c, -s],
                         [0, s, c]])
    
     
    def rot_y(self,theta):
        self.theta = theta
        c = np.cos(np.radians(theta))
        s = np.sin(np.radians(theta))
        return np.array([[c, 0, s],
                         [0, 1, 0],
                         [-s, 0, c]])
    
     
    def rot_z(self,psi):
        self.psi = psi
        c = np.cos(np.radians(psi))
        s = np.sin(np.radians(psi))
        return np.array([[c, -s, 0],
                         [s, c, 0],
                         [0, 0, 1]])
    
    def update_state(self,alpha,beta,gamma,wind):

        # check units
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.wind = wind
    
    def state_actual(self,):

        return {
            "angles": {
            "alpha": self.alpha, # Angle of attack [deg]
            "beta": self.beta, # Sideslip angle [deg]
            "gamma": self.gamma # climb angle [deg]
            },
            "velocities_body": self.wind, # [u, v, w] in body frame
            
            # "angular_rates": np.array([p, q, r]), # [p, q, r] roll, pitch, yaw r
            
            "attitude": np.array([self.phi, self.theta, self.psi]) # [φ, θ, ψ] Euler angles [ra
            
        }
         
    
    



    
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
    
    
