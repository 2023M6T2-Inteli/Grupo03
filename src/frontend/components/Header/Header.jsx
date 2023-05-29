import React from 'react';
import styles from 'components/Header/Header.module.scss'

function Header() {
  return (
   <>
   <div className={styles.container}>
   <img src="logo.png" alt="logo" />
   <div className={styles.stroke}>
   <p>Histórico</p>
   </div>
   </div>
   </>
  );
}

export default Header;
