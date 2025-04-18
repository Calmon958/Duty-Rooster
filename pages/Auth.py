from nicegui import ui
from database.crud import create_user, authenticate_user

def loginPage(navigate):
    ui.label('Login').classes('text-2xl fold-bold')
    name = ui,label('Name').classes('w-full')