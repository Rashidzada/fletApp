import flet as ft
from flet import *
from flet.view import View
def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(

                "/",

                [
                    AppBar(title=Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT,
                           leading=Icon(icons.PALETTE_SHARP),
                           leading_width=40,
                           center_title=False,
                           actions=[
                               IconButton(icons.PERSON, on_click=lambda e:page.go("/about")),
                               IconButton(icons.CONTACT_PAGE,tooltip="contact page", on_click=lambda e:page.go("/contact")),
                               PopupMenuButton(
                                   items=[
                                       PopupMenuItem(text="iteam 1"),
                                       PopupMenuItem(text="iteam 2"),
                                       PopupMenuItem(text="iteam 3"),
                                       PopupMenuItem(text="iteam 4"),
                                       PopupMenuItem(text="iteam 5"),

                                   ]
                               ),

                           ]

                           ),

                    ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),

                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Store Page"), bgcolor=colors.BLACK,
                               color=colors.WHITE,
                               leading=Icon(icons.PALETTE_SHARP),
                               leading_width=40,
                               center_title=False,
                               actions=[
                                   IconButton(icons.HOME,on_click=lambda e:
                                              page.go("/")
                                              ),
                                   PopupMenuButton(
                                       items=[
                                           PopupMenuItem(text="iteam 1"),
                                           PopupMenuItem(text="iteam 2"),
                                           PopupMenuItem(text="iteam 3"),
                                           PopupMenuItem(text="iteam 4"),
                                           PopupMenuItem(text="iteam 5"),

                                       ]
                                   )
                               ]
                               ),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        elif page.route == "/about":
            page.views.append(
                View(
                '/about',
                [
                    AppBar(title=Text("About Page"), bgcolor=ft.colors.SURFACE_VARIANT,
                           leading=Icon(icons.PALETTE_SHARP),
                           leading_width=40,
                           center_title=False,
                           actions=[
                               IconButton(icons.HOME,on_click=lambda e:page.go("/")),
                               PopupMenuButton(
                                   items=[
                                       PopupMenuItem(text="iteam 1"),
                                       PopupMenuItem(text="iteam 2"),
                                       PopupMenuItem(text="iteam 3"),
                                       PopupMenuItem(text="iteam 4"),
                                       PopupMenuItem(text="iteam 5"),

                                   ]
                               )
                           ]
                           ),
                ]
            ))
        elif page.route == "/contact":
            page.views.append(
                View(
                    '/contact',
                    [
                        AppBar(title=Text("Contact Page")),
                        TextField(label="Name"),
                        TextField(label="Father"),
                        TextField(label="email"),
                        ElevatedButton("Submit",on_click=lambda e:
                                       page.go("/")
                                       )
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=FLET_APP)