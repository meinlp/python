PLACEHOLDER = '[name]'

with open("Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()


with open('Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, f'{name}')
        with open(f'Output/ReadyToSend/letter_to_{name}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)

