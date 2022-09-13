import src.interpreters.addSubstractInterpreter as addSubstractInterpreter
import src.interpreters.complexEquationInterpreter as complexEquationInterpreter
import src.interpreters.simpleEquationInterpreter as simpleEquationInterpreter
import src.interpreters.simpleFunctionInterpreter as simpleFunctionInterpreter
import src.interpreters.complexFunctionInterpreter as complexFunctionInterpreter


def interpret(prediction, statement):
    if prediction == "suma" or prediction == "resta":
        return Response("equation", addSubstractInterpreter.translate_statement(statement))
    if prediction == "ecuacion-explicita":
        return Response("equation", simpleEquationInterpreter.translate_statement(statement))
    if prediction == "ecuacion-implicita":
        return Response("equation", complexEquationInterpreter.translate_statement(statement))
    if prediction == "funcion-explicita":
        return Response("function", simpleFunctionInterpreter.translate_statement(statement))
    if prediction == "funcion-implicita":
        return Response("function", complexFunctionInterpreter.translate_statement(statement))
    else:  # TODO poner los demas interpreters
        return Response("ecuacion default", "x + 1 = 2")


class Response:

    def __init__(self, tag, expression):
        self.tag = tag
        self.expression = expression
