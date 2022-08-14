import spacy
from numerizer import numerize

# from googletrans import Translator, constants
# from pprint import pprint

npl = spacy.load('es_core_news_lg') # TODO: Ver de hacerlo mas global
# translator = Translator() # init the Google API translator

# TODO: Ver por que no funcionan estos enunciados
# resta 3616 y 1095
# cual es el resultado de restar 3616 y 1095

def translate_statement(statement):
    operators = {"suma": "+", "resta": "-", "sumar": "+", "restar": "-", "más": "+", "mas": "+", "menos": "-"} # Aca deberia ir la palabra raiz nomas
    doc = npl(statement)
    mathProblem = []
    for token in doc:
        if token.pos_ in ["NOUN", "NUM"] or token.text.isnumeric():
            #print('Encontre un numero ' + token.text)
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
            # translation = translator.translate(palabra)
            # print('Esto NO es numerico ' + palabra + ' pero lo acabo de traducir ' + translation)
            # print('Y aca esta numerizado ' + numerize(translation))
            finalTranslatedProblem.append(numerize(palabra)) # TODO: Chequear que si es un numero palabra, transformar a numero posta
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