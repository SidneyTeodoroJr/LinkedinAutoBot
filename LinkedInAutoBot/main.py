import warnings

# Ignorar DeprecationWarnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
import flet as ft
import webbrowser  # Importando o módulo para abrir o navegador
import subprocess
import sys

def main(page: ft.Page):
    page.title = "LinkedIn Auto Bot"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window.bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT

    # Configurações da janela
    page.window.maximizable = False
    page.window.minimizable = True

    page.window.width = 600
    page.window.height = 1050

    page.window.max_width = 600
    page.window.max_height = 1050
    
    page.window.min_width = 600
    page.window.min_height = 1050

    page.window.center()

    # Função para abrir o site
    def open_website(e):
        webbrowser.open("https://github.com/SidneyTeodoroJr/Insta-Auto-Bot")  

    # Função para fechar a janela
    def close_app(e):
        page.window.close()  # Fecha a janela e encerra a aplicação


    # Configurando o appbar com o botão "INFO" que abre o site e "CLOSE" que fecha a aplicação
    page.appbar = ft.CupertinoAppBar(
        leading=ft.IconButton(ft.icons.INFO, icon_color=ft.colors.WHITE, on_click=open_website),  # Adicionando o evento de clique para abrir o site
        bgcolor=ft.colors.TRANSPARENT,
        trailing=ft.IconButton(ft.icons.PAUSE_CIRCLE, icon_color=ft.colors.WHITE),  # Adicionando o evento de clique para fechar a aplicação
    )

    # Adicionando um container com uma imagem como background
    background = ft.Container(
        width=600,
        height=1050,
        margin=ft.margin.all(-10),
        image_src=os.path.join("LinkedInAutoBot", "img", "background.png"),
        image_fit=ft.ImageFit.COVER,
        alignment=ft.alignment.center,  # Centraliza o conteúdo dentro do container
        content=ft.Column(
            [
                ft.Text("Best engagement bot for", 
                        offset=ft.Offset(x=0, y=-2.5),
                        size=40, 
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                ),

                ft.Text("LinkedIn",
                        offset=ft.Offset(x=0, y=-2.5),
                        size=40, 
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                ),

                # ft.Image(
                #         src=os.path.join("InstaAutoBot", "img", "bot.png"),
                #         src=os.path.join("InstaAutoBot", "img", "bot.png"),
                #         width=300,
                #         height=300,
                #         fit=ft.ImageFit.CONTAIN,
                # ),

                ft.Text("Nice to meet you!",
                        color=ft.colors.WHITE,
                        offset=ft.Offset(x=0, y=0.1),
                        size=25,
                        weight=ft.FontWeight.BOLD,
                ),

                ft.Text("Log in to LinkedIn first, then click the", 
                        color=ft.colors.WHITE,
                        offset=ft.Offset(x=0, y=1),
                        size=25,
                ),

                ft.Text("button below!",
                        color=ft.colors.WHITE,
                        offset=ft.Offset(x=0, y=1),
                        size=25,
                ),

                ft.ElevatedButton("Start Automation",
                                  style=ft.ButtonStyle(
                                      text_style=ft.TextStyle(size=34, weight=ft.FontWeight.BOLD),
                                  ),
                                  offset=ft.Offset(x=0, y=1), 
                                  bgcolor=ft.colors.WHITE, 
                                  color="#37e2ab",
                                  width=450,
                                  height=80, # Adicionando o evento de clique para iniciar o bot
                )
            ],
            alignment="center",  # Centraliza os itens dentro da coluna
            horizontal_alignment="center",  # Centraliza horizontalmente
        )
    )

    # Centraliza o próprio container dentro da página
    page.add(
        ft.Container(
            content=background,
            alignment=ft.alignment.center,  # Centraliza o container de background na página
        )
    )

ft.app(main)