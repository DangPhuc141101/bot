from main import*
from button.choice_difficult.index import*
from  helper.Index_correct import*
from helper.getDataApi import*
from helper.index import*
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
)

def create_button_type_question():
    keyboard = []
    arrTam = []
    i = 0
    for ele in typeOfQuestion:
        #    ele['value'] get value 20->28
        arrTam.append(InlineKeyboardButton(str(ele['text']), callback_data=ele['value']))
        i = i + 1
        if (i == 3):
            keyboard.append(arrTam)
            i = 0
            arrTam = []
    keyboard.append([InlineKeyboardButton('Back to Menu', callback_data='29')])
    return keyboard

# List button keyboard type question
keyboard_type_question = create_button_type_question()

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

# List button option
keyboard_option = create_button_option()

def choice_type_question(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    reply_markup = InlineKeyboardMarkup(keyboard_type_question)
    query.edit_message_text(
        text="choose type question", reply_markup=reply_markup
    )
    return FOURTH

def choice_type_one(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '20', '')

    reply_markup = InlineKeyboardMarkup(keyboard_option)

    query.edit_message_text(
        text="you have choosen Mythology", reply_markup=reply_markup
    )

    return FIRST

def choice_type_two(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '21', '')

    keyboard = create_button_type_question()
    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen Sports", reply_markup=reply_markup
    )
    return FIRST

def choice_type_three(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '22', '')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen Geography", reply_markup=reply_markup
    )
    return FIRST

def choice_type_four(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '23', '')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen History", reply_markup=reply_markup
    )
    return FIRST

def choice_type_five(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '24', '')

    keyboard = create_button_type_question()
    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen Politics", reply_markup=reply_markup
    )
    return FIRST

def choice_type_six(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '25', '')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen Art", reply_markup=reply_markup
    )
    return FIRST

def choice_type_seven(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '26', '')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen Celebrities", reply_markup=reply_markup
    )
    return FIRST

def choice_type_eight(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '27', '')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen Animals", reply_markup=reply_markup
    )
    return FIRST

def choice_type_nine(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    # edit độ khó dễ cho câu hỏi
    editTypeAddDifficulty(teleId, '28', '')

    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen Vehicles", reply_markup=reply_markup
    )
    return FIRST

def choice_back_menu(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    teleId = query['message']['chat']['id']

    print(getUserById(teleId))
    reply_markup = InlineKeyboardMarkup(keyboard_option)
    query.edit_message_text(
        text="you have choosen back to menu", reply_markup=reply_markup
    )
    return FIRST