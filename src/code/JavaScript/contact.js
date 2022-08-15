function init() {
    const form = document.querySelector("form");
    statusTxt = form.querySelector(".button-area span");

    form.onsubmit = (e)=>{
      e.preventDefault();
      statusTxt.style.color = "#0D6EFD";
      statusTxt.style.display = "block";
      statusTxt.innerText = "Sending your message...";
      let xhr = new XMLHttpRequest();
      xhr.open("POST", "message.php" , true);

      xhr.onload = () =>{
        
        if(xhr.readyState == 4 && xhr.status == 200){
          let response = xhr.response;
          console.log(response);
          statusTxt.innerText = response; 

          if(response.indexOf("Email and message field are required")!= -1 || response.indexOf("Failed to send an email")!= -1 || response.indexOf("Wrong email address format")!= -1 ){
            statusTxt.style.color = "red";
          } else{
            form.reset();
            setTimeout(()=>{
              statusTxt.style.display = "none";
            })
          }
        }
      }

      let formData = new FormData(form);
      xhr.send(formData);

    }

    
    
    
    
}



window.addEventListener('DOMContentLoaded', init);
