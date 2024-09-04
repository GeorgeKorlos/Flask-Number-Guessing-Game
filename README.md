# Flask Number Guessing Game

This repository contains a simple Flask web application where users can guess a randomly generated number between 0 and 9. The application provides feedback on whether the guess is too high, too low, or correct, and displays a corresponding GIF.

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

- Python 3.x
- Flask

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/flask-number-guessing-game.git
   cd flask-number-guessing-game
   
2. **Install Dependencies Install Flask using pip if you haven't already:**
    ```bash
    pip install Flask
    
3. **Run the Application Start the Flask application by running:**
    ```bash
    python main.py

4. **Access the Application Open your web browser and go to http://127.0.0.1:5000/ to start the game.**

**How to Play**
- The game will ask you to guess a number between 0 and 9.
- Enter your guess by appending it to the URL (e.g., http://127.0.0.1:5000/5).
- The application will respond with feedback on whether your guess is too high, too low, or correct, along with a fun GIF.

**Project Structure**
- main.py: The main application file containing the Flask routes and game logic.
