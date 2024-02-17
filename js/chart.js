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

new Chart(temperatureChart, temperatureChartConfig);




