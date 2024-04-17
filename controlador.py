# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:23:06 2024

@author: lab
"""

class RobotController:
    def _init_(self):
        self.model = None
        self.view = None

    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view
        view.set_model(self.model)

    def process_command(self, command):
        if command == "mover":
            elevation, rotation, length = self.view.get_user_input()
            self.model.move_elevation(elevation)
            self.model.move_rotation(rotation)
            self.model.move_length(length)
        elif command == "detener":
            self.model.stop_movement()
        else:
            self.view.display_message("ERROR....INGRESE UN COMANDO CORRECTO")