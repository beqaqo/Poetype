// Configuration and state management
const GameState = {
    timer: null,
    startTime: 0,
    isGameOver: false
};

const TOP_BORDER = 275;
const IGNORED_SIMBOLS = [',', '„', '”', '“', '"', '-', '_', '—', '.', '!', '?', ':', ';', '(', ')', '[', ']', '{', '}', '*'];

// DOM element cache
const Elements = {
    game: null,
    words: null,
    time: null,
    cursor: null
};

// Initialize the game
function initGame() {
    // Cache DOM elements
    Elements.game = document.getElementById('game');
    Elements.words = document.getElementById('words');
    Elements.time = document.getElementById('time');
    Elements.cursor = document.getElementById('cursor');

    // Set up event listeners
    Elements.game.addEventListener('keyup', handleKeyPress);

    // Start a new game
    resetGame();
}

// Reset game to starting state
function resetGame() {
    // Clear existing timer
    if (GameState.timer) {
        clearInterval(GameState.timer);
    }

    GameState.timer = null;
    GameState.startTime = 0;
    GameState.isGameOver = false;

    // Reset UI
    const firstLetter = document.querySelector('.letter');
    if (firstLetter) {
        firstLetter.classList.add('current');

        // Restore line alignment functionality
        alignFirstLineInView();
        updateCursorPosition();
    }

    // Reset game UI
    Elements.game.classList.remove('over');
}

// Ensure first line is visible at start
function alignFirstLineInView() {
    const currentLetter = document.querySelector('.letter.current');
    if (!currentLetter) return;

    while (currentLetter.getBoundingClientRect().top > TOP_BORDER) {
        const currentMargin = parseInt(Elements.words.style.marginTop || '0');
        Elements.words.style.marginTop = (currentMargin - 55) + 'px';
    }

    while (currentLetter.getBoundingClientRect().top < TOP_BORDER - 10) {
        const currentMargin = parseInt(Elements.words.style.marginTop || '0');
        Elements.words.style.marginTop = (currentMargin + 55) + 'px';
    }
    updateCursorPosition();
}

// Handle key press events
function handleKeyPress(event) {
    if (GameState.isGameOver) return;

    const key = event.key;
    let currentLetter = document.querySelector('.letter.current');

    // Ignore modifier keys
    if (['Shift', 'Control', 'Alt', 'Meta', 'CapsLock', 'Tab', 'Escape'].includes(key)) return;

    // Check if we have a current letter to work with
    if (!currentLetter) return;

    // Start timer on first key press
    if (!GameState.timer) {
        startTimer();
    }

    // Check game end condition
    if (handleLastLetter(currentLetter)) {
        return;
    }

    // Handle different key types
    if (key.length === 1) {
        handleLetterKey(key, currentLetter);
        // If we just typed a space and the next character is also a space, skip it
        currentLetter = document.querySelector('.letter.current');
        if (handleLastLetter(currentLetter)) {
            return;
        }
        while (currentLetter.textContent.trim() === '' && currentLetter.previousSibling.textContent.trim() === '') {
            moveClassRight(currentLetter);
            currentLetter = document.querySelector('.letter.current');
            keepCurrentLetterInView(currentLetter);
        }
        while (IGNORED_SIMBOLS.includes(currentLetter.textContent)) {
            currentLetter.classList.add("correct");
            moveClassRight(currentLetter);
            currentLetter = document.querySelector('.letter.current');
            handleLastLetter(currentLetter);
        }
    } else if (key === 'Backspace') {
        handleBackspace(currentLetter, event);
    }

    // Update UI
    updateCursorPosition();
    keepCurrentLetterInView(key);
}

// Handle single letter key presses
function handleLetterKey(key, currentLetter) {
    const expectedLetter = currentLetter.innerHTML;
    const isCorrect = key === expectedLetter;

    // Mark current letter as correct/incorrect and move to next
    currentLetter.classList.add(isCorrect ? "correct" : "incorrect");
    moveClassRight(currentLetter)
}

function moveClassRight(currentLetter) {
    currentLetter.classList.remove("current");

    if (currentLetter.nextSibling) {
        currentLetter.nextSibling.classList.add("current");
    }
}

function moveClassLeft(currentLetter) {
    currentLetter.classList.remove("current");
    const previousLetter = currentLetter.previousSibling;
    previousLetter.classList.add("current");

    // Reset letter state
    previousLetter.classList.remove("correct");
    previousLetter.classList.remove("incorrect");
}

function handleBackspace(currentLetter, event) {
    if (!currentLetter.previousSibling) return;
    // Check if previous letter is on the same line
    const currentRect = currentLetter.getBoundingClientRect();
    const prevRect = currentLetter.previousSibling.getBoundingClientRect();
    if (currentRect.top !== prevRect.top) return;

    if (event.ctrlKey) {
        if (currentLetter.previousSibling.textContent.trim() === '') {
            moveClassLeft(currentLetter);
            currentLetter = document.querySelector('.letter.current');
        }
        // Move left until we reach a space or the start of the text
        while (currentLetter.previousSibling && currentLetter.previousSibling.textContent.trim() !== '') {
            moveClassLeft(currentLetter);
            currentLetter = document.querySelector('.letter.current');
        }

    } else {
        // Normal Backspace (move one character back)
        while (IGNORED_SIMBOLS.includes(currentLetter.previousSibling.textContent)) {
            moveClassLeft(currentLetter);
            currentLetter = document.querySelector('.letter.current');
        }
        moveClassLeft(currentLetter);
    }
}

function handleLastLetter(currentLetter) {
    if (!currentLetter.nextSibling) {
        endGame();
        return true;
    }
}

// Keep current letter visible in view
function keepCurrentLetterInView(key) {
    const currentLetter = document.querySelector('.letter.current');
    if (!currentLetter) return;

    const currentRect = currentLetter.getBoundingClientRect();
    const prevRect = currentLetter.previousSibling
        ? currentLetter.previousSibling.getBoundingClientRect()
        : currentRect;

    if (currentRect.top !== prevRect.top && key !== 'Backspace') {
        const currentMargin = parseInt(Elements.words.style.marginTop || '0');
        Elements.words.style.marginTop = (currentMargin - (currentRect.top - prevRect.top)) + 'px';
        updateCursorPosition();
    }
}

// Start the game timer
function startTimer() {
    GameState.startTime = Date.now();
    GameState.timer = setInterval(() => {
        const secondsPassed = Math.round((Date.now() - GameState.startTime) / 1000);
        Elements.time.textContent = `${secondsPassed + 1}`;
    }, 1000);
}

// End the game
function endGame() {
    if (GameState.isGameOver) return;

    GameState.isGameOver = true;
    clearInterval(GameState.timer);
    Elements.game.classList.add('over');

    // Display WPM score
    const count = parseInt(Elements.words.dataset.count) || 0;
    const time = parseFloat(Elements.time.textContent) || 1;
    const wpm = Math.round((count / time) * 60);
    Elements.time.innerHTML = `<span class="font-color">წუთში</span> ${wpm} <span class="font-color">სიტყვა</span>`;
}

// Update cursor position
function updateCursorPosition() {
    const currentLetter = document.querySelector('.letter.current');
    if (!currentLetter || !Elements.cursor) return;

    Elements.cursor.style.animation = 'none';

    const rect = currentLetter.getBoundingClientRect();
    Elements.cursor.style.top = `${rect.top}px`;
    Elements.cursor.style.left = `${rect.left}px`;
}

// Initialize the game when DOM is ready
document.addEventListener('DOMContentLoaded', initGame);

// Ensure first line is aligned on load
window.onload = function () {
    alignFirstLineInView();
    updateCursorPosition();
};