from random import *
import json

import easygui

phonebook = {}

def save():
    with open("phonebook.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Наш телефонный справочник был успешно сохранен в файле phonebook.json")
    
def load():
    with open("phonebook.json", "r", encoding="utf-8") as file: 
        return json.loads(file.read())
 
# Получить списки контактов    
def Get_list_of_contacts(phones):
    list_of_contacts = []
    for k, v in phonebook.items():
        list_of_contacts.append(k + ': ' + str(v))
    return list_of_contacts

try:
    phonebook = load()
    easygui.msgbox("Телефонная книга загружена")
except:
    easygui.msgbox("Что-то пошло не так")

while True:
    Bottons_commands = ["Показать все записи", "Добавить контакт", "Изменить контакт", "Удалить контакт", "Сохранить телефонную книгу", "Загрузить телефонную книгу"]
    command = easygui.choicebox(text:="Выберете команду для продолжения работы", title:="", Bottons_commands)
         
    if command == None:
        save()
        easygui.msgbox("Заходите еще")
        break
    elif command == "Показать все записи":
        list_of_contacts = Get_list_of_contacts(phonebook)
        contact = easygui.choicebox(text:="Ниже приведен список контактов", title:="", list_of_contacts)
        
    elif command == "Добавить контакт":
        Phones = []   
        input_list = ["Имя", "Телефон 1", "Телефон 2", "Телефон 3", "Дата рождения", "Email"]
        output = easygui.multenterbox("Новый контакт", "Создание нового кантакты", input_list, input_list)
        
        Name = output[0]
        
        i = 1
        while i <= 3:
            if output[i] != None or output[i] != '':
                Phones.append(output[i])
            i += 1
                
        Birthday = output[4]
        Email = output[5]
        
        phonebook[Name] = { 'phones': Phones }
        
        if len(Phones) != 0:
            phonebook[Name]['phones'] = Phones     
        if Birthday != '':
            phonebook[Name]['birthday'] = Birthday         
        if Email != '':
            phonebook[Name]['email'] = Email
        
        easygui.msgbox("Контакт успешно добавлен в телефонную книгу!")
        
    elif command == "Изменить контакт":
        Name = ''
        Phones = []
        Birthday = ''
        Email = ''
        
        contact = easygui.choicebox(text:="Какой из контактов вы хотели бы изменить", title:="", phonebook)
        if contact:
            
            com = easygui.choicebox(text:="Выберете пункт который вы бы хотели изменить", title:="", ['Name', 'Phone', 'Birthday', 'Email'])            
            
            if com == "Name":
                
                New_Name = easygui.enterbox(msg:="Введите новое имя", title:="Новое имя", "Name")     
                phonebook[New_Name] = phonebook.pop(contact)
                
            elif com == "Phone":
                New_Phone = easygui.enterbox(msg:="Введите новый телефон", title:="Новый телефон", "Phone") 
                Phones.append(New_Phone)
                phonebook[contact]['phones'] = Phones
            elif com == "Birthday":
                New_Birthday = easygui.enterbox(msg:="Введите дату рождения", title:="Новая дата рождения", "Birthday")                           
                phonebook[contact]['birthday'] = New_Birthday
            elif com == "Email":
                New_Email = easygui.enterbox(msg:="Введите Email", title:="Новый email", "Email") 
                phonebook[contact]['email'] = New_Email
            
            easygui.msgbox("Контакт изменен")
        else:
            easygui.msgbox("Такого контакта не существует")
    
    #Help ненужен так как это GUI 
    # elif command == "/help":     
    #     with open('Readme.md', encoding='utf-8') as f:
    #         text = f.read()
    #         print(text)
        
    elif command == "Удалить контакт":
        contact = easygui.choicebox(text:="Какой из контактов вы хотели бы удалить", title:="", phonebook)
        try:
            del phonebook[contact]
            easygui.msgbox("Контакт успешно удален")
        except:
            easygui.msgbox("Такого контакта нет в телефонной книге!")
    elif command == "Соханить телефонную книгу":
        save()
        easygui.msgbox("Телефонная книга сохранена")
    elif command == "Загрузить телефонную книгу":
        phonebook = load()
        easygui.msgbox("Телефонная книга успешно загружена")
    else:
        easygui.msgbox("Неопознанная команда")
        