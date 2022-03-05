import copy

import latex
import sys
import csv
from pylatexenc.latex2text import UnknownMacroError

CSV_HEADER = ['title', 'topics', 'text']


class Problem:
    def __init__(self):
        self.title: str = ""
        self.question: str = ""
        self.answer_choices: [str] = []
        self.parsed_solution: [int] = []
        self.unparsed_solution: str = ""

    def to_csv_row(self, max_answer_count):
        topic = "unlabeled"
        sol_string = ''
        for sol in self.parsed_solution:
            sol_string += str(sol) + ','
        return [self.title, topic, self.question] + \
               self.answer_choices + \
               (max_answer_count - len(self.answer_choices)) * [''] + \
               [sol_string]

    def to_latex(self):
        """
            \\section
                \\probheadernum{4}
                    Question_Text
                    \\begin{enumerate}[(a)]
                        \\item Answer_Choice_Text
                    \\end{enumerate}
                    \\begin{solution}
                        Solution_Text
                    \\end{solution}
        """
        ret = "\\probheadernum{4}\n"
        ret += self.question
        ret += "\\begin{enumerate}[(a)]\n"
        for ans in self.answer_choices:
            ret += f'\t\\item {ans}\n'
        ret += "\\end{enumerate}\n"
        ret += "\\begin{solution}\n"
        ret += self.unparsed_solution + "\n"
        ret += "\\end{solution}"
        return ret

    def parse_solution(self):
        i = self.unparsed_solution.find('(')
        i += 1
        done = False
        while not done:
            if 97 <= ord(self.unparsed_solution[i]) <= 97 + len(self.answer_choices):
                self.parsed_solution.append(ord(self.unparsed_solution[i]) - 96)
            elif self.unparsed_solution[i] not in {'(', ',', ')'}:
                done = True
            i += 1


def readLatexFile(file) -> ([str], [str]):
    text = file.read()
    text = text.split(latex.begin('document'))
    header = text[0]
    document = text[1]
    document = document[:document.find(latex.end('document'))]
    return header, document


def getProblemList(document: str, filename: str) -> [Problem]:
    # TODO check section and num answers (SAMC => 1)
    # TODO title
    problems: [Problem] = []
    # document latex structure should be:
    """
    \\section
        \\probheadernum{4}
            Question_Text
            \\begin{enumerate}[(a)]
                \\item Answer_Choice_Text
            \\end{enumerate}
            \\begin{solution}
                Solution_Text
            \\end{solution}
    """
    sections = document.split('\\section')
    sections = sections[2:4]
    problem_number = 1
    for section in sections:
        problem_strings = section.split('\\probheadernum{4}')[1:]
        for prob in problem_strings:
            begin_enum_idx = prob.find('\\begin{enumerate}[(a)]')
            end_enum_idx = prob.find('\\end{enumerate}')
            begin_sol_idx = prob.find('\\begin{solution}')
            end_sol_idx = prob.find('\\end{solution}')

            problem = Problem()
            problem.title = f'{filename}_Q{problem_number}'
            problem.question = prob[:begin_enum_idx]
            answer_choice_string = prob[begin_enum_idx + len('\\begin{enumerate}[(a)]'):end_enum_idx]
            problem.answer_choices = answer_choice_string.split('\\item')[1:]
            problem.unparsed_solution = prob[begin_sol_idx + len('\\begin{solution}'):end_sol_idx]

            problems.append(problem)
            problem_number += 1
    return problems


def convertFile(filename: str):
    with open(f'tex/{filename}.tex', "r") as f:
        header, document = readLatexFile(f)
    problems: [Problem] = getProblemList(document, filename)
    max_answer_count = 0
    fail_list: [Problem] = []
    success_list: [Problem] = []
    for prob in problems:
        fail = copy.deepcopy(prob)
        try:
            prob.parse_solution()
            prob.question = latex.compile(header, prob.question)
            prob.answer_choices = [latex.compile(header, ans) for ans in prob.answer_choices]
            success_list.append(prob)
        except UnknownMacroError:
            # Add to unknown list
            fail_list.append(fail)
            print(f'Failed on: {prob.title}')

        max_answer_count = max(max_answer_count, len(prob.answer_choices))

    with open('EECS203.csv', "a", newline='') as f:
        csvwriter = csv.writer(f)
        for prob in success_list:
            csvwriter.writerow(prob.to_csv_row(max_answer_count))

    with open(f'fails.tex', 'a') as f:
        for prob in fail_list:
            f.write(prob.to_latex())


if __name__ == '__main__':
    convertFile(sys.argv[0])
