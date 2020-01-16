
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        self.root.ids.main_label.text = "Enter a number and pick a Square"
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call),
        output result to label widget."""
        try:
            result= float(value)
            ans = result ** 2
            self.root.ids.output_label.text = str(ans)
        except ValueError:
            self.root.ids.output_label.text = str("Error")


SquareNumberApp().run()
