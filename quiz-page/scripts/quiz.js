// Functions
function buildQuiz(){ // Starts the quiz.

    // Store HTML to insert.
    const output = []; 

    // For each Q...
    questionTexts.forEach(
        (currentQuestion, questionNumber) => {
        
        // Store answer-buttons.
        const answerlist = []; 

        // For each answer in the Q... 
        for(letter in currentQuestion.answers){

            // Turn answers into HTML buttons.
            answerlist.push(
                `<button class="answer-button">${currentQuestion.answers[letter]}</button>`
            );
        }

        // Add questions and answer-buttons to output.
        output.push(
            `<div class="slide">
                <div class="question"> ${currentQuestion.question} </div>
                <div class="answers"> ${answerlist.join('')} </div>
            </div>`
            );
        }    
    );    

        // Combine into a string of HTML and display.
        quizContainer.innerHTML = output.join('');
        // console.log(output)
}

function storeResults(answerInteger){ // Adds chosen answers to an array.
    answerArray.push(answerInteger);
    console.log(answerArray);
}

function showSlide(n, alsofade = false) { // Fades in current slide.
    if (alsofade === true) {
        fadeout(slides[currentSlide]);
    } 

    slides[currentSlide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    currentSlide = n;
    delayFadeIn();
    // console.log(currentSlide);
}

function fadeout(element) { // Fades out a slide.
    var op = 1;  // Initial opacity.
    var timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
            element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
        // console.log(element.style.opacity);
    }, 50);
}

function fadein(element) { // Fades in a slide.
    var op = 0.1;  // Initial opacity.
    element.style.display = 'block';
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.14;
        // console.log(element.style.opacity);
    }, 35);
}

var fadeVar;

function delayFadeIn() { // Puts a delay on fadein.
    fadeVar = setTimeout(function() { fadein(slides[currentSlide]); }, 2000);
}

// Variables
var answerArray = [];
const quizContainer = document.getElementById('quiz');
const answerSubmit = document.querySelectorAll('button');
const questionTexts = [
    {
        question: 'QUESTION 1',
        answers: {
            a: 'ANSWER 1A',
            b: 'ANSWER 1B',
            c: 'ANSWER 1C'
        },
    },
    {
        question: 'QUESTION 2',
        answers: {
            a: 'ANSWER 2A',
            b: 'ANSWER 2B',
            c: 'ANSWER 2C'
        },
    },
    {
        question: 'QUESTION 3',
        answers: {
            a: 'ANSWER 3A',
            b: 'ANSWER 3B',
            c: 'ANSWER 3C'
        }
    },
    {
        question: 'END OF QUIZ',
        answers: {}
    }
];

// Kick things off
buildQuiz(); // Call to enable first Q.

// Pagination variables
const answerSet = document.getElementsByClassName("answers");
const answerButtons = document.getElementsByClassName("answer-button")
const slides = document.querySelectorAll(".slide");
const returnButton = document.getElementById("return-button");
let currentSlide = 0;

// Show the first slide
showSlide(currentSlide);

// Two more functions
function showNextSlide() { // Fades out current slide, calls showSlide() for current + 1.

    if (currentSlide === slides.length - 1) {
        fadeout(slides[currentSlide]);
    } else {
        fadeout(slides[currentSlide]);
        showSlide(currentSlide + 1);
    }
}

function backtoStart() { // Resets current slide.
    let currentSlide = 0;
    answerArray.length = 0;
    showSlide(currentSlide, alsofade = true);
} 

// Event listeners
for (let i = 0 ; i < answerButtons.length; i++) { // Go to next slide on button click.
    answerButtons[i].addEventListener('click', showNextSlide, false); 
    answerButtons[i].addEventListener('click', function() {console.log(this);});
    answerButtons[i].addEventListener('click', storeResults.bind(null, i), false);
    // answerButtons[i].addEventListener('click', function() {storeResults(i);}, false);
}

returnButton.addEventListener('click', backtoStart, false); // Reset current slide on button click.

