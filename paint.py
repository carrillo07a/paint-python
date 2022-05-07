from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.core.window import Window


class Draw(Widget):
    Window.clearcolor = (1, 1, 1, 1)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            touch.ud['draw'] = Line(points=touch.pos)

    def on_touch_move(self, touch):
        touch.ud['draw'].points += touch.pos


class Paint(App):
    def build(self):
        return Draw()


if __name__ == "__main__":
    Paint().run()
