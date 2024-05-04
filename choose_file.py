from os import walk
import inquirer
from tools import colors


def choose_file():
	print(colors.clr.fg.cyan)
	print("")
	print("")
	print("####################################################################################################################")
	print("")
	print("                                              Choose dataset file                                                   ")
	print("")
	print("")
	print("")

	f = []
	for (dirpath, dirnames, filenames) in walk("datasets/"):
		for elt in filenames:
			if elt.lower().endswith('.csv'):
				f.append(elt)
		break

	questions = [
	inquirer.List(
		"datasets_file",
		message="Choose file",
        choices=f,
    ),
	]
	return inquirer.prompt(questions)