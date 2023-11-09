from kivy.app import App
from kivy.lang import Builder
from model import Product

class ShoppingApp(App):
    """Build the Shopping App GUI."""
    def build(self):
        self.root = Builder.load_file('view.kv')
        return self.root

    def create_widgets(self):
        """Create the widgets."""
        pass

    def clear_all(self):
        """Clear the widgets."""
        pass
