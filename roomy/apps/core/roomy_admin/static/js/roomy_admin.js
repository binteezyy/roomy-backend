// SideNav Button Initialization
$(".button-collapse").sideNav({
    breakpoint: 1290
});
// SideNav Scrollbar Initialization
var sideNavScrollbar = document.querySelector('.custom-scrollbar');
var ps = new PerfectScrollbar(sideNavScrollbar);

// Chart customizer
(function (global) {

    var Samples = global.Samples || (global.Samples = {});
    var Color = global.Color;

    Samples.utils = {
        // Adapted from http://indiegamr.com/generate-repeatable-random-numbers-in-js/
        srand: function (seed) {
            this._seed = seed;
        },

        rand: function (min, max) {
            var seed = this._seed;
            min = min === undefined ? 0 : min;
            max = max === undefined ? 1 : max;
            this._seed = (seed * 9301 + 49297) % 233280;
            return min + (this._seed / 233280) * (max - min);
        },

        numbers: function (config) {
            var cfg = config || {};
            var min = cfg.min || 0;
            var max = cfg.max || 1;
            var from = cfg.from || [];
            var count = cfg.count || 8;
            var decimals = cfg.decimals || 8;
            var continuity = cfg.continuity || 1;
            var dfactor = Math.pow(10, decimals) || 0;
            var data = [];
            var i, value;

            for (i = 0; i < count; ++i) {
                value = (from[i] || 0) + this.rand(min, max);
                if (this.rand() <= continuity) {
                    data.push(Math.round(dfactor * value) / dfactor);
                } else {
                    data.push(null);
                }
            }

            return data;
        },

        labels: function (config) {
            var cfg = config || {};
            var min = cfg.min || 0;
            var max = cfg.max || 100;
            var count = cfg.count || 8;
            var step = (max - min) / count;
            var decimals = cfg.decimals || 8;
            var dfactor = Math.pow(10, decimals) || 0;
            var prefix = cfg.prefix || '';
            var values = [];
            var i;

            for (i = min; i < max; i += step) {
                values.push(prefix + Math.round(dfactor * i) / dfactor);
            }

            return values;
        },

        months: function (config) {
            var cfg = config || {};
            var count = cfg.count || 12;
            var section = cfg.section;
            var values = [];
            var i, value;

            for (i = 0; i < count; ++i) {
                value = MONTHS[Math.ceil(i) % 12];
                values.push(value.substring(0, section));
            }

            return values;
        },

        color: function (index) {
            return COLORS[index % COLORS.length];
        },

        transparentize: function (color, opacity) {
            var alpha = opacity === undefined ? 0.5 : 1 - opacity;
            return Color(color).alpha(alpha).rgbString();
        }
    };

    // DEPRECATED
    window.randomScalingFactor = function () {
        return Math.round(Samples.utils.rand(40, 120));
    };

    // INITIALIZATION

    Samples.utils.srand(Date.now());

    // Google Analytics
    /* eslint-disable */
    if (document.location.hostname.match(/^(www\.)?chartjs\.org$/)) {
        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r;
            i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date();
            a = s.createElement(o),
                m = s.getElementsByTagName(o)[0];
            a.async = 1;
            a.src = g;
            m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');
        ga('create', 'UA-28909194-3', 'auto');
        ga('send', 'pageview');
    }
    /* eslint-enable */

}(this));

// Line chart
var ctxL = document.getElementById("lineChart").getContext('2d');
var gradientFill = ctxL.createLinearGradient(0, 0, 0, 250);
gradientFill.addColorStop(0, "rgba(29, 140, 248, 1)");
gradientFill.addColorStop(1, "rgba(29, 140, 248, 0.1)");

var config = {
    type: 'line',
    data: {
        labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
        datasets: [{
            data: [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100],
            backgroundColor: gradientFill,
            borderColor: [
                '#1d8cf8',
            ],
            borderWidth: 2,
            pointBackgroundColor: "#1d8cf8",
        }]
    },
    options: {
        responsive: true,
        legend: {
            display: false,
        },
        title: {
            display: true,
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                },
                ticks: {
                    fontColor: 'rgba(255, 255, 255, .5)'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                },
                ticks: {
                    min: 40,
                    max: 120,
                    padding: 0,
                    fontColor: 'rgba(255, 255, 255, .5)'
                },
                gridLines: {
                    display: false,
                }
            }]
        }
    }
};

window.onload = function () {
    var ctxL = document.getElementById("lineChart").getContext('2d');
    window.myLine = new Chart(ctxL, config);
};

document.getElementById('accountsData').addEventListener('click', function () {
    config.data.datasets.forEach(function (dataset) {
        dataset.data = dataset.data.map(function () {
            return randomScalingFactor();
        });

    });

    window.myLine.update();
});

document.getElementById('purchasesData').addEventListener('click', function () {
    config.data.datasets.forEach(function (dataset) {
        dataset.data = dataset.data.map(function () {
            return randomScalingFactor();
        });

    });

    window.myLine.update();
});

document.getElementById('sessionsData').addEventListener('click', function () {
    config.data.datasets.forEach(function (dataset) {
        dataset.data = dataset.data.map(function () {
            return randomScalingFactor();
        });

    });

    window.myLine.update();
});

var ctxY = document.getElementById("horizontalBar").getContext('2d');
var myLineChart = new Chart(ctxY, {
    type: "horizontalBar",
    data: {
        labels: ["JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
        datasets: [{
            data: [105, 95, 85, 100, 115, 125],
            fill: false,
            borderColor: ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)",
                "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"
            ],
            borderWidth: 2
        }]
    },
    options: {
        legend: {
            display: false,
        },
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: false,
                    min: 50,
                    max: 130,
                    padding: 0,
                    fontColor: 'rgba(255, 255, 255, .5)'
                }
            }],
            yAxes: [{
                display: true,
                ticks: {
                    fontColor: 'rgba(255, 255, 255, .5)'
                },
            }]
        }
    }
});

// Line
var ctxY = document.getElementById("lineChartSecond").getContext('2d');
var gradientFill = ctxY.createLinearGradient(0, 0, 0, 250);
gradientFill.addColorStop(0, "rgba(29, 140, 248, 1)");
gradientFill.addColorStop(1, "rgba(29, 140, 248, 0.1)");
var myLineChart = new Chart(ctxY, {
    type: 'line',
    data: {
        labels: ["JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
        datasets: [{
            label: "My Second dataset",
            data: [80, 100, 70, 80, 120, 80],
            backgroundColor: gradientFill,
            borderColor: [
                '#1d8cf8',
            ],
            borderWidth: 2,
            pointBackgroundColor: "#1d8cf8",
        }]
    },
    options: {
        legend: {
            display: false,
        },
        scales: {
            xAxes: [{
                ticks: {
                    fontColor: 'rgba(255, 255, 255, .5)'
                }
            }],
            yAxes: [{
                display: true,
                ticks: {
                    min: 60,
                    max: 130,
                    padding: 0,
                    fontColor: 'rgba(255, 255, 255, .5)'
                },
                gridLines: {
                    display: false,
                }
            }]
        }
    }
});

// Bar
var ctxB = document.getElementById("barChart").getContext('2d');
var myBarChart = new Chart(ctxB, {
    type: 'bar',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            data: [12, 19, 3, 5, 2, 3],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        legend: {
            display: false,
        },
        scales: {
            xAxes: [{
                ticks: {
                    fontColor: 'rgba(255, 255, 255, .5)'
                }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    fontColor: 'rgba(255, 255, 255, .5)'
                }
            }]
        }
    }
});
