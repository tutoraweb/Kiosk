# -*- coding: utf-8 -*-
"""
    Kiosk Tests
    ~~~~~~~~~~~

    Tests for the Kiosk microservice.

    :license: MPL v2.0, see LICENSE for more details.
"""

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2015, Serapheim Dimitropoulos
#

import pytest

import kiosk

@pytest.fixture
def client(request):
    return kiosk.app.test_client()

def test_hello(client):
    """Get Hello Message :-)"""

    r = client.get('/')

    assert r.status == '200 OK'
    assert b'Hello, World!' in r.data

