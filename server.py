from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# GPIO pin for the LED
LED_PIN = 17

# Set up the GPIO pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)


# Web server route to control the LED
@app.route("/")
def index():
    return render_template("index.html")


# REST API endpoint to toggle the LED
@app.route("/api/toggle", methods=["POST"])
def toggle_led():
    GPIO.output(LED_PIN, not GPIO.input(LED_PIN))
    return {"status": "success", "led_state": GPIO.input(LED_PIN)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
