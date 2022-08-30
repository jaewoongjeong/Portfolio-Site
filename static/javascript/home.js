$(window).scroll(function() {
    var windscroll = $(window).scrollTop();
    if (windscroll >= 100) {
        $('section').each(function(i) {
            // The number at the end of the next line is how pany pixels you from the top you want it to activate.
            if ($(this).position().top <= windscroll - 0) {
                $('.nav-link.active').removeClass('active');
                $('.nav-link').eq(i).addClass('active');
            }
        });
    } else {
        $('.nav-link.active').removeClass('active');
        $('.nav-link:first').addClass('active');
    }
}).scroll();

function getDates(){
    var date = new Date();
    date.setDate(date.getDate() - 7);
    var dateArray = new Array();

    for(var i = 0; i <= 6; i++) {
        date.setDate(date.getDate() + 1);
        dateArray.push(date.getFullYear()+'/'+(date.getMonth()+1)+'/'+date.getDate());
    }
    return dateArray;
}

const data = {
    //labels: {{ tag_names|safe }},
    labels: tag_names,
    datasets: [{
        label: 'Tags Histogram',
        //data: {{ tag_values|safe }},
        data: tag_values,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 205, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(201, 203, 207, 0.2)'
        ],
        borderColor: [
          'rgb(255, 99, 132)',
          'rgb(255, 159, 64)',
          'rgb(255, 205, 86)',
          'rgb(75, 192, 192)',
          'rgb(54, 162, 235)',
          'rgb(153, 102, 255)',
          'rgb(201, 203, 207)'
        ],
        borderWidth: 1
    }]
};

new Chart(document.getElementById("myChart1"), {
    type: 'bar',
    data: data,
    options: {
        responsive: false,
        legend: {
            display: false
        },
        tooltips: {
            enabled: true,
            mode: 'single',
            callbacks: {
                label: function(tooltipItems, data){
                    return 'Occurences: ' + tooltipItems.yLabel;
                }
            }
        },
        scales: {
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Skills',
                    fontSize: 15,
                    fontFamily: 'times new roman',
                },
                ticks: {
                   fontSize: 15,
                   fontFamily: 'times new roman',
                },
                gridLines: {
                   color: "rgba(0,0,0,0)",
                }
            }],
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'No. of Usage',
                    fontSize: 15,
                    fontFamily: 'times new roman',
                },
               ticks: {
                   beginAtZero: true,
                   fontSize: 15,
                   fontFamily: 'times new roman',
                   userCallback: function(label, index, labels){
                       if (Math.floor(label) == label){
                           return label;
                       }
                   }
               },
                gridLines: {
                   color: "rgba(0,0,0,0)",
                }
            }],
        }
    },
});

var config_crypto = {
    type: 'line',
    data: {
        labels: getDates(),
        datasets: [{
            label: 'BitCoin',
            fill: false,
            data: [0,0,0,0,0,0,0],
            borderColor: "rgba(255, 162, 58, 1)",
            backgroundColor: 'rgba(255, 226, 172, 0.4)',
            borderWidth: 1,
        }, {
            label: 'Ethereum',
            fill: false,
            data: [0,0,0,0,0,0,0],
            borderColor: "rgba(182, 172, 255, 1)",
            backgroundColor: 'rgba(182, 172, 255, 0.3)',
            borderWidth: 1,
        },{
            label: 'Automated Trader',
            fill: false,
            data: [0,0,0,0,0,0,0],
            borderColor: "rgba(87, 169, 83, 1)",
            backgroundColor: 'rgba(87, 169, 83, 0.3)',
            borderWidth: 1,
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Upbit: 7 Days',
            fontFamily: 'times new roman',
            fontSize: 18,
        },
        scales: {
            xAxes: [{
                display: false,
                gridLines: {
                    color: "rgba(0,0,0,0)",
                },
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    stepSize: 2.5,
                    fontSize: 15,
                    fontFamily: 'times new roman',
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Profit (%)',
                    fontSize: 15,
                    fontFamily: 'times new roman',
                },

            }]
        },
        legend: {
            position: 'bottom',
            labels:{
                fontSize: 15,
                fontFamily: 'times new roman',
            },
        },
        tooltips: {
            enabled: true,
            mode: 'single',
            callbacks: {
                label: function(tooltipItems, data){
                    return data.datasets[tooltipItems.datasetIndex].label + ": " +
                        tooltipItems.yLabel.toFixed(2) + "%";
                }
            }
        }
    }
};

var chart_crypto = new Chart(document.getElementById("myChart3"), config_crypto);

// It opens the websocket via WebSocket()
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/crypto/'
    + 'details/'
);


// Adds on to the chatting box when received via websocket
chatSocket.onmessage = function(e) {
    const value = JSON.parse(e.data);

    var dataset = config_crypto.data.datasets;
    var btc = dataset[0].data;
    var eth = dataset[1].data;
    var portfolio = dataset[2].data;
    for (var j=0; j < btc.length; j++){
        btc[j] = value.message.btc[j];
        eth[j] = value.message.eth[j];
        portfolio[j] = value.message.portfolio[j];
    }

    chart_crypto.update();
    $('#update-time').text(new Date());
    $('#bitcoin').text(btc[6].toFixed(2));
    $('#ethereum').text(eth[6].toFixed(2));
    $('#automated').text(portfolio[6].toFixed(2));
};

// Shows an error if websocket connection is closed
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};