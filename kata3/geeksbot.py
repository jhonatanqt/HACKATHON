from telegram.ext import Updater,CommandHandler


def main():
    updater = Updater(token="1152215992:AAFIFGuPBZ2KDcMdK5-CMIJpthjav8L24bA",use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start",start))
    updater.dispatcher.add_handler(CommandHandler("repite",repite))
    updater.dispatcher.add_handler(CommandHandler("suma",suma))
    updater.start_polling()
    updater.idle()

def start(update,context):
    update.message.reply_text("hola soy un bot")


def repite(update,context):
    update.message.reply_text(update.message.text)


def suma(update,context):
    # args = [2, 2]
    resultado = int(context.args[0])+int(context.args[1])
    update.message.reply_text("el resultado es " + str(resultado))

main( )
