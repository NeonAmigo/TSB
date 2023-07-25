import json, os
import telebot as tb
from time import sleep
print("""

████████╗███████╗██████╗ 
╚══██╔══╝██╔════╝██╔══██╗
   ██║   ███████╗██████╔╝
   ██║   ╚════██║██╔══██╗
   ██║   ███████║██████╔╝
   ╚═╝   ╚══════╝╚═════╝ 
 \n\033[33m<\033[37m/\033[33m>\033[36m Author: \033[37miNeonYT \033[31m| \033[32m@iNeonYT\033[0m
 \n\033[33m<\033[37m/\033[33m>\033[36m Author: \033[37mPyCodeMan \033[31m| \033[32m@PyCodeMan\033[0m
""")
while True:
    print("Choose an action number:")
    print("1. Start")
    print("2. About us")
    print("3. Links")
    print("4. Exit")

    choice = input("\033[32mEnter action number:\033[0m ")

    if choice == "1":
        os.system('cls||clear')
        from modules import load
        os.system('cls||clear')
        slot = input('\033[32mВыберите слот \033[0m(\033[36m1, 2, 3\033[0m)\033[32m:\033[0m')
        os.system('cls||clear')
        filename = 'modules/load/slot{}.json'.format(slot)
        with open(filename, 'r') as file:
         data = json.load(file)
        var1 = data['var1']
        var2 = data['var2']
        sleep(1.3)
        bot = tb.TeleBot(var1)
        admin_id = var2
        print('Status: \033[32monline\033[0m')
        def send_to_admin(message):
            bot.send_message(admin_id, message)

        @bot.message_handler(commands=['start'])
        def start_command(message):
            bot.reply_to(message, '💠Привет! Здесь ты можешь поделится своими пожеланиями, предложениями или\nвстреченными багами. \n\n🛠Разработчик просматривает все сообщения.')

        @bot.message_handler(func=lambda message: True)
        def text_message(message):
            if str(message.chat.id) != admin_id:
                send_to_admin(f'💠Новое сообщение от {message.chat.first_name} ({message.chat.id}): {message.text}')
                bot.reply_to(message, '💠Спасибо за сообщение! \n\n ✉️Оно было успешно отправлено администратору.')
            else:
                if message.reply_to_message:
                    user_id = message.text
                    user_id = user_id[:10]
                    bot.send_message(user_id, f'🛠Ответ от администратора: {message.text[11:]}')
                    bot.reply_to(message, '💠Ответ отправлен.')
                else:
                    bot.reply_to(message, '💠Ответ можно отправить только на сообщение с предложкой.')

        if __name__ == '__main__':
            while True:
                try:
                    bot.polling(none_stop=True)
                except Exception as _ex:
                    print(_ex)
                    sleep(15)
    elif choice == "2":
        sleep(0.9)
        print('\n\nWe are a team of developers, creating open source software to help people around the world solve their problems and improve the quality of life. We strive to ensure that our products are available to everyone who needs them, and that our work is available to the public. We believe in the power of community and encourage everyone to join us in creating a better world. Thanks for choosing us!\n\n')
        sleep(2)
        pass
    elif choice == "3":
        sleep(0.9)
        print(""" \n<\033[33m/\033[0m> \033[42mTelegram : @iNeonYT | @PyCodeMan \033[0m\n<\033[33m/\033[0m> \033[43mCoding Telegram : t.me/acodebeta \033[0m\n<\033[33m/\033[0m> \033[41mGithub : https://github.com/ACodeBeta \033[0m\n                    
""")
        sleep(2)
        pass
    elif choice == "4":
        break
    else:
        print("\033[31mWrong choice. Try again.\033[0m")