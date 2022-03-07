import json
import pickle
import numpy as np

__locations = None
__model     = None
__data_columns = None

def predict_home_price(loc,sqft,bhk,bath):

    try:
        loc_index = __data_columns.index(loc.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[2] = bath
    x[1] = bhk

    if loc_index>0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def get_loc_names():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts...')
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/columns.json",'r') as f:
       __data_columns =  json.load(f)['data_columns']
       __locations    = __data_columns[3:]


    with open("./artifacts/BHP_model.pickle", 'rb') as f:
        __model = pickle.load(f)


if __name__ == '__main__':
  load_saved_artifacts()
  print(get_loc_names())
  print(predict_home_price('Whitefield',1000,3,3),'Lakhs')
  print(predict_home_price('Whitefield',1000,2,2),'Lakhs')
  print(predict_home_price('Indira Nagar', 1000, 3, 3), 'Lakhs')
  print(predict_home_price('Indira Nagar', 1000, 2, 2) ,'Lakhs')
  print(predict_home_price('Kalhalli', 1000, 3, 3), 'Lakhs')
  print(predict_home_price('Kalhalli',1000,2,2),'Lakhs')
