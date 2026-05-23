from flask import Flask
from routes.auth_routes import auth_bp
from routes.appointment_routes import appointment_bp

app = Flask(__name__)
app.secret_key = "medtrack_secret"

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(appointment_bp)

@app.route("/")
def home():
    return "Welcome to MedTrack"

if __name__ == "__main__":
    app.run(debug=True)