from abc import ABC, abstractmethod


class TextComponent(ABC):
    @abstractmethod
    def render(self):
        pass


class PlainText(TextComponent):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class TextDecorator(TextComponent):
    def __init__(self, component: TextComponent):
        self.component = component

    def render(self):
        return self.component.render()


class BoldDecorator(TextDecorator):
    def render(self):
        text = self.component.render()
        return f"<b>{text}</b>"


class ItalicDecorator(TextDecorator):
    def render(self):
        text = self.component.render()
        return f"<i>{text}</i>"



text = PlainText("This my test text!")
text = BoldDecorator(text)
text = ItalicDecorator(text)
print("Class-based decorator")
print(text.render())
print("-"*100)


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        changed_text = f"<b>{text}</b>"
        return changed_text
    return wrapper


def italic_decorator(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        changed_text = f"<i>{text}</i>"
        return changed_text
    return wrapper

@italic_decorator
@bold_decorator
def my_text(text):
    return text

print("Pythonic decorator")
print(my_text("hello world!"))
print("-"*100)

