from flet import (
    Page, app, ThemeMode, View, MainAxisAlignment, CrossAxisAlignment, 
    AppBar, Icons, Colors, IconButton, Icon, Container, Row, ScrollbarTheme, Theme
)
from modules.GUI_elements import CustonText
from pages.setup import setup_page
from pages.home import home_page  

def main(page: Page) -> None:
    page.title = 'LinkedIn Auto Bot'
    page.theme_mode = ThemeMode.LIGHT
    # Scrollbar
    page.theme = Theme(
        scrollbar_theme=ScrollbarTheme(thumb_color=Colors.with_opacity(0.5, Colors.TEAL))
    )
    page.window.center()
    page.update()

    def open_website(e):
        page.launch_url("https://github.com/SidneyTeodoroJr/LinkedinAutoBot")
        page.update()

    def toggle_theme(e):
        e.control.selected = not e.control.selected
        e.control.update()
        page.theme_mode = ThemeMode.DARK if page.theme_mode == ThemeMode.LIGHT else ThemeMode.LIGHT
        page.update()

    def start_setup(e):
        page.go("/setup")

    def start_home(e):
        page.go("/")

    def route_change(e) -> None:
        
        page.views.clear()

        if page.route == "/":
            page.views.append(
                View(
                    route="/",
                    padding=0,
                    bgcolor=Colors.TEAL_900,
                    controls=[
                        home_page(
                            open_website=open_website, 
                            toggle_theme=toggle_theme, 
                            start_setup=start_setup
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    scroll="AUTO"
                )
            )
        elif page.route == "/setup":
            page.views.append(
                View(
                    route="/setup", 
                    appbar=AppBar(
                        leading=IconButton(
                            icon=Icons.ARROW_BACK_IOS,
                            on_click=start_home,
                            icon_color=Colors.WHITE,
                            tooltip="Back to home"
                        ),
                        leading_width=50,
                        title=Container(content=Row([CustonText(valeu="Bot Setup"), Icon(name=Icons.SETTINGS, color=Colors.WHITE)], alignment='CENTER')),
                        bgcolor=Colors.TEAL_900,
                    ),
                    padding=0,
                    controls=[
                        setup_page(
                            start_home=start_home
                        )
                    ],
                    scroll="AUTO"
                )
            )
        page.update()

    def view_pop(e, ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    app(target=main)