# TODO integrar modelo

import src.interpreters.addSubstractInterpreter as addSubstractInterpreter
import src.interpreters.simpleEquationInterpreter as simpleEquationInterpreter


def interpret(prediction, statement):
    if prediction == 'suma':
        return addSubstractInterpreter.translate_statement(statement)
    if prediction == 2:
        return simpleEquationInterpreter.translate_statement(statement)
    else:  # TODO poner los demas interpreters
        return "ecuacion default"
