# python-telegram-bot-openshift

Starter kit for running a Telegram bot (built with the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library) on [Openshift](https://www.openshift.com/).

Instructions:

1. Register at [Openshift](https://www.openshift.com/). This starter kit works on Openshift online v2 and v3.
2. Create a Python3 application.
3. Add the following environment variables (for v2 only the TOKEN is needed):
    * TOKEN: your telegram bot token
    * APP_FILE: wsgi.py
    * OPENSHIFT_REPO_DIR: [base dir of the project], i.e. /opt/app-root/src
    * OPENSHIFT_GEAR_DNS: [domain of the app], see the hostname of the route
    * OPENSHIFT_PYTHON_IP: 0.0.0.0
    * OPENSHIFT_PYTHON_PORT: 8080
4. Complete the `bot.py` file with your handlers.
5. Put the `wsgi.py` file at the root of your app directory tree. The `bot.py` file can go anywhere as long as you update the `import` statement in the previous file.
6. Deploy everything to Openshift.
