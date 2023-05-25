import Header from '@/components/Header/Header'
import styles from '@/styles/Home.module.scss'
import Card from '@/components/Card/Card'
import Grafico from '../public/grafico.svg'
import { useRef } from 'react'

export default function Home() {

const ambienteInputRef = useRef()
const submitHandler = (event) => {
  event.preventDefault()
  const ambienteValue = ambienteInputRef.current.value
  console.log(ambienteValue)
} 

  return (
    <>
      <div className={styles.main}>
        <Header />
        <div className={styles.container}>
        <h1>Ensaio do robô</h1>
        <form id='forms' onSubmit={submitHandler}>
          <div className={styles.field}>
            <label htmlFor="Ambiente">Nome do ambiente</label>
            <input ref={ambienteInputRef} type="text" id='Ambiente' />
          </div>
        </form>

        <button form='forms'>Gerar</button>
        <Card 
        title = "Concentração de gás"
      />
        <Card 
        title = "Tempo de ensaio"
        type = "time"
      />
        </div>

      </div>

    </>
  )
}
