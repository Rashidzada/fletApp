import flet

from flet import *

class App(UserControl):
    def build(self):
        return Container(
            content=Row(
                controls=[
                    Text("this is a first time to show ")
                ]
            )
        )

def main(page:Page):
    page.add(App())

if __name__ == '__main__':
    flet.app(target=main)