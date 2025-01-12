import os
from flet import ImageFit, Column, Image, ImageRepeat, ElevatedButton, ButtonStyle, TextStyle, Colors, LinearGradient, alignment
from modules.GUI_elements import *

def home_page(open_website, toggle_theme, start_setup):
    return Container(
        content=Container(
            border_radius=16,
            content=Column([
                CustonAppBar(open_website=open_website, toggle_theme=toggle_theme),
                Container(content=Column([CustonText(valeu='Best engagement bot for LinkedIn', size=35)], horizontal_alignment='center')),
                Container(expand=True),

                Container(margin=margin.only(top=50), content=Image(os.path.join('icon.png'), repeat=ImageRepeat.NO_REPEAT, width=350, height=350)),

                Container(content=Column([
                    CustonText(valeu='Nice to meet you!'),
                    CustonText(valeu='Log in to LinkedIn first, then click the button below!')
                ], horizontal_alignment='center', spacing=50)),
                
                Container(
                    margin=margin.only(top=60, bottom=10, left=10, right=10),
                    content=ElevatedButton(
                        'Start Setup',
                        style=ButtonStyle(text_style=TextStyle(size=25, weight=FontWeight.BOLD)),
                        color=Colors.TEAL,
                        width=400,
                        height=60,
                        on_click=start_setup
                    ),
                ),
            ], alignment='center', horizontal_alignment='center'),
        )
    )