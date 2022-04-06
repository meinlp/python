# Python_learning

[# Lists, Dicts, Variables](./docs/basic.md)

[# Tkinter](./docs/tkinter.md)

## Useful Thingies
``` python
from functools import cache, lru_cache # вызывается перед описанием функции
                                       # сохраняет в памяти предыдущие вызовы функции
@cache                  # это хранит ВСЕ вызовы
@lru_cache(max_size=5)  # a это только 5 последних
def func()
    #some math

import pyperclip # работа с буфером обмена
pyperclip.copy('text')

#html entities
import html
text = 'sometext&#039'
print(html.unescape(text))
```

## Working with files
``` python
with open('my_file.txt', mode='a') as file:
                    # 'r'=open for reading (default)
                    # 'w'=open for writing, truncating the file first
                    # 'x'=create a new file and open it for writing
                    # 'a'=open for writing, appending to the end of the file if it exists
                    # 'b'=binary mode
                    # 't'=text mode (default)
                    # '+'=open a disk file for updating (reading and writing)
i = file.read()
file.write(i)
file.readlines() # построчное чтение, на выходе - список
file.writelines() # построчная запись
```

## CSV
``` python
import pandas
data = pandas.read_csv("some.csv")

# item from a row
i = data['item'].item()

# dict to csv:
data_dict = { "data":["data", "data", "data"]}
data = pandas.DataFrame(data_dict)
data.to_csv("path_to_new.csv")

#looping through pandas
for (index, row) in dataframe.iterrows():
    print(row)

```

## Comprehensions
``` python
# list
new_list = [item for item in list if test]

# dict
new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# dict comprehension with pandas
new_dict = {row.new_key: row.new_value for (index, row) in pandas.DataFrame.iterrows()}
```

## Catching exceptions

``` python
try: #something may cause the exception

except FileNotFoundError as error_message: #will be executed if there was an exception, may use different types of errors
    print(error_message)

else: #do this if there no exceptions

finally: #do this no matter what happens

#you can raise en exception if you want
raise KeyError
```

## JSON
``` python
import json

with open('data.json', 'r') as file:
    data = json.load(file)

new_data = {$some_dict}
data.update(new_data)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

## SMTP
``` python
import smtplib

my_email = "test@gmail.com"
my_pass = "qwerty"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='test@yahoo.com',
        msg='Subject:hello\n\nThis is the body of email'
    )
    connection.close()
```

## Datetime
``` python
import datetime as dt

now = dt.datetime.now()
print(now.year)
```

## Resuests
``` python
import requests
params = {
    'key': 'value'
}
response = requests.get(url='http://url.com/some_data.json', params=params)
print(response)  # it returns response codes, not the data
# print(response.raise_for_status()) # it raises an exception if something goes wrong

data = response.json()  # you can access the data from request in json format
print(data)

```

## Type hints
``` python
def func(var: int) -> bool: #we can declare data type of incoming variables and type of the output for the function
    if condition:
        return True
    else:
        return False
```