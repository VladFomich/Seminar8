import json
import os
os.chdir("DZ8")
db_path = 'phone_book.json'
head_1 = 'Выберите: 1 - Показать справочник | 2 - Добавить запись | 3 - Поиск | 4 - Изменить/Удалить | 0 - Выход\n'
head_2 = 'Действия: 1 - Удалить | 2 - Изменить | 0 - Назад\n '

phone_book = {}

def print_db(book):
    print('______________________________Справочник_______________________________\n')
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()
    print('________________________________________________________________________\n')

def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as tmp: 
        tmp.write(json.dumps(db, ensure_ascii=False)) 
        print('Справочнк сохранен\n')

def load_db(path):
    # загрузить из json
    with open(path, 'r', encoding='utf-8') as tmp: 
        BD = json.load(tmp) 
    print('Справочник загружен\n')
    return BD

def new_record_indb(book):
    usr={}
    tmp=input('Введите имя: ')
    usr['телефон(ы): ']=list(input('телефон(ы): ').split())
    usr['День рождения: ']=input('день рождения: ')
    usr['эл.почта: ']=input('эл.почта: ')
    for i in usr:
        if usr[i] == "":  usr[i] = "Нет"
    book[tmp]=usr
    

def change_indb(book):
    sirc = input("Введите имя для изменения: ")
    for k,v in book.items():
        if sirc in k or sirc in v:
            print (k,v)
            option = None
            while option != '3':
                option = input(f'{head_2}').lower()
                if option == '1':
                    del book[k]
                    print("Запись удалена\n")
                    return
                elif option == '2':
                    del book[k]
                    new_record_indb(book)
                    print("Запись изменена\n")
                    return
                elif option == '0': 
                    return      
    else: 
        print("Запись не найдена\n")    
            
def find_indb(book):
    sirc = input("Введите имя для поиска: ")
    for k,v in book.items():
        if sirc in k or sirc in v:
            print (k,v)
            return
    else: 
        print("Запись не найдена\n")              
        
try:
    phone_book=load_db(db_path)
except:
    phone_book = {
    'Антон Петров':{'телефон(ы): ': ['79893456789','790634547684'] , 'День рождения: ': '07.09.1974', 'эл.почта: ':"mail@mail.ru"},
    'Сергей Иванов':{'телефон(ы): ': ['78436840045','77554802591'] , 'День рождения: ': '10.01.1982', 'эл.почта: ':"yandex@yandex.ru"},
    'Елена Михайлова':{'телефон(ы): ': ['78436840045'] , 'День рождения: ': '13.11.1989', 'эл.почта: ':"gmail@gmail.ru"}}
    print('Справочник не найден. Создан шаблон\n')


option = None
while option != '0':
    option = input(f'{head_1}').lower()
    if option == '1':
        print_db(phone_book)
    elif option == '2':
        new_record_indb(phone_book)
    elif option == '3':
        find_indb(phone_book)
    elif option == '4':
        change_indb(phone_book)
save_db(db_path, phone_book)