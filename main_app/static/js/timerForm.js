const dateInput = document.getElementById('id_when')
console.log(dateInput)

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
    
    
    dateInput.value = `${finalTime}`
        
    
}

dateInput.addEventListener("click", (e) => {
    myEvent = e.target.id
    sp.open()
  
})


 sp.on('submit', handler)


  

