import asyncio
import logging
from io import BytesIO

from telegram import Update, ChatAction
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

import settings
from screenshot import capture_screenshot, prepare_url

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=settings.LOGGING_LEVEL,
)

logger = logging.getLogger(__name__)

event_loop = asyncio.get_event_loop()


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(settings.START_MESSAGE)


def make_screenshot(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # prepare url from the message appending http
    url = prepare_url(update.message.text)

    logger.info(f"screenshot-bot.capturing_screenshot, url={url}")

    context.bot.send_chat_action(update.effective_user.id, ChatAction.UPLOAD_DOCUMENT)

    # capture screenshot and get bytes
    screenshot = event_loop.run_until_complete(capture_screenshot(url))

    # send the screenshot
    update.message.reply_document(BytesIO(screenshot), filename="screenshot.png")


def main():
    """Start the bot."""

    updater = Updater(settings.BOT_TOKEN)

    # Get the dispatcher to register handlers.
    dispatcher = updater.dispatcher

    # Connect start handler for /start command.
    dispatcher.add_handler(CommandHandler("start", start))

    # For any message which matches web url regex - use make_screenshot handler.
    dispatcher.add_handler(
        MessageHandler(Filters.regex(settings.WEB_URL_REGEX), make_screenshot)
    )

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
