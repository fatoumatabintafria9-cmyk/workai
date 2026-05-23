from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>WorkAI</title>
        <style>
            body{
                font-family:Arial;
                background:#0f172a;
                color:white;
                text-align:center;
                padding:50px;
            }

            .card{
                background:#1e293b;
                padding:30px;
                border-radius:20px;
                width:80%;
                margin:auto;
            }

            button{
                background:#2563eb;
                color:white;
                border:none;
                padding:15px 25px;
                margin:10px;
                border-radius:12px;
                font-size:18px;
                cursor:pointer;
            }

            button:hover{
                background:#1d4ed8;
            }

            #result{
                margin-top:30px;
                font-size:22px;
                color:#22c55e;
            }
        </style>
    </head>

    <body>

        <div class="card">
            <h1>🚀 WorkAI</h1>
            <p>L’IA qui révolutionne le recrutement</p>

            <button onclick="analyze()">
                Analyser candidat
            </button>

            <button onclick="jobs()">
                Voir emplois
            </button>

            <div id="result"></div>
        </div>

        <script>
            function analyze(){
                document.getElementById("result").innerHTML =
                "Score : 93/100 ✅ Excellent candidat";
            }

            function jobs(){
                document.getElementById("result").innerHTML =
                "Médecin - Pechiney | Développeur IA - WorkAI";
            }
        </script>

    </body>
    </html>
    """