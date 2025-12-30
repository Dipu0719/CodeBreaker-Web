{/* <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
    const input = document.querySelector('input[name="guess"]');
    input.addEventListener('input', function() {
        // This logic prevents users from typing anything except numbers
        this.value = this.value.replace(/[^0-9]/g, '');
        
        // This logic warns them if they use duplicate numbers
        const digits = this.value.split('');
        const uniqueDigits = new Set(digits);
        if (digits.length !== uniqueDigits.size) {
            input.style.borderColor = "red";
        } else {
            input.style.borderColor = "#ddd";
        }
    });
</script> */}


// --- [1] Input Validation Logic ---
const input = document.querySelector('input[name="guess"]');

if (input) {
    input.addEventListener('input', function() {
        // Prevent typing non-numbers
        this.value = this.value.replace(/[^0-9]/g, '');
        
        // Warn if digits are not unique (turns border red)
        const digits = this.value.split('');
        const uniqueDigits = new Set(digits);
        if (digits.length !== uniqueDigits.size) {
            input.style.borderColor = "#ff4757";
            input.style.boxShadow = "0 0 5px #ff4757";
        } else {
            input.style.borderColor = "#ddd";
            input.style.boxShadow = "none";
        }
    });
}

// --- [2] Cheat Mode Logic ---
// Press 'H' to see the secret code in the browser console
document.addEventListener('keydown', (e) => {
    if (e.key.toLowerCase() === 'h') {
        console.log("Developer Hint: Keep guessing! Use unique digits.");
    }
});