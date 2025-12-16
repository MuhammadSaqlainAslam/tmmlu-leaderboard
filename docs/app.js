// Fetch JSON leaderboard
fetch('leaderboard.json')
    .then(res => res.json())
    .then(data => {
        renderRadarChart(data);
        renderBarChart(data);
    })
    .catch(err => {
        console.error('Error loading leaderboard:', err);
        document.getElementById('radarChart').innerHTML =
            '<p style="color:red;">⚠️ Error loading leaderboard data.</p>';
        document.getElementById('barChart').innerHTML =
            '<p style="color:red;">⚠️ Error loading leaderboard data.</p>';
    });

// Radar chart for TMMLU+ categories
function renderRadarChart(data) {
    const models = data.models;
    const categories = Object.keys(models[0].tmmlu_categories);

    const traces = models.map(model => ({
        type: 'scatterpolar',
        r: categories.map(cat => model.tmmlu_categories[cat]),
        theta: categories,
        fill: 'toself',
        name: model.name
    }));

    const layout = {
        polar: {
            radialaxis: {
                visible: true,
                range: [0, 1]
            }
        },
        title: '📊 TMMLU+ Category Radar Comparison',
        font: { size: 12 },
        showlegend: true
    };

    Plotly.newPlot('radarChart', traces, layout, {responsive: true});
}

// Bar chart for TMMLU+ category comparison
function renderBarChart(data) {
    const models = data.models;
    const categories = Object.keys(models[0].tmmlu_categories);

    const traces = models.map(model => ({
        x: categories,
        y: categories.map(cat => model.tmmlu_categories[cat]),
        name: model.name,
        type: 'bar'
    }));

    const layout = {
        barmode: 'group',
        title: '📊 TMMLU+ Category Comparison (Bar Chart)',
        xaxis: { title: 'Category' },
        yaxis: { title: 'Score', range: [0, 1] },
        font: { size: 12 }
    };

    Plotly.newPlot('barChart', traces, layout, {responsive: true});
}
