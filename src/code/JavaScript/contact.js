function init() {
    const form = document.getElementById("form");
    const result = document.getElementById("result");
    
    form.addEventListener("submit", function (e) {
        const formData = new FormData(form);
        console.log(formData)
        e.preventDefault();
        var object = {};
        formData.forEach((value, key) => {
          object[key] = value;
        });
        console.log(object);
        var json = JSON.stringify(object);

        
        fetch("https://api.web3forms.com/submit", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json"
          },
          body: json
        })
          .then(async (response) => {
            let json = await response.json();
            if (response.status == 200) {
              result.innerHTML = json.message;
              result.classList.remove("text-gray-500");
              result.classList.add("text-green-500");
            } else {
              console.log(response);
              result.innerHTML = json.message;
              result.classList.remove("text-gray-500");
              result.classList.add("text-red-500");
            }
          })
          .catch((error) => {
            console.log(error);
            result.innerHTML = "Something went wrong!";
          })
          .then(function () {
            form.reset();
            setTimeout(() => {
              result.style.display = "none";
            }, 5000);
          });
      });
    
}



window.addEventListener('DOMContentLoaded', init);
