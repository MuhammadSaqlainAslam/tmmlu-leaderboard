// Load JSON
fetch("leaderboard.json")
  .then(response => response.json())
  .then(data => {
    renderLeaderboard(data.models);
    renderRadarChart(data.models);
    renderBarChart(data.models);
  })
  .catch(err => {
    document.getElementById("leaderboard").innerHTML = 
      "⚠️ Error loading leaderboard data.";
    console.error(err);
  });

// Render leaderboard table
function renderLeaderboard(models) {
  let html = `<table>
                <tr>
                  <th>Model</th>
                  <th>TMMLU Avg</th>
                  <th>General Avg</th>
                </tr>`;
  models.forEach(m => {
    html += `<tr>
               <td>${m.name}</td>
               <td>${m.tmmlu_avg}</td>
               <td>${m.general_avg}</td>
             </tr>`;
  });
  html += `</table>`;
  document.getElementById("leaderboard").innerHTML = html;
}

// Radar chart
function renderRadarChart(models) {
  const categories = Object.keys(models[0].tmmlu_categories);
  const traces = models.map(m => ({
    type: 'scatterpolar',
    r: categories.map(c => m.tmmlu_categories[c]),
    theta: categories,
    fill: 'toself',
    name: m.name
  }));

  const layout = {
    polar: {
      radialaxis: { visible: true, range: [0, 1] }
    },
    showlegend: true
  };

  Plotly.newPlot('radar-chart', traces, layout, {responsive:true});
}

// Bar chart
function renderBarChart(models) {
  const categories = Object.keys(models[0].tmmlu_categories);
  const traces = models.map(m => ({
    x: categories,
    y: categories.map(c => m.tmmlu_categories[c]),
    type: 'bar',
    name: m.name
  }));

  const layout = {barmode: 'group', yaxis: {range: [0, 1]}};

  Plotly.newPlot('bar-chart', traces, layout, {responsive:true});
}
