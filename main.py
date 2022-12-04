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
          IconButton(icons.FACEBOOK),
          IconButton(icons.MESSENGER),
          IconButton(icons.LOGIN),
          IconButton(icons.PERSON_ADD),
          PopupMenuButton(

              items=[
                  PopupMenuItem(text="item 1"),
                  PopupMenuItem(text="item 2"),
                  PopupMenuItem(text="item 3"),
                  PopupMenuItem(text="item 4")

              ]
          )

        ]
    )
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(label="Setting", icon=icons.SETTINGS),
            NavigationDestination(label="FILE", icon=icons.FILE_OPEN)
        ]
    )
    page.add(App())



if __name__ == '__main__':
    flet.app(target=main)