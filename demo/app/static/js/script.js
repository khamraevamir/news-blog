let btn = document.querySelector('#btn')
let btn2 = document.querySelector('#btn2')
let sidebar = document.querySelector('.sidebar')
let searchBtn = document.querySelector('.bx-search')

let topNavigator = document.querySelector('.top_navigator')

btn.addEventListener('click',  ()=> {
    sidebar.classList.toggle('active')
    topNavigator.classList.toggle('active')
})


btn2.addEventListener('click',  ()=> {
    sidebar.classList.toggle('active')
    topNavigator.classList.toggle('active')
})

