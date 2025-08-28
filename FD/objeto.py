import numpy as np
from stl import mesh
import tkinter as tk
from tkinter import filedialog

class maya():

    def __init__(self):
        self.model = None
        self.original_vectors = None
        self.normalized_vectors = None

    def file_load(self, filename: str):
            if not filename:
                raise ValueError("STL file not found")
            self.model = mesh.Mesh.from_file(filename)
            self.original_vectors = self.model.vectors.copy()
            self.normalized_vectors = None

    def get_original_vertices(self):
         if self.original_vectors is None:
             raise ValueError("No STL file loaded")
         return self.original_vectors
    
    def get_normalized_vertices(self):
        if self.original_vectors is None:
            raise ValueError("No STL file loaded")
        
        if self.normalized_vectors is not None:
            return self.normalized_vectors
        
        model_flat = self.model.vectors.reshape(-1,3)

        centroid = np.mean(model_flat, axis=0)
        model_centered = model_flat - centroid
        
        ranges = np.ptp(model_centered, axis=0)
        max_range = np.max(ranges)
        if max_range == 0:
         max_range = 1

        normalized = model_centered/ max_range
        self.normalized_vectors = normalized.reshape(self.model.vectors.shape)
        return self.normalized_vectors
