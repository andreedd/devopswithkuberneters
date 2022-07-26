// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default function handler(req, res) {
  if (req.method === 'POST') {
  
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(req.body),
    }
  
    console.log(options)
    
    console.log('sending todo POST request')
    let data = fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}todo/todos/`, options)
      .then()
    // let data = { data: [{title: 'asd', id:'123'}, {title: 'qwer', id:'321'}] }
    console.log('todo data: ' + data)
    res.status(200).json(data)
  } else {
    console.log('sending todo GET request')
    fetch('http://localhost:8005/')
        .then((res) => res.json())
        .then((res) => {
          console.log(res)
        })
    //console.log('todo data: ' + data)
    let data = { data: [{title: 'asd', id:'123'}, {title: 'qwer', id:'321'}] }
    res.status(200).json(data)
  }
}
