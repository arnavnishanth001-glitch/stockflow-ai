
from flask import Flask, redirect, url_for
from models import db
from controllers.db_controller import db_bp
from controllers.auth_controller import auth_bp
from controllers.main_controller import main


app = Flask(__name__)

# Secret key for Flask sessions and flash messages
app.secret_key = "inventory-store-secret-key"


# MySQL Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:Deepika%40123@127.0.0.1:3306/inventory_db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize database
db.init_app(app)


# Register blueprints
app.register_blueprint(db_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(main)


# Home page → Login page
@app.route("/")
def home():
    return redirect(url_for("auth.login"))


# Health check
@app.route("/health")
def health():
    return {
        "status": "success",
        "message": "Server is healthy"
    }


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )