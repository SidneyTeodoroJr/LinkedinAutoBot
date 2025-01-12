from flet import Colors, IconButton, Icons, Container, margin, Text, FontWeight, Row, TextAlign, UserControl, margin

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
    
class CustonText(UserControl):
    def __init__(self, valeu='Start Automation', color=Colors.WHITE, weight=FontWeight.BOLD, text_align=TextAlign.CENTER, size=25, selectable=True):
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