# ********************88********************************************


import telebot
from config import token  # из файла config.py забираем нашу переменную с токеном
from telebot import types  # для работы с кнопками
import random

# Создаем экземпляр бота
bot = telebot.TeleBot(token)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши "/help, если нужна помощь!')


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "/start - приветствие, /info - информация")


@bot.message_handler(commands=['info'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Этот объект представляет клавиатуру с опциями ответа
    item1 = types.KeyboardButton("/Скрипты")
    item2 = types.KeyboardButton("/Чек-листы")
    item3 = types.KeyboardButton("/Работа_с_возражениями")
    item4 = types.KeyboardButton("/Вопросы_по_объекту")
    item5 = types.KeyboardButton("/Районы_города")

    markup.add(item1, item2)  # Дальше к клавиатуре добавим нашу кнопку
    markup.add(item3, item4)
    markup.add(item5)

    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(commands=['Скрипты'])
def inlinebutton_message(message):
    start_markup = telebot.types.InlineKeyboardMarkup()

    # первый ряд (две кнопки)
    btn1 = types.InlineKeyboardButton('Холодный звонок!', callback_data='1')
    btn2 = types.InlineKeyboardButton('Первая встреча!', callback_data='2')
    start_markup.row(btn1, btn2)

    # второй ряд (одна кнопка)
    btn3 = types.InlineKeyboardButton('Презентация услуги!', callback_data='3')

    start_markup.row(btn3)

    bot.send_message(message.chat.id, 'Скрипты', reply_markup=start_markup)


# **********************************
@bot.message_handler(commands=['Работа_с_возражениями'])
def inlinebutton_message(message):
    start_markup = telebot.types.InlineKeyboardMarkup()

    # первый ряд (две кнопки)
    btn11 = types.InlineKeyboardButton('1) Я не хочу платить комиссию', callback_data='11')
    btn12 = types.InlineKeyboardButton('2) Я и сам могу продать', callback_data='12')
    start_markup.row(btn11, btn12)

    btn13 = types.InlineKeyboardButton('3) Зачем мне услуги агентства?', callback_data='13')
    btn14 = types.InlineKeyboardButton('4) Я лучше обращусь сразу в несколько агентств', callback_data='14')
    start_markup.row(btn13, btn14)

    bot.send_message(message.chat.id, 'Работа с возражениями', reply_markup=start_markup)


@bot.message_handler(commands=['Вопросы_по_объекту'])
def inlinebutton_message(message):
    start_markup = telebot.types.InlineKeyboardMarkup()
    btn31 = types.InlineKeyboardButton('Вопросы по квартире', callback_data='31')
    start_markup.row(btn31)

    bot.send_message(message.chat.id, 'Вопросы_по_объекту', reply_markup=start_markup)


@bot.message_handler(commands=['Чек-листы'])
def inlinebutton_message(message):
    start_markup = telebot.types.InlineKeyboardMarkup()

    btn41 = types.InlineKeyboardButton('1. Вступление в контакт', callback_data='41')
    btn42 = types.InlineKeyboardButton('2. Первичный осмотр квартиры', callback_data='42')

    start_markup.row(btn41, btn42)

    bot.send_message(message.chat.id, 'Чек-листы', reply_markup=start_markup)


@bot.message_handler(commands=['Районы_города'])
def inlinebutton_message(message):
    start_markup = telebot.types.InlineKeyboardMarkup()

    btn51 = types.InlineKeyboardButton('Районы города', callback_data='51')

    start_markup.row(btn51)

    bot.send_message(message.chat.id, 'Районы города', reply_markup=start_markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == ('11'):
        bot.send_message(callback.message.chat.id, '''1) - Собственник: Я не хочу платить комиссию'
Вы: «Согласен(на) с Вами, это абсолютно нормальное желание сэкономить там, где это возможно! И многие продавцы поначалу пробуют продать самостоятельно, но как только узнают, с чем сопряжена продажа недвижимости, они все же обращаются к услугам риэлторов. Наверное, поэтому, свыше 90% квартир на рынке продаются агентами. Давайте я расскажу, что я сделаю, чтобы продать Вашу квартиру по максимальной цене и в нужные Вам сроки, чтобы Вы могли...(указать мотивацию клиента)».''')
    elif callback.data == '12':
        bot.send_message(callback.message.chat.id, '''2) «Я и сам могу продать. Что может сделать агент?»
1. «Скажите, кем вы работаете?... Замечательно, я вот, например сам могу...»
2. «Вы знаете, одно дело – самостоятельно продавать автомобиль. За годы вождения любой автомобилист начинает замечательно разбираться в своем автомобиле, знает все его плюсы и минусы, к тому же, продавая машину куда проще не ставить ее в салон, а продолжать вождение. Другое дело – квартира».''')
    elif callback.data == ('13'):
        bot.send_message(callback.message.chat.id, '''3) «Зачем мне услуги агентства?»
    1. «А разве можно продать квартиру без агентства?»
    2. «Чтобы продать Вашу квартиру по максимально выгодной цене в нужные для Вас сроки»
    ''')
    elif callback.data == '14':
        bot.send_message(callback.message.chat.id, '''4) «Я лучше обращусь сразу в несколько агентств»
    1. «Я понимаю Ваше желание продать как можно быстрее. Возможно, Вы знаете о том, что ЛЮБАЯ недвижимость, как только появляется в продаже у одного АН, сразу подается во все существующие на рынке. Между агентствами существует общая БД. Теперь представьте, Вы выставляете Вашу квартиру в несколько АН, каждое АН начинает с Вами работать: звонить, тревожить... Наверняка Вам не хотелось бы этого, потому что это то же самое, что просто подать объявление и самостоятельно отвечать на звонки потенциальных Покупателей. Вряд ли Вы, как занятой человек, можете себе позволить бросить все свои дела и заниматься только продажей. Заключив Договор с одним АН, Вы получаете ОДНОГО сотрудника, Вашего персонального риэлтора, с которым ведете все переговоры. По крайней мере, Вы точно знаете, с кого спросить, если что».''')



    elif callback.data == ('1'):
        bot.send_message(callback.message.chat.id, '''Скрипт «Холодный звонок собственнику»
1. Вступление в контакт
Здравствуйте! Меня зовут ________________, компания «_____________________». Звоню по объявлению о продаже квартиры. Продаётся? ... Отлично!
Оно заинтересовало меня. Вы собственник? ... Ок!
Хочу уточнить несколько моментов, меня заинтересовала ваша квартира. Удобно сейчас? ...
Меня зовут __________. Как вас зовут? ...
2. Диагностика квартиры
В квартире 2 комнаты, 65 м2, правильно? ... Замечательно! Куда выходят окна квартиры? ...
Сколько лет владеете квартирой? ...
3. Диагностика собственника
В случае продажи этой квартиры, куда-то планируете переезжать дальше? ...
Как скоро Вам нужно продать (переехать)? ...
В связи с чем Вы решили продать (переехать)? ... Прекрасно!
4. Формирование потребности в услуге
Почему вы решили продавать самостоятельно вместо того, чтобы подписать договор с агентом? ... Понимаю!
Вы знакомы с технологиями, которые мы используем для...?
– продажи квартир (стратегии)
– ... или ...
– поиска покупателей (маркетинг)
5. Назначение встречи
Вариант 1.
Когда я могу познакомить вас с этими технологиями, сегодня в 15-00 или в 17-00 будет удобнее?''')

    elif callback.data == ('2'):
        bot.send_message(callback.message.chat.id, '''Задача встречи на объекте: 
•	• Выявление мотивации собственника
Результат: у собственника есть мотивация для продажи объекта; 
•	• Вход в доверие к собственнику
Результат: собственник доверяет риэлтору и готов к его предложениям; 
•	• Продажа «статуса эксперта»
Результат: собственник считает риэлтора профессионалом; 
''')

    elif callback.data == ('3'):
        bot.send_message(callback.message.chat.id, '''
Презентация Эксклюзивного Договора Собственнику
«Подписав договор с Вами, мы обязуем себя выполнить комплекс действий по поиску покупателя, который сможет предложить максимальную цену за Вашу квартиру, а также сопроводить сделку купли-продажи, обеспечив безопасность взаиморасчетов. Договор заключается на срок (3 месяца для объектов дешевле 6 млн рублей, 6 месяцев для объектов стоимостью свыше 6 млн рублей). В договоре прописана стоимость Вашей квартиры, равная ________________, и стоимость услуг агентства, которая составит ____________________. Стоимость рекламы и продвижения квартиры оплачивает агентство, для Вас это не будет стоить ничего в том случае, если с Вашей стороны будут Выполнены все условия по договору. Вас договор ограничивает только в одном – не заключать аналогичных договоров с другими агентствами, и, в случае нахождения покупателя в течение договора с нами, позволить нам выполнить свои обязательства по Договору и оплатить стоимость наших услуг. Оплату за наши услуги мы получаем тогда же, когда Вы получаете деньги за свою квартиру. Никаких предоплата с Вас не требуется...
Я могу заполнять Договор? или Я могу подготовить Договор?»''')

    elif callback.data == ('31'):
        bot.send_message(callback.message.chat.id, '''1. Сколько лет дому? Из чего он построен и чем отделан?
Если в объявлении не было этой информации, непременно поинтересуйтесь и присмотритесь сами. Например, дом может оказаться не кирпичным, как любят указывать продавцы, а просто с кирпичной облицовкой. Кстати, если возраст солидный, не мешало бы выяснить, не получал ли собственник уведомление о сносе. Этот вопрос очень важен, если покупаете жильё на вторичном рынке. Процедура изъятия недвижимости и снос могут доставить много хлопот. На всякий случай информацию можно проверить в акимате.
2. Проводился ли ремонт дома? Когда и какой?
В каком состоянии сети, подъезд, фасад? Это необходимо знать для принятия решения. Если окажется, что дом недавно обновляли, уточните, за чей счёт. Если работы проводили по программе модернизации ЖКХ, то учтите: с квартирой вы покупаете и долг за этот ремонт. Платежи сравнительно небольшие, но неприятно, если они станут сюрпризом.
Разумеется, будет полезно узнать о наличии и состоянии бытовой техники и мебели, выяснить, какая сантехника установлена — есть ли в квартире ванная или только душевая кабина? Обратите внимание на озеленение двора и то, что из себя представляет детская площадка.''')





    elif callback.data == ('41'):
        bot.send_message(callback.message.chat.id, '''1. Вступление в контакт
➢ Первое впечатление
➢ «Обезьяна» собственника успокаивается ➢ Внешний вид – Ваш фасад
Пунктуальность
Улыбка
Приветствие
Благодарность за встречу Зачем пришли?
Спокойно, без суеты и спешки ...''')

    elif callback.data == ('42'):
        bot.send_message(callback.message.chat.id, '''2. Первичный осмотр квартиры
Избегать оценочных суждений
Очень важный этап для установления контакта с собственником Никаких чек-листов, только вопросы-ответы
Больше открытых вопросов
Говоритьтолько о квартире (стены, потолок, пол, снаружи, истории) Не говорить о задачах, проблемах, деньгах, документах и тд Small-talk об интерьере (личном) собственника''')



    elif callback.data == ('51'):
        map_city = open('map_1.png', 'rb')
        bot.send_photo(callback.message.chat.id, map_city)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
