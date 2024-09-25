from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Получение токена на бота
TOKEN = '7264979692:AAGo6En-dG-Wkjz4LW9B6tfrpH38jk5WJdE'


# Команда /start с кнопкой
async def start(update: Update, context: CallbackContext):
    keyboard = [
        ['📚Расписание группы📚'],
        ['👩🏻‍🏫Расписание преподавателя👩🏻‍🏫'],
        ['🏠Расписание аудитории🏠'],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text('Здравствуйте! '
                                    'Я бот "Расписание занятий ВолгГТУ" '
                                    'Я помогу вам, кто бы вы не были, студент, преподаватель или даже аудитория! '
                                    'Пожалуйста, выберите, для кого вы хотите получить расписание', reply_markup=reply_markup)