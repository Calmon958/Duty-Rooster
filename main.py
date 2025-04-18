from nicegui import ui, app
# from database.db import init_db
from pages.auth import login_page, register_page
from pages.user_dashboard import user_dashboard
from pages.client_dashboard import client_dashboard
from pages.admin_dashboard import admin_dashboard
from pages.settings import settings_page
from components.navbar import navbar
# from components.messages import message_system

# Initialize database
# init_db()

# Navigation logic
def navigate(page):
    ui.clear()
    navbar(navigate)
    if page == 'login':
        login_page(navigate)
    elif page == 'register':
        register_page(navigate)
    elif page == 'user_dashboard':
        user_dashboard()
    elif page == 'client_dashboard':
        client_dashboard()
    elif page == 'admin_dashboard':
        admin_dashboard()
    elif page == 'settings':
        settings_page()
    elif page == 'messages':
        message_system()

# Start app on login page
navigate('login')

# Run NiceGUI app
ui.run(title="NiceGUI App", port=8080, dark=True)
