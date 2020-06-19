try:
    with open('text.txt') as fobj:
        contents = fobj.read()
        print(contents)
        
except Exception as e:
    print("File Error ", e)

______________

with open('text.txt') as fobj:
    for number, lines in enumerate(fobj):
        print (number+1, lines.upper())
______________

with open('number.txt', 'w'/'a') as fobj:
    fobj.write('100')
    fobj.write('\n')
    fobj.write('5000')
    fobj.write('\n')
    fobj.write('10000')
_______________

with open('number.txt', 'a', encoding='utf-8') as fobj:
    fobj.write('use utf-8 for bangla text')
    fobj.write('\n')
    fobj.write('use utf-8 for bangla text')

_______________

with open('nothing.txt', 'a', encoding='utf-8') as fobj:
    print("Nothing goes unpaid", file=fobj)

_______________ binary-files write and read____________

with open('binary', 'wb') as fobj:
    fobj.write(b'Life is extreamly bad')
    
with open('binary', 'rb') as fobj:
    binary_data = fobj.read()
    decode_data = binary_data.decode('utf-8')
    print(decode_data)

__________________________

import os

if os.path.exists('nothing.txt'):
    print('Yes! your files exist !!!!')
else:
    print('File does not exists')

_______________________


from tempfile import TemporaryFile

with TemporaryFile('w+') as fobj:
    fobj.write("Life is cool . \n")

    fobj.seek(0)
    data = fobj.read()
    print(data)


____________________serialize________

import pickle

dict_data  = {'name':'Ahsan', 'country':'bangladesh'}

with open('serialize', 'wb') as fobj:
    pickle.dump(dict_data, fobj)

with open('serialize', 'rb') as fobj:
    dict_data= pickle.load(fobj)
    print(dict_data)

________________________




