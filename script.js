function appendToDisplay(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = "";
}

function calculate() {
    try {
        document.getElementById("display").value = eval(document.getElementById("display").value);
    } catch {
        document.getElementById("display").value = "Error";
    }
}
document.addEventListener("keydown", function(event) {
    let key = event.key;
    
    // Allow numbers (0-9) and operators (+, -, *, /, .)
    if (/[0-9+\-*/.]/.test(key)) {
        appendToDisplay(key);
    }
    
    // Enter key to calculate
    if (key === "Enter") {
        calculate();
    }
    
    // Backspace key to delete one character
    if (key === "Backspace") {
        let display = document.getElementById("display");
        display.value = display.value.slice(0, -1);
    }

    // Escape key or "C" to clear the display
    if (key === "Escape" || key.toLowerCase() === "c") {
        clearDisplay();
    }
});