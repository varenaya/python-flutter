import flet
from flet import Page, Row, IconButton , icons, TextField

def main(page:Page):
    page.title = "Counter App"
    page.vertical_alignment = "center"

    text_field = TextField(value="0",width=100,text_align="center")

    def plus(button):
        text_field.value = str(int(text_field.value) + 1)
        page.update()
    
    def minus(button):
        text_field.value = str(int(text_field.value) - 1)
        page.update()

    page.add(
        Row([
        IconButton(icon=icons.ADD, on_click=plus),
        text_field,
        IconButton(icon=icons.REMOVE, on_click=minus),
        ],alignment = "center")
    )

flet.app(target=main, view=flet.WEB_BROWSER)
