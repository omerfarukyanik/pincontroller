function sendSliderData() {
  const slider = document.getElementById('ledRange')
  const headers = {
    'Content-Type': 'application/json',
  }
  const requestPayload = {
    slider: slider.value,
  }
  fetch('/api/slider', {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(requestPayload),
  })
    .then((response) => response.json())
    .then((data) => setAllLedParameters(data.led_state))
    .catch((error) => console.error('Error toggling LED:', error))
}

function setAllLedParameters(value) {
  const slider = document.getElementById('ledRange')
  slider.value = value
}
