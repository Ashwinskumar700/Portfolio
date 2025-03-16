document.addEventListener('DOMContentLoaded', () => {
    const toggleSwitch = document.querySelector('#dark-mode-toggle');
    if (toggleSwitch) {
        toggleSwitch.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }
});


// Load theme from local storage on page load
window.addEventListener('load', () => {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
    }
});
const button = document.getElementById('my-button');
if (button) {
    button.addEventListener('click', () => {
        console.log('Button clicked!');
    });
}

const textElement = document.getElementById('text-element');
if (textElement) {
    textElement.textContent = "New Content";
}

document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('my-button');
    if (button) {
        button.addEventListener('click', () => {
            console.log('Button clicked!');
        });
    }

    const textElement = document.getElementById('text-element');
    if (textElement) {
        textElement.textContent = "New Content";
    }
});
