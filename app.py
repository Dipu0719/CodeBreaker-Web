from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "logic_master_key_2025"

def generate_secret_code(length):
    secret = "".join(random.sample("0123456789", length))
    print(f"--- DEBUG: The secret code is {secret} ---") # This shows in your terminal!
    return secret

@app.route("/", methods=["GET", "POST"])
def index():
    # Set default difficulty (4 digits) if not already set
    if "code_length" not in session:
        session["code_length"] = 4
    
    # Initialize game state
    if "secret" not in session:
        session["secret"] = generate_secret_code(session["code_length"])
        session["attempts"] = []
        session["remaining"] = 10 
    
    message = ""
    status = "playing"

    if request.method == "POST":
        # Check if the user is changing difficulty
        if "difficulty" in request.form:
            session["code_length"] = int(request.form.get("difficulty"))
            session.pop("secret", None) # Clear secret to trigger new game
            return redirect(url_for('index'))

        # Check if the user is making a guess
        user_guess = request.form.get("guess")
        if user_guess:
            secret = session["secret"]
            length = session["code_length"]

            # Validation Logic: Check for unique digits
            if len(set(user_guess)) < length:
                message = f"Logic Error: Please use {length} UNIQUE digits!"
            else:
                session["remaining"] -= 1
                bulls = 0
                cows = 0
                
                # Core Game Logic: Calculate Bulls and Cows
                for i in range(length):
                    if user_guess[i] == secret[i]:
                        bulls += 1
                    elif user_guess[i] in secret:
                        cows += 1
                
                result = f"Guess: {user_guess} | {bulls} Bulls, {cows} Cows"
                session["attempts"].insert(0, result)

                if bulls == length:
                    message = "🏆 BRILLIANT! You cracked the code!"
                    status = "won"
                    session.pop("secret", None)
                elif session["remaining"] <= 0:
                    message = f"💀 GAME OVER! The code was {secret}."
                    status = "lost"
                    session.pop("secret", None)
            
            session.modified = True 

    return render_template("index.html", 
                           attempts=session.get("attempts"), 
                           message=message, 
                           remaining=session.get("remaining"),
                           status=status,
                           length=session["code_length"])

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)