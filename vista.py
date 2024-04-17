# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:23:06 2024

@author: lab
"""

class RobotView:
    def _init_(self):
        self.model = None

    def set_model(self, model):
        self.model = model

    def display_message(self, message):
        print(message)

    def get_user_input(self):
        elevation = int(input("INGRESE LA ELEVACION: "))
        rotation = int(input("INGRESE LA ROTACION: "))
        length = int(input("INGRESE LA LONGITUD: "))
        return elevation, rotation, length