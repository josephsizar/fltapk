from flet import *

def main(page):
    text = Text("Abdelalim",size=30,text_align=TextAlign.CENTER)
    spacer = Container(height=15)
    img = Image(src="img.png",size=30,text_align=TextAlign.CENTER)

    column  = Column(
        controls=[text,spacer,img],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )

    page.add(column)
    
    page.update()



app(target=main)
