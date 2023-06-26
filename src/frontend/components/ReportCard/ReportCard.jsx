import styles from "components/ReportCard/ReportCard.module.scss";
import Link from "next/link";
import { Modal, Text, Input, Row, Column, Button } from "@nextui-org/react";
import { useState, useEffect } from "react";
import html2canvas from "html2canvas";
import jsPDF from "jspdf";

function ReportCard({ report }) {
  const [visible, setVisible] = useState(false);
  const handler = () => setVisible(true);
  const [url, setUrl] = useState("");
  const { id, nome_local, endereco, data, gas } = report;

  const handleDownloadPDF = () => {
    const modalContent = document.getElementById("modal-content");

    html2canvas(modalContent).then((canvas) => {
      const imgData = canvas.toDataURL("image/png");
      const pdf = new jsPDF();
      pdf.addImage(imgData, "PNG", 0, 0);
      pdf.save("modal.pdf");
    });
  };

  const closeHandler = () => {
    setVisible(false);
    console.log("closed");
  };

  // useEffect(() => {
  //   const fetchLink = async () => {
  //     const response = await fetch(`http://0.0.0.0:8000/get-video-url/`);
  //     const data = await response.json();
  //     setUrl(data.data);
  //   };

  //   fetchLink();
  // }, []);

  const readableDate = new Date(data).toLocaleDateString("pt-BR");
  const readableHour = new Date(data).toLocaleTimeString("pt-BR");
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
              Relatório
              <br />
              {endereco}
            </Text>
          </Text>
        </Modal.Header>
        <Modal.Body>
          <div id="modal-content" className={styles.modalContent}>
            <div>Id do relatório: {id}</div>
            <div>Endereço do ambiente: {endereco}</div>
            <div>
              Data: {readableDate} - {readableHour}
            </div>
            <div>Quantidade mínima de gás: 10%</div>
            <div>Quantidade máxima de gás: 75%</div>
            <div>Temperatura mínima: 27°</div>
            <div>Temperatura máxima: 31°</div>
            <div>Umidade: 20</div>
            <div>Link para vídeo: {url.detail}</div>
          </div>
          <Button flat onClick={handleDownloadPDF}>Baixar PDF</Button>
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
