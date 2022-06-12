from werkzeug.serving import run_simple

from server.envs import PORT, URL
from server.wsgi import App


if __name__ == '__main__':
    # Run the Werkzeug development server to serve the WSGI application (App)
    app = App()
    run_simple(URL, int(PORT), app, use_debugger=True, use_reloader=True)
