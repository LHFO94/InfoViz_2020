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
        question: 'A lion is missing from the circus.<br> Where was it last seen?',
        answers: {
            a: 'At the empty parking lot.',
            b: 'On its way home.',
            c: 'Strapped to a remote control plane.',
            d: 'At the circus.',
            e: 'Chasing lawnmowers.'
        },
    },
    {
        question: 'Which has the strongest smell?',
        answers: {
            a: 'Success.',
            b: 'A blank canvas.',
            c: 'Personalized marketing.',
            d: 'Lies.',
            e: 'Home cooking.'
        },
    },
    {
        question: 'Who just parked your car?',
        answers: {
            a: 'I have a self-driving car.',
            b: 'Check the security footage.',
            c: 'The bus driver.',
            d: 'My second husband.',
            e: 'You mean my helicopter?'
        }
    },
    {
        question: 'What was the last thing you lost?',
        answers: {
            a: 'My phone.',
            b: '10 kilos.',
            c: 'Myself, on the dance floor.',
            d: 'My voice.',
            e: 'My job.'
        }
    },
    {
        question: 'What turns the streetlights on?',
        answers: {
            a: 'The passage of time.',
            b: 'Nobody.',
            c: 'Fear of the dark.',
            d: 'Property developers.',
            e: 'The desire to be seen.'
        }
    },
    {
        question: 'Where do you disappear?',
        answers: {
            a: 'In the spotlight.',
            b: 'Under the bridge.',
            c: 'The cinema at noon.',
            d: 'Behind the desk.',
            e: 'At the checkout queue.'
        }
    },
    {
        question: 'The elevator doors close.<br>You\'re with a laundry worker.<br>They ask you to be quiet.<br>You haven\'t said anything. What do you reply?',
        answers: {
            a: '<i>I have been silent long enough.</i>',
            b: '<i>Next time, take the stairs.</i>',
            c: 'Nothing.',
            d: '<i>That suit is dry-clean only.</i>',
            e: '<i>Where are we?</i>'
        }
    },
    {
        question: 'Who would you lose a fight to?',
        answers: {
            a: 'An Instagram filter.',
            b: 'My kids.',
            c: 'The apple that gave us gravity.',
            d: 'The temptation of a perfect crime.',
            e: 'Bulldozers.'
        }
    },
    {
        question: 'What do you see on your way to work?',
        answers: {
            a: 'Old men in new apartment blocks.',
            b: 'The rising sun.',
            c: 'The corridor ahead lights up.',
            d: 'Empty shopping malls.',
            e: 'My bad decisions.'
        }
    },
    {
        question: 'What is the greatest miracle of the 21st Century?',
        answers: {
            a: 'On-demand streaming.',
            b: 'The trans-atlantic highway.',
            c: 'Space tourism.',
            d: 'The persistence of paper mail.',
            e: 'Minecraft.'
        }
    },
    {
        question: 'How are you getting home?',
        answers: {
            a: 'I\'m already there.',
            b: 'Ask my driver.',
            c: 'Where\'s home?',
            d: 'With a map.',
            e: 'By elevator.'
        }
    },
    {
        question: 'Where do the stars shine brightest?',
        answers: {
            a: 'Hollywood.',
            b: 'I have a concussion.',
            c: 'On the American flag.',
            d: 'In a dark room.',
            e: 'When cars reflect the streetlights.'
        }
    },
    {
        question: 'Why do you wear hats?',
        answers: {
            a: 'My parents made hats.',
            b: 'I\'ve lost my wig.',
            c: 'Why don\'t you?',
            d: 'A man is only as tall as his hat.',
            e: 'I\'m not wearing anything else.'
        }
    },
    {
        question: 'You\'re walking down the pavement.<br>A familiar face sits by the cafe window.<br>It\'s a teacher from high school.<br>What happened to them?',
        answers: {
            a: 'Revolution.',
            b: 'Children.',
            c: 'The lottery.',
            d: 'Pornography.',
            e: 'Vietnam.'
        }
    },
    {
           question: 'Where is your somewhere?',
           answers: {
               a: 'Europe.',
               b: 'North America.',
               c: 'The Middle East.',
               d: 'Asia.',
               e: 'South America.'
           },
       },
    {
        question: 'END OF QUIZ',
        answers: {a: 'CONTINUE'}
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
console.log(slides.length);

// Two more functions
function showNextSlide() { // Fades out current slide, calls showSlide() for current + 1.

    if (currentSlide === slides.length - 1) {
        fadeout(slides[currentSlide]);
    } else {
        fadeout(slides[currentSlide]);
        showSlide(currentSlide + 1);
    }
    if(answerArray.length === 15) {
         $.ajax({type:"Post", url:"/quiz/", data: {"col_filter":answerArray} })
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
