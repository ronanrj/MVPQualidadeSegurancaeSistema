from sklearn.model_selection import train_test_split
import pickle
import numpy as np

class PreProcessador:

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """ Cuida de todo o pré-processamento. """
        # limpeza dos dados e eliminação de outliers

        # feature selection

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        # normalização/padronização
        
        return (X_train, X_test, Y_train, Y_test)
    
    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        dados = dataset.values
        X = dados[:, 0:-1]
        Y = dados[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)
    
    def preparar_form(self,form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([form.age,
                            form.sex,
                            form.cp,
                            form.trtbps,
                            form.chol,
                            form.fbs,
                            form.restecg,
                            form.thalachh,
                            form.exng,
                            form.oldpeak
                        ])
        
        # Print dos dados recebidos
        print("Dados recebidos do formulário:", X_input)
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        return X_input
    
    def scaler(self,X_train):
        """ Normaliza os dados. """
        # normalização/padronização
        scaler = pickle.load(open('./MachineLearning/scalers/standard_scaler_heart.pkl', 'rb'))
        reescaled_X_train = self.scaler.transform(X_train)
        return reescaled_X_train
