const dateInput = document.getElementById('id_start_time')
const dateEnd = document.getElementById('id_end_time')

const sp = new SimplePicker();
let myEvent = null


function handler(date, readableDate){
    console.log(date)
   

    let stringInput = JSON.stringify(dateInput)

    let stringDate = JSON.stringify(date)
    let day = stringDate.split('T')[0]
    let newTime = stringDate.split('T')[1]

    let combineTime = `${day} ${newTime}`
    let noDot = combineTime.split('.')
    let formatTime = noDot[0]
    let finalTime = formatTime.split('"')[1]
    
    if(myEvent === 'id_start_time'){
        dateInput.value = `${finalTime}`
        dateEnd.value = dateEnd.value
    }else if(myEvent === 'id_end_time'){
        dateEnd.value = `${finalTime}`
        dateInput.value = dateInput.value
    }
    
}

dateInput.addEventListener("click", (e) => {
    myEvent = e.target.id
    sp.open()
  
})


dateEnd.addEventListener("click", (e) => {
    myEvent = e.target.id
    sp.open()
    
    
 })

 sp.on('submit', handler)


  

