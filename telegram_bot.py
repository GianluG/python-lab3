from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from telegram import ChatAction
from sys import argv

updater = Updater("598486728:AAHxLy96_9grf-0qx7Kfmnjr06I8d8-XnmA")
dp = updater.dispatcher
filename = argv[1]
txt = open(filename)
tasks = txt.read().split("\n")
length = len(tasks)
if tasks[length - 1] == "":
    tasks.pop(len(tasks)-1)
    length -= 1
txt.close()
ordered = 1


def start(bot,update):
    update.message.reply_text("This is your tasks_bot!")

def showTasks(bot, update):
    global length, ordered
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if length == 0:
        update.message.reply_text("Nothing to do!")
    if ordered == 0:
        tasks.sort()
        ordered = 1
    i = 0
    text = ""
    while i < length:
        text += "- "+tasks[i]
        if i < length-1:
            text += "\n"
        i += 1
    update.message.reply_text(text)


def newTask(bot, update, args):
    global length, ordered
    text = ""
    i = 0
    while i < len(args):
        text += args[i]
        if i < len(args) - 1:
            text += " "
        i += 1
    tasks.append(text)
    length += 1
    ordered = 0
    update.message.reply_text("Task has been added succesfully!")

def removeTask(bot, update, args):
    global length, tasks
    text = ""
    i=0
    while i < len(args):
        text += args[i]
        if i < len(args)-1:
            text += " "
        i += 1

    found = 0
    for element in tasks:
        if element == text:
            tasks.remove(element)
            update.message.reply_text("Found!")
            length -= 1
            found = 1
            break
    if found == 0:
        update.message.reply_text("None task has that name!")
    else:
        update.message.reply_text("Task has been removed successfully!")

def removeAllTasks(bot, update):
    global tasks, length
    if length > 0:
        tasks.clear()
    update.message.reply_text("Every task has been removed!")
    length = 0

def unknown(bot, update):
    update.message.reply_text("Unrecognized command!")


if __name__ == "__main__":
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("show_tasks", showTasks))
    dp.add_handler(CommandHandler("new_task", newTask, pass_args=True))
    dp.add_handler(CommandHandler("remove_task", removeTask, pass_args=True))
    dp.add_handler(CommandHandler("remove_all_tasks", removeAllTasks))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()

    updater.idle()
