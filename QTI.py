assessmentItem = """"[
"<qti-assessment-item>" 
  "<qti-item-body>" 
    "<p> %s </p>",
    "<qti-choice-interaction max-choices="1" response-identifier="RESPONSE">"
        <qti-simple-choice identifier="ChoiceA">You must stay with your luggage at all times.</qti-simple-choice>
        <qti-simple-choice identifier="ChoiceB">Do not let someone else look after your luggage.</qti-simple-choice>
        <qti-simple-choice identifier="ChoiceC">Remember your luggage when you leave.</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
  </qti-assessment-item>
"""


def generate_assessment_item(title: str, question: str, answerChoices: [str], answer: [int]):
    choices = [
        f'<qti-simple-choice identifier=Choice{chr(95+i)}>{choice}</qti-simple-choice>'
        for (i, choice) in enumerate(answerChoices)
    ]

    return ''.join([
        "<qti-assessment-item>",
        "<qti-item-body>",
        f"<p> {question} </p>",
        f'<qti-choice-interaction max-choices={len(answer)} response-identifier="RESPONSE">"',
        ] + choices + [
        "</qti-choice-interaction>",
        "</qti-item-body>",
        "</qti-assessment-item>",
    ])
