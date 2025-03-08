// Font size increase and decrease
// Default font size in pixels
const DEFAULT_FONT_SIZE = 16; // Adjust this to match your default font size
let currentQuestion = 0;
const questions = {
    0: {
        text: "Hello! How can I help you? Please choose a category below.",
        options: ["Blindness and Low Vision", "Deaf and Hard of Hearing", "Locomotor Disabilities", "Autism and Intellectual Disabilities", "Multiple Disabilities"],
        next: {
            "Blindness and Low Vision": 1,
            "Deaf and Hard of Hearing": 2,
            "Locomotor Disabilities": 3,
            "Autism and Intellectual Disabilities": 4,
            "Multiple Disabilities": 5
        }
    },
    1: {
        text: "What best describes your condition?",
        options: ["I have complete blindness", "I have partial vision"],
        next: { 
            "I have complete blindness": 6,
            "I have partial vision": 7 
        }
    },
    2: {
        text: "Which best describes your hearing ability?",
        options: ["I am completely deaf", "I have some hearing loss"],
        next: { 
            "I am completely deaf": 8,
            "I have some hearing loss": 9 
        }
    },
    3: {
        text: "What mobility aids do you use?",
        options: ["Wheelchair", "Cane", "None"],
        next: { 
            "Wheelchair": 10,
            "Cane": 11,
            "None": 12 
        }
    },
    4: {
        text: "What type of work environment do you thrive in?",
        options: ["Structured and predictable environments", "Flexible and dynamic environments"],
        next: { 
            "Structured and predictable environments": 13, 
            "Flexible and dynamic environments": 14 
        }
    },
    5: {
        text: "What challenges do you face in finding employment?",
        options: ["Communication", "Mobility", "Social interaction"],
        next: { 
            "Communication": 15, 
            "Mobility": 16, 
            "Social interaction": 17 
        }
    },
    6: { 
        text: "Would you prefer a job that allows for remote work or direct interaction?", 
        options: ["Remote work", "Direct interaction"],
        next: { "Remote work": 18, "Direct interaction": 19 }
    },
    7: { 
        text: "Are you comfortable using screen reading software?", 
        options: ["Yes", "No"],
        next: { "Yes": 20, "No": 21 }
    },
    8: { 
        text: "Do you prefer jobs with visual communication methods?", 
        options: ["Yes", "Not necessarily"],
        next: { "Yes": 22, "Not necessarily": 23 }
    },
    9: { 
        text: "Are you comfortable with lip reading?", 
        options: ["Yes", "No"],
        next: { "Yes": 24, "No": 25 }
    },
    10: { 
        text: "Do you need a workplace that is wheelchair accessible?", 
        options: ["Yes", "No"],
        next: { "Yes": 26, "No": 27 }
    },
    11: { 
        text: "Do you prefer jobs that involve minimal mobility?", 
        options: ["Yes", "No"],
        next: { "Yes": 28, "No": 29 }
    },
    12: { 
        text: "Are you comfortable with tasks that require a lot of movement?", 
        options: ["Yes", "No"],
        next: { "Yes": 30, "No": 31 }
    },
    13: { 
        text: "Do you prefer working with specific tasks or larger projects?",
        options: ["Specific tasks", "Larger projects"],
        next: { "Specific tasks": 32, "Larger projects": 33 }
    },
    14: { 
        text: "Are you comfortable with frequent changes in tasks?", 
        options: ["Yes", "No"],
        next: { "Yes": 34, "No": 35 }
    },
    15: { 
        text: "Would you prefer jobs with team interaction or independent work?",
        options: ["Team interaction", "Independent work"],
        next: { "Team interaction": 36, "Independent work": 37 }
    },
    16: { 
        text: "Do you need accommodations for mobility requirements?", 
        options: ["Yes", "No"],
        next: { "Yes": 38, "No": 39 }
    },
    17: {
        text: "Do you require support in social interactions at work?",
        options: ["Yes", "No"],
        next: { "Yes": 40, "No": 41 }
    },
    18: { text: "Thank you! We will find remote work options for you." },
    19: { text: "Thank you! We will find jobs that involve direct interaction." },
    20: { text: "Thank you! We will find jobs compatible with screen readers." },
    21: { text: "Thank you! We will find jobs that do not require screen reading." },
    22: { text: "Thank you! We will find jobs with visual communication methods." },
    23: { text: "Thank you! We will find jobs suitable for you." },
    24: { text: "Thank you! We will find jobs that utilize lip reading." },
    25: { text: "Thank you! We will find jobs that do not rely on lip reading." },
    26: { text: "Thank you! We will find wheelchair-accessible workplaces." },
    27: { text: "Thank you! We will find jobs that do not require wheelchair access." },
    28: { text: "Thank you! We will find jobs with minimal mobility requirements." },
    29: { text: "Thank you! We will find jobs that require some movement." },
    30: { text: "Thank you! We will find jobs requiring physical movement." },
    31: { text: "Thank you! We will find jobs that do not require much movement." },
    32: { text: "Thank you! We will find jobs with specific task-based work." },
    33: { text: "Thank you! We will find jobs involving larger projects." },
    34: { text: "Thank you! We will find jobs with dynamic task changes." },
    35: { text: "Thank you! We will find structured jobs with minimal changes." },
    36: { text: "Thank you! We will find jobs with team interaction." },
    37: { text: "Thank you! We will find independent work opportunities." },
    38: { text: "Thank you! We will find jobs with mobility accommodations." },
    39: { text: "Thank you! We will find jobs that do not require accommodations." },
    40: { text: "Thank you! We will find jobs with social interaction support." },
    41: { text: "Thank you! We will find jobs that do not require social support." }
};

function initializeChat() {
    console.log("Chat initialized"); // Debugging
    document.querySelector(".message-content").innerHTML = ""; // Reset chat
    currentQuestion = 0;
    displayQuestion(currentQuestion);
}

function displayQuestion(id) {
    console.log("Displaying question:", id); // Debugging
    const question = questions[id];
    const messageContent = document.querySelector(".message-content");

    if (!messageContent) {
        console.error("Message content element not found!"); // Debugging
        return;
    }

    const botMessage = document.createElement("li");
    botMessage.className = "message bot-message";
    botMessage.innerHTML = `<span class="text">${question.text}</span>`;
    messageContent.appendChild(botMessage);

    if (question.options) {
        const optionsContainer = document.createElement("div");
        optionsContainer.className = "options-container";

        question.options.forEach(option => {
            const optionButton = document.createElement("button");
            optionButton.className = "option-btn";
            optionButton.textContent = option;
            optionButton.addEventListener("click", () => handleOptionClick(option));
            optionsContainer.appendChild(optionButton);
        });
        messageContent.appendChild(optionsContainer);
    } else {
        const endMessage = document.createElement("li");
        endMessage.className = "message bot-message";
        endMessage.innerHTML = `<span class="text">Thank you! The conversation has ended.</span>`;
        messageContent.appendChild(endMessage);
    }

    messageContent.scrollTop = messageContent.scrollHeight;
}

function handleOptionClick(selectedOption) {
    console.log("Option clicked:", selectedOption); // Debugging
    const userMessage = document.createElement("li");
    userMessage.className = "message user-message";
    userMessage.innerHTML = `<span class="text">${selectedOption}</span>`;
    document.querySelector(".message-content").appendChild(userMessage);

    const nextQuestionId = questions[currentQuestion].next[selectedOption];
    currentQuestion = nextQuestionId !== undefined ? nextQuestionId : currentQuestion;

    setTimeout(() => {
        displayQuestion(currentQuestion);
    }, 500);
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded"); // Debugging
    document.getElementById("chatButton").addEventListener("click", () => {
        console.log("Chat button clicked"); // Debugging
        document.getElementById("chatContainer").style.display = "block";
        initializeChat();
    });

    document.getElementById("closeChat").addEventListener("click", () => {
        console.log("Close chat button clicked"); // Debugging
        document.getElementById("chatContainer").style.display = "none";
    });
});

// Function to change font size
function changeFontSize(step) {
    const htmlElement = document.documentElement;
    const currentSize = parseFloat(window.getComputedStyle(htmlElement).fontSize);
    const newSize = currentSize + step;
    htmlElement.style.fontSize = `${newSize}px`;
}

// Function to reset font size to default
function resetFontSize() {
    document.documentElement.style.fontSize = `${DEFAULT_FONT_SIZE}px`;
}

// Event listeners for buttons
document.getElementById('increase-font-size').addEventListener('click', () => {
    changeFontSize(2); // Increase font size by 2px
});

document.getElementById('decrease-font-size').addEventListener('click', () => {
    changeFontSize(-2); // Decrease font size by 2px
});

document.getElementById('reset-font-size').addEventListener('click', () => {
    resetFontSize(); // Reset font size to default
});



document.getElementById('theme-selector').addEventListener('change', function() {
    const selectedTheme = this.value;
  
    switch (selectedTheme) {
        case 'theme1':
            setThemeVariables('#00B98E', '#FF6922', '#EFFDF5', '#0E2E50'); // High Contrast Black & White
            break;  
        case 'theme2':
            setThemeVariables('#FFFFFF', '#000000', '#000000', '#FFFFFF'); // High Contrast White & Black
            break;
        case 'theme3':
            setThemeVariables('#1E90FF', '#FFD700', '#F0F8FF', '#00008B'); // High Contrast Blue & Gold
            break;
        case 'theme4':
            setThemeVariables('#8B0000', '#FFA07A', '#FFE4E1', '#8B0000'); // High Contrast Red & Light Coral
            break;
        case 'theme5':
            setThemeVariables('#006400', '#ADFF2F', '#F0FFF0', '#006400'); // High Contrast Green & Green Yellow
            break;
    }
});


function setThemeVariables(primaryColor, secondaryColor, lightColor, darkColor) {
    document.documentElement.style.setProperty('--primary', primaryColor);
    document.documentElement.style.setProperty('--secondary', secondaryColor);
    document.documentElement.style.setProperty('--light', lightColor);
    document.documentElement.style.setProperty('--dark', darkColor);
}

(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top');
        } else {
            $('.nav-bar').removeClass('sticky-top');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });
    
})(jQuery);

