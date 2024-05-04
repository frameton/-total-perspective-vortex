import inquirer
from tools import colors
from get_create_parameters_settings import *
from get_parameters_settings_path import *


def choose_epochs(src_list):
	print(colors.clr.fg.cyan)
	print("")
	print("")
	print("####################################################################################################################")
	print("")
	print("                                    What epoch do you want to use?                                          ")
	print("")
	print("")
	print("")

	questions = [
    inquirer.List(
        "epochs",
        message="Choose epoch(s)",
        choices=src_list,
    ),
	]
	return inquirer.prompt(questions)


def choose_learning_rate(src_list):
	print(colors.clr.fg.cyan)
	print("")
	print("")
	print("####################################################################################################################")
	print("")
	print("                                    Which learning rate do you want to use?                                         ")
	print("")
	print("")
	print("")

	questions = [
    inquirer.List(
        "learning_rate",
        message="Choose learning rate",
        choices=src_list,
    ),
	]
	return inquirer.prompt(questions)


def gradient_parameters_settings_step_display(params):

    print(colors.clr.fg.cyan)
    print("")
    print("")
    print("####################################################################################################################")
    print("")
    print("                                                   Gradient setting                                                   ")
    print("")
    print(colors.clr.fg.yellow)
    print("                                                  Current parameters:                                                ")
    print("")
    print(f"                                                      Epochs: {params['epochs']}                                                 ")
    print(f"                                        Learning rate number: {params['learning_rate']}                                                 ")
    print(colors.clr.reset)
    print(colors.clr.reset)
    print("")
    print("")
    print("")

    questions = [
    inquirer.List(
        "gradient_parameters_settings_step_answer",
        message="You can choose parameters in list or create new parameters",
        choices=["Choose in list", "Add new dimension to list", "Back"],
    ),
    ]
    return inquirer.prompt(questions)


def choose_parameters_step_display():
    path_list = get_parameters_settings_path()

    try:
        file1 = open(path_list["dimensions_list"], 'r')
        count = 0
        dimensions_list = []

        for line in file1:
            count += 1
            dimensions_list.append(line.strip())
 
        file1.close()
    except Exception as error:
        print(colors.clr.fg.red, "Error:", error, colors.clr.reset)
        exit(1)

    if len(dimensions_list) == 0:
        print(colors.clr.fg.yellow, "Error: no data in dimensions list, you can create it.", colors.clr.reset)
        return None

    print(colors.clr.fg.cyan)
    print("")
    print("")
    print("####################################################################################################################")
    print("")
    print("                                             Choose gradient parameters                                                 ")
    print("")
    print(colors.clr.fg.orange)
    print("")
    print(f"                                            1st number -> epochs                                     ")
    print(f"                                            2nd number -> learning rate number                                             ")
    print(colors.clr.reset)
    print(colors.clr.reset)
    print("")
    print("")
    print("")

    questions = [
    inquirer.List(
        "choose_parameters_step_answer",
        message="Choose a gradient parameters in list:",
        choices=dimensions_list,
    ),
    ]
    return inquirer.prompt(questions)


def choose_dimensions(params):
    answer = choose_parameters_step_display()
    if answer is None:
        return params
    try:
        tab = [float(x) for x in answer["choose_parameters_step_answer"].split()]
    except Exception as error:
        print(colors.clr.fg.red, "Error: dimensions invalid.", colors.clr.reset)
        return params
    if len(tab) != 2:
        print("")
        print(colors.clr.fg.red, "Error: dimensions invalid.", colors.clr.reset)
        return params

    params["epochs"] = int(tab[0])
    params["learning_rate"] = float(tab[1])

    return params


def add_dimension_to_list():
    src_dic = get_create_parameters_settings()

    new_dimensions = {}

    answer = choose_epochs(src_dic["epochs"])
    new_dimensions["epochs"] = answer["epochs"]

    answer = choose_learning_rate(src_dic["learning_rate"])
    new_dimensions["learning_rate"] = answer["learning_rate"]

    path_list = get_parameters_settings_path()

    try:
        file1 = open(path_list["dimensions_list"], 'r')
        count = 0
        dimensions_list = []

        for line in file1:
            count += 1
            dimensions_list.append(line.strip())
 
        file1.close()
    except Exception as error:
        print(colors.clr.fg.red, "Error:", error, colors.clr.reset)
        exit(1)
    
    string = str(new_dimensions["epochs"]) + " " + str(new_dimensions["learning_rate"])
    dimensions_list.insert(0, string)

    if len(dimensions_list) > 10:
        dimensions_list = dimensions_list[:9]

    try:
        file1 = open(path_list["dimensions_list"], 'w')

        count = 0
        for line in dimensions_list:
            file1.write(line)
            if count < len(dimensions_list) - 1:
                file1.write('\n')
 
        file1.close()
    except Exception as error:
        print(colors.clr.fg.red, "Error:", error, colors.clr.reset)
        exit(1)

    print("")
    print(colors.clr.fg.green, "The new parameters has been added.", colors.clr.reset)
    print("")


def gradient_parameters_settings_step(params):
    while True:
        answer = gradient_parameters_settings_step_display(params)
        if answer["gradient_parameters_settings_step_answer"] == "Choose in list":
            params = choose_dimensions(params)
        if answer["gradient_parameters_settings_step_answer"] == "Add new dimension to list":
            add_dimension_to_list()
        if answer["gradient_parameters_settings_step_answer"] == "Back":
            break
    return params