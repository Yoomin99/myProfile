function init() {
    // Add event listener for "Add Ingredient" Button Press
    const pathButton = document.querySelector('.path');
    pathButton.addEventListener('click', addIngredient);
  
    // Add event listener for "Remove Ingredient" Button Press
    const Button2048 = document.querySelector('.2048');
    Button2048.addEventListener('click', removeIngredient);
  
    // Add event listener for "Add Step" Button Press
    const gomokuButton = document.querySelector('.Gomoku');
    gomokuButton.addEventListener('click', addStep);
  
    // Add event listener for "Remove Step" Button Press
    const blackjackButton = document.querySelector('.BlackJack');
    blackjackButton.addEventListener('click', removeStep);
  
  }
  
  window.addEventListener('DOMContentLoaded', init);