

def begin(arg: str):
    return '\\begin{' + arg + '}'


def end(arg: str):
    return '\\end{' + arg + '}'


def isProbheaderNum(string: str) -> bool:
    prob = "\\probheadernum"
    return string[0:len(prob)].lower() == prob