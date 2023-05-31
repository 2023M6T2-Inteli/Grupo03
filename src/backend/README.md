## Intruções para rodar o sistema integrado com ROS2 > websocket > HTML na ordem descrita:

- entre na pasta ```src/embedded```  e rode ``` python main.py``` ou ``` python3 main.py ``` para iniciar o publisher que coleta os frames da camera do robô e publica no frontend.

- entre na pasta ```src/backend``` e rode ```uvicorn app:app --reload``` para rodar o servidor com o websocket e acesse a porta http://localhost:8000/

- entre na pasta ```src/backend/ros``` e rode ``` python main.py ``` ou ``` python3 main.py ``` para iniciar o subscriber do tópico "/camera" que está recebendo os frames do robô