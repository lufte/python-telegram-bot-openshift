# python-telegram-bot-openshift

Starter kit for running a Telegram bot (built with the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library) on [Openshift](https://www.openshift.com/).

Instructions:

1. ~~Register at [Openshift](https://www.openshift.com/).~~ This starter kit works on Openshift online v2, which no longer accepts registration as Red Hat is moving to the new (v3) version. You must either have an existing account for the previous version or adapt the code to run in the new one. Send me a pull request if you manage to do so.
2. Create a Python3 application.
3. Add 
4. Complete the `bot.py` file with your handlers.
5. Put the `wsgi.py` file at the root of your app directory tree. The `bot.py` file can go anywhere as long as you update the `import` statement in the previous file.
6. Deploy everything to Openshift.
