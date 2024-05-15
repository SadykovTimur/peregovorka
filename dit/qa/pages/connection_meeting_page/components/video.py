from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['Video']


class VideoWrapper(ComponentWrapper):
    connect_meet = Component(css='[class*="title"]')
    connect = Button(css='[class*="actionButton"]')
    toolbox = Component(id="new-toolbox")
    preview = Component(id="preview")
    timer = Component(css='[class*="timer"]')
    items = Component(class_name="toolbox-content-items")
    remote_video = Component(id="remoteVideos")
    context_menu = Button(css='[class*="context-menu"]')
    record = Button(xpath="//span[text()='Start recording']")
    stop_record = Button(xpath="//span[text()='Stop recording']")
    checkbox = Button(id="recording-switch-local")
    go_record = Button(id="modal-dialog-ok-button")
    exit = Button(css='[class*="hangup-button"]')
    title_exit = Component(id="thanksMessage")
    user = TextField(css='[data-testid="prejoin.screen"] input')


class Video(Component):
    def __get__(self, instance, owner) -> VideoWrapper:
        return VideoWrapper(instance.app, self.find(instance), self._locator)
