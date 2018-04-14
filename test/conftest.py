# если вынести в глобальную папку то перестает работать при запуске ВСЕХ тестов их папки с тестами
#fixture
#'app'
#not found
#available fixtures: pytestconfig, capfd, capsys, tmpdir, monkeypatch, recwarn
#use 'py.test --fixtures [testpath]' for help on them.

# если оставить
import pytest
from fixture.application import Application

#создание фикстуры
@pytest.fixture(scope="session", autouse=True)
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture