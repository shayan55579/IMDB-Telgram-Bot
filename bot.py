from telegram.ext import * # for Telegram methods

import keys

import imdbAPI


def start_command(update, context):
    name = update.message.from_user.first_name
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


# Global variable
user_input = None
number_movie = None
list_of_movies = None
selected_movie = None

def search(update, context):
    update.message.reply_text("What Movie do you want to see?")
    return 1

def get_name_moive(update, context):
    global list_of_movies, user_input
    user_input = update.message.text
    list_of_movies = imdbAPI.search_imdb_movies(user_input)
    reply_text = '\n'.join([f"{index}. {movie_title}" for index, movie_title in enumerate(list_of_movies, start=1)])
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)
    update.message.reply_text("Choose Number")
    return 2


def get_number_of_movie(update, context):
    global number_movie, selected_movie
    number_movie = update.message.text
    number_movie = int(number_movie)
    selected_movie = list_of_movies[number_movie - 1]
    update.message.reply_text(selected_movie)
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text("Canceled")
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('search', search)],
    states={
        1: [MessageHandler(Filters.text, get_name_moive)],
        2: [MessageHandler(Filters.text, get_number_of_movie)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)



if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(conv_handler)

    updater.start_polling(1.0)
    updater.idle()
