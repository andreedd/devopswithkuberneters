import { useState, useEffect } from 'react';

export default function Img() {

    const [data, setData] = useState(null)
    const [isLoading, setLoading] = useState(false)
  
    useEffect(() => {
      setLoading(true)
      fetch(process.env.NEXT_PUBLIC_BACKEND_URL + 'todo/image/')
        .then((res) => res.json())
        .then((data) => {
          setData(data)
          setLoading(false)
        })
    }, [])
  
    if (isLoading) return <p>Loading...</p>
    if (!data) return <p>No Image Found</p>

    console.log(data)

  return (
    <img style={{ width : 400, height: 400 }} src={process.env.NEXT_PUBLIC_BACKEND_URL + data.img_path}/>
  )
}
