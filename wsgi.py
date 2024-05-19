from app import app  # Replace with your actual file name

def application(environ, start_response):
    return app(environ, start_response)

# You can add additional configurations here if needed (e.g., workers, logging)