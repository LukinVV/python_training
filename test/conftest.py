import pytest
from fixture.application import Application

fixture = None


# создание фикстуры
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    elif not fixture.is_vald():
        fixture = Application()

    fixture.session.ensure_login(user_name="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(end)
    return fixture
