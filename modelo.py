# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:21:40 2024

@author: lab
"""

class RobotModel:
    def _init_(self):
        self.elevation = 0
        self.rotation = 0
        self.length = 0

    def move_elevation(self, value):
        self.elevation = value
        print(f"ELEVACION {self.elevation}")

    def move_rotation(self, value):
        self.rotation = value
        print(f"ROTACION {self.rotation}")

    def move_length(self, value):
        self.length = value
        print(f"LONGITUD {self.length}")

    def stop_movement(self):
        self.move_elevation(0)
        self.move_rotation(0)
        self.move_length(0)
        print("SE DETUVO")

