import json
import csv
import os

def save_game(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
        
def write_to_csv(data):
    with open("data.csv", "a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)
        

print("\nНажмите 'g' чтобы начать ваш путь")
road = input()
if road.lower() == "g":
    nam = input("Введите свое имя:")
    smiley = "\u263A"
    stress = 100
    characteristic1 = {"name": "Звери", "age": "неизвестно", "osobennosty": "Убивать сразу"}
    damage = int 
    characters = ["animals", "the main character", "killer"]
    locations = ["passage", "room", "cave", "library"]
    actions = ["pass", "explore", "escape", "sleep"]

    print(f"{nam}, добро пожаловать в игру!{smiley}")
    print(" ")
    for i in range(len(characters)):
        print(f"{characters[i]} was in the {locations[i]} and was {actions[i]}.")

    print(f"{nam}, добро пожаловать в игру!{smiley}")
    print(f"Вы просыпаетесь в загадочном особняке. Вокруг вас темнота и тишина.\nВаш стресс: {stress - 80}")
    print("Что вы хотите сделать?")
    print("1. Встать и осмотреться.")
    print("2. Попытаться заснуть снова.")

    vybraty1 = input("Введите номер выбранного действия: ")

    if vybraty1 == "1":
        print(f"Вы встаете и осматриваетесь. В комнате вы видите старинный камин и дверь.\nВаш стресc: {stress - 50}")
        print("Что вы хотите сделать?")
        print("1. Подойти к камину.")
        print("2. Открыть дверь и выйти из комнаты.")

        vybraty2 = input("Введите номер выбранного действия: ")

        if vybraty2 == "1":
            print(f"Вы подходите к камину и обнаруживаете секретный проход.\nВаш стресс: {stress - 40}")
            print("Что вы хотите сделать?")
            print("1. Войти в проход.")
            print("2. Исследовать комнату дальше.")
            data = [nam, vybraty1, vybraty2]
            save_game(data)
            write_to_csv(data)

            vybraty3 = input("Введите номер выбранного действия: ")

            if vybraty3 == "1":
                print(f"Вы входите в проход и на вас нападают звери непонятной породы.\nВаш стресс: {stress}")
                print("Вы мертвы")
                data = [nam, vybraty1, vybraty2, vybraty3]
                save_game(data)
                write_to_csv(data)
            elif vybraty3 == "2":
                print(f"Вы чудом одумались и успели избежать опасность")
                print("Вы живы, Продолжениие следует...")
                data = [nam, vybraty1, vybraty2, vybraty3]
                save_game(data)
                write_to_csv(data)
        elif vybraty2 == "2":
            print(f"Вы открываете дверь и оказываетесь в коридоре с множеством других дверей.\nВаш стресс: {stress - 45}")
            print("Что вы хотите сделать?")
            print("1. Выбрать случайную дверь и войти в нее.")
            print("2. Вернуться обратно в комнату.")
            data = [nam, vybraty1, vybraty2]
            save_game(data)
            write_to_csv(data)

        vybraty4 = input("Введите номер выбранного действия: ")
        if vybraty4 == "1":
            print(f"Вы выбираете случайную дверь и попадаете в тайную библиотеку.\nВаш стресс: {stress - 70}")
            print("Продолжениие следует...")
            data = [nam, vybraty1, vybraty2, vybraty4]
            save_game(data)
            write_to_csv(data)
        elif vybraty4 == "2":
            print("Вы возвращаетесь обратно в комнату и решаете исследовать ее дальше.")
            print("Продолжениие следует...")
            data = [nam, vybraty1, vybraty2, vybraty4]
            save_game(data)
            write_to_csv(data)
    elif vybraty1 == "2":
        print(f"Вы пытаетесь заснуть снова, но не можете успокоиться.\nВаш стресс: {stress - 10}")
        print("Что вы хотите сделать?")
        print("1. Встать и осмотреться.")
        print("2. Попытаться заснуть снова.")
        data = [[nam, vybraty1]]
        save_game(data)
        write_to_csv(data)
                
        vybraty5 = input("Введите номер выбранного действия: ")

        if vybraty5 == "1":
            print(f"Вы встаете и осматриваетесь. В комнате вы видите старинный камин и дверь.\nВаш стресс: {stress - 50}")
            print("Что вы хотите сделать?")
            print("1. Подойти к камину.")
            print("2. Открыть дверь и выйти из комнаты.")
            data = [nam, vybraty1, vybraty5]
            save_game(data)
            write_to_csv(data)
            
            vybraty6 = input("Введите номер выбранного действия: ")

            if vybraty6 == "1":
                print(f"Вы подходите к камину и обнаруживаете секретный проход.\nВаш стресс: {stress - 40}")
                print("Что вы хотите сделать?")
                print("1. Войти в проход.")
                print("2. Исследовать комнату дальше.")
                data = [nam, vybraty1, vybraty5, vybraty6]
                save_game(data)
                write_to_csv(data)
                
                vybraty7 = input("Введите номер выбранного действия: ")

                if vybraty7 == "1":
                    print(f"Вы входите в проход и на вас нападают звери непонятной породы.\nВаш стресс: {stress},{characteristic1}")
                    print("Продолжениие следует...")
                    data = [nam, vybraty1, vybraty5, vybraty6, vybraty7]
                    save_game(data)
                    write_to_csv(data)
                elif vybraty7 == "2":
                    print("Вы продолжаете исследовать комнату и находите старинный дневник.")
                    print("Продолжениие следует...")
                    data = [nam, vybraty1, vybraty5, vybraty6, vybraty7]
                    save_game(data)
                    write_to_csv(data)
            elif vybraty6 == "2":
                print(f"Вы открываете дверь и оказываетесь в коридоре с множеством других дверей.\nВаш стресс: {stress - 45}")
                print("Что вы хотите сделать?")
                print("1. Выбрать случайную дверь и войти в нее.")
                print("2. Вернуться обратно в комнату.")
                data = [nam, vybraty1, vybraty5, vybraty6]
                save_game(data)
                write_to_csv(data)
                
                vybraty8 = input("Введите номер выбранного действия: ")

                if vybraty8 == "1":
                    print("Вы выбираете случайную дверь и попадаете в тайную библиотеку.")
                    print("Продолжениие следует...")
                    data = [nam, vybraty1, vybraty5, vybraty6, vybraty8]
                    save_game(data)
                    write_to_csv(data)
                elif vybraty8 == "2":
                    print("Вы возвращаетесь обратно в комнату и решаете исследовать ее дальше.")
                    print("Продолжениие следует...")
                    data = [nam, vybraty1, vybraty5, vybraty6, vybraty8]
                    save_game(data)
                    write_to_csv(data)
        elif vybraty5 == "2":
            print("Вы продолжаете пытаться заснуть, но ничего не получается.")
            print("Продолжениие следует...")
            data = [nam, vybraty1, vybraty5]
            save_game(data)
            write_to_csv(data)
else:
    print("Извините, но это некорректный выбор. Пожалуйста, выберите действие 1 или 2.Или перезапустите команду")

