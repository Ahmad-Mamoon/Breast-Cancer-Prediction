import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

def get_data():
    df = pd.read_csv('data/data.csv')

    df = df.drop(['Unnamed: 32', 'id'], axis=1)

    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

    return df

def create_model(data):
    X = data.drop('diagnosis', axis=1)
    y = data['diagnosis']
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    model = LogisticRegression()
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    return model,scaler


    
def main():
    data = get_data()    
    model, scaler = create_model(data)

    with open('model/model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    with open('model/scaler.pkl', 'wb') as scaler_file:
        pickle.dump(scaler, scaler_file)

        

if __name__ == '__main__':
    main()