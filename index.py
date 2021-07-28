import logging
import requests
from  helper.Index_correct import*
from helper.getDataApi import*
from helper.index import*

from telegram import *
from telegram.ext import *

from button.choice_answer.index import*
from button.choice_difficult.index import*
from button.choice_type_question.index import*
from button.command.index import*
from constant.index import*

def main() -> None:
    """Run the bot."""
    updater = Updater(tokenBot)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(choice_level, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(choice_type_question, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(startNow, pattern='^' + str(THREE) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(easy, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(medium, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(difficult, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(randomDifficult, pattern='^' + str(FOUR) + '$'),
            ],
            THIRD: [
                CallbackQueryHandler(AnswerA, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(AnswerB, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(AnswerC, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(AnswerD, pattern='^' + str(FOUR) + '$')
            ],
            FOURTH: [
                CallbackQueryHandler(choice_type_one, pattern='^' + str(20) + '$'),
                CallbackQueryHandler(choice_type_two, pattern='^' + str(21) + '$'),
                CallbackQueryHandler(choice_type_three, pattern='^' + str(22) + '$'),
                CallbackQueryHandler(choice_type_four, pattern='^' + str(23) + '$'),
                CallbackQueryHandler(choice_type_five, pattern='^' + str(24) + '$'),
                CallbackQueryHandler(choice_type_six, pattern='^' + str(25) + '$'),
                CallbackQueryHandler(choice_type_seven, pattern='^' + str(26) + '$'),
                CallbackQueryHandler(choice_type_eight, pattern='^' + str(27) + '$'),
                CallbackQueryHandler(choice_type_nine, pattern='^' + str(28) + '$'),
                CallbackQueryHandler(choice_back_menu, pattern='^' + str(29) + '$'),
             ]

        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()