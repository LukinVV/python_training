import pytest
from fixture.application import Application

fixture=None

#создание фикстуры
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture=Application()
        fixture.session.login(user_name="admin", password="secret")
    else:
        if not fixture.is_vald():
            fixture = Application()
            fixture.session.login(user_name="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse = True)
def stop(request):
    def end():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(end)
    return fixture

