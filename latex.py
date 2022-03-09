from pylatexenc.latex2text import LatexNodes2Text, UnknownMacroError

class EmptyCompilationResult(Exception):
    pass

def begin(arg: str):
    return '\\begin{' + arg + '}'


def end(arg: str):
    return '\\end{' + arg + '}'


def isProbheaderNum(string: str) -> bool:
    prob = "\\probheadernum"
    return string[0:len(prob)].lower() == prob


def compile(header, text):
    ret = LatexNodes2Text().latex_to_text(text)
    if len(ret) == 0 or ret.isspace():
        raise EmptyCompilationResult
    return ret
