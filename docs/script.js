// Fetch leaderboard JSON
fetch("leaderboard.json")
  .then(response => response.json())
  .then(data => {
    renderAvgPlot(data.models);
    renderRadarPlot(data.models);
    renderBarPlot(data.models);
  })
  .catch(error => {
    console.error("Error loading leaderboard data:", error);
    document.body.innerHTML += '<p style="color:red;">⚠️ Error loading leaderboard data.</p>';
  });

// Average TMMLU+ performance plot
function renderAvgPlot(models) {
  const names = models.map(m => m.name);
  const scores = models.map(m => m.tmmlu_avg);

  const trace = {
    x: names,
    y: scores,
    type: 'bar',
    marker: { color: '#1f77b4' }
  };

  const layout = {
    yaxis: { title: 'TMMLU+ Average Score', range: [0,1] },
    margin: { t:30, l:50, r:30, b:50 }
  };

  Plotly.newPlot('avg-plot', [trace], layout);
}

// Radar chart for categories
function renderRadarPlot(models) {
  const categories = Object.keys(models[0].tmmlu_categories);
  const traces = models.map(m => ({
    type: 'scatterpolar',
    r: categories.map(c => m.tmmlu_categories[c]),
    theta: categories,
    fill: 'toself',
    name: m.name
  }));

  const layout = {
    polar: { radialaxis: { visible: true, range: [0,1] } },
    showlegend: true,
    margin: { t:30, l:50, r:50, b:50 }
  };

  Plotly.newPlot('category-radar', traces, layout);
}

// Bar chart for categories
function renderBarPlot(models) {
  const categories = Object.keys(models[0].tmmlu_categories);
  const traces = models.map(m => ({
    x: categories,
    y: categories.map(c => m.tmmlu_categories[c]),
    type: 'bar',
    name: m.name
  }));

  const layout = {
    barmode: 'group',
    yaxis: { title: 'Score', range: [0,1] },
    margin: { t:30, l:50, r:30, b:50 }
  };

  Plotly.newPlot('category-bar', traces, layout);
}
