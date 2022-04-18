import telegram.ext 
from telegram.ext import Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
import os

bot_token = 'Put here token'
setvol_path = "Put here path to setvol"

updater = telegram.ext.Updater(bot_token, use_context=True)

def start(update, context):
    if os.path.exists(setvol_path) == True:
        buttons = [[KeyboardButton('🖥️ Lock sessions 🔒')], [KeyboardButton('🖥️ Shutdown system 🔌')]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🖥 Remote control 🖥", reply_markup=ReplyKeyboardMarkup(buttons))
    if os.path.exists(setvol_path) == False:
        update.message.reply_text("❌ Path to setvol is not valid ❌")
        update.message.reply_text("❗ * Create a script and try re-entering the file path, something like this: C:\\Users\\user\\Documents\\SetVol.exe. If you wanna download SetVol check this link: https://rlatour.com/setvol/") 
        exit()

def messageHandler(update, context):
    if '🖥️ Lock sessions 🔒' in update.message.text:
        os.system(setvol_path + " -100")
        os.system("Rundll32.exe user32.dll,LockWorkStation")
        update.message.reply_text("✅ Session has been locked 👌👌👌")
    if '🖥️ Shutdown system 🔌' in update.message.text:
        os.system("shutdown -p")
        update.message.reply_text("✅ System has been disabled 👌👌👌")
                
updater.dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
updater.dispatcher.add_handler(telegram.ext.MessageHandler(Filters.text, messageHandler))
updater.start_polling()
updater.idle()
