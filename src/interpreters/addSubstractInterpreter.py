import spacy

npl = spacy.load('es_core_news_lg') # TODO: Ver de hacerlo mas global

def translate(statement):
    operators = {"suma": "+", "resta": "-"} # Aca deberia ir la palabra raiz nomas
    doc = npl(statement)
    mathProblem = []
    for token in doc:
        if token.pos_ in ["NOUN", "NUM"]:
            mathProblem.append(token)
        print(f"{token.text:{10}} {token.pos_:{10}} {token.is_stop:{10}} {spacy.explain(token.tag_)}")
    # print(problema)

    def translate(token):
      if token.text in list(operators.keys()): # TODO: Agregar logica lemmatizar y abstraer (se repite abajo)
        return (operators[token.text], token)
      else:
        return (token.text, token)
    translatedProblem = list(map(translate, mathProblem))
    # print(problema_traducido)
    finalTranslatedProblem = []
    for palabra, token in translatedProblem:
      if token.text in list(operators.keys()):
        noun = palabra
      else:
        finalTranslatedProblem.append(palabra)
        finalTranslatedProblem.append(noun)
    finalTranslatedProblem.pop()
    # print(problema_traducido2)
    equation = ' '.join(finalTranslatedProblem)
    return equation