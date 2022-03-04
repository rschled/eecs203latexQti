import pylatexenc
import latex
import QTI


def readDocument(file) -> ([str], [str]):
    header = []
    document = []
    line = file.readline()
    while line and line != latex.begin('document'):
        header.append(line)
        line = file.readline()
    while line:
        document.append(line)
        line = file.readline()
    return header, document


def getProblems(document: [str]):
    problems = []
    for line in document:
        if line == '\n' or line[0] == '%':
            continue
        if latex.isProbheaderNum(line):
            problems.append([])
        else:
            problems[-1].append(line)
    return problems


def convertFile(filename: str):
    file = open(filename)
    header, document = readDocument(file)
    file.close()
    document = getProblems(document)









