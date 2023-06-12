import Header from "@/components/Header/Header";
import ReportCard from "@/components/ReportCard/ReportCard";
import React, { useState, useEffect } from "react";
import styles from "@/styles/Historic.module.scss";
import { Modal,  Text , Input, Row} from "@nextui-org/react";

export default function Historic({ children }) {
  const [visible, setVisible] = React.useState(false);
  const handler = () => setVisible(true);

  const closeHandler = () => {
    setVisible(false);
    console.log("closed");
  };
  const [isLoading, setIsLoading] = useState(false);
  const [reports, setReports] = useState(false);

  useEffect(() => {
    const fetchReports = async () => {
      setIsLoading(true);
      const response = await fetch("http://127.0.0.1:8000/relatorios");
      const data = await response.json();
      setReports(data.data);
      setIsLoading(false);
    };
    fetchReports();
  }, []);

  return (
    <>
    <Modal
        closeButton
        aria-labelledby="modal-title"
        open={visible}
        onClose={closeHandler}
      >
        <Modal.Header>
          <Text id="modal-title" size={18}>
            Welcome to
            <Text b size={18}>
              NextUI
            </Text>
          </Text>
        </Modal.Header>
        <Modal.Body>
          <Input
            clearable
            bordered
            fullWidth
            color="primary"
            size="lg"
            placeholder="Email"
            
          />
          <Input
            clearable
            bordered
            fullWidth
            color="primary"
            size="lg"
            placeholder="Password"
           
          />
          <Row justify="space-between">
            <Text size={14}>Forgot password?</Text>
          </Row>
        </Modal.Body>
      </Modal>
      <Header />
      <div className={styles.title}>
        <h1>Histórico</h1>
      </div>
      <main className={styles.main}>
        <div className={styles.cardContainer}>
          {isLoading && <p>Carregando...</p>}
          {!isLoading &&
            reports &&
            reports.map((report) => (
              <ReportCard
                key={report.id}
                id={report.id}
                nome_local={report.nome_local}
                data={report.data}
                onPressed={handler}
              />
            ))}


        </div>
      </main>
     
    </>
  );
}
