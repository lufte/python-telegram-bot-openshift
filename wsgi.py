#!/usr/bin/env python

# Copyright (C) 2016 Javier Ayres
#
# This file is part of python-telegram-bot-openshift.
# 
# python-telegram-bot-openshift is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# python-telegram-bot-openshift is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with python-telegram-bot-openshift.  If not, see <http://www.gnu.org/licenses/>.

import os
import bot
from flask import Flask, request
from telegram import Update


application = Flask(__name__, instance_path=os.environ['OPENSHIFT_REPO_DIR'])
update_queue, bot_instance = bot.setup(webhook_url='https://{}/{}'.format(
    os.environ['OPENSHIFT_GEAR_DNS'],
    bot.TOKEN
))


@application.route('/')
def not_found():
    """Server won't respond in OpenShift if we don't handle the root path."""
    return ''


@application.route('/' + bot.TOKEN, methods=['GET', 'POST'])
def webhook():
    if request.json:
        update_queue.put(Update.de_json(request.json, bot_instance))
    return ''


if __name__ == '__main__':
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    application.run(host=ip, port=port)
