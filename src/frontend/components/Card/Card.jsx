import React from 'react';
import styles from 'components/Card/Card.module.scss'
import Bateria from '../Bateria/Bateria';


function Card(props) {
  return (
    <div className={styles.main}>
      <h3>{props.title}</h3>
        <div className={styles.imageBox}>
          <Bateria></Bateria>
        </div>
      
    </div>
  );
}

export default Card;
