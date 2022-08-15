import spacy
from recognizers_number import recognize_number, Culture

npl = spacy.load('es_core_news_lg') # TODO: Ver de hacerlo mas global

# TODO: Ver por que no funcionan estos enunciados
# resta 3616 y 1095
# cual es el resultado de restar 3616 y 1095

def translate_statement(statement):
    operators = {"suma": "+", "resta": "-", "sumar": "+", "restar": "-", "más": "+", "mas": "+", "menos": "-"} # Aca deberia ir la palabra raiz nomas
    doc = npl(statement)
    mathProblem = []
    for token in doc:
        if token.pos_ in ["NOUN", "NUM"] or token.text.isnumeric():
            mathProblem.append(token)
        print(f"{token.text:{10}} {token.pos_:{10}} {token.is_stop:{10}} {spacy.explain(token.tag_)}")

    def translate(token):
      if token.text in list(operators.keys()): # TODO: Agregar logica lemmatizar y abstraer
        return (operators[token.text], token)
      else:
        return (token.text, token)
    translatedProblem = list(map(translate, mathProblem))
    finalTranslatedProblem = []
    for palabra, token in translatedProblem:
      if token.text in list(operators.keys()):
        operator = palabra
      else:
        if palabra.isnumeric():
            finalTranslatedProblem.append(palabra)
        else:
            result = recognize_number(palabra, Culture.Spanish)[0].resolution["value"]
            finalTranslatedProblem.append(result)
        finalTranslatedProblem.append(operator)
    finalTranslatedProblem.pop()
    equation = ' '.join(finalTranslatedProblem)
    return equation


  #  def is_operator(token):
  #        if token.text in list(operators.keys()):
  #          return true
  #        else:
  #          return false

  # TODO: Definir lemmatization para las keys. Ojo con que:
  # Lemma de suma es suma, sumar es sumar, sumatoria es sumatoria (deberia poner todas)
  # Si pongo un verbo conjugado de sumar, ahi si me lo va a tomar como sumar
  # Lo mismo sucede con adición y derivados
  # print('Lemmatization:')
  # print(f"{token.text:{10}} {token.pos_:{10}} {token.lemma:<{22}} {token.lemma_}")