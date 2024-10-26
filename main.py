import flet as *

def main(page):
    text = Text("Abdelalim",size=30,text_align=TextAlign.CENTER)
    spacer = Container(height=15)
    img = Image(src="img.png",width=150,height=150)

    column  = Column(
        controls=[text,spacer,img],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )

    page.add(column)
    
    page.update()



app(target=main)
