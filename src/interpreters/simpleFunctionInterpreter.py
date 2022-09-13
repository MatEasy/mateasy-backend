init_characters = ["(", "{", "[", "F", "f", "x", "y", "X", "Y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
end_characters = [")", "}", "]", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# TODO: Si no arranca con f(x) agregarselo
# TODO: normalizar espacios al final de todo
# Pasar todo a minuscula ni bien entra

def translate_statement(statement):
    init_index = search_character(init_characters, statement) - 1  # TODO: Revisar
    end_index = len(statement) - search_character(end_characters, statement[::-1])
    equation = statement[init_index:end_index]
    # Chequeo si esta igualado a f(x) -> Ver que hacer con caso y = (...)
    # if not statement.replace(" ", "").contains("f(x)"):
    #    equation = "f(x) = " + equation
    return equation


def search_character(characters, statement):
    index = len(statement) + 1
    for character in characters:
        searched_index = statement.find(character)
        if searched_index < index and searched_index != -1 and following_characters_accepted(statement, searched_index):
            index = searched_index
    return index


# Si viene algo como "Despeja x de tal ecuacion (...)" veo que el proximo caracter sea un caracter aceptado
def following_characters_accepted(statement, index):
    accepted_characters = [*init_characters, *end_characters, "(", "x", "[", "+", "-", "*", "/", "=", "^", " "]
    return statement[index + 1] in accepted_characters and statement[index + 2] in accepted_characters
