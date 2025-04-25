let numberDisplay = document.getElementById('number')
let button = document.getElementById('togglebtn')
let interval = null;

function getRandomNumber() {
    return Math.floor(Math.random() * 100) + 1;
    
}
function startRandom() {
    if (!interval) {
        interval = setInterval(() => {
            const randomNum = getRandomNumber();
            numberDisplay.textContent = randomNum;
        },500);       
    }
}
function stopRandom() {
    clearInterval(interval);
    interval = null;
}

button.addEventListener('click' , () => {
   const currentNumber = parseInt(numberDisplay.textContent);
   if (currentNumber % 2 === 0) {
    startRandom();
   } else {
    stopRandom();
   }

});
startRandom();




