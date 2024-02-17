const temperatureChart = document.getElementById('temperature');

var data = data_12h
var chartLabels
var temperature
var humidity
var temperatureHumidityData
var temperatureChartConfig

function initDatasets() {
    chartLabels = []
    temperature = []
    humidity = []
    temperatureHumidityData = {}
    temperatureChartConfig = {}
    chartLabels = data.map(function(e) {
       return e.timestamp;
    });
    temperature = data.map(function(e) {
       return e.averaged_temp;
    });
    humidity = data.map(function(e) {
       return e.humidity;
    });

    temperatureHumidityData = {
      labels: chartLabels,
      datasets: [
        {
          label: 'Temperatura [°C]',
          data: temperature,
          yAxisID: 'y',
        },
        {
          label: 'Wilgotność powietrza [%]',
          data: humidity,
          yAxisID: 'y1',
        }
      ]
    };

    temperatureChartConfig = {
      type: 'line',
      data: temperatureHumidityData,
      options: {
        responsive: true,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        stacked: false,
        plugins: {
          title: {
            display: true,
            text: 'Warunki w pokoju'
          }
        },
        scales: {
          y: {
            type: 'linear',
            display: true,
            text: 'Temperatura [°C]',
            position: 'left',
            grace: '25%',
            border: {
                color: 'blue'
             }
          },
          y1: {
            type: 'linear',
            display: true,
            text: 'Wilgotność powietrza [%]',
            position: 'right',
            grace: '25%',
            // grid line settings
            grid: {
              drawOnChartArea: false, // only want the grid lines for one axis to show up
            },
            border: {
                color: 'red'
             }
          },
        },
      },
    }

}
initDatasets()

var tempHumChart = new Chart(temperatureChart, temperatureChartConfig);

function changeDataset(clickedButton) {
    switch (clickedButton.id) {
        case "12h":
            data = data_12h;
            break;
        case "24h":
            data = data_24h;
            break;
        case "7d":
            data = data_7d;
            break;
        default:
            // Handle unexpected cases
            break;
    }

    var buttons = document.getElementsByClassName("data-selector");

    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove("btn-primary");
        buttons[i].classList.add("btn-secondary");
    }

    clickedButton.classList.remove("btn-secondary");
    clickedButton.classList.add("btn-primary");
    temperatureHumidityData.datasets[0].data = data.map(function(e) { return e.averaged_temp; });
    temperatureHumidityData.datasets[1].data = data.map(function(e) { return e.humidity; });
    temperatureHumidityData.labels = data.map(function(e) { return e.timestamp; });
    tempHumChart.update()
}

