from telegram import *
from telegram.ext import Updater, CommandHandler, ConversationHandler
import requests
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv
from os import getenv
load_dotenv("envs")
TELEGRAM_TOKEN=getenv("TELEGRAM_TOKEN")

#Your zillow link
URL=getenv("URL")

#Your browser header
headers = {
    "Content-type": "text/html; charset=iso-8859-1",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


def retrieves_estates():
    estates_info = []

    response = requests.get(URL, headers=headers)
    time.sleep(2)
    parser = BeautifulSoup(response.text, "html.parser")

    for address, link, price in zip(parser.find_all("address"), parser.select(".property-card-link"), parser.select("[data-test='property-card-price']")):
        if link['href'] in estates_info:
            continue
        estates_info.append({"address": address.text, "link": link['href'], "price": price.text})

    return estates_info


# Conversation states
SHOW_ESTATES = range(1)


def start(update, context):
    update.message.reply_text("Hello! Welcome to the Estates Bot. Type /show to see available estates in Los Angeles")
    return SHOW_ESTATES


def handle_showing_estates(update, context):
   for estate in retrieves_estates():
        estate_list_message = f"Title: {estate['address']}\n"
        estate_list_message += f"Link: {estate['link']}\n"
        estate_list_message += f"Price: {estate['price']}\n\n"

        update.message.reply_text(estate_list_message, reply_markup=ReplyKeyboardRemove())

   return SHOW_ESTATES


def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SHOW_ESTATES: [
                CommandHandler('show', handle_showing_estates),  # Removed the parentheses

            ]
        },
        fallbacks=[]
    )
    dispatcher.add_handler(conv_handler)


    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()