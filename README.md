# 100-MINI-PYTHON-PROJECTS
A curated collection of 100 beginner-to-intermediate Python projects designed to build coding skills, logic, and portfolio diversity. From simple scripts to games and automation tools, this repo serves as a practical roadmap for mastering Python.

# 100 Mini Python Projects 🐍

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Welcome to **100 Mini Python Projects**! This repository is a journey through 100 practical, fun, and challenging Python projects. Whether you are a beginner looking to understand the basics or an intermediate developer wanting to sharpen your problem-solving skills, this collection has something for everyone.

## 🚀 Goals of this Repo
* **Build Muscle Memory:** Reinforce syntax and core concepts through repetition.
* **Diverse Applications:** Explore different domains like automation, games, web scraping, and data handling.
* **Portfolio Ready:** Create a library of working code to showcase your skills.

## 📂 Project Structure

Each project is contained in its own folder (or file) with a descriptive name. Inside, you will typically find:
* `main.py` (The source code)
* `requirements.txt` (If external libraries are needed)
* `README.md` (Specific instructions for that project)

# 📋 The Python Master Roadmap (1-100)

This roadmap integrates practical management systems, text-based simulations, and engineering challenges. Checked items (`[x]`) indicate completed projects.

---

## 1. Basic Management Systems (OOP Foundations)
**Focus:** Classes, Object interactions, and State management.

- [x] **01. Hello World with a Twist**
  - **Goal:** Input user name/age, output specific greetings based on time of day (using `datetime`).
- [x] **02. Library Management System**
  - **Classes:** `Book` (title, author, isbn, status), `Member`, `Library`.
  - **Features:** `add_book`, `lend_book`, `return_book`.
- [x] **03. Banking System Simulation**
  - **Classes:** `Account` (parent), `SavingsAccount` (min balance), `CurrentAccount` (overdraft).
  - **Features:** Encapsulation (`__balance`), polymorphic `withdraw` methods.
- [ ] **04. Employee Payroll System**
  - **Classes:** `Employee` (abstract), `FullTime` (fixed), `Contract` (hourly).
  - **Features:** Calculate monthly salary, tax deduction logic.
- [ ] **05. Smart Parking Lot**
  - **Classes:** `Vehicle` (plate, type), `Ticket` (timestamp), `ParkingLot`.
  - **Features:** Hourly fee calculation, spot availability tracking.

## 2. Python Games (Logic & Loops)
**Focus:** Game loops, Conditionals, and Randomness.

- [ ] **06. Text-Based RPG Game**
  - **Classes:** `Character` (parent), `Hero`, `Monster`.
  - **Features:** Turn-based combat loop, random damage calculation, inventory.
- [ ] **07. Deck of Cards (Blackjack/War)**
  - **Classes:** `Card` (suit, rank), `Deck` (list handling), `Hand`.
  - **Features:** `shuffle()`, `deal()`, value comparison logic.
- [ ] **08. Quiz Application**
  - **Classes:** `Question` (text, answer), `Quiz` (score tracking).
  - **Features:** Input validation (A/B/C/D), final percentage score.
- [ ] **09. Vending Machine Simulation**
  - **Classes:** `Item`, `Machine` (State Machine).
  - **Features:** Balance tracking, change dispensing algorithm.
- [ ] **10. Tic-Tac-Toe AI**
  - **Focus:** Grid management (2D Lists) and a simple Minimax algorithm or random bot.

## 3. Python Scripts (Data & File I/O)
**Focus:** Persistence (Saving data) and Automation.

- [ ] **11. Inventory Management System**
  - **Features:** JSON/CSV file saving. Add products, update stock levels, alert when low.
- [ ] **12. Expense Tracker**
  - **Features:** Log daily expenses to a file, categorize (Food, Travel), and read file to sum totals.
- [ ] **13. Junk File Cleaner**
  - **Features:** Recursively scan a directory and delete `.tmp` files older than 30 days.
- [ ] **14. Auto-Backup Script**
  - **Features:** Zip a specific folder and move it to a backup directory with a timestamped filename.
- [ ] **15. Clipboard Manager**
  - **Features:** Runs in background; saves the last 10 things you copied to a text file.

## 4. Text Processing & RegEx (NLP Basics)
**Focus:** String manipulation and pattern matching.

- [ ] **16. Plagiarism Checker**
  - **Features:** Compare two text files and calculate percentage similarity (Jaccard).
- [ ] **17. Email Extractor**
  - **Features:** Scan a text block and extract all valid emails using RegEx.
- [ ] **18. Markdown to HTML Converter**
  - **Features:** Parse `# Heading` and `**bold**` syntax into HTML tags.
- [ ] **19. Profanity Filter**
  - **Features:** Replace banned words in a sentence with `****` while preserving case.
- [ ] **20. Syntax Highlighter**
  - **Features:** Print Python code with keywords in color using ANSI escape codes.

## 5. Network Programming (Sockets)
**Focus:** How the internet works.

- [ ] **21. Local Chat Room:** Server/Client scripts for messaging.
- [ ] **22. Port Scanner:** Scan IP for open ports (21, 80, etc.).
- [ ] **23. P2P File Transfer:** Send an image from one script to another.
- [ ] **24. DDOS Simulator (Educational):** Stress test a local dummy server.
- [ ] **25. WiFi Password Extractor:** Retrieve saved system WiFi passwords.

## 6. Cybersecurity & Encryption
**Focus:** Protecting data.

- [ ] **26. Password Strength Checker:** Score entropy and character variety.
- [ ] **27. Caesar Cipher Tool:** Shift ASCII values to encrypt text.
- [ ] **28. Steganography:** Hide a text message inside an image file's bits.
- [ ] **29. Hash Verifier:** Compare MD5/SHA256 hashes for file integrity.
- [ ] **30. Keylogger (Ethical):** Log keystrokes to a local file for study.

## 7. Web Scraping (Data Harvesting)
**Focus:** Automating the web.

- [ ] **31. Job Post Scraper:** Fetch job titles/links to CSV.
- [ ] **32. Social Bot (Selenium):** Log in and like posts automatically.
- [ ] **33. Price Drop Notifier:** Monitor a URL; alert if price < target.
- [ ] **34. Wiki-Hopper:** Click random links until arriving at "Philosophy".
- [ ] **35. Image Crawler:** Download all `<img>` tags from a URL.

## 8. API Development (Backend)
**Focus:** Serving data via HTTP.

- [ ] **36. Weather API Wrapper:** Class to fetch OpenWeatherMap data.
- [ ] **37. Currency Converter API:** Flask app for currency exchange rates.
- [ ] **38. To-Do List API:** REST API (GET, POST, DELETE) for tasks.
- [ ] **39. URL Shortener:** Backend to map short codes to full URLs.
- [ ] **40. Login System:** Backend auth with password hashing.

## 9. Databases (SQL/NoSQL)
**Focus:** Persistent storage.

- [ ] **41. SQLite Contact Book:** Store Name/Phone using raw SQL.
- [ ] **42. Music Library (ORM):** SQLAlchemy for Artist/Song relationships.
- [ ] **43. NoSQL JSON Store:** Save Dictionaries as JSON documents.
- [ ] **44. CSV to SQL Importer:** Efficiently load massive CSVs to DB.
- [ ] **45. Leaderboard System:** Redis-style logic for high scores.

## 10. Data Analysis (Pandas)
**Focus:** Insights from data.

- [ ] **46. Data Cleaning Bot:** Remove duplicates/nulls from CSV.
- [ ] **47. Sales Trend Analyzer:** Group data by Month/Region.
- [ ] **48. Stock Correlation:** Calculate movement similarity of two stocks.
- [ ] **49. Census Demographics:** Analyze population/age averages.
- [ ] **50. Pokemon Stat Analyzer:** Find strongest types via average stats.

## 11. Data Visualization
**Focus:** Plotting and Charts.

- [ ] **51. Real-time CPU Graph:** Live plotting of system usage.
- [ ] **52. Heatmap of Activity:** Visualize active hours in a day.
- [ ] **53. 3D Terrain Plot:** Mathematical surface plotting.
- [ ] **54. Interactive Pie Chart:** Expenses chart with "explode" feature.
- [ ] **55. Word Cloud Generator:** Visualize most frequent words in text.

## 12. Computer Vision (OpenCV)
**Focus:** Image processing.

- [ ] **56. Face Detector:** Draw boxes around faces in photos.
- [ ] **57. Color Picker:** Get RGB/Hex from pixel clicks.
- [ ] **58. Document Scanner:** Perspective warping for scanned papers.
- [ ] **59. Motion Detector:** Trigger alarm on webcam pixel changes.
- [ ] **60. Watermark Adder:** Batch process images to add logos.

## 13. Audio & Signals
**Focus:** Sound processing.

- [ ] **61. Text-to-Speech:** Read text files aloud.
- [ ] **62. Audio Visualizer:** Frequency bars for MP3s.
- [ ] **63. Voice Recorder:** Record mic input to `.wav`.
- [ ] **64. Noise Remover:** Filter static from audio using Scipy.
- [ ] **65. Morse Code Translator:** Text to audio beeps.

## 14. Mathematics Simulations
**Focus:** Pure math and algorithmic visualization.

- [ ] **66. Pi Estimation (Monte Carlo):** Throw random "darts" to calculate Pi.
- [ ] **67. Prime Spiral (Ulam):** Visualizing prime number patterns on a grid.
- [ ] **68. Fractals (Julia Set):** Recursive image generation.
- [ ] **69. Sudoku Solver:** Backtracking algorithm implementation.
- [ ] **70. Fourier Series Drawing:** Drawing shapes with rotating circles.

## 15. Physics Simulations
**Focus:** Modeling the physical world.

- [ ] **71. Projectile Motion:** Cannonball trajectory with gravity/wind.
- [ ] **72. N-Body Gravity:** Solar system orbit simulation.
- [ ] **73. Pendulum Wave:** Harmonic motion of multiple pendulums.
- [ ] **74. Gas Particle Simulation:** Ideal Gas Law (atoms bouncing in box).
- [ ] **75. Soft Body Physics:** Deforming mass-spring systems (jelly).

## 16. Game Development (Pygame)
**Focus:** Graphical games.

- [ ] **76. Pong:** The classic arcade game.
- [ ] **77. Snake:** Grid movement and growth logic.
- [ ] **78. Breakout:** Brick breaking with physics bounces.
- [ ] **79. Flappy Bird Clone:** Gravity and scrolling obstacles.
- [ ] **80. Platformer:** Jumping and collision detection.

## 17. GUI Applications
**Focus:** User Interface (Tkinter/PyQt).

- [ ] **81. Calculator App:** Grid layout GUI.
- [ ] **82. Notepad Clone:** File menus and text editing.
- [ ] **83. Music Player:** MP3 playback controls.
- [ ] **84. Pomodoro Timer:** Countdown with work/break modes.
- [ ] **85. Currency Converter GUI:** Frontend for your API (#37).

## 18. Machine Learning (No magic libraries)
**Focus:** Understanding the math behind AI.

- [ ] **86. Linear Regression:** House price prediction (Gradient Descent).
- [ ] **87. K-Nearest Neighbors:** Classification (Cat vs Dog data).
- [ ] **88. Sentiment Analysis:** Positive/Negative review classification.
- [ ] **89. Digit Recognizer:** MNIST handwritten digit identification.
- [ ] **90. Recommendation Engine:** User similarity logic.

## 19. Generative AI & LLMs
**Focus:** Modern AI APIs.

- [ ] **91. Local Chatbot:** Run a small model (GPT-2/Llama) locally.
- [ ] **92. Prompt Generator:** Tool to refine user prompts.
- [ ] **93. AI Summarizer:** API-based article summarization.
- [ ] **94. Code Explainer:** Explain code snippets via LLM.
- [ ] **95. PDF RAG System:** Chat with a PDF document.

## 20. Capstone Integration
**Focus:** Combining domains.

- [ ] **96. Smart Home Dashboard:** GUI + Network control.
- [ ] **97. Stock Trading Bot:** Scraper + Analysis + Automation.
- [ ] **98. Multiplayer Game:** Game + Network Sockets.
- [ ] **99. AI Voice Assistant:** Speech + LLM + TTS.
- [ ] **100. The "OS" Simulation:** Text-based OS with login, file system, and apps.
      
## 🛠️ Getting Started

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/100-mini-python-projects.git](https://github.com/your-username/100-mini-python-projects.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd 100-mini-python-projects
    ```
3.  **Run a specific project:**
    ```bash
    cd 01-hello-world
    python main.py
    ```

## 📦 Dependencies

Some projects require external libraries. You can install them individually or install all at once (if a master requirements file is provided):

```bash
pip install -r requirements.txt
