from src.modelTrainer import model, clean_text


def predict(statement):
    cleaned_statement = clean_text(statement)
    return model.predict([cleaned_statement])[0]
