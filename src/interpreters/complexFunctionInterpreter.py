import spacy
from recognizers_number import recognize_number, Culture

npl = spacy.load('es_core_news_lg')
# Si vienen los conceptos "ordenada" y "pendiente" -> resolucion 1
# Si vienen dos puntos -> resolucion 2
# Si viene como ecuacion -> resolucion 3

dividing_characters = ["y", ",", "-", "/"]
ordenada_al_origen = ["ordenada", "ord.", "ordenada al origen", "ord. al origen", "ord al origen",
                      "ordenada en el origen", "ord en el origen", "ord. en el origen"]
pendiente = ["pendiente"]


def translate_statement(statement):
    statement = statement.lower()
    for character in dividing_characters:
        if character in statement:
            return translate(statement, character)

# TODO: Ver numeros negativos
def translate(statement, character):
    divided_statement = statement.split(character)
    first_part = npl(divided_statement[0])
    second_part = npl(divided_statement[1])
    # Analisis de la primera parte
    for token in first_part:
        if token.text in ordenada_al_origen:
            ord_al_origen = search_number(first_part)
    for token in first_part:
        if token.text in pendiente:
            pend = search_number(first_part)
    # Analisis de la segunda parte
    for token in second_part:
        if token.text in ordenada_al_origen:
            ord_al_origen = search_number(second_part)
    for token in second_part:
        if token.text in pendiente:
            pend = search_number(second_part)
    equation = "f(x) = " + str(pend) + " * x" + " + " + str(ord_al_origen)
    return equation


def search_number(statement):
    statement = npl(statement)
    for token in statement:
        if token.pos_ == "NUM" or token.text.isnumeric():
            if token.text.isnumeric():
                return token.text
            else:  # Es un numero en palabras
                number = recognize_number(token.text, Culture.Spanish)[0].resolution["value"]
                return number
