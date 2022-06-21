from flask import Flask
from google.cloud import storage
def create_app():
    storage_client = storage.Client()
    bucket_name = "testborsuk"
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        bucket = storage_client.get_bucket(bucket_name)
        return f'Hello, World!'
    return app
app = create_app()

