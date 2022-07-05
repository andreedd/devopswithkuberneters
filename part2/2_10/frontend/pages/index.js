import Head from 'next/head'
import Img from '../components/image'
import styles from '../styles/Home.module.css'
import Form from '../components/form'
import FormResults from '../components/formResults'
import { useState } from 'react';

export default function Home() {

  const [todos, setTodos] = useState([]);
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h2>TODO APP</h2>
      <Img/>
      <Form todos={todos} setTodos={setTodos}/>
      <FormResults todos={todos} setTodos={setTodos}/>


    </div>
  )
}