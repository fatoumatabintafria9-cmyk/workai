function register(){
showRoleChoice();
}

function showRoleChoice(){
document.body.innerHTML=`
<div class="auth-box">
<h1>🚀 WorkAI</h1>
<p>Choisissez votre profil</p>
<button onclick="showEmployerDashboard()">🏢 Employeur</button>
<button onclick="showCandidateDashboard()">👨‍💼 Candidat</button>
</div>`;
}

function showEmployerDashboard(){
document.body.innerHTML=`
<div class="dashboard">
<h1>🏢 Dashboard Employeur</h1>

<div class="nav">
<button onclick="showEmployerDashboard()">Accueil</button>
<button onclick="employerJobs()">Publier</button>
<button onclick="showCandidateDashboard()">Vue candidat</button>
</div>

<div id="result"></div>
</div>`;
}

function employerJobs(){
document.getElementById("result").innerHTML=`

<div class="card">
<h2>Publier une offre</h2>

<input id="title" placeholder="Titre">
<input id="company" placeholder="Entreprise">
<input id="location" placeholder="Localisation">
<input id="salary" placeholder="Salaire">
<input id="experience" placeholder="Expérience">

<button onclick="publishJob()">Publier</button>

</div>
`;
}

async function publishJob(){

let job={
title:document.getElementById("title").value,
company:document.getElementById("company").value,
location:document.getElementById("location").value,
salary:document.getElementById("salary").value,
experience:document.getElementById("experience").value
};

await fetch("http://localhost:8000/create-job",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(job)
});

alert("Offre publiée 🚀");
}

function showCandidateDashboard(){
fetchJobs();
}

async function fetchJobs(){

let response=await fetch("http://localhost:8000/jobs");
let jobs=await response.json();

let html=`
<div class="dashboard">
<h1>👨‍💼 Offres disponibles</h1>
`;

jobs.forEach(job=>{
html+=`
<div class="card">
<h2>${job.title}</h2>
<p>${job.company}</p>
<p>${job.location}</p>
<p>${job.salary}</p>
<p>${job.experience}</p>
<button>Postuler</button>
</div>`;
});

html+=`</div>`;

document.body.innerHTML=html;
}