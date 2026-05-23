from flask import Blueprint, render_template, request
from services.sns_service import send_notification

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/book", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        doctor = request.form["doctor"]
        date = request.form["date"]

        message = f"Appointment booked with {doctor} on {date}"
        send_notification(message)

        return "Appointment Booked Successfully"

    return render_template("book_appointment.html")
