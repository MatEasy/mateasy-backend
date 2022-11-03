from flask import jsonify

import src.interpreters.interpreter as interpreter
import src.modelPredictor as modelPredictor
from src.utils import is_valid_statement


def result(statement):
    if not is_valid_statement(statement):
        print("no es un enunciado matematico")
        return jsonify({"error": "Invalid input - A mathematical statement is required"}), 400
    statement = statement.lower()
    prediction = modelPredictor.predict(statement)
    equation = interpreter.interpret(prediction, statement)
    return equation
