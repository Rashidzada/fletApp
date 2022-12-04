import flet

from flet import *


class App(UserControl):
    def build(self):
        return Container(
            content=Row(
                controls=[
                  Text('this is a first time to the main while')
                ]
            )
        )


def main(page:Page):
    page.appbar = AppBar(
        leading=Icon(icons.PALETTE_SHARP),
        leading_width=40,
        bgcolor=colors.BLACK,
        color=colors.WHITE,
        title=Text("My AppBar"),
        center_title=False,
        actions=[

        ]
    )
    page.add(App())



if __name__ == '__main__':
    flet.app(target=main)