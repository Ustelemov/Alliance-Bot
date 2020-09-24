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

bot = telebot.TeleBot('1222713781:AAEPr9PeHeIrtqI1txgCxGWDyw7E1kac17I') #Здесь наш токен от бота

watchers_chat_id = '-1001130791087' #ID канала, куда попадают заявки

chats_dict = {} # Словарь чатиков

time = datetime.datetime.now() #текущее время

#Файл с информацией о ближайших вебинарах (кнопка "Ближайшие вебинары")
seminars_url_download = 'https://drive.google.com/uc?id=1CugYOKgRjikNBbfn2JSGj8JnGMu5_PRz'
seminars_file_name = 'Семинары.docx'
seminars_file_path = './'+seminars_file_name

#Файл с информацией по информационным ресурсам (кнопка "Информационные ресурсы")
socials_url_download = 'https://drive.google.com/uc?id=133Vghn24eI05qa3_yZVTFCF7sYSpZxF3'
socials_file_name = 'Информационные ресурсы.docx'
socials_file_path = './'+socials_file_name

#Файл со скриптом внедрения (кнопка "Скрипт внедрения")
script_url_download = 'https://drive.google.com/uc?id=1Nq3bVfuVYy-cBdwqDbGZdCVQ6jABz6ku'
script_url_send = 'https://drive.google.com/file/d/1Nq3bVfuVYy-cBdwqDbGZdCVQ6jABz6ku/view'
script_file_name = 'DPA.080.Программа внедрения DPA.pdf'
script_file_path = './'+script_file_name

#Файл с опросным листом (кнопка "Опросный лист")
survey_url_download = 'https://drive.google.com/uc?id=14yAd8gr6yYWN2rawoQ7yHUaRYonCuSwX'
survey_url_send = 'https://drive.google.com/file/d/14yAd8gr6yYWN2rawoQ7yHUaRYonCuSwX/view?usp=sharing'
survey_file_name = 'Опросный лист.xlsx'
survey_file_path = './'+survey_file_name

### Клавиатуры
#Меню - клавиатура
menu_keybord = telebot.types.ReplyKeyboardMarkup(True,True)
menu_keybord.row('Подать заявку на бесплатный тест')
menu_keybord.row('У меня есть вопрос, свяжитесь со мной')
menu_keybord.row('Опросный лист', 'Скрипт внедрения')
menu_keybord.row('Ближайшие вебинары','Информационные ресурсы')

#В меню - клавиатура
go_menu_keybord = telebot.types.ReplyKeyboardMarkup(True,True)
go_menu_keybord.row('В меню')

#Подтверждение заявки - клавиатура#
send_order_keybord = telebot.types.ReplyKeyboardMarkup(True,True)
send_order_keybord.row('Все верно. Отправить')
send_order_keybord.row('Заполнить заного')
send_order_keybord.row('В меню')

#Свяжитесь со мной - клавиатура
communication_keybord = telebot.types.ReplyKeyboardMarkup(True,True)
communication_keybord.row('Telegram','WhatsUp','Viber')
communication_keybord.row('Электронная почта', 'Телефон')
communication_keybord.row('В меню')


@bot.message_handler(commands=['start','help','menu'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)

@bot.message_handler(content_types=['text'])
def handle_message(message):
  try:
    if message.text=='Подать заявку на бесплатный тест':
      msg = bot.send_message(message.chat.id, 'Ваше ФИО',reply_markup=go_menu_keybord)
      bot.register_next_step_handler(msg, proccess_name_step)
    elif message.text == 'У меня есть вопрос, свяжитесь со мной':
      msg = bot.send_message(message.chat.id, 'Выберите как с вами связаться',reply_markup=communication_keybord)
      bot.register_next_step_handler(msg, how_to_communicate_asker)
    elif message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    elif message.text == 'Скрипт внедрения':
      gdown.download(script_url_download, script_file_path, quiet=False) 
      doc = open(script_file_path, 'rb')
      bot.send_document(message.chat.id, doc)
      msg = bot.send_message(message.chat.id, script_url_send,reply_markup=menu_keybord)
    elif message.text == 'Опросный лист':
      gdown.download(survey_url_download, survey_file_path, quiet=False) 
      doc = open(survey_file_path, 'rb')
      bot.send_document(message.chat.id, doc)
      msg = bot.send_message(message.chat.id, survey_url_send,reply_markup=menu_keybord)
    elif message.text == 'Ближайшие вебинары':
      gdown.download(seminars_url_download, seminars_file_path, quiet=False) 
      doc = docx.Document(seminars_file_path) 
      seminars_data = ""
      fullText = []
      for para in doc.paragraphs:
        fullText.append(para.text)
        seminars_data = '\n'.join(fullText)
      msg = bot.send_message(message.chat.id, seminars_data,reply_markup=menu_keybord)
    elif message.text == 'Информационные ресурсы':
      gdown.download(socials_url_download, socials_file_path, quiet=False) 
      doc = docx.Document(socials_file_path)
      socials_data = ""
      fullText = []
      for para in doc.paragraphs:
        fullText.append(para.text)
        socials_data = '\n'.join(fullText)
 
      msg = bot.send_message(message.chat.id, socials_data,reply_markup=menu_keybord)

  except Exception as e:
    bot.reply_to(message, 'exception')

#Результат по кнопке "У меня есть вопрос, свяжитесь со мной"
def how_to_communicate_asker(message):
    chat_id = message.chat.id
    if message.text == 'Электронная почта':
      msg = bot.send_message(chat_id, 'Введите свою электронную почту',reply_markup=go_menu_keybord)
    elif message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:
      msg = bot.send_message(chat_id, 'Введите свой номер телефона',reply_markup=go_menu_keybord)
    bot.register_next_step_handler(msg,send_communication_order,message.text)

#Отправка заявки на обратную связь в чат заявок
def send_communication_order(message,commtype):
    chat_id = message.chat.id
    if message.text =='В меню':
      bot.send_message(chat_id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:
      username =  message.from_user.username

      t = Template('Заявка на обратную связь \nВремя отправки: $time \nUsername: @$username \nВариант связи: $commtype \nДанные: $contact')

      bot.send_message(watchers_chat_id,t.substitute(time = time,username=username,commtype=commtype,contact=message.text))
      bot.send_message(chat_id,'Заявка принята, мы свяжемся с вами в ближайшее время',reply_markup=menu_keybord)

#Проверка пользователем заявки на тест: отправка в чат заявок либо повторный ввод
def send_or_rewrite_order(message):
    if message.text == 'Все верно. Отправить':
      chat_id = message.chat.id
      user = chats_dict[chat_id]
      username =  message.from_user.username
      msg = bot.send_message(watchers_chat_id, getOrderData('Заявка на тестирование DPA',user,username,True),parse_mode="MARKDOWN")
      msg = bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена, мы скоро свяжемся с вами',reply_markup=menu_keybord)   
    elif message.text == 'Заполнить заного':
      msg = bot.send_message(message.chat.id, 'Ваше ФИО',reply_markup=go_menu_keybord)
      bot.register_next_step_handler(msg, proccess_name_step)
    elif message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
      

#1ый-Шаг заявки на тест (ФИО->Город)
def proccess_name_step(message):
  try:
    chat_id = message.chat.id
    chats_dict[chat_id] = User(message.text)
    
    if message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:
      msg = bot.send_message(chat_id, 'Ваш город',reply_markup=go_menu_keybord)
      bot.register_next_step_handler(msg, proccess_city_step)

  except Exception as e:
    bot.reply_to(message, 'exception')

#2ый-Шаг заявки на тест (Город->Предприятие)
def proccess_city_step(message):
  try:
    chat_id = message.chat.id
    chats_dict[chat_id].city = message.text
    
    if message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:
      msg = bot.send_message(chat_id, 'Ваше предприятие',reply_markup=go_menu_keybord)
      bot.register_next_step_handler(msg, proccess_company_step)
    
  except Exception as e:
    bot.reply_to(message, 'exception')

#3ый-Шаг заявки на тест (Предприятие->Должность)
def proccess_company_step(message):
  try:
    chat_id = message.chat.id
    chats_dict[chat_id].company = message.text
    
    if message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:
      msg = bot.send_message(chat_id, 'Ваша должность',reply_markup=go_menu_keybord)
      bot.register_next_step_handler(msg, proccess_position_step)
      
  except Exception as e:
    bot.reply_to(message, 'exception')

#4ый-Шаг заявки на тест (Должность->Телефон)
def proccess_position_step(message):
  try:
    chat_id = message.chat.id
    chats_dict[chat_id].position = message.text
    
    if message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:
      msg = bot.send_message(chat_id, 'Ваш номер телефона',reply_markup=go_menu_keybord)
      bot.register_next_step_handler(msg, proccess_phone_step)
  
  except Exception as e:
    bot.reply_to(message, 'exception')

#5ый-Шаг заявки на тест (Телефон->Электронная почта)
def proccess_phone_step(message):
  try:
    chat_id = message.chat.id
    chats_dict[chat_id].phone = message.text
    
    if message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:
      msg = bot.send_message(chat_id, 'Ваша электронная почта',reply_markup=go_menu_keybord)
      bot.register_next_step_handler(msg, proccess_email_step)
  
  except Exception as e:
    bot.reply_to(message, 'exception')

#6ый-Шаг заявки на тест (Элктронная почта->Проверка данных)
def proccess_email_step(message):
  try:
    chat_id = message.chat.id
    chats_dict[chat_id].email = message.text
    user = chats_dict[chat_id]
    username =  message.from_user.username
    
    if message.text =='В меню':
      bot.send_message(message.chat.id, 'Выберите интересующий пункт меню',reply_markup=menu_keybord)
    else:  
      msg = bot.send_message(chat_id,'Проверьте данные в сформированной заявке')
      msg = bot.send_message(chat_id, getOrderData('Заявка на тестирование DPA',user,username),parse_mode="MARKDOWN",reply_markup=send_order_keybord)
      bot.register_next_step_handler(msg, send_or_rewrite_order)

  except Exception as e:
    bot.reply_to(message, 'exception')   

#Формирование заявки
def getOrderData(title,user,username,with_time=False):
    if with_time:
      t = Template('$title \nВремя отправки: $time \nUsername: @$username \nФИО: $name \nГород: $city \nПредприятие: $company \nДолжность: $position \nТелефон: $phone \nЭлектронная почта: $email')
    else:
      t = Template('$title \nUsername: @$username \nФИО: $name \nГород: $city \nПредприятие: $company \nДолжность: $position \nТелефон: $phone \nЭлектронная почта: $email')

    return t.substitute(title=title,time = time,username=username,name=user.name,city=user.city,company=user.company,position=user.position,phone=user.phone, email=user.email)

bot.polling()
