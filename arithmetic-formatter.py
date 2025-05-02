def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."

        first, operator, second = parts

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2

        top_line.append(first.rjust(width))
        bottom_line.append(operator + second.rjust(width - 1))
        dashes.append('-' * width)

        if display_answers:
            if operator == '+':
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            answers.append(result.rjust(width))

    arranged_problems = "    ".join(top_line) + "\n" + \
                        "    ".join(bottom_line) + "\n" + \
                        "    ".join(dashes)

    if display_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems
