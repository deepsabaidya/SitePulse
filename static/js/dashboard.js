
document.addEventListener("DOMContentLoaded", function () {

    // Update uptime progress bars
    const uptimeBars = document.querySelectorAll(".uptime-bar");

    uptimeBars.forEach(function (bar) {

        const uptime = Number(bar.dataset.uptime);

        const safeUptime = Math.max(0, Math.min(100, uptime));

        bar.style.width = safeUptime + "%";

    });


    // Find all response-time charts
    const charts = document.querySelectorAll("canvas[data-records]");

    charts.forEach(function (canvas) {

        let records;

        // Read monitoring data
        try {

            records = JSON.parse(canvas.dataset.records);

        } catch (error) {

            console.error("Unable to read chart data:", error);

            return;

        }

        if (!records || records.length === 0) {
            return;
        }


        // Prepare chart labels
        const labels = records.map(function (record) {

            return record.checked_at.substring(11, 19);

        });


        // Prepare response-time values
        const responseTimes = records.map(function (record) {

            return record.response_time_ms;

        });


        // Create response-time chart
        new Chart(canvas, {

            type: "line",

            data: {

                labels: labels,

                datasets: [{

                    label: "Response Time (ms)",

                    data: responseTimes,

                    borderColor: "#0d6efd",

                    backgroundColor: "rgba(13, 110, 253, 0.1)",

                    borderWidth: 2,

                    pointRadius: 4,

                    tension: 0.3,

                    fill: true

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                scales: {

                    y: {

                        beginAtZero: true,

                        title: {

                            display: true,

                            text: "Milliseconds"

                        }

                    },

                    x: {

                        title: {

                            display: true,

                            text: "Check Time"

                        }

                    }

                }

            }

        });

    });

});
