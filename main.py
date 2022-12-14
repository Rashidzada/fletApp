import flet

from flet import *


class App(UserControl):


    def build(self):
        t = ListView(expand=True, auto_scroll=True,spacing=20,padding=40)
        for x in range(60):
            t.controls.append(
                ElevatedButton(f"ADD  {x}")
                #dsfjksdhkfjsdhgjkhsdfkjh
                #dkfsjghfklghsdklfjh 2345345234kjsdghfjksdhgklsdjfh
            )
        return Container(
            content=Row(
                width=400,
                height=500,
                controls=[
                  Tabs(
                      tabs=[
                          Tab(
                              text="Add"
                          )
                      ]
                  ),
                  t,

                ],

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
