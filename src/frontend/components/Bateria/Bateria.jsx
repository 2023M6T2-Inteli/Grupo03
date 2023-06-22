import React, { useEffect } from 'react';
import styles from './Bateria.module.scss';

function Bateria() {
    useEffect(() => {
        const socket = new WebSocket("ws://10.128.68.32:8000/battery"); 
    
        socket.onopen = function(event) {
          console.log("WebSocket connection established.");
        };
    
        socket.onmessage = function(event) {
          let data = JSON.parse(event.data);
          const newData = (data*100);
          document.getElementById('batteryData').innerText = newData.toFixed(2) + '%';
        };
    
        socket.onclose = function(event) {
          console.log("WebSocket connection closed.");
        };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div id="batteryData" className={styles.battery}></div>
  );
}

export default Bateria;