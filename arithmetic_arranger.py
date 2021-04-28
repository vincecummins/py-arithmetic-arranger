import re
def arithmetic_arranger(problems, solve = False):
    regex = '\D'
    first_line = ''
    second_line = ''
    dash_line = ''
    sol = ''
    string = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for x in problems:
        arr = x.split()
        if arr[1] != '+' and arr[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if re.search(regex, arr[0]) or re.search(regex, arr[2]):
            return 'Error: Numbers must only contain digits.'
        if len(arr[0]) > 4 or len(arr[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        maxLen = max(len(arr[0]), len(arr[2])) + 2
        first_line = first_line + arr[0].rjust(maxLen) + '    '
        second_line = second_line + arr[1] + ' ' + arr[2].rjust(maxLen - 2) + '    '
        dash_line = dash_line + maxLen*'-' + '    '
        sol = sol + str(eval(x)).rjust(maxLen) + '    '
    if solve:
        string = first_line.rstrip() + '\n' + second_line.rstrip() + '\n'  + dash_line.rstrip() + '\n'  + sol.rstrip()
    else:
        string = first_line.rstrip() + '\n'  + second_line.rstrip() + '\n'  + dash_line.rstrip()

    return string
        


