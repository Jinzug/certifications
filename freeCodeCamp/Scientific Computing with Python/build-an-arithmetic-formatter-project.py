def arithmetic_arranger(problems, show_answers=False):

    #Check if there are more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #lists
    all_operands = []
    top_operands = []
    operators = []
    bottom_operands = []
    dashes = []
    answers = []
    top_lines = []
    bot_lines = []
    dashes_lines = []
    answers_lines = []

    #Split in all lists
    for problem in problems:
        parts = problem.split()
        top_operands.append(parts[0]), all_operands.append(parts[0])
        operators.append(parts[1])
        bottom_operands.append(parts[2]), all_operands.append(parts[2])

    #Check for the length of operations
    for digit in all_operands:
        #Check if numbers are digits
        if digit.isdigit():
            if len(digit) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                pass
        else:
            return "Error: Numbers must only contain digits."

    #Check signs
    for sign in operators:
        if sign not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        else:
            #Create answers
            if show_answers == True:
                for i in range(len(operators)):
                    if operators[i] == '+':
                        answers.append(str(int(top_operands[i]) + int(bottom_operands[i])))
                    else:
                        answers.append(str(int(top_operands[i]) - int(bottom_operands[i])))
            else:
                #Add empty answers when False
                answers = [''] * len(problems)

    #Adjust lengths by adding spaces
    for i in range(len(top_operands)):
        top = top_operands[i]
        bottom = bottom_operands[i]
        answer = answers[i]
        if len(top) > len(bottom):
            top_operands[i] = top.rjust(len(top) + 2)
            bottom_operands[i] = bottom.rjust(len(top) + 1)
            answers[i] = answer.rjust(len(top) + 2)
            dashes.append(len(top_operands[i]))
        else:
            bottom_operands[i] = bottom.rjust(len(bottom) + 1)
            top_operands[i] = top.rjust(len(bottom) + 2)
            answers[i] = answer.rjust(len(bottom) + 2)
            dashes.append(len(bottom_operands[i]) + 1)
    
    #Create all ligns
    for i in range(len(problems)):
        top = top_operands[i]
        bottom = operators[i] + bottom_operands[i]
        dash = '-' * dashes[i]
        answer = answers[i]

        top_lines.append(top)
        bot_lines.append(bottom)
        dashes_lines.append(dash)
        answers_lines.append(answer)

    #Align everything
    if show_answers == True:
        arranged_problems = "    ".join(top_lines) + "\n" + \
                            "    ".join(bot_lines) + "\n" + \
                            "    ".join(dashes_lines) + "\n" + \
                            "    ".join(answers_lines)
    else:
        arranged_problems = "    ".join(top_lines) + "\n" + \
                            "    ".join(bot_lines) + "\n" + \
                            "    ".join(dashes_lines)

    #Return everything
    return arranged_problems


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')