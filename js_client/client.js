const content = document.querySelector('#content')
const loginForm = document.forms['login']
const message = document.querySelector('#message')

const endpoint = 'http://localhost:8000'

const storeTokens = (access, refresh) => {
    localStorage.setItem('access_token', JSON.stringify(access))
    localStorage.setItem('refresh_token', JSON.stringify(refresh))
}

const handleLogin = async(e) => {

    e.preventDefault()

    const rawFormData = new FormData(loginForm)
    const loginObjData = Object.fromEntries(rawFormData)
    const loginJsonData = JSON.stringify(loginObjData)


    // send a post reyuest
    const options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: loginJsonData
    }

    response = await fetch(`${endpoint}/api/token/`, options)
    const data = await response.json()

    if(response.status === 200) storeTokens(data['access'], data['refresh'])

    return content.innerHTML = '<pre>' + JSON.stringify(data, null, 4) + '</pre>'
}

const initLogin = async() => {
    if(loginForm){
        loginForm.addEventListener('submit', handleLogin)
    }
}

const fetch_products = async (endpoint) => {
    const access_token = JSON.parse(localStorage.getItem('access_token'))
    if(access_token !== null){
        const options = {
            method: 'GET',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${access_token}`}
        }

        const response = await fetch(`${endpoint}`, options)
        return response.json()
    }else{
        return { 'message': 'Login to access products' }
    }
} 


const displayContent = async()=>{
    if(content){
        const products = await fetch_products(`${endpoint}/api/products/`)
        
        if(products['next'] !== null){
            const btn = document.createElement('button')
            btn.innerText = "Next"
            btn.addEventListener('click', async (e) => {
                const resp = await fetch_products(products['next'])
                console.log(resp)
            })
            content.after(btn)
        }
        
        content.innerHTML = '<pre>' + JSON.stringify(products, null, 4) + '</pre>';
    }
}


initLogin()
displayContent()
