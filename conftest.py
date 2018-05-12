import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None

# создание фикстуры
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)
    if fixture is None or not fixture.is_vald():
        fixture = Application(browser=browser, base_url=target['base_url'])
    fixture.session.ensure_login(user_name=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(end)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption('--target', action='store', default='target.json')