from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.connection_meeting_page.components.video import Video
from dit.qa.pages.start_page.components.menu import Menu

__all__ = ['ConnectionMeetingPage']


class ConnectionMeetingPage(Page):
    iframe = Component(tag='iframe')
    video = Video(id="react")
    menu = Menu(css='[class*="mud-list"]')

    def click_meet(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)
        self.video.connect.click()
        self.driver.switch_to.default_content()

    def data_input(self, user: str) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)
        self.video.user.send_keys(user)
        self.driver.switch_to.default_content()

    def wait_for_loading_connection(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)

        def condition() -> bool:
            try:
                assert self.video.connect_meet.visible
                assert self.video.connect.visible
                assert self.video.toolbox.visible
                assert self.video.preview.visible

                return self.video.toolbox.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

        self.driver.switch_to.default_content()

    def wait_for_loading_connection_meeting(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)

        def condition() -> bool:
            try:
                assert self.video.timer.visible
                assert self.video.remote_video.visible

                return self.video.items.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

        self.driver.switch_to.default_content()

    def wait_logout_meeting(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)

        def condition() -> bool:
            try:
                return self.video.title_exit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg="Page was not loaded")
        self.app.restore_implicitly_wait()

        self.driver.switch_to.default_content()
