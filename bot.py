from telegram.ext import *
import telegram
import keys

import imdbAPI

def start_command(update, context):
    name  = update.message.from_user.first_name
    update.message.reply_text("Hello {} and Welcome To My IMDB Robot".format(name))
    
def help(update, context):
    update.message.reply_text(
    """
    /start
    /Search 
    /show the list
    /Select
    /Show the information!
    """   
    )


user_input = None
number_moive = None
list_of_movies = None
def search(update, context):
    update.message.reply_text("What Movie do you want to see?")
    return 1

# def reply (update,context):
#     global user_input
#     user_input = update.message.text
#     list_of_movies = imdbAPI.search_imdb_movies(user_input)
#     for index, movie_title in enumerate(list_of_movies, start=1):
#         update.message.reply_text(f"{index}. {movie_title}")
def get_name_moive(update, context):
    global list_of_movies
    user_input = update.message.text
    list_of_movies = imdbAPI.search_imdb_movies(user_input)
    reply_text = '\n'.join([f"{index}. {movie_title}" for index, movie_title in enumerate(list_of_movies, start=1)])
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text) 
    update.message.reply_text("Choose Number") 
    return 2

def get_numer_of_movie(update,context):
    global number_moive
    number_moive = update.message.text
    number_moive = int(number_moive)
    update.message.reply_text(list_of_movies[number_moive-1])
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("Canceled")
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('search', search)],
    states={
        1: [MessageHandler(Filters.text, get_name_moive)],
        2: [MessageHandler(Filters.text, get_numer_of_movie)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

def search_item(update, context):
    #update.message.reply_text(imdbAPI.Search_Movie(user_input))
    pass

if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('search', search))
    dp.add_handler(CommandHandler('search_item', search_item))
    dp.add_handler(conv_handler)
    # dp.add_handler(MessageHandler(Filters.text, reply))
    
    updater.start_polling(1.0)
    updater.idle()
