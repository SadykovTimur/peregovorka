import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.auth_page import AuthPage
from dit.qa.pages.connection_meeting_page import ConnectionMeetingPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'open_auth_page',
    'sign_in',
    'open_start_page_after_auth',
    'open_connection_meeting',
    'logout',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def open_auth_page(app: Application) -> None:
    with allure.step('Opening Auth page'):
        try:
            StartPage(app).header.auth.click()
            AuthPage(app).wait_for_loading()

            screenshot_attach(app, 'auth_page')
        except Exception as e:
            screenshot_attach(app, 'auth_page_error')

            raise TimeoutError('Auth page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = AuthPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_start_page_after_auth(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            StartPage(app).wait_for_loading_after_auth()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def logout(app: Application) -> None:
    with allure.step('Logout page'):
        try:
            start_page = StartPage(app)
            app.move_to_element(start_page.header.user.webelement)
            start_page.menu.exit.click()
            start_page.wait_for_loading()

            screenshot_attach(app, 'logout_page')
        except Exception as e:
            screenshot_attach(app, 'logout_page_error')

            raise TimeoutError('Logout was not loaded') from e


def open_connection_meeting(app: Application, meet: str) -> None:
    with allure.step('Opening Connection meeting page'):
        try:
            start_page = StartPage(app)
            start_page.main.input_auth.send_keys(meet)
            start_page.main.create_meeting.click()

            connection_meeting_page = ConnectionMeetingPage(app)
            connection_meeting_page.wait_for_loading_connection()
            connection_meeting_page.click_meet()
            connection_meeting_page.wait_for_loading_connection_meeting()

            screenshot_attach(app, 'connection_meeting_page')
        except Exception as e:
            screenshot_attach(app, 'connection_meeting_page_error')

            raise TimeoutError('Connection meeting page was not loaded') from e
