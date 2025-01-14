from flet import (
    Colors, IconButton, Icons, Container, margin, CupertinoSwitch, TextField,
    FontWeight, Row, TextAlign, UserControl, alignment, Slider, Text,
)

class CustonAppBar(UserControl):
    def __init__(self, open_website, toggle_theme):
        super().__init__()
        self.open_website = open_website
        self.toggle_theme = toggle_theme

    def build(self):
        return Container(
            height=50,
            bgcolor=Colors.TRANSPARENT,
            margin=margin.only(left=30, right=30),
            content=Row([
                IconButton(
                    icon=Icons.INFO,
                    icon_color=Colors.SURFACE,
                    icon_size=35,
                    on_click=self.open_website, 
                    tooltip='Information'
                ),
                IconButton(
                    icon=Icons.LIGHT_MODE,
                    selected_icon=Icons.DARK_MODE,
                    icon_color=Colors.SURFACE,
                    selected_icon_color=Colors.SURFACE,
                    icon_size=35,
                    on_click=self.toggle_theme,
                    tooltip='Theme Mode'
                ),
            ], alignment="spaceBetween"),
        )

class CustonCard(UserControl):
    def __init__(self, content, bgcolor):
        super().__init__()
        self.content = content
        self.bgcolor = bgcolor

    def build(self):
        return Container(
            margin=10,
            padding=10,
            alignment=alignment.top_left,
            bgcolor=self.bgcolor,
            width=415,
            height=200,
            border_radius=10,
            content=self.content
        )
    
class CustonSwitch(UserControl):
    def __init__(self, label=str, active_color=Colors.TEAL, tooltip=str, valeu=True):
        super().__init__()
        self.label = label
        self.active_color = active_color
        self.tooltip = tooltip
        self.value = valeu

    def build(self):
        return CupertinoSwitch(
            label=self.label,
            active_color=self.active_color,
            tooltip=self.tooltip,
            value=self.value
        )
    
class CustonText(UserControl):
    def __init__(self, valeu=str, color=Colors.WHITE, weight=FontWeight.BOLD, text_align=TextAlign.CENTER, size=25, selectable=True):
        super().__init__()

        self.value = valeu
        self.color = color
        self.weight = weight
        self.text_align = text_align
        self.size = size
        self.selectable = selectable

    def build(self):
        return Text(
            value=self.value,
            color=self.color,
            weight=self.weight,
            text_align=self.text_align,
            size=self.size,
            selectable=self.selectable
        )

bot_name = TextField(
    label="Bot name",
    hint_text="Name the robot",
    prefix_icon=Icons.BOLT,
    col={"sm": 12, "md": 6, "xl": 6}
)

InputSearch = TextField(
    label="Search",
    hint_text="What is the search term?",
    prefix_icon=Icons.SEARCH,
    col={"sm": 12, "md": 6, "xl": 6}
)

time_slider = Slider(
    min=1, 
    max=15, 
    divisions=14, 
    label="{value}",
    active_color=Colors.TEAL_300,
    tooltip='Adjust the time between clicks according to your internet connection'
)

connects_slider = Slider(
    min=1, 
    max=7, 
    divisions=6, 
    label="{value}",
    active_color=Colors.TEAL_500,
    tooltip='Number of connections per page'
)

pages_slider = Slider(
    min=1, 
    max=10, 
    divisions=9, 
    label="{value}",
    active_color=Colors.TEAL_700,
    tooltip='Set the number of pages the bot will browse'
)