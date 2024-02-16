function updateReadout(data) {
    let lastReadout = data[data.length - 1];
    let timestamp = lastReadout.timestamp;
    let temp = lastReadout.averaged_temp;
    let hum = lastReadout.humidity;

    document.querySelector('.date').innerHTML = timestamp;
    document.querySelector('.temperature').innerHTML = temp;
    document.querySelector('.humidity').innerHTML = hum;
}

updateReadout(data);