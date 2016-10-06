# python-telegram-bot-openshift

Starter kit for running a Telegram bot (built with the [python-telegram-bot](https://github.com/lufte/python-telegram-bot-openshift.git) library) in [Openshift](https://www.openshift.com/).

Instructions:

1. Register at [Openshift](https://www.openshift.com/).
2. Create a Python3 application.
3. Complete the `bot.py` file with your bot's token and handlers.
4. Put the `wsgi.py` file at the root of your app directory tree. The `bot.py` file can go anywhere as long as you update the `import` statement in the previous file.
5. Put a `requirements.txt` file also at the root of the directory tree. Include **Flask** and **python-telegram-bot** among your dependencies.
6. Deploy everything to Openshift.
