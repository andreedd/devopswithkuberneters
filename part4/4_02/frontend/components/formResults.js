import { useState, useEffect } from 'react';

export default function FormResults({todos, setTodos}) {

    const [isLoading, setLoading] = useState(false)

    useEffect(() => {
      setLoading(true)
      fetch('api/form/')
        .then((res) => res.json())
        .then((res) => {
            setTodos([...res.data])
            setLoading(false)
        })
    }, [])
  
    if (isLoading) return <p>Loading Todos...</p>
    if (!todos) return <p>No Todos Found</p>
    console.log(todos)

  return (
    <>
        <ul>
            {todos.map((todo) => <li key={todo.id}>{todo.title}</li>)}
        </ul>
    </>
  )
}
