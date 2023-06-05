import styles from "@/styles/Home.module.scss";
import Card from "@/components/Card/Card";
import { useRef } from "react";
import React, { useState, useEffect } from "react";
import Header from "@/components/Header/Header";
import WebSocketComponent from "@/components/WebSocket/WebSocket";

export default function Home({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const handleSidebarToggle = () => {
    setSidebarOpen(!sidebarOpen);
  };



  const ambienteInputRef = useRef();
  const submitHandler = async (event) => {
    event.preventDefault();
    const ambienteValue = ambienteInputRef.current.value;
    console.log(ambienteValue);

    const relatorioData = {
      id: 24,
      nome_local: ambienteValue,
      endereco: "sp",
      data: "2023-05-25T10:30:00Z",
      gas: 100,
      condicoes_ambientais: "as condições estão boas",
      observacoes: "nenhuma observação",
    };

    const response = await fetch("http://127.0.0.1:8000/relatorios", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify(relatorioData),
    });
    const data = await response.json();
  };

  return (
    <>
      <Header />
      <div className={styles.main}>
        <div className={styles.container}>
          <div>
            <h1>Ensaio do robô</h1>
            <form id="forms" onSubmit={submitHandler}>
              <div className={styles.field}>
                <label htmlFor="Ambiente">Nome do ambiente</label>
                <input ref={ambienteInputRef} type="text" id="Ambiente" />
              </div>
              <div className={styles.field}>
                <label htmlFor="Address">Endereço</label>
                <input type="text" id="Ambiente" />
              </div>
            </form>
            <Card title="Quantidade de bateria do robô" />
          </div>
          <div className={styles.files}>
            <div className={styles.compvis}>
              <WebSocketComponent />
            </div>
            <div>
              <button form="forms" className={styles.button}>Gerar Relatório</button>
              {/* <button className={styles.button}>Iniciar movimentação <br/>do robô</button> */}
            </div>
           
          </div>
        </div>
        
      </div>
    </>
  );
}
