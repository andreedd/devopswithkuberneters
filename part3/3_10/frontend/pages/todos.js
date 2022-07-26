import Head from 'next/head'
import Img from '../components/image'
import styles from '../styles/Home.module.css'
import Form from '../components/form'
import FormResults from '../components/formResults'
import { useState } from 'react';

export default function Todos() {

  const [todos, setTodos] = useState([]);
  return (
    <div className={styles.container}>
      <h2>TODO APP</h2>
      <Img/>
      <Form todos={todos} setTodos={setTodos}/>
      <FormResults todos={todos} setTodos={setTodos}/>


    </div>
  )
}
