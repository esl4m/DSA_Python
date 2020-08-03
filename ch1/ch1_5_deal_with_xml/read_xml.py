#!/usr/bin/python3
#
# By Islam (esl4m)
# 3 Aug 2020
#

from ..ch1_3_polymorphism.polymorphism import BeginFillCommand, CircleCommand, EndFillCommand, GoToCommand, PenUpCommand, PenDownCommand
import xml.dom.minidom

filename = input("Please enter xml filename: ")
xmldoc = xml.dom.minidom.parse(filename)

# read a specific type of element from the XML file by calling the method getElementsByTagName
graphicsCommands = xmldoc.getElementsByTagName("GraphicsCommands")[0]

for commandElement in graphicsCommands:
    print(type(commandElement))
    command = commandElement.firstChild.data.strip()
    attr = commandElement.attributes

    if command == "GoTo":
        x = float(attr["x"].value)
        y = float(attr["y"].value)
        width = float(attr["width"].value)
        color = attr["color"].value.strip()
        cmd = GoToCommand(x, y, width, color)

    elif command == "Circle":
        radius = float(attr["radius"].value)
        width = float(attr["width"].value)
        color = attr["color"].value.strip()
        cmd = CircleCommand(radius, width, color)

    elif command == "BeginFill":
        color = attr["color"].value.strip()
        cmd = BeginFillCommand(color)

    elif command == "EndFill":
        cmd = EndFillCommand()

    elif command == "PenUp":
        cmd = PenUpCommand()

    elif command == "PenDown":
        cmd = PenDownCommand()
        
    else:
        raise RuntimeError("Unknown Command: " + command)
        self.append(cmd)
