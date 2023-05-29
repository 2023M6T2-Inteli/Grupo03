import React from "react";
import styles from "components/Header/Header.module.scss";
import Link from "next/link";

function Header() {
  return (
    <>
      <div className={styles.container}>
        <img src="logo.png" alt="logo" />

        <nav className={styles.stroke}>
          <ul>
            <li>
              <Link href="/historic">Histórico</Link>
            </li>
          </ul>
        </nav>
        {/* <div className={styles.stroke}>
          <Link href={"/historic"}>
            <div className={styles.stroke}>
              <p>Histórico</p>
            </div>
          </Link>
        </div> */}
      </div>
    </>
  );
}

export default Header;
