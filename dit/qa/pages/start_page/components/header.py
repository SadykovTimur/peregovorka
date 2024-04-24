from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    menu_btn = Component(css="[class*='mud-icon-button-edge-start']")
    auth = Button(xpath='//span[text()="Войти"]')
    user = Component(xpath="//p[text()='ФИО не заполнено']")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
