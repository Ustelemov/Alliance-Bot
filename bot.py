import telebot
from string import Template
import datetime
import gdown
import docx

class User:
  def __init__(self,name):
   self.name = name
  
   keys = ['position','city','company','phone','email']

   for key in keys:
     self.key = None

bot = telebot.TeleBot('1449765866:AAFgVKHseibuUDEPpw9EqY6_pNR5oDCeFYg') #Здесь наш токен от бота

### Клавиатуры
#Меню - клавиатура
menu_keybord = telebot.types.ReplyKeyboardMarkup(True,True)
menu_keybord.row('Пункт 1 :)', 'Пункт 2 <3')
menu_keybord.row('Пункт 3 (люблю тебя)', 'Пункт 4 ^^')
menu_keybord.row('Пункт 5 (родная моя)', 'Пункт 6 (мур-мур)')
menu_keybord.row('Пункт 7 (киса моя :*)', 'Пункт 8 (c -> NY)')
menu_keybord.row('Пункт 9 (ты лучшая)', 'Пункт 10 (Ух, не устала? :>)')
menu_keybord.row('Пункт 11 (финалочка)')


@bot.message_handler(commands=['start','help','menu'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбирай пунктик в менюшке :)',reply_markup=menu_keybord)

@bot.message_handler(content_types=['text'])
def handle_message(message):
  try:
    if message.text=='Пункт 1 :)':
      msg = bot.send_message(message.chat.id, 'ун отч? яанчонимзар, ежад итди адукин ен одан, от-огесв ьтунревереп аволс: атэ авкуб - яавреп авкуб аволс, огоннасипан ан екчилбат ан йондохв иревд хиовт йелетидор.',reply_markup=menu_keybord)
    elif message.text=='Пункт 2 <3':
      msg = bot.send_message(message.chat.id, 'Первая буква полного имени твоего любимого дяди, у которого не понять ещё: сколько времени, и день или ночь или че вообще :)))',reply_markup=menu_keybord)
    elif message.text=='Пункт 3 (люблю тебя)':
      msg = bot.send_message(message.chat.id, 'Спотифайчиком пользуешься? Тебе нужна первая буква имени (не псевдонима, а прямо имени C:) этого исполнителя: https://clck.ru/SghpZ',reply_markup=menu_keybord)
    elif message.text=='Пункт 4 ^^':
      msg = bot.send_message(message.chat.id, 'Послушала трек из предыдущего пункта (3)? В тексте упоминается одна песня, тебе нужна первая гласная буква русского прочтения имени её исполнителя.',reply_markup=menu_keybord)
    elif message.text=='Пункт 5 (родная моя)':
      msg = bot.send_message(message.chat.id, 'Что там тебе Артем подарил? Внутри было что-то интересное?',reply_markup=menu_keybord)
    elif message.text=='Пункт 6 (мур-мур)':
      msg = bot.send_message(message.chat.id, 'Ой, ну тут тебе халявка считай: напиши номер своей квартиры боту, он скажет тебе букву (не ту напишешь, будет молчать :D).',reply_markup=menu_keybord)
    elif message.text=='293':
      msg = bot.send_message(message.chat.id, 'Спасибочки. Твоя буковка: Й. С Наступающим, кста <3',reply_markup=menu_keybord)
    elif message.text=='Пункт 7 (киса моя :*)':
      msg = bot.send_message(message.chat.id, 'Ну, мы неплохо продвигаемся, я тебе скажу. Нужно бы передохнуть и выпить тебе Доброго Утра (доброе утро все-таки жи), там и буковка ещё одна для тебя в пачечке.',reply_markup=menu_keybord)
    elif message.text=='Пункт 8 (c -> NY)':
      msg = bot.send_message(message.chat.id, 'Под мягонькой пушистой штучкой, на которую ты любишь вставать на коленки :) для тебя ещё буковка.',reply_markup=menu_keybord)
    elif message.text=='Пункт 9 (ты лучшая)':
      msg = bot.send_message(message.chat.id, 'Надо посчитать по формулке, тебе нужна буква алфавита с номером: (сумма номеров алфавита букв твоего короткого четырех буквенного имени) минус (номер дня моего рождения, гы) минус (количество бутылочек сока стоящего в ближнем к тебе ряду: второй от стеночки ряд).',reply_markup=menu_keybord)
    elif message.text=='Пункт 10 (Ух, не устала? :>)':
      msg = bot.send_message(message.chat.id, 'В кармане твоей курточки карта, возьми в её названии вторую букву с конца ^^',reply_markup=menu_keybord)
    elif message.text=='Пункт 11 (финалочка)':
      msg = bot.send_message(message.chat.id, 'Cоставляй буквы пунктов в следующем порядке номеров пунктов: 1-10-3-7-9-4-8-2-5-6. А теперь топай лапками туда и забирай подарочек, с Наступающим, люблю тебя <3',reply_markup=menu_keybord)
    
  except Exception as e:
    bot.reply_to(message, 'exception')

bot.polling()
