# from kivy.app import App

# class MyApp(App):
#    pass

# if __name__ == "__main__":
#    MyApp().run()
from kivy.app import App
from kivy.uix.button import Button


class TestApp( App ) :
    def build( self ) :
        return Button( text = 'Hello World' )


TestApp().run()