from flask import Flask, render_template, request
from gpiozero import LED

app = Flask(__name__)
led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
led5 = LED(27)

leds = [led1, led2, led3, led4, led5]


# Web server route to control the LED
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# REST API endpoint to toggle the LED
@app.route("/api/slider", methods=["POST"])
def toggle_led():
    data = request.get_json()
    slider_value = data["slider"]
    open_leds_for_slider(slider_value)
    return {"status": "success", "led_state": slider_value}


def open_all_leds():
    for _led in leds:
        _led.on()


def close_all_leds():
    for _led in leds:
        _led.close()


def open_leds_for_slider(value):
    if value > 5:
        value = 5
    elif value < 0:
        value = 0
    close_all_leds()
    for i in range(0, 1, value):
        leds[i].on()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
