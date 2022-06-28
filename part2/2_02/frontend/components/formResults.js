import { useState, useEffect } from 'react';

export default function FormResults({todos, setTodos}) {

    const [isLoading, setLoading] = useState(false)

    useEffect(() => {
      setLoading(true)
      fetch(process.env.NEXT_PUBLIC_BACKEND_URL + 'todo/todos/')
        .then((res) => res.json())
        .then((res) => {
            setTodos([...res.data])
            setLoading(false)
        })
    }, [])
  
    if (isLoading) return <p>Loading Todos...</p>
    if (!todos) return <p>No Todos Found</p>

  return (
    <>
        <ul>
            {todos.map((todo) => <li key={todo.id}>{todo.title}</li>)}
        </ul>
    </>
  )
}
