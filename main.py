from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from wikiped import search_wiki

TOKEN = "1851211986:AAGjmciomSdwMzi225X53sxt1hyKK68afrY"

def start(update, context):
    update.message.reply_text(
        "Доброго времени суток! Я - ваш личный дворецкий. Чем могу быть полезен?")

def help(update, context):
    update.message.reply_text(
        "Приветствую, я - Темный Дворецкий, Ваш личный бот и слуга. Если хотите посмотреть, что я умею, то нажимайте это: \n"
        "/comands")

def comands(update, context):
    update.message.reply_text(
        "Раз уж Вы обратились ко мне за помощью, то вот список всех моих доступных команд:\n"
        "/help - помощь\n"
        "/comands - список всех команд\n"
        "/wiki - поиск в Wikipedia (формат ввода команды: /wiki [слово для поиска])")

def wiki(update, context):
    print(context.args)
    word = ' '.join(context.args)
    if word:
        update.message.reply_text("Идет поиск...")
        response, url = search_wiki(word)
        update.message.reply_text(response+url)
    else:
        update.message.reply_text("Необходимо ввести данные для поиска")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Ваш Темный Дворецкий пробудился....")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("comands", comands))
    dp.add_handler(CommandHandler("wiki", wiki))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
