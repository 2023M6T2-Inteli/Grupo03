from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <img id="image-container" src="" alt="Received Image">

  <script>
    const socket = new WebSocket("ws://localhost:8000/ws"); // Substitua pelo URL correto do WebSocket

    socket.onopen = function(event) {
      console.log("WebSocket connection established.");
    };

    socket.onmessage = function(event) {
      const imageContainer = document.getElementById("image-container");
      const receivedData = event.data;
      imageContainer.src = "data:image/jpg;base64," + receivedData; // Define o src da tag img com o valor base64 recebido
    };

    socket.onclose = function(event) {
      console.log("WebSocket connection closed.");
    };
  </script>
</body>
</html>

"""

@app.get("/frames")
async def get():
    return HTMLResponse(html)

connected_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(data)
    except Exception as e:
        print(f"WebSocket connection closed with exception: {e}")
    finally:
        connected_clients.remove(websocket)