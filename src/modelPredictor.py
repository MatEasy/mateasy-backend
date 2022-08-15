from src.modelTrainer import model, X_train, y_train, clean_text

def predict(statement):
    print('estoy por predecir')
    model.fit(X_train, y_train) #TODO moverlo para que entrene en otro lado una sola vez al principio
    print('entrene')
    cleaned_statement = clean_text(statement)
    print(model.predict([cleaned_statement])[0])
    return model.predict([cleaned_statement])[0]
