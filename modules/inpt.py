import json
while True:
 
    def save_data(slot, var1, var2):
        data = {
            "var1": var1,
            "var2": var2
        }
        with open(f'modules/load/slot{slot}.json', 'w') as file:
            json.dump(data, file)
        print(f'Данные сохранены в слот \033[32m{slot}\033[0m')

    def load_data(slot):
        try:
            with open(f'modules/load/slot{slot}.json', 'r') as file:
                data = json.load(file)
                var1 = data["var1"]
                var2 = data["var2"]
                return var1, var2
        except FileNotFoundError:
            return None, None

    def check_slot(slot):
        try:
            with open(f'modules/load/slot{slot}.json', 'r') as file:
                return True
        except FileNotFoundError:
            return False
        
    def check_overwrite(slot):
        overwrite = input(f'Слот \033[32m{slot}\033[0m занят. \033[31mВы хотите перезаписать его?\033[0m (\033[32my\033[0m/\033[31mn\033[0m): ')
        return overwrite.lower() == 'y'

    choice = input('\033[32mЗагрузчик v1.1\033[0m\n\n\033[33mВыберите действие:\033[0m\n\033[36m1\033[0m. Проверить сохраненные значения\n\033[36m2\033[0m. Ввести новые значения\n\033[36m3\033[0m. Загрузка\n\033[32mВыбор:\033[0m ')
    if choice == '1':
        slot = input('\nВыберите слот (1, 2, 3): ')
        var1, var2 = load_data(slot)
        if var1 is None or var2 is None:
            print(f'\n\033[31mСлот {slot} пуст\033[0m\n')
        else:
            print(f'Сохранëнные значения: \nToken = {var1} \nID = {var2}')
    elif choice == '2':
        var1 = input('\nВведите токен: ')
        var2 = input('Введите айди администатора: ')
        next_choice = input('\n\033[33mВыберите действие:\033[0m\n\033[36m1\033[0m. Продолжить без сохранения\n\033[36m2\033[0m. Сохранить переменные и продолжить\n\033[32mВыбор:\033[0m ')
        if next_choice == '1':
            print('\nПродолжение без сохранения')
        elif next_choice == '2':
            slot = input('\nВыберите слот для сохранения (1, 2, 3): ')
            if check_slot(slot):
                if check_overwrite(slot):
                    save_data(slot, var1, var2)
                else:
                    print(f'\n\033[31mСлот {slot} не перезаписан\033[0m')
            else:
                save_data(slot, var1, var2)
    elif choice == '3':
        print('\033[32mВыход из загрузчика\033[0m')
        break
    else:
        print('\n\033[31mНекорректный выбор действия\033[0m\n')