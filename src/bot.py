import ip
import config
import logging
from telegram import (
    Update,
    User,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    BotCommand
)
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
from telegram.constants import ParseMode, ChatAction

welcome_message = '''Hi, Welcome to IP Echo bot. /n
I am a simple echo bot. I will echo the publis IP of the machine I'm running on to you everytime you send a message to me.
'''
logger = logging.getLogger(__name__)


async def handle(update: Update, context: CallbackContext):
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
    print(f'sending message ... {message}')
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)
    print(f'Message sent to "{user_name}" with chat_id: {chat_id}')


async def error_handle(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:",
                 exc_info=context.error)


def run_bot() -> None:
    app = (
        ApplicationBuilder()
        .token(config.bot_token)
        .concurrent_updates(True)
        .build()
    )
    app.add_handler(CommandHandler('start', handle))
    app.add_handler(MessageHandler(filters.TEXT, handle))
    app.add_error_handler(error_handle)
    print('The Bot is running now...')
    app.run_polling()


if __name__ == "__main__":
    print('Welcome!\n\n')
    run_bot()
