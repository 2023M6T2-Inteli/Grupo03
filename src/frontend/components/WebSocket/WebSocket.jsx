import React, { useEffect } from 'react';
import styles from './WebSocket.module.scss';

function WebSocketComponent() {
  useEffect(() => {
    const socket = new WebSocket("ws://10.128.69.212:8000/ws"); 

    socket.onopen = function(event) {
      console.log("WebSocket connection established.");
    };

    socket.onmessage = function(event) {
      const imageContainer = document.getElementById("image-container");
      const receivedData = event.data;
      imageContainer.src = "data:image/jpg;base64," + receivedData;
    };

    socket.onclose = function(event) {
      console.log("WebSocket connection closed.");
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    // <div className={styles.visComp}>
      <img className={styles.visCompImg} id="image-container" src="" alt="Received Image" />
    // </div>
  );
}

export default WebSocketComponent;
