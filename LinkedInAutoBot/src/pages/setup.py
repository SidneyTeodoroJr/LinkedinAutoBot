import os
from flet import (
    ButtonStyle, TextStyle, MainAxisAlignment, Column, Row,  
    Icons, Icon, Colors, ResponsiveRow, alignment, Container,
    Offset, ImageFit, Image, ImageRepeat, padding, margin, border_radius, ElevatedButton
)
from modules.GUI_elements import (
    CustonText, CustonCard,
    bot_name, InputSearch, time_slider, connects_slider, pages_slider,
)
from back import AutoBot
    

def setup_page(start_home):
    return Container(
        content=Container(
            content=Column([ 
                # Banner
                Container(
                    expand=True,
                    image_src=os.path.join('banner.png'),
                    image_fit=ImageFit.COVER,
                    content=ResponsiveRow([
                        Container(
                            margin=margin.only(top=100, left=10),
                            content=CustonText(valeu="Simplify your LinkedIn tasks with ease, automate repetitive actions and maximize your engagement. Strategically expand your network, save valuable time and have complete control over your bot's performance with an easy and intuitive setup!", size=20, text_align=alignment.top_left),
                            col={"sm": 12, "md": 6, "xl": 8}),
                        Container(
                            margin=margin.only(top=30, bottom=30),
                            content=Image(os.path.join('icon.png'), repeat=ImageRepeat.NO_REPEAT, width=350, height=350),
                            col={"sm": 12, "md": 6, "xl": 4})
                    ])
                ),
                # Cards
                Container(
                    offset=Offset(x=0, y=-0.2),
                    content=Row(
                        expand=False,
                        wrap=False,
                        scroll="AUTO",
                        controls=[
                            # Card connect
                            connects_card:=CustonCard(
                                bgcolor=Colors.TEAL_500,
                                content=CustonText(valeu=f"Connects: {int(connects_slider.value)}")
                            ),
                            # Card Pages
                            pages_card:=CustonCard(
                                bgcolor=Colors.TEAL_700,
                                content=CustonText(valeu=f"Pages: {int(pages_slider.value)}")
                            ),
                            # Card Time
                            time_card:=CustonCard(
                                bgcolor=Colors.TEAL_300,
                                content=CustonText(valeu=f"Time: {int(time_slider.value)}")
                            )
                        ]
                    )
                ),
                #Set up automation
                Container(
                    border_radius=border_radius.only(top_left=10, top_right=10),
                    margin=margin.only(left=10, right=10, bottom=0),
                    padding=padding.only(top=30),
                    bgcolor=Colors.OUTLINE_VARIANT,

                    content=Column([
                        CustonText(valeu="Set up your automation here", color=Colors.TEAL),

                        # Inputs
                        Container(
                            margin=margin.all(10),
                            padding=padding.all(10),
                            content=ResponsiveRow([
                                bot_name,
                                InputSearch
                            ])
                        ),
                        # Controls slider
                        Container(
                            padding=padding.all(10),
                            content=ResponsiveRow([
                                Container(
                                    content=Column([
                                        CustonText(valeu="Time:", color=Colors.TEAL_300),
                                        time_slider
                                    ]),
                                    col={"sm": 12, "md": 6, "xl": 4}),
                                Container(
                                    content=Column([
                                        CustonText(valeu="Connects:", color=Colors.TEAL_500),
                                        connects_slider
                                    ]),
                                    col={"sm": 12, "md": 6, "xl": 4}),
                                Container(
                                    content=Column([
                                        CustonText(valeu="Pages:", color=Colors.TEAL_700),
                                        pages_slider
                                    ]),
                                    col={"sm": 12, "md": 12, "xl": 4}),
                            ])
                        ),
                        # Button start robot
                        Container(
                            margin=margin.only(top=60, bottom=60),
                            content=ElevatedButton(
                                style=ButtonStyle(text_style=TextStyle(size=20)),
                                color=Colors.TEAL,
                                width=300,
                                height=50,
                                tooltip='Click here to start automation',
                                disabled=False,
                                on_click=AutoBot,
                                content=Row([
                                    CustonText('GO', color=Colors.TEAL, selectable=False), 
                                    Icon(name=Icons.PLAY_ARROW)
                                ], alignment=MainAxisAlignment.CENTER, spacing=5)
                            )
                        )
                    ], horizontal_alignment="center")
                )
            ], alignment='center', horizontal_alignment='center', spacing=0)
        )
    )