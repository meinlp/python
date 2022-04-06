import pandas


def prepare_dict(filename, lang_from, lang_to):
    df = pandas.read_csv(filename)
    df.to_csv(f'{filename}_backup', index=False)

    # df = df.drop(df[df[lang_to] == 'Загрузка...'].index)

    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True)
    df.dropna(subset=[lang_from], inplace=True)

    # df = df.drop(df[df[lang_from].map(len) < 3].index)
    # df = df.sort_values(by='Index')
    # df['Index'] = range(1, len(df) + 1)
    # df = df.reset_index()
    # df = df.reindex()

    df.to_csv(filename, index=False)
