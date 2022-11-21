from config import token
import telebot


bot = telebot.TeleBot(token)

flag = False


@bot.message_handler(commands=["start"])  # обрабатываем входщее сообщение по его типу (комманда)
def start(message):
   bot.send_message(message.chat.id, "Привет, я скажу тебе сколько дней в интересующим тебя месяце\n"
                                     "Используй комманду /rec, что бы узнать колличесвто дней")


@bot.message_handler(commands=["rec"])  # обрабатываем входщее сообщение по его типу (комманда)
def get_year(message):
   msg = bot.send_message(message.chat.id, 'Введите год')   # говорим пользователю что мы от него хотим
   bot.register_next_step_handler(msg, get_month)   # включаем пошаговый обработчик, во втором аргументе указываем функцию, куда нас перекинет


def get_month(message):   # здесь у нас текст, который мы получили от пользователя в предыдущей функции
   print(message.text)
   if message.text.isdigit() and int(message.text) != 0:

      if int(message.text) % 4 == 0 and int(message.text) % 100 != 0 or int(message.text) % 100 == 0 and int(message.text) % 400 == 0:  # високосный
         global flag
         flag = True

      msg = bot.send_message(message.chat.id, 'Введите месяц')
      bot.register_next_step_handler(msg, result)  # 2-ым аргументом указывем функцию, куда нас кинет
   else:
      bot.reply_to(message, "На ввод требуется целое число отличное от нуля")  # функция replay_to отвечает на сообщение
      bot.register_next_step_handler(message, get_month)


def result(rezult_month):  # здесь у нас сообщение полученное от пользователя из предыдущий функции)
   print(rezult_month.text)

   if not rezult_month.text.isdigit() or int(rezult_month.text) > 12 or int(rezult_month.text) == 0:
      bot.reply_to(rezult_month, "На ввод нужно целое число, означающее номер месяца")
      bot.register_next_step_handler(rezult_month, result)

   else:
      if flag == True:  # високосный
         f_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
         bot.send_message(rezult_month.chat.id, f"В этом месяце дней: {f_months[int(rezult_month.text)]}")

      if flag == False:  # невисокосный
         f_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
         bot.send_message(rezult_month.chat.id, f"В этом месяце дней: {f_months[int(rezult_month.text)]}")



if __name__ == "__main__":  # если программа выполняется в этом файле:
   print("Hello1")
   bot.infinity_polling()  #  этой функцией мы зацикливаем опрос пользователя
   print("By")




# def get_days(rezult_year, rezult_month):
#
#    if rezult_year % 4 == 0 and rezult_year % 100 != 0 or rezult_year % 100 == 0 and rezult_year % 400 == 0:  # високосный
#       f_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#       return f_months[rezult_month]
#    if rezult_year % 4 != 0 or rezult_year % 100 == 0:  # невисокосный
#       f_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#       return f_months.get(rezult_month)
#
#
# while True:
#    year = input("Введите интересующий вас год: ")
#    if year.isdigit():
#       year = (int(year))
#       break
#    else: print("На ввод принимаются только целые числа")
#
# while True:
#    month = input("Введите интересующий вас месяц: ")
#
#    if month.isdigit():     # если ввод был числом
#       month = int(month)
#       if month > 12:
#          continue
#       break
#
#    elif month.lower().isalpha():    # если ввод был строкой
#       months = {"январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
#                       "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12}
#       month = months.get(month)
#       if month is not None:
#          break
#       else:
#          print("Получен некорректный параметр, попробуйте снова.")
#          continue
#
#
# print(f"В этом месяце дней: {get_days(year, month)}")
