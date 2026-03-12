const API = "http://127.0.0.1:8000"

async function loadDashboard() {

    const issues = await fetch(`${API}/issues`).then(r => r.json())
    const trends = await fetch(`${API}/trends`).then(r => r.json())

    document.getElementById("totalTickets").innerText =
        issues.reduce((a, b) => a + b.mentions, 0)

    document.getElementById("totalClusters").innerText = issues.length

    document.getElementById("emergingIssues").innerText =
        trends.filter(t => t.trend == "Increasing").length

    createTrendChart(issues)
    createClusterChart(issues)

    renderClusters(issues, trends)

}


function createTrendChart(issues) {

    const labels = issues.map(i => `Cluster ${i.cluster}`)
    const data = issues.map(i => i.mentions)

    new Chart(document.getElementById("trendChart"), {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Ticket Mentions",
                data: data,
                backgroundColor: "#4e79a7",
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: "#eeeeee"
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    })

}


function createClusterChart(issues){

const labels = issues.map(i => i.issue)
const data = issues.map(i => i.mentions)

const colors = [
"#4e79a7",
"#f28e2c",
"#e15759",
"#76b7b2",
"#59a14f",
"#edc948",
"#b07aa1",
"#ff9da7",
"#9c755f",
"#bab0ab"
]

new Chart(document.getElementById("clusterChart"),{
type:"pie",
data:{
labels:labels,
datasets:[{
data:data,
backgroundColor:colors
}]
},
options:{
responsive:true,
maintainAspectRatio:false,
plugins:{
legend:{
position:"right",
labels:{
boxWidth:12,
padding:10
}
}
}
}
})

}


function renderClusters(issues, trends) {

    const container = document.getElementById("clusters")

    container.innerHTML = ""

    issues.forEach(issue => {

        let trend = trends.find(t => t.cluster == issue.cluster)

        let label = "Stable"
        let badge = "stable"

        if (trend) {
            if (trend.trend == "Increasing") {
                label = "Increasing"
                badge = "up"
            }
            if (trend.trend == "Decreasing") {
                label = "Decreasing"
                badge = "down"
            }
        }

        let examples = ""

        issue.examples.forEach(e => {
            examples += `<li>${e}</li>`
        })

        container.innerHTML += `

        <div class="cluster">

            <h3>
            Cluster ${issue.cluster} - ${issue.issue}
            <span class="badge ${badge}">${label}</span>
            </h3>

            <p>${issue.mentions} mentions</p>

            <ul class="examples">
            ${examples}
            </ul>

        </div>

        `
    })

}

loadDashboard()