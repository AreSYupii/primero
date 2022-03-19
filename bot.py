import telegram
from genericpath import exists
import os
from telegram import *
from telegram.ext import *

def start_handler(update, context):
    update.message.reply_text(parse_mode="HTML", text=f"🚀 Gracias por Iniciarme <b>@{update.effective_user.username}</b>\nSoy un Bot para dar Soporte en :\n<b>Python Insights 🐍</b>\n<b>🐍 Python Ideas Community</b>\n👨‍💻Bot Creado por : @AresDza\nCon - <pre>Python Telegram Bot</pre>".replace("🚀 Gracias por Iniciarme <b>@None</b>", f"🚀 Gracias por Iniciarme <b>{update.effective_user.first_name}</b>").replace("🚀 Gracias por Iniciarme <b>@AresDza</b>", "✨Bienvenido de Nuevo <b>Jefe</b>"),
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Python Insights 🐍", url="t.me/Python_Insights")], [InlineKeyboardButton(text="🐍 Python Ideas Community", url="t.me/Python_Ideas_Community")]]))
def welcomemsg(update, context):
    update.message.reply_text(text=f"👋🏻Hola {update.effective_user.first_name} te doy la Bienvenida a {update.message.chat.title}\n\nEspero que pases una agradable estancia aquí, y que encuentres lo que estás buscando 😉, de vez en cuando puedes hacer que tus compañeros aprendan de ti, así que no tengas miedo en compartir tus conocimientos sobre la programación en este grupo : {update.message.chat.title}.\n\nEl canal tiene las cosas bien ordenadas, y de vez en cuando se harán encuestas para que puedan decidir sobre lo siguiente a resolver 👍, aquí estamos aprendiendo todos.",
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Python Insights 🐍", url="t.me/Python_Insights"), InlineKeyboardButton(text="🐍 Python Ideas Community", url="t.me/Python_Ideas_Community")],[InlineKeyboardButton(text="[SUPPORT] Python Ideas", url="t.me/PythonIdeasSupport_bot"), InlineKeyboardButton(text="🤖 🅻🅾️🅶 DE BOTS", url="t.me/Rregistro_De_Bots_AresDza")]]))
def goodbyemsg(update, context):
    update.message.reply_text(text=f"{update.effective_user.first_name} se ha marchado, 👋🏻 adiós Compañer@".replace("[SUPPORT] Python Ideas se ha marchado, 👋🏻 adiós Compañer@", "Expulsado por mala influencia 😐👌"))
def banear(update, context):
    fromchatid=update.message.reply_to_message.chat.id
    fromuserid=update.message.reply_to_message.from_user.id
    fromname=update.message.reply_to_message.from_user.first_name
    chatid=update.message.chat.id
    userid=update.effective_user.id
    if (update.effective_user.id):
        if (update.effective_user.id == 1307228755):
            context.bot.banChatMember(chat_id=fromchatid, user_id=fromuserid), bot.sendMessage(chat_id=fromchatid, text=f"{fromname} ha sido Baneado Indefinidamente.")
        if (update.effective_user.id != 1307228755):
            context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
    else:
        context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
def desbanear(update, context):
    fromchatid=update.message.reply_to_message.chat.id
    fromuserid=update.message.reply_to_message.from_user.id
    fromname=update.message.reply_to_message.from_user.first_name
    chatid=update.message.chat.id
    userid=update.effective_user.id
    if (update.effective_user.id):
        if (update.effective_user.id == 1307228755):
            context.bot.unbanChatMember(chat_id=fromchatid, user_id=fromuserid), bot.sendMessage(chat_id=fromchatid, text=f"{fromname} Ya puede entrar denuevo al Chat.")
        if (update.effective_user.id != 1307228755):
            context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
    else:
        context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
def anclar(update, context):
    if (update.effective_user.id):
        if (update.effective_user.id == 1307228755):
            if (update.message.reply_to_message):
                if (update.message.reply_to_message != exists):
                    context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id), bot.pinChatMessage(chat_id=update.message.chat.id, message_id=update.message.reply_to_message.message_id)
            else:
                context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id), bot.sendMessage(chat_id=update.message.chat.id ,text="El Comando Sólo funciona cuando le Respondes a un Mensaje 🔄")
        if (update.effective_user.id == 1087968824):
            if (update.message.reply_to_message):
                if (update.message.reply_to_message != exists):
                    context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id), bot.pinChatMessage(chat_id=update.message.chat.id, message_id=update.message.reply_to_message.message_id)
            else:
                context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id), bot.sendMessage(chat_id=update.message.chat.id ,text="El Comando Sólo funciona cuando le Respondes a un Mensaje 🔄")
        if (update.effective_user.id != 1307228755):
            context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
    else:
        context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
def desanclar(update, context):
    if (update.effective_user.id):
        if (update.effective_user.id == 1307228755):
            if (update.message.reply_to_message):
                if (update.message.reply_to_message != exists):
                    context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id), bot.unpinChatMessage(chat_id=update.message.chat.id, message_id=update.message.reply_to_message.message_id)
            else:
                context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id), bot.sendMessage(chat_id=update.message.chat.id ,text="El Comando Sólo funciona cuando le Respondes a un Mensaje 🔄")
        if (update.effective_user.id != 1307228755):
            context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
    else:
        context.bot.sendMessage(chat_id=update.message.chat.id, parse_mode="HTML", text="🤨 No eres Nadie para Darme <b>órdenes</b>")
def yinfo(update, context):
    fromchatid=update.message.reply_to_message.chat.id
    fromuserid=update.message.reply_to_message.from_user.id
    userid=update.effective_user.id
    context.bot.sendMessage(chat_id=fromchatid, parse_mode="HTML", text=f"<b>USER_ID :</b> <pre>{fromuserid}</pre>\n<b>CHAT_ID :</b> <pre>{fromchatid}</pre>\n<b>MI_ID :</b> <pre>{userid}</pre>")
    context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)

        # TOKEN
if __name__ == '__main__':
    token = os.environ['TOKEN']
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)

    # Despachadores
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_handler))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcomemsg))
    dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, goodbyemsg))
    dp.add_handler(CommandHandler("ban", banear))
    dp.add_handler(CommandHandler("unban", desbanear))
    dp.add_handler(CommandHandler("pin", anclar))
    dp.add_handler(CommandHandler("unpin", desanclar))
    dp.add_handler(CommandHandler("yinfo", yinfo))
    
    # Para Ejecutar el Bot
    updater.start_polling()
    print(f'Ejecutando el bot @{bot.username}')
    updater.idle()
