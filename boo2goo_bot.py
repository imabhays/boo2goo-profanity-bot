from telegram.ext import Updater, MessageHandler, Filters
import threading
import os

def handle_message(update, context):
    message = update.message
    chat_id = message.chat_id

    # Objectionable words to be replaced
    objectionable_words = load_profanity_list()
    
    # Funny replacements for objectionable words
    funny_replacements = ['googoo', 'booboo']

    # Split the message into individual words
    words = message.text.split()

    # Check each word in the message
    for i in range(len(words)):
        if words[i].lower() in objectionable_words:
            # Replace objectionable word with a funny replacement
            words[i] = funny_replacements[i % len(funny_replacements)]  # Cycling through funny replacements

    # Reconstruct the filtered message
    filtered_message = ' '.join(words)

    if filtered_message != message.text:
        # Delete the original message after 5 seconds
        threading.Timer(5, delete_message, args=(context.bot, chat_id, message.message_id)).start()

        # Get the username of the original message sender
        username = message.from_user.username or message.from_user.first_name

        # Construct the new message with the "message posted by" information
        new_message = f"from {username}:\n{filtered_message}"

        # Send a new message with the filtered content after 5 seconds
        threading.Timer(5, send_message, args=(context.bot, chat_id, new_message)).start()

def delete_message(bot, chat_id, message_id):
    bot.delete_message(chat_id=chat_id, message_id=message_id)

def send_message(bot, chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

def load_profanity_list():
    with open('profanity-list.txt', 'r') as file:
        return [line.strip() for line in file]

def main():
    # Create an updater and pass your bot's API token
    updater = Updater(token=os.environ['BOT_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    
    # Register the message handler
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(message_handler)
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
