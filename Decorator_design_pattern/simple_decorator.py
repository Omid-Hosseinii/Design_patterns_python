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
        return f"{text}: text became **bold**"



text = PlainText("This my test text!")
text = BoldDecorator(text)

print(text.render())