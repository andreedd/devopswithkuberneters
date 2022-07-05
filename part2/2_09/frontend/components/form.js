import { useEffect } from 'react';

export default function Form( {todos, setTodos} ) {
    const handleSubmit = async (event) => {
      event.preventDefault()
  
      const data = {
        todo: event.target.todo.value,
      }
  
      const JSONdata = JSON.stringify(data)
  
      const endpoint = `${process.env.NEXT_PUBLIC_BACKEND_URL}todo/todos/`
  
      const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSONdata,
      }
      
      fetch(endpoint, options)
      .then(res => res.json())
      .then(res => {
          setTodos([...res.data
          ])
      })

    }
    return (
      <form onSubmit={handleSubmit}>
        <label htmlFor="todo">First Name</label>
        <input type="text" id="todo" name="todo" required />
        <button type="submit">Submit</button>
      </form>
    )
  }