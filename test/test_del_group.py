# -*- coding: utf-8 -*-

def test_del_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.del_first_group()
    app.session.logout()