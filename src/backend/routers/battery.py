from fastapi import APIRouter, WebSocket

router = APIRouter()

battery_clients = set()
@router.websocket("/battery")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    battery_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in battery_clients:
                await client.send_text(data)
    except Exception as e:
        print(f"WebSocket connection closed with exception: {e}")
    finally:
        battery_clients.remove(websocket)