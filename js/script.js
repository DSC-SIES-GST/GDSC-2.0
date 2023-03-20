const scriptURL = 'https://script.google.com/macros/s/AKfycbxG1ltIrpJxhPmlVNiBXPkcVLpYwYwiLJgBzT1XZrI2siWJKDgBmt-71nSm6Z04D9jPow/exec'
const form = document.forms['submit-to-google-sheet']
const msg = document.getElementById("msg")

form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
      .then(response => {
        msg.innerHTML = "Message sent successfully"
        setTimeout(function(){
          msg.innerHTML = ""
        },5000)
        form.reset()
      })
      .catch(error => {
        msg.innerHTML = "There is Error, Please Check the values again"
        setTimeout(function(){
          msg.innerHTML = ""
        },5000)
        form.reset()
      })
  })


// Timer

 // The data/time we want to countdown to
 var countDownDate = new Date("Mar 25, 2023 12:00:00").getTime();
      
 // Run myfunc every second
 var myfunc = setInterval(function() {

 var now = new Date().getTime();
 var timeleft = countDownDate - now;
     
 // Calculating the days, hours, minutes and seconds left
 var days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
 var hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
 var minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
 var seconds = Math.floor((timeleft % (1000 * 60)) / 1000);
     
 // Result is output to the specific element
 document.getElementById("days").innerHTML = days + "d "
 document.getElementById("hours").innerHTML = hours + "h " 
 document.getElementById("minutes").innerHTML = minutes + "m " 
 document.getElementById("seconds").innerHTML = seconds + "s " 
     
 // Display the message when countdown is over
 if (timeleft < 0) {
     clearInterval(myfunc);
     document.getElementById("days").innerHTML = ""
     document.getElementById("hours").innerHTML = "" 
     document.getElementById("mins").innerHTML = ""
     document.getElementById("secs").innerHTML = ""
     document.getElementById("end").innerHTML = "TIME UP!!";
 }
 }, 1000);
 
