import React from 'react';
import styles from 'components/ReportCard/ReportCard.module.scss'
import Link from 'next/link';
import { Modal,  Text , Input, Row, Column, Button} from "@nextui-org/react";

function ReportCard({id, nome_local, data}) {
  const [visible, setVisible] = React.useState(false);
  const handler = () => setVisible(true);

  const closeHandler = () => {
    setVisible(false);
    console.log("closed");
  };
  const readableDate = new Date(data).toLocaleDateString('pt-BR')  
  const readableHour = new Date(data).toLocaleTimeString('pt-BR')  
  return (
    <>
      <Modal
        closeButton
        blur
        aria-labelledby="modal-title"
        open={visible}
        onClose={closeHandler}
      >
        <Modal.Header>
          <Text id="modal-title" size={18}>
            
            <Text b size={18}>
              Relatório<br/>Inteli - Usp
            </Text>
          </Text>
        </Modal.Header>
        <Modal.Body>
          
            <div>
            Id do relatório: 1
            </div>
            <div>
            Endereço do ambiente: Inteli - Usp
            </div>
            <div>
              Data: 06/06/2023
            </div>
            <div>
              Quantidade mínima de gás: 10%
            </div>
            <div>
              Quantidade máxima de gás: 75%
            </div>
            <div>
             Temperatura mínima: 27°
            </div>
            <div>
             Temperatura máxima: 31°
            </div>
            <div>
             Umidade: 20
            </div>
            <Button flat>Baixar PDF</Button>
          
        </Modal.Body>
      </Modal>
   <div onClick={handler} className={styles.card}>
   <div className={styles.titleCard}>
    <h1>{id}</h1>
    <p>{nome_local}</p>
   </div>
    <div className={styles.time}>
    <p>{readableDate}</p>
    <p> - {readableHour}</p>
    </div>

   </div>
    </>

  );
}

export default ReportCard;
