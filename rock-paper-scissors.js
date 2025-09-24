const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'scissors'|| userInput === 'paper' || userInput === 'bomb') {
    return userInput;
  } else {
    console.log('Incorrect Input!')
  }
}

const getComputerChoice = () => {
  let num = Math.floor(Math.random() * 3);
  if (num === 0) {
    return 'rock';
  } else if (num === 1) {
    return 'paper';
  } else {
    return 'scissors';
  }
}

const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === 'bomb') {
    return 'Boom! You win!';
  }
  if (userChoice === computerChoice) {
    return 'game is a tie.';
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'scissors') {
      return 'You win!';
    } else {
      return 'You lose :(';
    }
  } else if (userChoice === 'paper') {
    if (computerChoice === 'scissors') {
      return 'You lose :(';
    } else {
      return 'You win!';
    }
  } else if (userChoice === 'scissors'){
    if (computerChoice === 'rock') {
      return 'You lose :(';
    } else {
      return 'You win!';
    }
  }
}

const playGame = () => {
  let userChoice = getUserChoice('bomb')
  let computerChoice = getComputerChoice()
  console.log('The computer chose ' + computerChoice +'.')
  console.log(determineWinner(userChoice,computerChoice))
}
playGame()