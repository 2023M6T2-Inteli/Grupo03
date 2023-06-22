from fastapi import APIRouter, WebSocket

router = APIRouter()

frames_clients = set()
@router.websocket("/frames")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    frames_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in frames_clients:
                await client.send_text(data)
    except Exception as e:
        print(f"WebSocket connection closed with exception: {e}")
    finally:
        frames_clients.remove(websocket)