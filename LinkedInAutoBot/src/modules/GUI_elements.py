from flet import (
    Colors, IconButton, Icons, Container, margin, CupertinoSwitch,
    FontWeight, Row, TextAlign, UserControl, margin, alignment,  Slider, Text,
)

class CustonAppBar(UserControl):
    def __init__(self, open_website, toggle_theme):
        super().__init__()
        self.open_website=open_website
        self.toggle_theme=toggle_theme

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
        self.content=content
        self.bgcolor=bgcolor

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
    
class CustonSlider(UserControl):
    def __init__(self, min=int, max=int, divisions=int, label=str, active_color=Colors.OUTLINE, tooltip=str):
        super().__init__()
        self.min=min
        self.max=max
        self.divisions=divisions
        self.label=label
        self.active_color=active_color
        self.tooltip=tooltip
    
    def build(self):
        return Slider(
            min=self.min,
            max=self.max,
            divisions=self.divisions,
            label=self.label,
            active_color=self.active_color,
            tooltip=self.tooltip
        )
    
class CustonSwitch(UserControl):
    def __init__(self, label=str, active_color=Colors.TEAL, tooltip=str, valeu=True,):
        super().__init__()
        self.label=label
        self.active_color=active_color
        self.tooltip=tooltip
        self.value=valeu

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

        self.value=valeu
        self.color=color
        self.weight=weight
        self.text_align=text_align
        self.size=size
        self.selectable=selectable

    def build(self):
        return Text(
            value=self.value,
            color=self.color,
            weight=self.weight,
            text_align=self.text_align,
            size=self.size,
            selectable=self.selectable
        )