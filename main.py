# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:23:07 2024

@author: lab
"""

from modelo import RobotModel
from vista import RobotView
from controlador import RobotController

def main():
    robot_model = RobotModel()
    robot_view = RobotView()
    robot_controller = RobotController()

    robot_controller.set_model(robot_model)
    robot_controller.set_view(robot_view)
    robot_view.set_model(robot_model)

    while True:
        user_command = input("INGRESE (mover/detener): ")
        robot_controller.process_command(user_command)

if __name__ == "__main__":
    main()