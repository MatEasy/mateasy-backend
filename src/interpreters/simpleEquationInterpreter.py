import spacy

# Resolvé la ecuación: x - 695 = 4432.
# Resolvé 17x + 12y = 51.
npl = spacy.load('es_core_news_lg')


def translate_statement(statement):
    doc = npl(statement)  # TODO
    operators = ['+', '-', '*', '/', '=', '^', '<', '>']
    equation_parts = []
    for token in doc:
        # TODO: Agregar chequeo numerico, idem suma y resta
        if token.pos_ == "NUM" or token.text in operators or (token.text.isalpha() and token.__len__() == 1):
            equation_parts.append(token.text)
        print(f"{token.text:{10}} {token.pos_:{10}} {token.is_stop:{10}} {spacy.explain(token.tag_)}")
    print(equation_parts)
    equation = ' '.join(equation_parts)
    return equation
