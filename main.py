from telegram.ext import *
import config_data
import  reply_func as reply
import pandas as pd
import pandas_datareader.data as web

print("bot started...")


def start_message(update, context):
    update.message.reply_text("Type something random to get started!")


def help_message(update, context):
    update.message.reply_text("""
    /stock ticker - get the price
    """)


def handle_message(update, context):
    text = str(update.message.text.lower())
    response = reply.sample_reply(text)
    update.message.reply_text(response)


def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]["Close"]
    update.message.reply_text(f"Current price of {ticker} is {price:.2f}$")


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(config_data.api_key, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_message))  # /start will call the function "start_message"
    dp.add_handler(CommandHandler("help", help_message))    # /help will call the function "help_message"
    dp.add_handler(CommandHandler("stock", stock))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling(2)    # 2 seconds between updates
    updater.idle()

if __name__ == '__main__':
    main()