import pandas as pd


def aggregate_generator(generator):
    return aggregate_list([g for g in generator])


def aggregate_list(list_items):
    if list_items:
        return pd.concat(list_items)
    return pd.DataFrame()
