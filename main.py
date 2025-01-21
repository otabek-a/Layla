from telegram.ext import Updater,MessageHandler,Filters
from telegram import Bot, Update
import os
from telegram import ReplyKeyboardMarkup
def start(update: Update, context):
    
     keyboard = [
    ['MILLIY TAOMLAR 🍽️', 'YAXNA ICHIMLIKLAR 🥤'],
    ['ALKOGOL MAXSULOTLARI 🍷'],
]
    
  
     reply_markup = ReplyKeyboardMarkup(keyboard)
    
     update.message.reply_text(
        'Assalomu alaykum, iltimos bot ishlashi uchun menyuni tanlang:',
        reply_markup=reply_markup
    )


def milliy_taomlar(update: Update, context):
    keyboard = [
    ['PLOV 🍚', 'SHASHLIK 🍢'],
    ['MANTI 🥟', 'SHURBO 🍲'],
]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        'ILtimos buyurtma berish uchun maxsulot ustiga bosing:',
        reply_markup=reply_markup
    )
def ichimliklar(update: Update, context):
    keyboard = [
    ['ISSIQINA CHOY 🍵 & HOT WATER 💧'],
    ['MOXITO 🍹', 'PEPSI 🥤'],
    ['COCA COLA 🥤', 'FANTA 🥤'],
]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        'ILtimos buyurtma berish uchun maxsulot ustiga bosing:',
        reply_markup=reply_markup
    )
def aroq(update: Update, context):
    keyboard = [
    ['VODKA 🍸', 'VINO 🍷'],
    ['VISKIY 🥃', 'KONYAK 🥃'],
    ['PIVA 🍺']
]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        'ILtimos buyurtma berish uchun maxsulot ustiga bosing:',
        reply_markup=reply_markup
    )




   

TOKEN = os.environ['TOKEN']

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
def plov(update: Update, context):
    update.message.reply_text("""
    PLOV 🍚
    Narxi: 35 000 so'm
    Hajmi: 1 ta porsiya
    Tarkibi: Guruch, go'sht (mol go'shti yoki qo'y go'shti), sabzavotlar, ziravorlar, ko'katlar.
    Qo'shimchalar: Salat yoki non bilan.
    """)

def shashlik(update: Update, context):
    update.message.reply_text("""
    SHASHLIK 🍢
    Narxi: 40 000 so'm
    Hajmi: 1 porsiya (5 ta shashlik)
    Tarkibi: Mol go'shti yoki qo'y go'shti, piyoz, ziravorlar, yog'.
    Qo'shimchalar: Pita noni yoki shirinlik bilan.
    """)

def manti(update: Update, context):
    update.message.reply_text("""
    MANTI 🥟
    Narxi: 25 000 so'm
    Hajmi: 1 porsiya (5 ta manti)
    Tarkibi: Go'sht (mol yoki qo'y go'shti), piyoz, xamirturush, ziravorlar.
    Qo'shimchalar: O'zbekcha qaymoq yoki oshqovoq qo'shish mumkin.
    """)

def shurbo(update: Update, context):
    update.message.reply_text("""
    SHURBO 🍲
    Narxi: 30 000 so'm
    Hajmi: 1 porsiya
    Tarkibi: Go'sht, kartoshka, sabzavotlar, ziravorlar, guruch.
    Qo'shimchalar: Qaymoq yoki non bilan xizmat qilinadi.
    """)

def issiqina_choy(update: Update, context):
    update.message.reply_text("""
    ISSIQINA CHOY 🍵
    Narxi: 5 000 so'm
    Hajmi: 1 chashka
    Tarkibi: Choy yaprog'i, issiq suv, shakar.
    Qo'shimchalar: Limon, asal yoki qaymoq.
    """)

def hot_water(update: Update, context):
    update.message.reply_text("""
    HOT WATER 💧
    Narxi: 2 000 so'm
    Hajmi: 1 stakan
    Tarkibi: Issiq suv.
    Qo'shimchalar: Qulupnay, limon, yoki yana biror meva.
    """)

def moxito(update: Update, context):
    update.message.reply_text("""
    MOXITO 🍹
    Narxi: 15 000 so'm
    Hajmi: 1 porsiya
    Tarkibi: Limmoning sharbati, nane, rom, muz.
    Qo'shimchalar: Limon bo'laklari yoki nane barglari bilan bezatish mumkin.
    """)

def pepsi(update: Update, context):
    update.message.reply_text("""
    PEPSI 🥤
    Narxi: 8 000 so'm
    Hajmi: 0.5L
    Tarkibi: Gazli ichimlik, shakar, kofein.
    Qo'shimchalar: Muz bilan.
    """)

def coca_cola(update: Update, context):
    update.message.reply_text("""
    COCA COLA 🥤
    Narxi: 8 000 so'm
    Hajmi: 0.5L
    Tarkibi: Gazli ichimlik, shakar, kofein.
    Qo'shimchalar: Muz bilan.
    """)

def fanta(update: Update, context):
    update.message.reply_text("""
    FANTA 🥤
    Narxi: 7 000 so'm
    Hajmi: 0.5L
    Tarkibi: Apelsin sharbati, gazli ichimlik, shakar.
    Qo'shimchalar: Muz bilan.
    """)

def vodka(update: Update, context):
    update.message.reply_text("""
    VODKA 🍸
    Narxi: 50 000 so'm
    Hajmi: 0.5L
    Tarkibi: Suyuq alkogol, kartoshka kraxmalidan tayyorlanadi.
    Qo'shimchalar: Salatlar yoki achchiq taomlar bilan.
    """)

def vino(update: Update, context):
    update.message.reply_text("""
    VINO 🍷
    Narxi: 70 000 so'm
    Hajmi: 0.75L
    Tarkibi: Uzum sharobidan tayyorlanadi.
    Qo'shimchalar: Pishloq yoki engaklar bilan.
    """)

def viski(update: Update, context):
    update.message.reply_text("""
    VISKIY 🥃
    Narxi: 80 000 so'm
    Hajmi: 0.5L
    Tarkibi: Arpa donidan tayyorlanadi.
    Qo'shimchalar: Muz yoki suv bilan.
    """)

def konyak(update: Update, context):
    update.message.reply_text("""
    KONYAK 🥃
    Narxi: 90 000 so'm
    Hajmi: 0.5L
    Tarkibi: Uzum sharobidan tayyorlanadi.
    Qo'shimchalar: Xushbo'y taomlar yoki pishloq bilan.
    """)

def piva(update: Update, context):
    update.message.reply_text("""
    PIVA 🍺
    Narxi: 15 000 so'm
    Hajmi: 0.5L
    Tarkibi: Arpa, suv, xamirturush.
    Qo'shimchalar: Achchiq taomlar yoki sho'rvalar bilan.
    """)





# add handlers here
dispatcher.add_handler(MessageHandler(Filters.command('start'), start))
dispatcher.add_handler(MessageHandler(Filters.text('YAXNA ICHIMLIKLAR 🥤'), ichimliklar))
dispatcher.add_handler(MessageHandler(Filters.text('MILLIY TAOMLAR 🍽️'), milliy_taomlar))
dispatcher.add_handler(MessageHandler(Filters.text('ALKOGOL MAXSULOTLARI 🍷'), aroq))






dispatcher.add_handler(MessageHandler(Filters.text('PLOV 🍚'), plov))
dispatcher.add_handler(MessageHandler(Filters.text('SHASHLIK 🍢'), shashlik))
dispatcher.add_handler(MessageHandler(Filters.text('MANTI 🥟'), manti))
dispatcher.add_handler(MessageHandler(Filters.text('SHURBO 🍲'), shurbo))
dispatcher.add_handler(MessageHandler(Filters.text('ISSIQINA CHOY 🍵'), issiqina_choy))
dispatcher.add_handler(MessageHandler(Filters.text('HOT WATER 💧'), hot_water))
dispatcher.add_handler(MessageHandler(Filters.text('MOXITO 🍹'), moxito))
dispatcher.add_handler(MessageHandler(Filters.text('PEPSI 🥤'), pepsi))
dispatcher.add_handler(MessageHandler(Filters.text('COCA COLA 🥤'), coca_cola))
dispatcher.add_handler(MessageHandler(Filters.text('FANTA 🥤'), fanta))
dispatcher.add_handler(MessageHandler(Filters.text('VINO 🍷'), vino))
dispatcher.add_handler(MessageHandler(Filters.text('VODKA 🍸'), vodka))
dispatcher.add_handler(MessageHandler(Filters.text('VISKIY 🥃'), viski))
dispatcher.add_handler(MessageHandler(Filters.text('KONYAK 🥃'), konyak))
dispatcher.add_handler(MessageHandler(Filters.text('PIVA 🍺'), piva))



updater.start_polling()
updater.idle()