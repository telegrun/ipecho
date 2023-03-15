import ip
import telegram
from telegram import (
    Update,
    User,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    BotCommand
)

welcome_message = '''Hi, Welcome to IP Echo bot. /n
I am a simple echo bot. I will echo the publis IP of the machine I'm running on to you everytime you send a message to me.
'''


async def handle(update: Update, context: telegram.ext.CallbackContext):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    user_first_name = update.message.from_user.first_name
    user_last_name = update.message.from_user.last_name
    user_language = update.message.from_user.language_code
    my_ip = ip.get_my_ip()
    message = f''' Hi {user_first_name}, 
    The public IP address of my machine is: {my_ip}
    '''
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)


