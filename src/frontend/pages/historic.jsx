import Header from "@/components/Header/Header";
import ReportCard from "@/components/ReportCard/ReportCard";
import React, { useState, useEffect } from "react";
import styles from "@/styles/Historic.module.scss";

export default function Historic({ children }) {
    const [isLoading, setIsLoading] = useState(false);
    const [reports, setReports] = useState(false);

    useEffect(() => {
        const fetchReports = async () => {
            setIsLoading(true);
            const response = await fetch("http://127.0.0.1:8000/relatorios");
            const data = await response.json();
            setReports(data.data);
            setIsLoading(false);
        }
        fetchReports();
    }, [])

    return (
        <>
        <Header />
        <div className={styles.title}> 
        <h1 >Histórico</h1>
        </div>
        <main className={styles.main}>

            <div className={styles.cardContainer}>
            {isLoading && <p>Carregando...</p>}
            {!isLoading && reports && reports.map((report) => (
                <ReportCard key={report.id} id={report.id} nome_local={report.nome_local} data={report.data} />
            ))}
            </div>
        </main>
        </>
    )
}