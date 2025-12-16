const DATA_URL = "leaderboard.json";

fetch(DATA_URL)
  .then(r => r.json())
  .then(data => {
    renderTable(data);
    renderRadar(data);
    renderBar(data);
    renderAccordion(data);
  })
  .catch(err => {
    console.error(err);
    document.body.insertAdjacentHTML(
      "afterbegin",
      "<p style='color:red'>⚠️ Error loading leaderboard data.</p>"
    );
  });

/* ================= TABLE ================= */

function renderTable(data) {
  const table = document.getElementById("leaderboard-table");
  const models = Object.keys(data);

  let html = "<tr><th>Model</th><th>TMMLU+ Avg</th><th>Overall</th></tr>";
  models.forEach(m => {
    html += `
      <tr>
        <td>${m}</td>
        <td>${(data[m].tmmlu_avg * 100).toFixed(2)}</td>
        <td>${(data[m].overall * 100).toFixed(2)}</td>
      </tr>`;
  });

  table.innerHTML = html;
}

/* ================= RADAR ================= */

function renderRadar(data) {
  const models = Object.keys(data);
  const categories = Object.keys(data[models[0]].tmmlu_categories);

  const traces = models.map(m => ({
    type: "scatterpolar",
    r: categories.map(c => data[m].tmmlu_categories[c] * 100),
    theta: categories,
    fill: "toself",
    name: m
  }));

  Plotly.newPlot("tmmlu-radar", traces, {
    polar: { radialaxis: { visible: true, range: [0, 100] } },
    showlegend: true,
    margin: { t: 40 }
  });
}

/* ================= BAR CHART ================= */

function renderBar(data) {
  const models = Object.keys(data);
  const categories = Object.keys(data[models[0]].tmmlu_categories);

  const traces = models.map(m => ({
    x: categories,
    y: categories.map(c => data[m].tmmlu_categories[c] * 100),
    type: "bar",
    name: m
  }));

  Plotly.newPlot("tmmlu-bar", traces, {
    barmode: "group",
    yaxis: { title: "Accuracy (%)" },
    margin: { t: 40 }
  });
}

/* ================= ACCORDION ================= */

function renderAccordion(data) {
  const container = document.getElementById("tmmlu-accordion");
  const models = Object.keys(data);
  const cats = data[models[0]].tmmlu_breakdown;

  Object.entries(cats).forEach(([cat, subs]) => {
    let html = `<details><summary>${cat}</summary>`;

    Object.entries(subs).forEach(([sub, _]) => {
      html += `<div class="sub"><b>${sub}</b><ul>`;
      models.forEach(m => {
        const val = data[m].tmmlu_breakdown[cat][sub];
        html += `<li>${m}: ${(val * 100).toFixed(2)}</li>`;
      });
      html += "</ul></div>";
    });

    html += "</details>";
    container.innerHTML += html;
  });
}
