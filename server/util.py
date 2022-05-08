import json
import pickle
import numpy as np

__locations = None
__markets = None
__data_columns = None
__model = None


def predict_price(area, market, district):
    try:
        district_index = __data_columns.index(district.lower())
    except:
        district_index = -1

    inputs = np.zeros(len(__data_columns))
    inputs[0] = area
    if market == '2nd_hand':
        inputs[1] = 1
    if district_index >= 0:
        inputs[district_index] = 1
    return round(__model.predict([inputs])[0], 2)


def get_district_names():
    return __locations


def get_market_types():
    return __markets


def load_save_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __markets
    global __model

    with open("./artifacts/columns.json", 'r') as file:
        __data_columns = json.load(file)['data_columns']
        __markets = __data_columns[1]
        __locations = __data_columns[2:]

    with open("./artifacts/hong_kong_home_price_model.pickle", 'rb') as file:
        __model = pickle.load(file)

    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_save_artifacts()
    print(get_district_names())
    print(get_market_types())
    print(predict_price(600, '2nd_hand', 'HK_Central_and_Western'))
