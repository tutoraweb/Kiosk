# -*- coding: utf-8 -*-
"""
    Kiosk
    ~~~~~

    The Kiosk microservice of Tutora.

    :license: MPL v2.0, see LICENSE for more details.
"""

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2015, Serapheim Dimitropoulos
#

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

