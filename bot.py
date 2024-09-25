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

# Для кого пользователь выбрал расписание
async def handle_message(update: Update, context:CallbackContext):
    user_schedule = update.message.text

    if user_schedule == '📚Расписание группы📚':
        await update.message.reply_text("Напишите группу, расписание которой вы хотите получить"
                                        " (в формате: ПрИн-368)")
    elif user_schedule == '👩🏻‍🏫Расписание преподавателя👩🏻‍🏫':
        await update.message.reply_text("Напишите ФИО преподавателя, расписание которого вы хотите получить"
                                        " (в формате: Иванов И.И)")
    elif user_schedule == '🏠Расписание аудитории🏠':
        await update.message.reply_text("Напишите номер аудитории, расписание которой вы хотите получить"
                                        " (в формате: В-902а)")

# Создаем экземпляр Application
application = Application.builder().token(TOKEN).build()

# Регистрация команд
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)

application.add_handler(start_handler)
application.add_handler(message_handler)

# Запуск бота
if __name__ == '__main__':
    application.run_polling()