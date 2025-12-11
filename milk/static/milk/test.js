var watchId = 0;

function forceRedraw(element) {
    var disp = element.style.display;
    element.style.display = 'none';
    var trick = element.offsetHeight; // Forces reflow
    element.style.display = disp;
}   

function supportsGeolocation() {
    return 'geolocation' in navigator;
}

function showMessage(message) {
  var container = document.getElementById('homie');
  var newDiv = document.createElement('div');
  newDiv.innerHTML = message;
  container.appendChild(newDiv);   
}

function getLocation() {
    if (supportsGeolocation()) {
        var options = { enableHighAccuracy: true };
        watchId = navigator.geolocation.watchPosition(showPosition, showError, options);
    } else {
        showMessage("Geolocation isn't supported by your browser");
    }
}

function endWatch() {
    if (watchId != 0) {
        navigator.geolocation.clearWatch(watchId);
        watchId = 0;
        showMessage("Monitoring ended.");
    }
}

function showPosition(position) {
    var datetime = new Date(position.timestamp).toTimeString();
    showMessage('Latitude: ' + position.coords.latitude + '<br>' +
        'Longitude: ' + position.coords.longitude + '<br>' +
        'Altitude: ' + position.coords.altitude + '<br>' +
        'Accuracy: ' + position.coords.accuracy + '<br>' +
        'Timestamp: ' + datetime.slice(0,8));
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            showMessage("User denied Geolocation access request.");
            break;
        case error.POSITION_UNAVAILABLE:
            showMessage("Location Information unavailable.");
            break;
        case error.TIMEOUT:
            showMessage("Get user location request timed out.");
            break;
        case error.UNKNOWN_ERROR:
            showMessage("An unknown error occurred.");
            break;
    }
}
