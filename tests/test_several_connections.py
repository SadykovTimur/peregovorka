from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    connection_meeting,
    open_auth_page,
    open_connection_meeting,
    open_start_page,
    open_start_page_after_auth,
    sign_in,
)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('PEREGOVORKA')
@allure.story('Подключение к встрече')
@allure.title('Проверка подключение нескольких пользователей к встрече')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_several_connections(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)
    app2 = make_app(browser, device_type)
    app3 = make_app(browser, device_type)

    open_start_page(app)
    open_start_page(app2)
    open_start_page(app3)

    open_auth_page(app)
    sign_in(app, request.config.option.username, request.config.option.password)
    open_start_page_after_auth(app)

    open_connection_meeting(app, 'тест мониторинг')

    link = app.driver.current_url
    connection_meeting(app2, link, 'мониторинг 2')
    connection_meeting(app3, link, 'мониторинг 3')
