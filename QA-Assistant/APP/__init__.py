from flask import Flask
from .route import doc_bp

def create_flask_app():
    
    app=Flask(__name__)
    app.register_blueprint(doc_bp, url_prefix='/sql')
    
    return app

if __name__=="__main__":
    create_flask_app()