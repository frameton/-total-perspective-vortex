import inquirer
import os
from tools import colors

def programs_step_display():
	print(colors.clr.fg.cyan)
	print("")
	print("")
	print("####################################################################################################################")
	print("")
	print("                                                 Choose program                                                     ")
	print("")
	print("")
	print("")

	questions = [
    inquirer.List(
        "program",
        message="This program is composed of 5 sub-programs, choose the one that interests you",
        choices=["Option1", "Back"],
    ),
	]
	return inquirer.prompt(questions)


def programs_step(params):
  while True:
    answer = programs_step_display()
    if answer["program"] == "Option1":
      print("Option1")
    if answer["program"] == "Back":
      break