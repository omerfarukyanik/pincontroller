from flask import Flask, render_template, request
from gpiozero import LEDBoard

app = Flask(__name__)

led_board = LEDBoard(5, 6, 13, 19, 26, pwm=True)


# Web server route to control the LED
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# REST API endpoint to toggle the LED
@app.route("/api/slider", methods=["POST"])
def toggle_led():
    data = request.get_json()
    slider_value = int(data["slider"])
    open_leds_for_slider(slider_value)
    return {"status": "success", "led_state": slider_value}


def open_all_leds():
    led_board.on()


def close_all_leds():
    led_board.close()


def open_leds_for_slider(value):
    if value > 5:
        value = 5
    elif value < 0:
        value = 0

    _new_led_values_array = [1] * value
    _new_led_values_array.extend([0] * (5 - value))

    if value == 5:
        led_board.value = (1, 1, 1, 1, 1)
    elif value == 4:
        led_board.value = (1, 1, 1, 1, 0)
    led_board.value = tuple(_new_led_values_array)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
