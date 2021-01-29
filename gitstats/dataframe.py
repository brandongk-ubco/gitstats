import pandas as pd


def aggregate_generator(generator, columns=[]):
    return aggregate_list([g for g in generator])


def aggregate_list(list_items, columns=[]):
    df = pd.DataFrame(columns=columns)
    if list_items:
        df = df.append(pd.concat(list_items), ignore_index=True)
    return df
