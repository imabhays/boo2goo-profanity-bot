# Boo2Goo Bot

Welcome to the Boo2Goo Bot! This bot is designed to filter out profanity in messages sent in Telegram groups. It replaces objectionable words with fun alternatives, making it a playful and safe environment for friends to communicate.

## About
- Bot Link: [t.me/boo2goo_bot](https://t.me/boo2goo_bot)
- This bot was inspired by Groot, my newborn, and a group of young college friends who wanted to use language that they wouldn't accidentally show to their parents.
- Profanity words are limited to English and Hindi only.
- It's a fun app created with the intention of providing a safe and enjoyable chat experience.
- The profanity list includes a wide range of words to ensure comfort in various situations.

## How It Works
- The bot functions within Telegram groups, where it is added as an additional user.
- Every message sent by users in the group is filtered by the bot.
- If a word in the message matches a word in the `profanity-list.txt` file, 
    - it allows receiver to read the original message with profanity,
    - after 5 seconds from reading the message it does the operation.
    - profanity is replaced with either "googoo" or "booboo."
- To accomplish this, the bot deletes the original message and reposts the edited version with a header.


**Example of original message**


![image-center](before.jpg){: .align-center}{: width="500" }


**Example of Edited message posted by Bot**


![image-center](after.jpg){: .align-center}{: width="500" }

Please note that due to Telegram bot limitations, the bot cannot directly edit messages from other users. Hence, the original message is deleted, and an edited version is posted with the header.

Enjoy chatting with your friends in a fun and friendly environment with Boo2Goo Bot!


## How To Make Your Own Telgram Bot and Host It On Railway.app

[Follow this tutorial]


