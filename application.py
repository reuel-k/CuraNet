import sys
import os

# Add the 'backend' directory to the Python path
# This ensures that modules inside 'backend' can be imported correctly
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

try:
    # Import the FastAPI app instance from backend.main
    from main import app as application
except ImportError as e:
    # If the import fails, create a simple fallback app that shows the error
    # This helps in debugging deployment issues
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        message = f"Failed to import FastAPI app. Error: {e}".encode('utf-8')
        start_response(status, headers)
        return [message]

