import styles from "../styles/Index.module.scss";
import { useRef } from "react";
import  Lottie  from "lottie-react";
import animationData from "../public/robot1.json";
import Link from 'next/link';

export default function Login() {
  return (
    <>
      <div className={styles.Container}>
        <div className={styles.login}>
          <div className={styles.content}>
            <p>
              Faça o login com o Google usando seu domínio da Gerdau e
              desbloqueie um mundo de possibilidades em nossa plataforma. Aqui,
              você pode explorar e testar robôs para ambientes confinados,
              desvendando novas soluções para sua empresa. Junte-se a nós e
              descubra o futuro da automação com segurança
            </p>
            <Link href={"/reportPage"}>
            <button className={styles.button}>Entrar</button>
            </Link>
          </div>
        </div>
        <div className={styles.lottie}>
        <div  style={{width:'320px'}}>
          <Lottie animationData={animationData} loop autoplay speed={1.5} />
        </div>
        </div>
      </div>
    </>
  );
}
