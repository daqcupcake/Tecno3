# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np

class ClaseCuadratica:
    def __init__(self, a,b,c):  #siempre recibe a self
        self.a=a
        self.b=b
        self.c=c
        self.vertX = -b/(2*a)
        
    def discriminante(self):
        return self.b**2-4*self.a*self.c
    
        
        
        

