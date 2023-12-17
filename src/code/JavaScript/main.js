const SECTIONS = ["home", "about" , "portfolio", "contact"];

function init() {
  const BTNS = document.getElementsByClassName("btn")
  const home = BTNS[0]
  home.addEventListener("click", HOME)
  const about = BTNS[1]
  about.addEventListener("click", ABOUT)
  const portfolio = BTNS[2]
  portfolio.addEventListener("click", PORTFOLIO)
  const contact = BTNS[3]
  contact.addEventListener("click", CONTACT)

  const hire_me = BTNS[4]
  hire_me.addEventListener("click", CONTACT)
  
}


function HOME() {
  const sections = document.getElementsByClassName("section")
  for(let i = 0; i < SECTIONS.length; i++){
    if (SECTIONS[i] == "home"){
      tempSection = sections[i]
      tempSection.classList.remove("hidden");
      temp = document.getElementById(SECTIONS[i])
      temp.classList.remove("inactive")
      temp.classList.add("active")
      continue
    }
    tempSection = sections[i]
    tempSection.classList.remove("hidden");
    temp = document.getElementById(SECTIONS[i])
    temp.classList.add("inactive")
    temp.classList.remove("active")
  }
  

  const home = document.getElementsByClassName("Home")

}

function ABOUT() {
  const sections = document.getElementsByClassName("section")
  for(let i = 0; i < SECTIONS.length; i++){
    if (SECTIONS[i] == "about"){
      tempSection = sections[i]
      tempSection.classList.remove("hidden");
      temp = document.getElementById(SECTIONS[i])
      temp.classList.remove("inactive")
      temp.classList.add("active")
      continue
    }
    tempSection = sections[i]
    tempSection.classList.add("hidden");
    temp = document.getElementById(SECTIONS[i])
    temp.classList.add("inactive")
    temp.classList.remove("active")
  }
}


function PORTFOLIO() {
  const sections = document.getElementsByClassName("section")
  for(let i = 0; i < SECTIONS.length; i++){
    if (SECTIONS[i] == "portfolio"){
      tempSection = sections[i]
      tempSection.classList.remove("hidden");
      temp = document.getElementById(SECTIONS[i])
      temp.classList.remove("inactive")
      temp.classList.add("active")
      continue
    }
    tempSection = sections[i]
    tempSection.classList.add("hidden");
    temp = document.getElementById(SECTIONS[i])
    temp.classList.add("inactive")
    temp.classList.remove("active")

  }
}

function CONTACT() {
  const sections = document.getElementsByClassName("section")
  for(let i = 0; i < SECTIONS.length; i++){
    if (SECTIONS[i] == "contact"){
      tempSection = sections[i]
      tempSection.classList.remove("hidden");
      temp = document.getElementById(SECTIONS[i])
      temp.classList.remove("inactive")
      temp.classList.add("active")
      continue
    }
    tempSection = sections[i]
    tempSection.classList.add("hidden");
    temp = document.getElementById(SECTIONS[i])
    temp.classList.add("inactive")
    temp.classList.remove("active")

  }
}


//When click the download button

const download = (p, f) => {
  const anchor = document.createElement('a');
  anchor.href = p;
  anchor.download = f;
  document.body.appendChild(anchor);
  anchor.click();
  document.body.removeChild(anchor);
};




window.addEventListener('DOMContentLoaded', init);
