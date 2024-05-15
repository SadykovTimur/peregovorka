from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    connect = Button(xpath="//span[text()='Присоединиться']")
    meet_link = TextField(css="input[class*='mud-input-slot']")
    meet_name = TextField(css='input[class*="mud-input-slot"]')
    meeting = Component(xpath="//span[text()='Запланировать встречу']")
    create_meeting = Button(xpath="//span[text()='Создать встречу']")


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
