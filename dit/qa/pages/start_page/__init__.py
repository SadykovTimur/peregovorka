from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.start_page.components.drawer import Drawer
from dit.qa.pages.start_page.components.header import Header
from dit.qa.pages.start_page.components.main import Main
from dit.qa.pages.start_page.components.menu import Menu

__all__ = ['StartPage']


class StartPage(Page):
    drawer = Drawer(class_name="mud-drawer-content")
    header = Header(tag="header")
    main = Main(css='[class*="mud-container"]')
    menu = Menu(css='[class*="mud-list"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.drawer.header.visible
                assert self.drawer.home.visible
                assert self.drawer.news.visible
                assert self.drawer.feedback.visible
                assert self.drawer.instruction.visible

                assert self.header.menu_btn.visible
                assert self.header.auth.visible

                assert self.main.connect.visible
                assert self.main.meet_name.visible

                return self.main.meet_link.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_after_auth(self) -> None:
        def condition() -> bool:
            try:
                assert self.drawer.header.visible
                assert self.drawer.home.visible
                assert self.drawer.news.visible
                assert self.drawer.feedback.visible
                assert self.drawer.instruction.visible
                assert self.drawer.history_meet.visible

                assert self.header.menu_btn.visible
                assert self.header.user.visible

                assert self.main.meeting.visible
                assert self.main.meet_name.visible

                return self.main.create_meeting.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
