function getPosition() {
  // Simple wrapper
  return new Promise((res, rej) => {
    navigator.geolocation.getCurrentPosition(res, rej);
  });
}

async function main() {
  var position = await getPosition();  // wait for getPosition to complete
  const el = document.getElementById("front");
  let { accuracy, altitude, latitude, longitude } = position.coords;
  console.log(position);
  el.textContent = `
  Latitude: ${latitude}
  Longitude: ${longitude}
  Accuracy: ${accuracy}
  Altitude: ${altitude}
  `
}
