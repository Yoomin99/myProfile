function init() {
    // Add event listener for "Add Ingredient" Button Press
    const buttons = document.querySelectorAll("button");
    //const btn2 = document.getElementsByClassName("bts-2");
    buttons[0].addEventListener('click' , Aboutme);
    buttons[1].addEventListener('click' , HireMe);
  }
  
  window.addEventListener('DOMContentLoaded', init);

  function Aboutme (event){
    window.location.href = 'website.html';
  }

  function HireMe (event){
    window.location.href = 'website.html';
  }