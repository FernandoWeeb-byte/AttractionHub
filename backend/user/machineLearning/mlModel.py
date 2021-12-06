import pandas as pd
import numpy as np
import joblib
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


SCRIPT_DIR = os.path.dirname(os.path.abspath('/home/lucas/Dev/SDProject/AttractionHub/backend/user/authentication/views.py'))
print('--------test----------')
print(SCRIPT_DIR)

sys.path.append(os.path.dirname(SCRIPT_DIR))

from authentication.views import permission
from attractionsList.models import Attraction, Genre


def getGenres(attrac):
    df = {}
    temp = []
    for i in Genre.objects.all():
        temp.append(i.title)
    temp = list(set(temp))
    for i in temp:
        df[i] = []
    return df

    

def preProcess(token):
    user = permission(token)
    # lista_final = []
    
    attrac = user.attractions
    #gen = user.attractions.all().genre.values()

    df = getGenres(attrac)

    for obj in attrac.all():
        temp = []
        for s in obj.genre.all().values():
            # lista_final[ind]['genre'].append(s['title'])
            df[s['title']].append(1)
            temp.append(s['title'])
        # df['genre'].append(temp)
        # temp = list(set(df.keys()).difference(set(temp)))
        temp2 = [i for i in df.keys() if i not in temp]
        for i in temp2:
            df[i].append(0)
    

    df['like'] = []
    for x in attrac.all().values():
        # x['stream'] = []
        # x['genre'] = []
        # lista_final.append(x)
        if x['like'] in [True,False]:
            if x['like']:
                df['like'].append(1)
            else:
                df['like'].append(0)
        else:
            df['like'].append(None)
        print(x['title'])

    # print('--------start lf--------')
    # print(lista_final)
    # print('--------end lf--------')
    # print('--------start gen--------')
    # print(gen)
    # print('--------end gen--------')
    # print(lista_final)
    print('\n\n-------------------')
    # print(df)
    df = pd.DataFrame(df)
    print(df)

    return df

def train(dataset:pd.DataFrame):
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)
    classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 24)
    classifier.fit(X_train, y_train)
    joblib.dump(classifier, "rfModel.joblib")

    

def predict(ident):
    try:
        attrac = Attraction.objects.get(id=ident)
    except Exception:
        raise Exception('attraction not found')
    
    df = getGenres(attrac)
    temp = []
    for s in attrac.genre.all().values():
        # lista_final[ind]['genre'].append(s['title'])
        df[s['title']].append(1)
        temp.append(s['title'])
    # df['genre'].append(temp)
    # temp = list(set(df.keys()).difference(set(temp)))
    temp2 = [i for i in df.keys() if i not in temp]
    for i in temp2:
        df[i].append(0)

    dataset = pd.DataFrame(df)

    
    X = dataset.iloc[:, :].values
    # load
    classifier = joblib.load("rfModel.joblib")
    prediction2 = classifier.predict(X)
    prediction = classifier.predict_proba(X)
    print(classifier.classes_,prediction)
    print(classifier.classes_,prediction2)
    ret = {str(classifier.classes_[0]):prediction[0][0],str(classifier.classes_[1]):prediction[0][1]}
    print(ret)
    return ret



