from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI on Vercel 🚀"}


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI on Vercel</title>
    </head>
    <body>
        <h1>✅ FastAPI Running on Vercel</h1>
        <button onclick="callApi()">Call API</button>
        <p id="result"></p>

        <script>
            async function callApi() {
                const res = await fetch('/api/hello');
                const data = await res.json();
                document.getElementById("result").innerText = data.message;
            }
        </script>
    </body>
    </html>
    """