from telegram.ext import *



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


def Search(update, context):
    update.message.reply_text("What Movie do you want to see?")

def reply (update,context):
    global user_input
    user_input = update.message.text
    update.message.reply_text(imdbAPI.Search_Movie(user_input))
    
def search_item(update,context):
    #update.message.reply_text(imdbAPI.Search_Movie(user_input))
    pass
if __name__ == '__main__':

    updater = Updater(keys.token,use_context=True)

    dp = updater.dispatcher


    # Commands

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('Search', Search))
    dp.add_handler(CommandHandler('search_item', search_item))
    
    dp.add_handler(MessageHandler(Filters.text, reply))
    
    
    updater.start_polling(1.0)
    updater.idle()