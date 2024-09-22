import pandas
import random
from card import Card


class Data:
    def __init__(self, lang_from, lang_to):
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.data = self.read(f'data/{self.lang_from}-{self.lang_to}.csv')
        self.learned = self.read(f'data/{self.lang_from}-{self.lang_to}_learned.csv')
        try:
            self.data = pandas.read_csv(f'data/{self.lang_from}-{self.lang_to}.csv')
        except FileNotFoundError:
            self.data = pandas.DataFrame(columns=['English', 'Russian'])
            self.save()
        self.to_learn = self.data.to_dict(orient='index')
        self.lang_from_full = self.data.columns[0]
        self.lang_to_full = self.data.columns[1]

    def prepare(self):
        # TODO check for duplicates
        # TODO check a structure
        # TODO backup
        pass

    def get_new_card(self, word='random'):
        if word == 'random':
            index = random.randint(0, len(self.data) - 1)
        else:
            index = self.data.loc[self.data[self.lang_from_full] == word].index.item()
        card = Card(index=index,
                    word=[self.data.values[index][0],
                          self.data.values[index][1]
                          ],
                    )
        return card

    def delete(self, card: Card):
        cur_choice = self.data.iloc[[card.index]]
        self.data = self.data.drop(cur_choice.index)
        self.save()

    def add(self, new_word, new_translation):
        new_data = pandas.DataFrame({self.lang_from_full: [new_word], self.lang_to_full: [new_translation]})
        self.data = pandas.concat([self.data, new_data], ignore_index=True)
        self.save()

    def read(self, filename):
        try:
            data_frame = pandas.read_csv(filename)
        except FileNotFoundError:
            data_frame = pandas.DataFrame(columns=[self.lang_from_full, self.lang_to_full])
            data_frame.to_csv(filename, index=False)
        except pandas.errors.EmptyDataError:
            data_frame = pandas.DataFrame(columns=[self.lang_from_full, self.lang_to_full])
            data_frame.to_csv(filename, index=False)
        return data_frame

    def alter(self, card: Card, new_word, new_translation):
        self.data.loc[card.index].at[self.lang_from_full] = new_word
        self.data.loc[card.index].at[self.lang_to_full] = new_translation
        self.save()

    def save(self):
        self.data.to_csv(f'data/{self.lang_from}-{self.lang_to}.csv', index=False)

    def move(self, card: Card):

        cur_choice = self.data.iloc[[card.index]]
        print(cur_choice)

        self.learned = pandas.concat([cur_choice, self.learned])
        self.learned.to_csv(f'data/{self.lang_from}-{self.lang_to}_learned.csv', index=False)

        self.data = self.data.drop(cur_choice.index)
        self.save()

    def find(self, word=None, translation=None):
        if word:
            try:
                index = self.data.loc[self.data[self.lang_from_full] == word].index.item()
                return self.data.values[index][0]
            except ValueError:
                return 'not_found'

        elif translation:
            try:
                index = self.data.loc[self.data[self.lang_to_full] == translation].index.item()
                return self.data.values[index][0]
            except ValueError:
                return 'not_found'

        else:
            return 'not_found'
