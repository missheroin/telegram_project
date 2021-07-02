from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from wikiped import search_wiki
from vzevent import writeevent
from vznote import writenote
from wrnotes import printnotes
from wrevents import printevents
from odnote import noteone

a = 'Y;r;f;a;8;6;K;K;y;h;1;t;x;s;3;5;X;5;2;2;i;z;M;w;d;S;m;o;i;c;m;j;G;A;A;:;6;8;9;1;1;2;1;5;8;1'
b = a.split(';')
b.reverse()
c = ''
for i in range(len(b)):
    c = c + str(b[i])

TOKEN = c


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
        "1. /eventwrite - создать событие (формат ввода команды: /eventwrite-[дата-время-заголовок-описание-время напоминания]\n"
        "2. /notewrite - создать заметку (формат ввода команды: /notewrite-[заголовок-описание]\n"
        "3. /allevents - вывести дату, время и заголовки всех событий\n"
        "4. /allnotes - вывести заголовки всех заметок\n"
        "5. !В разработке! /onenote - вывести заметку по заданному заголовку\n"
        "6. /wiki - поиск в Wikipedia (формат ввода команды: /wiki [слово для поиска])\n"
        "7. /comands - список всех команд\n"
        "/help - помощь\n"

    )


def eventwrite(update, context):
    writeevent(update.message.text)
    update.message.reply_text("Событие успешно создано")


def notewrite(update, context):
    writenote(update.message.text)
    update.message.reply_text("Заметка успешно создана")


def allnotes(update, context):
    update.message.reply_text(printnotes())


def allevents(update, context):
    update.message.reply_text(printevents())


def onenote(update, context):
    update.message.reply_text(noteone(update.message.text))


def wiki(update, context):
    print(context.args)
    word = ' '.join(context.args)
    if word:
        update.message.reply_text("Идет поиск...")
        response, url = search_wiki(word)
        update.message.reply_text(response + url)
    else:
        update.message.reply_text("Необходимо ввести данные для поиска")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Ваш Темный Дворецкий пробудился....")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("comands", comands))
    dp.add_handler(CommandHandler("eventwrite", eventwrite))
    dp.add_handler(CommandHandler("notewrite", notewrite))
    dp.add_handler(CommandHandler("allnotes", allnotes))
    dp.add_handler(CommandHandler("allevents", allevents))
    dp.add_handler(CommandHandler("onenote", onenote))
    dp.add_handler(CommandHandler("wiki", wiki))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
