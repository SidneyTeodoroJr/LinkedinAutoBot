import os
from flet import Column, Row, Container, Icons, Icon, Colors, ResponsiveRow, TextField, alignment, Offset, ImageFit, Image, ImageRepeat, padding, margin, border_radius, ElevatedButton, ButtonStyle, TextStyle, MainAxisAlignment, CupertinoSwitch, Slider

from modules.GUI_elements import CustonText


def setup_page(start_home):
    return Container(
        content=Container(
            content=Column([ 
                Container(
                    expand=True,
                    image_src=os.path.join('banner.png'),
                    image_fit=ImageFit.COVER,
                    content=ResponsiveRow([
                        Container(
                            margin=margin.only(top=100, left=10),
                            content=CustonText(valeu="Simplifique suas tarefas no LinkedIn com praticidade, automatize ações repetitivas e maximize seu engajamento. Amplie sua rede de contatos de forma estratégica, economize tempo valioso e tenha o controle completo do desempenho do bot com uma configuração fácil e intuitiva!", size=20, text_align=alignment.top_left),
                        col={"sm": 12, "md": 6, "xl": 8}),
                        Container(
                            margin=margin.only(top=30, bottom=30),
                            content=Image(os.path.join('icon.png'), repeat=ImageRepeat.NO_REPEAT, width=350, height=350),
                        col={"sm": 12, "md": 6, "xl": 4})
                    ])
                ),
                Container(
                    offset=Offset(x=0, y=-0.2),
                    content=Row(
                        expand=False,
                        wrap=False,
                        scroll="AUTO",
                        controls=[
                                Container(
                                    content=CustonText(valeu=f"Conects: {17}", size=20, weight="none"),
                                    margin=10,
                                    padding=10,
                                    alignment=alignment.top_left,
                                    bgcolor=Colors.TEAL_500,
                                    width=415,
                                    height=200,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: print("Card Conects!"),
                                ),
                                Container(
                                    content=CustonText(valeu=f"Pages: {4}", size=20, weight="none"),
                                    margin=10,
                                    padding=10,
                                    alignment=alignment.top_left,
                                    bgcolor=Colors.TEAL_700,
                                    width=415,
                                    height=200,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: print("Card Pages!"),
                                ),
                                Container(
                                    content=CustonText(valeu=f"Time: {3}", size=20, weight="none"),
                                    margin=10,
                                    padding=10,
                                    alignment=alignment.top_left,
                                    bgcolor=Colors.TEAL_300,
                                    width=415,
                                    height=200,
                                    border_radius=10,
                                    ink=True,
                                    on_click=lambda e: print("Card time!"),
                                ),
                        ]
                    )
                ),
                Container(
                    border_radius=border_radius.only(top_left=10, top_right=10),
                    margin=margin.only(left=10, right=10, bottom=0),
                    padding=padding.only(top=30),
                    bgcolor=Colors.OUTLINE_VARIANT,

                    content=Column([
                        Container(
                            content=CustonText(valeu="Configure your automation here", color=Colors.TEAL),
                        ),

                        Container(
                            margin=margin.all(10),
                            padding=padding.all(10),

                            content=ResponsiveRow([
                                TextField(
                                    label="Bot name",
                                    hint_text="Name the robot",
                                    prefix_icon=Icons.BOLT,
                                    col={"sm": 12, "md": 6, "xl": 6}
                                ),
                                TextField(
                                    label="Search",
                                    hint_text="What is the search term?",
                                    prefix_icon=Icons.SEARCH,
                                    col={"sm": 12, "md": 6, "xl": 6}
                                ),
                                
                            ])
                        ),
                        Container(
                            padding=padding.all(10),

                            content=ResponsiveRow([
                                Container(
                                    content=Column([
                                        CustonText(valeu="Time:", color=Colors.TEAL_300),
                                        Slider(
                                            min=1, 
                                            max=5, 
                                            divisions=4, 
                                            label="{value}",
                                            active_color=Colors.TEAL_300,
                                            tooltip="Adjust the time elapsed between click actions:"
                                        )
                                    ]),
                                col={"sm": 12, "md": 6, "xl": 4}),
                                Container(
                                    content=Column([
                                        CustonText(valeu="Connects:", color=Colors.TEAL_500),
                                        Slider(
                                            min=1, 
                                            max=7, 
                                            divisions=6, 
                                            label="{value}",
                                            active_color=Colors.TEAL_500,
                                            tooltip='Number of connections per page'
                                        )
                                    ]),
                                col={"sm": 12, "md": 6, "xl": 4}),
                                Container(
                                    content=Column([
                                        CustonText(valeu="Pages:", color=Colors.TEAL_700),
                                        Slider(
                                            min=1, 
                                            max=10, 
                                            divisions=9, 
                                            label="{value}",
                                            active_color=Colors.TEAL_700,
                                            tooltip='Set the number of pages to scroll through'
                                        )
                                    ]),
                                col={"sm": 12, "md": 12, "xl": 4}),
                            ])
                        ),

                        Container(
                            margin=margin.all(10),
                            padding=padding.all(10),

                            content=Row([
                                    CupertinoSwitch(
                                    label="Visible",
                                    active_color=Colors.TEAL,
                                    tooltip="Shows automation working",
                                    value=True,
                                )
                            ], alignment=MainAxisAlignment.CENTER)
                        ),
                        
                        Container(
                            margin=margin.only(top=60, bottom=60),
                            content=ElevatedButton(
                                style=ButtonStyle(text_style=TextStyle(size=20)),
                                color=Colors.TEAL,
                                width=300,
                                height=50,
                                tooltip='Clique aqui para começar a automação',
                                # disabled=True,
                                on_click=lambda e: print("Test"),
                                content=Row([
                                    CustonText('GO', color=Colors.TEAL, selectable=False), 
                                    Icon(name=Icons.PLAY_ARROW)
                                ], alignment=MainAxisAlignment.CENTER, spacing=5)
                            ),
                        ),
                    ], horizontal_alignment="center")
                )
            ],  alignment='center', horizontal_alignment='center', spacing=0)
        )
    )