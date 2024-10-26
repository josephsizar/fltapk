import flet as ft

def main(page):
    text = ft.Text("Abdelalim",size=30,text_align=ft.TextAlign.CENTER)
    spacer = ft.Container(height=15)
    img = ft.Image(src="img.png",width=150,height=150)

    column  = ft.Column(
        controls=[text,spacer,img],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(column)



ft.app(target=main)
