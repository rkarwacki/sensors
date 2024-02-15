const temperatureChart = document.getElementById('temperature');

var chartLabels = data.map(function(e) {
   return e.timestamp;
});
var temperature = data.map(function(e) {
   return e.averaged_temp;
});
var humidity = data.map(function(e) {
   return e.humidity;
});
var pressure = data.map(function(e) {
   return e.pressure;
});

const temperatureHumidityData = {
  labels: chartLabels   ,
  datasets: [
    {
      label: 'Temperature',
      data: temperature,
      yAxisID: 'y',
    },
    {
      label: 'Humidity',
      data: humidity,
      yAxisID: 'y1',
    }
  ]
};

const temperatureChartConfig = {
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
        text: 'Chart.js Line Chart - Multi Axis'
      }
    },
    scales: {
      y: {
        type: 'linear',
        display: true,
        position: 'left',
      },
      y1: {
        type: 'linear',
        display: true,
        position: 'right',

        // grid line settings
        grid: {
          drawOnChartArea: false, // only want the grid lines for one axis to show up
        },
      },
    },
    plugins: {
        decimation: {
            enabled: true,
            algorithm: 'lttb',
            samples: 50
        }
    }
  },
}

new Chart(temperatureChart, temperatureChartConfig);




