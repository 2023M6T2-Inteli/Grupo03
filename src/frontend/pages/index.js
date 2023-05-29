import Header from '@/components/Header/Header'
import styles from '@/styles/Home.module.scss'
import Card from '@/components/Card/Card'
import Grafico from '../public/grafico.svg'

export default function Home() {
  return (
    <>
      <div className={styles.main}>
        <Header />
        <div className={styles.container}>
        <h1>Ensaio do robô</h1>
        <p>Nome do ambiente</p>
        <input></input>
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
