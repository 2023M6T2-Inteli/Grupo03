import React from 'react';
import styles from 'components/Card/Card.module.scss'



function Card(props) {
  return (
    <div className={styles.main}>
      <h3>{props.title}</h3>
      {props.type ? (
        <div className={styles.time}>
            <p>10:10</p>
            </div>
      ):(
        <div className={styles.imageBox}>
          <p>20%</p>
        </div>
      )}
    </div>
  );
}

export default Card;
