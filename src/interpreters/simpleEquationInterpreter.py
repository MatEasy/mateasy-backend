import spacy

# Resolvé la ecuación: x - 695 = 4432.
# Resolvé 17x + 12y = 51.
npl = spacy.load('es_core_news_lg')


def translate(statement):
    doc = npl(statement)  # TODO
    incognita = ["x", "y"]
    operators = ["+", "-", "*", "/", '=']  # TODO
    equation_parts = []
    for token in doc:
        if token.pos_ == "NUM" or token.text in operators or token.text in incognita:
            equation_parts.append(token.text)
        print(f"{token.text:{10}} {token.pos_:{10}} {token.is_stop:{10}} {spacy.explain(token.tag_)}")
    print(equation_parts)
    equation = ' '.join(equation_parts)
    return equation
