import styles from "@/styles/Home.module.scss";
import Card from "@/components/Card/Card";
import { useRef } from "react";
import React, { useState, useEffect } from "react";
import Header from "@/components/Header/Header";
import WebSocketComponent from "@/components/WebSocket/WebSocket";
import Bateria from "@/components/Bateria/Bateria";
import toast, { Toaster } from "react-hot-toast";

export default function Home({ children }) {
  const addressInputRef = useRef();
  const ambienteInputRef = useRef();
  const notify = () => toast.success("Seu relatório foi criado com sucesso!");

  const submitHandler = async (event) => {
    event.preventDefault();
    const ambienteValue = ambienteInputRef.current.value;
    console.log(ambienteValue);
    const addressValue = addressInputRef.current.value;
    var timestamp = new Date().getTime();
    var date = new Date(timestamp);
    var formattedDate = date.toISOString();

    const generateNewId = () => {
      const maxNumber = Math.pow(10, 2) - 1;
      const newId = Math.floor(Math.random() * maxNumber);
      const formattedId = newId.toString().padStart(2, "0");
      return formattedId;
    };
    const newId = generateNewId(2);
    console.log(newId);

    const relatorioData = {
      nome_local: ambienteValue,
      endereco: addressValue,
      data: formattedDate,
      gas: 100,
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
    console.log(data);
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
                <input
                  ref={ambienteInputRef}
                  placeholder={"Insira o nome do ambiente"}
                  type="text"
                  id="Ambiente"
                />
              </div>
              <div className={styles.field}>
                <label htmlFor="Address">Endereço</label>
                <input
                  type="text"
                  ref={addressInputRef}
                  placeholder={"Insira o endereço"}
                  id="Ambiente"
                />
              </div>
            </form>
            <Card title="Quantidade de bateria do robô" />
          </div>
          <div className={styles.files}>
            <div className={styles.compvis}>
              <WebSocketComponent />
            </div>
            <div className={styles.buttons}>
              <Toaster position="bottom-right" reverseOrder={false} />
              <button onClick={notify} form="forms" className={styles.button}>
                Gerar Relatório
              </button>
              <button className={styles.button}>
                Iniciar movimentação <br />
                do robô
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
