import React, { useEffect } from 'react';
import styles from './Bateria.module.scss';

function Bateria() {
    useEffect(() => {
        const socket = new WebSocket("ws://10.128.68.32:8000/battery"); 
    
        socket.onopen = function(event) {
          console.log("WebSocket connection established.");
        };
    
        socket.onmessage = function(event) {
          const data = JSON.parse(event.data);
          document.getElementById('batteryData').innerText = data;
        };
    
        socket.onclose = function(event) {
          console.log("WebSocket connection closed.");
        };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div id="batteryData"></div>
  );
}

export default Bateria;