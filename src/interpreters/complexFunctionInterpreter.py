import re

import numpy as np
import spacy
from recognizers_number import recognize_number, Culture

import src.interpreters.complexEquationInterpreter as complexEquationInterpreter
from src.interpreters.domain import Response

npl = spacy.load('es_core_news_lg')
# TODO derivar a cada sub interprtador de cada funcion segun estos 3 tipos de abajo
# Si vienen los conceptos "ordenada" y "pendiente" -> resolucion 1 TODO: Si viene algo complejo, mandarlo al complex equation
# Si vienen dos puntos -> resolucion 2
# Si viene como ecuacion -> resolucion 3

dividing_characters = ["y", ",", "-", "/"]  # TODO: Se puede replicar con la logica del find_near_operator?
ordenada_al_origen = ["ordenada", "ord.", "ordenada al origen", "ord. al origen", "ord al origen",
                      "ordenada en el origen", "ord en el origen", "ord. en el origen"]
pendiente = ["pendiente"]


def translate_statement(statement, tag):
    statement = statement.lower()
    # TODO ver a que tipo de funcion segun los 3 casos de arriba
    if "puntos" in statement:
        result = translate_simple_points_fun(statement)
        return Response(result, tag)
    # Si es del tipo ord al origen y pendiente
    if any(word in statement for word in ordenada_al_origen + pendiente):
        for character in dividing_characters:
            if character in statement:
                result = translate_intercept_and_slope_fun(statement, character)
                return Response(result, tag)
    # Si viene como ecuacion
    else:
        result = complexEquationInterpreter.translate_statement(statement, tag)
        return Response(result, tag)


# TODO: Ver numeros negativos
# Funcion para resolver funciones lineales cuando nos dan el dato de la ordenada al origen y la pendiente
def translate_intercept_and_slope_fun(statement, character):
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


# .-------------------------------------------------------------------------------------------------------------------------

# Funcion para resolver con dato puntos por los que pasa la funcion
def translate_simple_points_fun(statement):  # TODO ver como escalar esto dependiendo de si es una cuadratica
    # TODO leer alguna palabra clave que me haga dar cuenta q es cuadratica
    r = r"(-?\d+\.?\d*);(-?\d+\.?\d*)"
    points = re.findall(r, statement)
    print(points)

    # TODO en una cuadratica es ax2 +bx +c => entonces tengo que hacer una lista de 3 elementos siendo el ultimo
    #  siempre 1
    def x(point):
        return [float(point[0]), 1]

    def y(point):
        return float(point[1])

    Xs = list(map(x, points))
    Ys = list(map(y, points))
    print(Xs)
    print(Ys)
    a = np.array(Xs)
    b = np.array(Ys)
    resolve = np.linalg.solve(a, b)
    pendiente = round(resolve[0], 2)
    ordenada = round(resolve[1], 2)
    equation = "f(x) = " + str(pendiente) + " * x" + " + " + str(ordenada)  # TODO En una cuadratica cambia la formula
    return equation