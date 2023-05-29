import React from 'react';
import styles from 'components/ReportCard/ReportCard.module.scss'
import Link from 'next/link';

function ReportCard({id, nome_local, data}) {

  const readableDate = new Date(data).toLocaleDateString('pt-BR')  
  const readableHour = new Date(data).toLocaleTimeString('pt-BR')  
  return (
   <div className={styles.card}>
   <div className={styles.titleCard}>
    <h1>{id}</h1>
    <p>{nome_local}</p>
   </div>
    <div className={styles.time}>
    <p>{readableDate}</p>
    <p> - {readableHour}</p>
    </div>

   </div>

  );
}

export default ReportCard;
