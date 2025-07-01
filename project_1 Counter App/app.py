import flet as ft


def main(page: ft.Page):
  
  # Page settings 
    page.title = 'PytronLAB'
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    counter_title = ft.Text("Counter WebApp by Python",weight="Bold", size=40, color='black')
    counter = ft.Text(value="0", size=20, color='black', weight='Bold')
    
  # Feture functions 
    def increase(e):
        counter.value = str(int(counter.value) + 1)
        counter.update()

    def decrease(e):
        counter.value = str(int(counter.value) - 1)
        
        
        counter.update()

    def reset(e):
        counter.value = "0"
        counter.update()

    def toggle_dark_mode(e):
        if swt.value:
            page.bgcolor = "#222222"
            counter_title.color = "white"
            counter.color = "white"
        else:
            page.bgcolor = "#FFFFFF"
            counter_title.color = "black"
            counter.color = "black"
        counter_title.update()
        counter.update()
        page.update()
        
  # Buttons
    increase_btn = ft.ElevatedButton("+", on_click=increase)
    decrease_btn = ft.ElevatedButton("-", on_click=decrease)
    reset_btn = ft.ElevatedButton("Reset", on_click=reset)
    swt = ft.Switch(label='Dark Mode', on_change=toggle_dark_mode, label_style=ft.TextStyle(color=ft.Colors.BLACK, weight="Bold"))

  # Layout
    page.add(
        counter_title,
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row([swt], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([decrease_btn, counter, increase_btn],
                           alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([reset_btn], alignment=ft.MainAxisAlignment.CENTER)
                ],
            
            ),
            bgcolor="#23ff7f",
            margin=20,
            padding=20,
            border_radius=20,
            width=500
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)
