const dateInput = document.getElementById('id_start_time')
const dateEnd = document.getElementById('id_end_time')

// const sp = new SimplePicker();
// dateInput.addEventListener("click", (evt) => {
//   sp.open()
//   let submit = handler(dateInput, readableDate)
// })

// dateEnd.addEventListener("click", (e) => {
//     sp.open()
    
//   })


 

//   // $eventLog.innerHTML += '\n\n';
//   sp.on('submit', (date, readableDate) => {
//     $eventLog.innerHTML += readableDate + '\n';
//   });

//   sp.on('close', (date) => {
//     $eventLog.innerHTML += 'Picker Closed'  + '\n';
//   });

let simplepicker = new SimplePicker({
    zIndex: 10
  });

  

  const $button = document.querySelector('button');
  const $eventLog = document.querySelector('.event-log');
  dateInput.addEventListener('click', (e) => {
    simplepicker.open();
  });

  // $eventLog.innerHTML += '\n\n';
  simplepicker.on('submit', (date, readableDate) => {
    $eventLog.innerHTML += readableDate + '\n';
  });

  simplepicker.on('close', (date) => {
    $eventLog.innerHTML += 'Picker Closed'  + '\n';
  });
