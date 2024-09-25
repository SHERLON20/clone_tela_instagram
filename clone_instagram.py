import flet as ft 
def main(page:ft.Page):
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.scroll=ft.ScrollMode.AUTO
    page.bgcolor=ft.colors.BLACK
    def clicked(e):
        e.control.selected = not e.control.selected
        e.control.update()
    layout=ft.Container(
        bgcolor=ft.colors.WHITE,
        width=350,
        #height=500,
        shadow=ft.BoxShadow(blur_radius=30,color=ft.colors.BLUE_300),
        border_radius=ft.border_radius.all(10),
        content=ft.Column(
            spacing=-10,
            controls=[
                ft.ListTile(#parte de cima onde ta o nome da nasa na aplicação
                    title=ft.Text(value='NASA',color=ft.colors.BLACK,weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(value='A LUA',color=ft.colors.BLACK),
                    leading=ft.Image(src='https://th.bing.com/th/id/R.dfe000c4d39e10adeac73e968d0081c0?rik=2qecWrg5GwkLaA&riu=http%3a%2f%2fpluspng.com%2fimg-png%2fnasa-logo-png-nasa-logo-1664.png&ehk=d%2bgvuoNz%2b0udsBSxL%2bAGF0N%2f1tWoj4H6GaKOJhRCIyQ%3d&risl=&pid=ImgRaw&r=0',fit=ft.ImageFit.CONTAIN),
                    trailing=ft.Icon(name=ft.icons.MORE_HORIZ,color=ft.colors.BLACK)
                ),
                ft.Image(
                    src='https://th.bing.com/th/id/OIP.Ims8Ma3AwCTqcuyJaMYAqwHaI0?rs=1&pid=ImgDetMain',
                    fit=ft.ImageFit.COVER,
                    height=300,
                    width=350,
                    ),
                ft.Container(
                    padding=ft.padding.all(15),
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns=12,
                                controls=[
                                    ft.IconButton(
                                       col=1,
                                        icon=ft.icons.FAVORITE_BORDER,
                                        selected_icon=ft.icons.FAVORITE,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.RED,
                                        padding=ft.padding.only(right=20),
                                    ),
                                   ft.Icon(
                                       col=1,
                                       name=ft.icons.CHAT_BUBBLE_OUTLINE,
                                       color=ft.colors.BLACK
                                   ),
                                   ft.Icon(
                                       col=1,
                                       name=ft.icons.SEND,
                                       color=ft.colors.BLACK,
                                   ),
                                   ft.Container(col=8),
                                   ft.IconButton(
                                       col=1,
                                        icon=ft.icons.BOOKMARK_BORDER,
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.BLACK,
                                        ),
                                   ft.Text(
                                       spans=[
                                           ft.TextSpan(text='curtido por ',style=ft.TextStyle(color=ft.colors.BLACK,size=15)),
                                           ft.TextSpan(text='sherlon.py',style=ft.TextStyle(color=ft.colors.BLACK,size=15,weight=ft.FontWeight.BOLD)),
                                           ft.TextSpan(text=' e ',style=ft.TextStyle(color=ft.colors.BLACK,size=15)),
                                           ft.TextSpan(text='3.000 outros',style=ft.TextStyle(color=ft.colors.BLACK,size=15,weight=ft.FontWeight.BOLD)),
                                       ],offset=ft.Offset(x=0,y=-0.5)
                                   ),
                                   ft.Text(
                                       value='um pequeno passo para o homem, um grande passo para a humanidade!!! ',
                                       color=ft.colors.BLACK,
                                       size=15,
                                       offset=ft.Offset(x=0,y=-0.4)
                                   ),
                                   ft.Text(
                                       value='55 anos atrás ',
                                       color=ft.colors.GREY,
                                       size=12,
                                       offset=ft.Offset(x=0,y=-1.4)
                                   ),
                                   ft.Text(
                                       spans=[ft.TextSpan(text='elon musk ',style=ft.TextStyle(color=ft.colors.BLACK,size=15,weight=ft.FontWeight.BOLD)),
                                              ft.TextSpan(text=': agora bora para marte #spacex',style=ft.TextStyle(color=ft.colors.BLACK,size=15)),
                                              ],offset=ft.Offset(x=0,y=-1.5)
                                   ),
                                   ft.Text(
                                       value='ver todos os 5.000 comentarios',
                                       color=ft.colors.GREY,
                                       size=12,
                                       offset=ft.Offset(x=0,y=-2.5)
                                   ),
                                   ft.TextField(
                                       hint_text='adicione um comentario...',
                                       offset=ft.Offset(x=0,y=-1.0),
                                       border=ft.InputBorder.UNDERLINE
                                   )
                                ],vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            )
                        ]
                    )
                )
            ]
        )
        
    )
    page.add(layout)

if __name__=='__main__':
    ft.app(target=main)