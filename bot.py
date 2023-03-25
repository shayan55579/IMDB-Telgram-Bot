from telegram.ext import *


import keys




def start_command(update, context):
    update.message.reply_text("Hello and Welcome")

def help(update, context):
    update.message.reply_text(
    """
    /start
    /Search a phrase
    /show the list of movies, based on your search!
    /Select the desired movie
    /Show the selected movies information!
    """   
    )

if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help))
    
    
    updater.start_polling(1.0)
    updater.idle()