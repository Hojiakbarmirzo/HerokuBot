
import logging
import  wikipedia
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

wikipedia.set_lang("uz")
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:

    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Assalomu alykum Wikibotga xush kelibsiz {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:

    update.message.reply_text('Help!')


def wiki_text(update: Update, context: CallbackContext) -> None:
    try:
        update.message.reply_text(wikipedia.summary(update.message.text))
    except:
        update.message.reply_text("Bunday maqola mavjud emas.")


def main() -> None:

    updater = Updater("1770875004:AAGR0ZamUiwOtQNtZamo6J0tciwg85SRzFQ")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, wiki_text))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()