### 🤡🤡🤡 ###

import pandas as pd
import numpy as np

# суть алгоритма:


# - сортируем участников по количеству песен
# - присваиваем веса участникам: 10 за первую и +10 за каждую последующую, каждому участнику даем по 6 жизней
#
# - для каждой песни высчитываем score:
#     score = avg_weight
#     for musician in musicians:
#         if musician < avg_weight:
#             score -= musician
#         else:
#             score += musician
# - если у всех членов топовой песни есть жизни, переносим самую топовую песню в финальный сетлист, если нет,
# смотрим на следующую
# - вычитаем у всех участников по одной жизни
# - UPDATE решил после каждого переноса пересчитывать веса и score, оставлять только жизни
# - повторяем сколько-то раз


# P.S. проверки ников:
#     lowercase
#     optional, n/a - delete
#     если один из символов не буква, цифра или подчеркивание, отрезать все до конца
#     добавить @ если забыли

LIVES_COUNT = 5
FINAL_SONGS_COUNT = 25
INSTRUMENTS_LIST = ['Vocal 1',
                     'Vocal 2',
                     'Guitar 1',
                     'Guitar 2',
                     'Bass',
                     'Drums',
                     'Keyboard+Other']

# читаем csv, создаем датафрейм, первую строку скипаем так как там полотно текста, которое без
# этого воспринимается как заголовок таблицы.
original_data = pd.DataFrame(pd.read_csv("test_info_2.csv", skiprows=1))

# нам похуй на несобравшиеся песни, удаляем
filtered_data = original_data[original_data.isin(["0.Ready!"]).any(axis=1)]
filtered_data.insert(0, "score", "")
filtered_data = filtered_data.reset_index(drop=True)

final_data = pd.DataFrame(
    columns=filtered_data.columns)  # плейсхолдер для финального сетлиста с таким же набором столбцов

# создаем и причесываем список музыкантов
member_list_full = []
member_list_unique = []
for instrument in INSTRUMENTS_LIST:
    for index, member in filtered_data[instrument].items():
        if type(member) == str:
            member = member.lower()  # у оззи блять пять написаний ника, сколько можно
            member = member.lstrip()  # пробелы слева - нахуй
            for i, char in enumerate(member):  # всякое " могу уступить" в конце - нахуй
                if not (char.isalnum() or char in ['@', '_', "/"]):
                    member = member[:i]
            if member not in ["nan", "optional", "n/a"]:
                if not member.startswith("@"):  # оззи с Дашей все забывают что ники в телеге начинваются с @
                    member = "@" + member
                member_list_full.append(member)
                filtered_data.loc[index, instrument] = member
            else:  # а ебну-ка я вообще все кроме ников, для постоянства
                filtered_data.loc[index, instrument] = np.nan
for item in member_list_full:
    if item not in member_list_unique:
        member_list_unique.append(item)

# подсчитываем вес для музыкантов
member_data = pd.DataFrame(columns=['name', 'weight', 'lives'])
for member in member_list_unique:
    lives = LIVES_COUNT
    name = member
    weight = member_list_full.count(member) * 10
    member_data.loc[len(member_data.index)] = [member, weight, lives]  # тут забавная логика. С каждым новым элементом
    # в member_data его len увеличивается на 1, так что каждый раз при вызове этой хуйни оно пишется в новую строку

# Цикл пока не наберем достаточно песен
while len(final_data) < FINAL_SONGS_COUNT:
    avg_weight = round(member_data["weight"].mean())
    filtered_data_len = len(filtered_data.index)

    people_with_one_song = member_data.loc[member_data['weight'] == 10]['name'].tolist()
    print('yo', people_with_one_song)

    for human in people_with_one_song:
        if member_data.loc[member_data['lives'] == LIVES_COUNT]['name'].tolist():
            print(human)
            index_list = filtered_data.index[filtered_data.isin([human]).any(axis=1)].tolist()
            print(index_list)
            index = index_list[0]
            print(index)
            row_to_add = pd.DataFrame([filtered_data.loc[index]], columns=filtered_data.columns)
            final_data = pd.concat([final_data, row_to_add], ignore_index=True)
            for instrument in INSTRUMENTS_LIST:
                member_name = filtered_data[instrument].iloc[index]
                if member_name in member_list_unique:
                    member_index = member_data[member_data['name'] == member_name].index[0]
                    member_data.loc[member_index, 'lives'] -= 1
        if len(final_data) >= FINAL_SONGS_COUNT:
            break
        filtered_data = filtered_data.drop(index)
        filtered_data.reset_index(drop=True, inplace=True)

    for index in range(0, filtered_data_len):
        # для каждой песни высчитываем score, выставляя сначала его как средний вес а потом либо вычитая из него тех
        # у кого вес ниже и прибавляя если выше.
        score = avg_weight
        for instrument in INSTRUMENTS_LIST:
            if filtered_data[instrument].iloc[index] in member_list_unique:
                member_name = filtered_data[instrument].iloc[index]
                member_weight = member_data[member_data['name'] == member_name]['weight'].iloc[0]
                if member_weight >= avg_weight:
                    score += member_weight
                else:
                    # для тех кто ниже среднего добавил множитель иначе они вообще ни на что не влияют
                    score -= member_weight
        filtered_data.loc[index, 'score'] = score
    filtered_data = filtered_data.sort_values(by='score').reset_index(drop=True)

    the_choice_is_made = 0
    index = 0
    while not the_choice_is_made:
        skip_the_song = 0
        # проверяем есть ли жизни у всех участников песни, если нет, переходим на следующую строку
        for instrument in INSTRUMENTS_LIST:
            member_name = filtered_data[instrument].iloc[index]
            if member_name in member_list_unique:
                if member_data[member_data['name'] == member_name]['lives'].iloc[0] < 1:
                    skip_the_song = 1
                    index += 1
        # если жизни есть, то переносим песню в финальный список и дропаем ее
        if not skip_the_song:
            row_to_add = pd.DataFrame([filtered_data.loc[index]], columns=filtered_data.columns)
            final_data = pd.concat([final_data, row_to_add], ignore_index=True)
            for instrument in INSTRUMENTS_LIST:
                member_name = filtered_data[instrument].iloc[index]
                if member_name in member_list_unique:
                    member_index = member_data[member_data['name'] == member_name].index[0]
                    member_data.loc[member_index, 'lives'] -= 1
            filtered_data = filtered_data.drop(index)
            filtered_data.reset_index(drop=True, inplace=True)
            the_choice_is_made = 1
        # если пробежались по всем и ничего не нашли то берем с меньшим весом, даже если жизней уже нет.
        # это для случаев когда не набралось песен подходящих по условиям.
        elif index >= filtered_data_len - 1:
            row_to_add = pd.DataFrame([filtered_data.loc[1]], columns=filtered_data.columns)
            final_data = pd.concat([final_data, row_to_add], ignore_index=True)
            for instrument in INSTRUMENTS_LIST:
                member_name = filtered_data[instrument].iloc[1]
                if member_name in member_list_unique:
                    member_index = member_data[member_data['name'] == member_name].index[0]
                    member_data.loc[member_index, 'lives'] -= 1
            filtered_data = filtered_data.drop(1)
            filtered_data.reset_index(drop=True, inplace=True)
            the_choice_is_made = 1

# все кто остались со всеми жизнями:
additional_data = pd.DataFrame(columns=filtered_data.columns)
for poor_bastard in member_data.loc[member_data['lives'] == 5, 'name'].tolist():
    data_to_add = filtered_data[filtered_data.isin([poor_bastard]).any(axis=1)]
    additional_data = pd.concat([additional_data, data_to_add], ignore_index=True)
columns = ["score", "Band / Группа", "Song / Название"] + INSTRUMENTS_LIST

print("\nФинальный список:\n", final_data)

print("\nНевошедшие песни:\n", filtered_data)

pd.set_option('display.max_rows', None)
print("\nСтатистика по пользователям:\n", member_data.sort_values(by='lives'))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print("\nПесни которые никуда не вошли и где есть люди которые нигде больше не играют:\n", additional_data[columns].sort_values(by='Song / Название').drop_duplicates())


