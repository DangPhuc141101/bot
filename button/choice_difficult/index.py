from index import*
from helper.Index_correct import*
from helper.getDataApi import*
from constant.index import*
from helper.index import*
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
   
    CallbackContext,
)

# create button option
def create_button_option():
    keyboard = [
        [
            InlineKeyboardButton("choose level", callback_data=str(ONE)),
            InlineKeyboardButton("choose type of question", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    return keyboard
keyboard_option = create_button_option()

def choice_level(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("easy", callback_data=str(ONE)),
            InlineKeyboardButton("medium", callback_data=str(TWO)),
            InlineKeyboardButton("difficult", callback_data=str(THREE)),
            InlineKeyboardButton("random", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="please choose level", reply_markup=reply_markup
    )
    return SECOND


# SECOND -> ONE

def easy(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id'] 

    #edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '','easy')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen easy", reply_markup=reply_markup
    )
    return FIRST


def medium(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id'] 

    #edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '','medium')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have chossen medium", reply_markup=reply_markup
    )

    return FIRST


def difficult(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id']   

    #edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '','hard')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have chossen difficult", reply_markup=reply_markup
    )
    return FIRST


def randomDifficult(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id']   

    #edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '','')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen random", reply_markup=reply_markup
    )
    return FIRST
