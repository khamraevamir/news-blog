let codify = () => {


    return({
        createModal: (name) => {
            let btns = document.querySelectorAll(`.${name}`)
            let modal = document.querySelector(`#${name}`)

            for(let btn of btns){
                btn.addEventListener('click', ()=> {
                    modal.classList.toggle('d-none')
                })
            }
            
        },
       
    })
}

