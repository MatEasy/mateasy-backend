import src.interpreters.interpreter as interpreter
import src.modelPredictor as modelPredictor


def result(statement):
    statement = statement.lower()
    # statement = unidecode.unidecode(statement)
    prediction = modelPredictor.predict(statement)
    equation = interpreter.interpret("funcion-explicita", statement)  # TODO: Modificar
    return equation
