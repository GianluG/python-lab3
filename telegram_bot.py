from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from sys import argv
import time

updater = Updater("598486728:AAHxLy96_9grf-0qx7Kfmnjr06I8d8-XnmA")
dp = updater.dispatcher
filename = argv[1]
txt = open(filename)
tasks = txt.read().split("\n")
txt.close()
ordered=1


def start(bot,update):
    update.message.reply_text("This is your tasks_bot!\nUse /help to see the command list!")

def showTasks(bot,update):
    for element in tasks:
        update.message.reply_text(element)

def newTask(bot,update, args):
    text=""
    for element in args:
        text += element+ " "
    print(text)
    print("ciao")
    tasks.append(text)
    for element in tasks:
        print(element)

    ordered = 0

def removeTask(bot,update):
    pass

def removeAllTasks(bot,update):
    pass

def help(bot,update):
    pass

def main():



    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("showTasks",showTasks))
    dp.add_handler(CommandHandler("newTask", newTask,pass_args=True))
    dp.add_handler(CommandHandler("removeTask", removeTask))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks))
    dp.add_handler(CommandHandler("help", help))


    updater.start_polling()



    updater.idle()

if __name__ == "__main__":
    main()