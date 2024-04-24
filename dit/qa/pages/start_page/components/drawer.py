from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Drawer']


class DrawerWrapper(ComponentWrapper):
    header = Component(xpath="//h6[text()='Переговорка']")
    home = Component(xpath="//div[text()='Главная']")
    news = Component(xpath="//div[text()='Новости']")
    feedback = Component(xpath="//div[text()='Обратная связь']")
    instruction = Component(xpath="//div[text()='Инструкции']")
    history_meet = Component(xpath="//div[text()='История встреч']")


class Drawer(Component):
    def __get__(self, instance, owner) -> DrawerWrapper:
        return DrawerWrapper(instance.app, self.find(instance), self._locator)
