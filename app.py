from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Venrand Website</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
            text-align: center;
        }

        header {
            background: #222;
            color: white;
            padding: 25px 15px;
        }

        header h2 {
            margin: 0;
        }

        .hero {
            padding: 70px 20px;
            background: white;
        }

        .hero h1 {
            font-size: 40px;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 19px;
            line-height: 1.6;
        }

        .button {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-size: 18px;
        }

        .section {
            padding: 45px 20px;
        }

        .cards {
            max-width: 900px;
            margin: auto;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            width: 250px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .card h3 {
            margin-top: 0;
        }

        footer {
            margin-top: 30px;
            padding: 25px;
            background: #222;
            color: white;
        }

        @media (max-width: 600px) {
            .hero h1 {
                font-size: 32px;
            }

            .card {
                width: 85%;
            }
        }
    </style>
</head>

<body>

<header>
    <h2>Venrand Website</h2>
</header>

<section class="hero">
    <h1>Welcome to Venrand 👋</h1>

    <p>
        Learn, build and grow with practical digital skills.
    </p>

    <a href="/python" class="button">Start Learning</a>
    <a href="/python" class="button">Get Started</a>
</section>

<section class="section" id="products">

    <h2>What We Offer</h2>

    <div class="cards">

        <div class="card">
            <h3>🐍 Learn Python</h3>
            <p>
                Start learning Python programming step by step.
            </p>
        </div>

        <div class="card">
            <h3>📚 Digital Learning</h3>
            <p>
                Discover useful educational resources and guides.
            </p>
        </div>

        <div class="card">
            <h3>💻 Digital Products</h3>
            <p>
                Explore practical digital products designed to help you learn.
            </p>
        </div>

    </div>

</section>

<footer>
    <p>© 2026 Venrand. All rights reserved.</p>
</footer>

</body>
</html>
"""
     
@app.route("/python-course")
def python_course():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Venrand Python Academy</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                color: #222;
            }

            .hero {
                background: #222;
                color: white;
                text-align: center;
                padding: 60px 20px;
            }

            .hero h1 {
                font-size: 38px;
                margin-bottom: 15px;
            }

            .hero p {
                font-size: 18px;
                max-width: 650px;
                margin: auto;
                line-height: 1.6;
            }

            .container {
                max-width: 900px;
                margin: 30px auto;
                padding: 20px;
            }

            .card {
                background: white;
                padding: 30px;
                margin-bottom: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 12px rgba(0,0,0,0.08);
            }

            h2 {
                margin-top: 0;
            }

            .lessons {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 12px;
            }

            .lesson {
                background: #f4f6f8;
                padding: 15px;
                border-radius: 8px;
            }

            .price {
                text-align: center;
                font-size: 32px;
                font-weight: bold;
                margin: 25px 0;
            }

            .button {
                display: inline-block;
                background: #222;
                color: white;
                padding: 14px 28px;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
            }

            .button:hover {
                opacity: 0.85;
            }

            .center {
                text-align: center;
            }

            footer {
                text-align: center;
                padding: 25px;
                color: #666;
            }
        </style>
    </head>

    <body>

        <div class="hero">
            <h1>🐍 Venrand Python Academy</h1>
            <p>
                Learn Python from the beginning through a practical
                15-lesson learning journey designed for beginners.
            </p>
        </div>

        <div class="container">

            <div class="card">
                <h2>Start Your Python Journey</h2>

                <p>
                    Venrand Python Academy is a beginner-friendly
                    programming course designed to help you understand
                    Python step by step.
                </p>

                <p>
                    You don't need previous programming experience.
                    Follow the lessons, practice the examples and build
                    your confidence as you learn.
                </p>
            </div>

            <div class="card">
                <h2>📚 What You Will Learn</h2>

                <div class="lessons">

                    <div class="lesson">Lesson 1: Python Basics</div>
                    <div class="lesson">Lesson 2: Variables</div>
                    <div class="lesson">Lesson 3: Data Types</div>
                    <div class="lesson">Lesson 4: Operators</div>
                    <div class="lesson">Lesson 5: Conditional Statements</div>
                    <div class="lesson">Lesson 6: Loops</div>
                    <div class="lesson">Lesson 7: Functions</div>
                    <div class="lesson">Lesson 8: Lists</div>
                    <div class="lesson">Lesson 9: Dictionaries</div>
                    <div class="lesson">Lesson 10: Tuples</div>
                    <div class="lesson">Lesson 11: Sets</div>
                    <div class="lesson">Lesson 12: String Manipulation</div>
                    <div class="lesson">Lesson 13: User Input</div>
                    <div class="lesson">Lesson 14: Error Handling</div>
                    <div class="lesson">Lesson 15: Working with Files</div>

                </div>
            </div>

            <div class="card">
                <h2>🎓 What You Get</h2>

                <p>✅ 15 structured Python lessons</p>
                <p>✅ Practical examples</p>
                <p>✅ Quizzes and exercises</p>
                <p>✅ Beginner-friendly learning</p>
                <p>✅ Course completion</p>
                <p>✅ Certificate of Completion</p>
            </div>

            <div class="card center">

                <h2>🚀 Start Learning Python</h2>

                <p>
                    Take the first step toward developing your
                    programming skills.
                </p>

               <div class="price">
            N$149
       </div>

                 <a href="/python" class="button">
    Start Learning </a>

            </div>

        </div>

        <footer>
            © 2026 Venrand Python Academy
        </footer>

    </body>
    </html>
    """
@app.route("/python")
def python_lesson():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 1 - Venrand</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 1: Python Basics</h2>

        <p>
            Welcome to your first Python lesson!
            Python is a programming language used to build websites,
            applications, automation tools and much more.
        </p>
    </div>

    <div class="lesson">
        <h2>Your First Python Program</h2>

        <p>Let's display a message on the screen:</p>

        <pre>print("Hello, Venrand!")</pre>

        <p>
            The <strong>print()</strong> function tells Python
            to display something on the screen.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>


<p>What do you think this code will display?</p>

<pre>print("I am learning Python!")</pre>

<form onsubmit="checkAnswer(event)">
    <input
        type="text"
        id="answer"
        placeholder="Type your answer"
        required
        style="padding:12px; width:80%; max-width:400px;"
    >

    <br><br>

    <button type="submit" class="button">
        Submit Answer
    </button>
</form>

<p id="result"></p>

<script>function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer.replace(/["']/g, "") === "I am learning Python!") {
        document.getElementById("result").textContent =
            "🎉 Correct! Well done!";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Try again!";
    }

    return false;
}

</script>        </p>

        <pre>print("I am learning Python!")</pre>
    </div>

   <a href="/" class="button">← Back to Home</a>
<a href="/python/lesson2" class="button">Next Lesson →</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

 <div style="margin-top:40px; padding:25px; background:#f4f4f4; border-radius:15px;">
    <h2>📚 All Python Lessons</h2>

    <a href="/python/lesson1" class="button">Lesson 1: Python Basics</a><br><br>
    <a href="/python/lesson2" class="button">Lesson 2: Variables</a><br><br>
    <a href="/python/lesson3" class="button">Lesson 3: Data Types</a><br><br>
    <a href="/python/lesson4" class="button">Lesson 4: Operators</a><br><br>
    <a href="/python/lesson5" class="button">Lesson 5: Conditional Statements</a><br><br>
    <a href="/python/lesson6" class="button">Lesson 6: Loops</a><br><br>
    <a href="/python/lesson7" class="button">Lesson 7: Functions</a><br><br>
    <a href="/python/lesson8" class="button">Lesson 8: Lists</a><br><br>
    <a href="/python/lesson9" class="button">Lesson 9: Dictionaries</a><br><br>
    <a href="/python/lesson10" class="button">Lesson 10: Tuples</a><br><br>
    <a href="/python/lesson11" class="button">Lesson 11: Sets</a><br><br>
    <a href="/python/lesson12" class="button">Lesson 12: String Manipulation</a><br><br>
    <a href="/python/lesson13" class="button">Lesson 13: User Input</a><br><br>
    <a href="/python/lesson14" class="button">Lesson 14: Error Handling</a><br><br>
    <a href="/python/lesson15" class="button">Lesson 15: Working with Files</a>
</div></body>
</html>
"""
@app.route("/python/lesson2")
def lesson2():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 2 - Variables</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 2: Variables</h2>

        <p>
            A variable is a name that stores a value.
        </p>

        <p>
            Think of a variable like a labeled box where you can
            keep information.
        </p>
    </div>

    <div class="lesson">
        <h2>Creating a Variable</h2>

        <p>
            In Python, we can create a variable like this:
        </p>

        <pre>name = "Venrand"</pre>

        <p>
            Here, <strong>name</strong> is the variable and
            <strong>"Venrand"</strong> is the value stored inside it.
        </p>
    </div>

    <div class="lesson">
        <h2>Numbers and Variables</h2>

        <p>
            Variables can also store numbers:
        </p>

        <pre>age = 38</pre>

        <p>
            Now the variable <strong>age</strong> contains the number 38.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What value is stored in the variable <strong>city</strong>?
        </p>

        <pre>city = "Windhoek"</pre>

        <form onsubmit="checkAnswer(event); return false;">
            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>
        </form>

        <p id="result"></p>
    </div>

    <a href="/python" class="button">← Lesson 1</a>
<a href="/python/lesson3" class="button">Next Lesson →</a>
    <a href="/" class="button">🏠 Home</a>

</main>
<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer.replace(/["']/g, "") === "Windhoek") {
        document.getElementById("result").textContent =
            "🎉 Correct! You understand variables!";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Try again!";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson3")
def lesson3():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 3 - Data Types</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 3: Data Types</h2>

        <p>
            Python uses different data types to represent different
            kinds of information.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Strings 🔤</h2>

        <p>
            A string is text surrounded by quotation marks.
        </p>

        <pre>name = "Venrand"</pre>
    </div>

    <div class="lesson">
        <h2>2. Integers 🔢</h2>

        <p>
            An integer is a whole number without a decimal point.
        </p>

        <pre>age = 38</pre>
    </div>

    <div class="lesson">
        <h2>3. Floats 🔢</h2>

        <p>
            A float is a number containing a decimal point.
        </p>

        <pre>price = 19.99</pre>
    </div>

    <div class="lesson">
        <h2>4. Booleans ✅</h2>

        <p>
            A Boolean has one of two values:
            <strong>True</strong> or <strong>False</strong>.
        </p>

        <pre>is_student = True</pre>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What data type is stored in the variable
            <strong>price</strong>?
        </p>

        <pre>price = 19.99</pre>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson2" class="button">← Lesson 2</a>
<a href="/python/lesson4" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim().toLowerCase();

    if (answer === "float") {
        document.getElementById("result").textContent =
            "🎉 Correct! 19.99 is a float!";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Try again!";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson4")
def lesson4():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 4 - Operators</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 4: Python Operators</h2>

        <p>
            Operators are symbols that allow us to perform
            calculations and other operations in Python.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Addition ➕</h2>

        <p>Use <strong>+</strong> to add numbers.</p>

        <pre>10 + 5</pre>

        <p>The answer is <strong>15</strong>.</p>
    </div>

    <div class="lesson">
        <h2>2. Subtraction ➖</h2>

        <p>Use <strong>-</strong> to subtract numbers.</p>

        <pre>10 - 5</pre>

        <p>The answer is <strong>5</strong>.</p>
    </div>

    <div class="lesson">
        <h2>3. Multiplication ✖️</h2>

        <p>Use <strong>*</strong> to multiply numbers.</p>

        <pre>10 * 5</pre>

        <p>The answer is <strong>50</strong>.</p>
    </div>

    <div class="lesson">
        <h2>4. Division ➗</h2>

        <p>Use <strong>/</strong> to divide numbers.</p>

        <pre>10 / 5</pre>

        <p>The answer is <strong>2.0</strong>.</p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What is the result of this calculation?
        </p>

        <pre>20 + 15</pre>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson3" class="button">← Lesson 3</a>
<a href="/python/lesson3" class="button">← Lesson 3</a>
<a href="/python/lesson5" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer === "35") {
        document.getElementById("result").textContent =
            "🎉 Correct! 20 + 15 = 35!";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Try again!";
    }

    return false;
}
</script>

</body>
</html>

"""
@app.route("/python/lesson5")
def lesson5():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 5 - Conditions</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 5: Conditional Statements</h2>

        <p>
            Conditional statements allow Python to make decisions.
        </p>

        <p>
            Python can check whether something is true or false
            and then decide what code to run.
        </p>
    </div>

    <div class="lesson">
        <h2>1. The if Statement</h2>

        <p>
            The <strong>if</strong> statement runs code when a condition
            is true.
        </p>

        <pre>age = 18

if age >= 18:
    print("You are an adult.")</pre>
    </div>

    <div class="lesson">
        <h2>2. The else Statement</h2>

        <p>
            The <strong>else</strong> statement runs when the
            condition is false.
        </p>

        <pre>age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")</pre>
    </div>

    <div class="lesson">
        <h2>3. The elif Statement</h2>

        <p>
            The <strong>elif</strong> statement lets Python check
            another condition.
        </p>

        <pre>score = 75

if score >= 80:
    print("Excellent!")
elif score >= 50:
    print("You passed!")
else:
    print("Try again.")</pre>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this code display?
        </p>

        <pre>age = 20

if age >= 18:
    print("Adult")
else:
    print("Under 18")</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

   <a href="/python/lesson4" class="button">← Lesson 4</a>
<a href="/" class="button">🏠 Home</a>
<a href="/python/lesson6" class="button">Next Lesson →</a>

   

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim().toLowerCase();

    if (answer === "adult") {
        document.getElementById("result").textContent =
            "🎉 Correct! The code displays Adult.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Try again!";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/complete")
def complete():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Certificate - Venrand Python Academy</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                color: #222;
                text-align: center;
            }

            .container {
                max-width: 850px;
                margin: 30px auto;
                padding: 25px;
            }

            input {
                width: 90%;
                max-width: 500px;
                padding: 14px;
                margin: 15px 0;
                font-size: 17px;
                border: 1px solid #ccc;
                border-radius: 8px;
                box-sizing: border-box;
            }

            button, .button {
                display: inline-block;
                padding: 12px 20px;
                margin: 8px;
                background: #222;
                color: white;
                text-decoration: none;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
            }

            .certificate {
                display: none;
                margin: 30px auto;
                padding: 45px 25px;
                background: white;
                border: 8px double #222;
                border-radius: 5px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }

            .logo {
                font-size: 42px;
            }

            .academy {
                font-size: 26px;
                font-weight: bold;
                margin: 10px 0 25px;
            }

            .title {
                font-size: 32px;
                letter-spacing: 2px;
                margin: 20px 0;
            }

            .student-name {
                font-size: 34px;
                font-weight: bold;
                margin: 25px 0;
                border-bottom: 2px solid #222;
                display: inline-block;
                padding: 0 25px 8px;
            }

            .course {
                font-size: 22px;
                font-weight: bold;
                margin: 15px 0;
            }

            .details {
                margin: 25px 0;
                line-height: 1.8;
            }

            .certificate-number {
                font-size: 14px;
                margin-top: 25px;
            }

            .signature {
                margin-top: 40px;
                font-style: italic;
                font-size: 18px;
            }

            @media print {
                body {
                    background: white;
                }

                .form-section,
                .navigation {
                    display: none;
                }

                .container {
                    max-width: none;
                    margin: 0;
                    padding: 0;
                }

                .certificate {
                    display: block !important;
                    box-shadow: none;
                    margin: 0;
                    min-height: 80vh;
                }
            }
        </style>
    </head>

    <body>

        <div class="container">

            <div class="form-section">

                <h1>🎉 Congratulations!</h1>

                <p>You have successfully completed all 15 lessons.</p>

                <h2>🐍 Venrand Python Academy</h2>

                <p>Enter your full name to generate your professional certificate:</p>

                <input
                    type="text"
                    id="studentName"
                    placeholder="Enter your full name"
                >

                <br>

                <button onclick="generateCertificate()">
                    🎓 Generate Certificate
                </button>

            </div>

            <div class="certificate" id="certificate">

                <div class="logo">🐍</div>

                <div class="academy">
                    VENRAND PYTHON ACADEMY
                </div>

                <div class="title">
                    CERTIFICATE OF COMPLETION
                </div>

                <p>This certificate is proudly presented to</p>

                <div class="student-name" id="displayName"></div>

                <p>for successfully completing the</p>

                <div class="course">
                    Python Programming Course
                </div>

                <div class="details">
                    <strong>15 Lessons Completed</strong><br>
                    Completion Date: <span id="completionDate"></span>
                </div>

                <div class="signature">
                    __________________________<br>
                    Venrand Python Academy
                </div>

                <div class="certificate-number">
                    Certificate No: <span id="certificateNumber"></span>
                </div>

            </div>

            <div class="navigation">

                <button onclick="printCertificate()">
                    🖨️ Print Certificate
                </button>

                <br>

                <a href="/python" class="button">
                    📚 Review All Lessons
                </a>

                <a href="/" class="button">
                    🏠 Home
                </a>

            </div>

        </div>

        <script>
            function generateCertificate() {

                const name = document.getElementById("studentName").value.trim();

                if (name === "") {
                    alert("Please enter your full name.");
                    return;
                }

                const today = new Date();

                const dateString = today.toLocaleDateString();

                const certificateNumber =
                    "VPA-" +
                    today.getFullYear() +
                    "-" +
                    Math.floor(100000 + Math.random() * 900000);

                document.getElementById("displayName").textContent = name;
                document.getElementById("completionDate").textContent = dateString;
                document.getElementById("certificateNumber").textContent = certificateNumber;

                document.getElementById("certificate").style.display = "block";
            }

            function printCertificate() {

                const certificate =
                    document.getElementById("certificate");

                if (certificate.style.display !== "block") {
                    alert("Please generate your certificate first.");
                    return;
                }

                window.print();
            }
        </script>

    </body>
    </html>
    """

@app.route("/python/lesson6")
def lesson6():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 6 - Loops</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 6: Loops</h2>

        <p>
            A loop allows Python to repeat a block of code
            multiple times.
        </p>

        <p>
            Loops are useful when you need to perform the same
            action repeatedly.
        </p>
    </div>

    <div class="lesson">
        <h2>1. The for Loop 🔄</h2>

        <p>
            A <strong>for</strong> loop can repeat code for each
            item in a sequence.
        </p>

        <pre>for number in range(5):
    print(number)</pre>

        <p>This displays:</p>

        <pre>0
1
2
3
4</pre>
    </div>

    <div class="lesson">
        <h2>2. The while Loop 🔁</h2>

        <p>
            A <strong>while</strong> loop repeats code while
            a condition is true.
        </p>

        <pre>count = 1

while count <= 3:
    print(count)
    count = count + 1</pre>

        <p>This displays:</p>

        <pre>1
2
3</pre>
    </div>

    <div class="lesson">
        <h2>Why Use Loops?</h2>

        <p>
            Imagine you wanted to print "Hello!" 100 times.
            You don't need to write the same line 100 times.
        </p>

        <pre>for i in range(100):
    print("Hello!")</pre>

        <p>
            The loop does the repetition for you. 💪
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            How many times will this loop print
            <strong>"Python"</strong>?
        </p>

        <pre>for i in range(5):
    print("Python")</pre>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>
-
    <a href="/python/lesson5" class="button">← Lesson 5</a>

    <a href="/" class="button">🏠 Home</a><a href="/python/lesson7" class="button">Next Lesson →</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer === "5") {
        document.getElementById("result").textContent =
            "🎉 Correct! The loop runs 5 times!";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Try again!";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson7")
def lesson7():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 7 - Functions</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 7: Functions</h2>

        <p>
            A function is a reusable block of code that performs
            a specific task.
        </p>

        <p>
            Functions help us organize our programs and avoid
            repeating the same code.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Creating a Function</h2>

        <p>
            We use the <strong>def</strong> keyword to create a function.
        </p>

        <pre>def greet():
    print("Hello, Venrand!")

greet()</pre>

        <p>
            Calling <strong>greet()</strong> runs the function.
        </p>
    </div>

    <div class="lesson">
        <h2>2. Parameters</h2>

        <p>
            A parameter allows a function to receive information.
        </p>

        <pre>def greet(name):
    print("Hello", name)

greet("Venrand")</pre>

        <p>
            Here, <strong>name</strong> is the parameter.
        </p>
    </div>

    <div class="lesson">
        <h2>3. Return Values</h2>

        <p>
            A function can return a result using the
            <strong>return</strong> statement.
        </p>

        <pre>def add(a, b):
    return a + b

result = add(5, 3)

print(result)</pre>

        <p>
            The result is <strong>8</strong>.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this function return?
        </p>

        <pre>def multiply(a, b):
    return a * b

result = multiply(4, 5)

print(result)</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson6" class="button">← Lesson 6</a><a href="/python/lesson8" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer === "20") {
        document.getElementById("result").textContent =
            "🎉 Correct! 4 × 5 = 20!";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Try again!";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson8")
def lesson8():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 8 - Lists</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 8: Lists</h2>

        <p>
            A list is used to store multiple items in one variable.
        </p>

        <p>
            Lists are useful when you want to keep a collection
            of related values together.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Creating a List 📋</h2>

        <p>
            We create a list using square brackets
            <strong>[ ]</strong>.
        </p>

        <pre>fruits = ["apple", "banana", "orange"]

print(fruits)</pre>

        <p>
            This list contains three fruits.
        </p>
    </div>

    <div class="lesson">
        <h2>2. Accessing List Items 🔢</h2>

        <p>
            Python uses indexes to access items in a list.
            The first index is <strong>0</strong>.
        </p>

        <pre>fruits = ["apple", "banana", "orange"]

print(fruits[0])</pre>

        <p>
            The result is:
        </p>

        <pre>apple</pre>
    </div>

    <div class="lesson">
        <h2>3. Adding Items ➕</h2>

        <p>
            We can add an item to a list using
            <strong>append()</strong>.
        </p>

        <pre>fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)</pre>

        <p>
            The list now contains three fruits.
        </p>
    </div>

    <div class="lesson">
        <h2>4. Removing Items ➖</h2>

        <p>
            We can remove an item using
            <strong>remove()</strong>.
        </p>

        <pre>fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)</pre>

        <p>
            Banana is removed from the list.
        </p>
    </div>

    <div class="lesson">
        <h2>5. Looping Through a List 🔄</h2>

        <p>
            A <strong>for</strong> loop can be used to process
            every item in a list.
        </p>

        <pre>fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)</pre>

        <p>
            Python prints each fruit one at a time.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this code print?
        </p>

        <pre>numbers = [10, 20, 30]

print(numbers[1])</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson7" class="button">← Lesson 7</a><a href="/python/lesson9" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer === "20") {
        document.getElementById("result").textContent =
            "🎉 Correct! The second item is 20.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Remember: Python starts counting indexes at 0.";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson9")
def lesson9():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 9 - Dictionaries</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 9: Dictionaries</h2>

        <p>
            A dictionary stores information using
            <strong>key-value pairs</strong>.
        </p>

        <p>
            Think of a dictionary like a real dictionary:
            you use a word to find its meaning.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Creating a Dictionary 📖</h2>

        <pre>student = {
    "name": "Venrand",
    "age": 38,
    "course": "Python"
}

print(student)</pre>

        <p>
            Each piece of information has a key and a value.
        </p>
    </div>

    <div class="lesson">
        <h2>2. Accessing Values 🔍</h2>

        <p>
            We use the key to access its value.
        </p>

        <pre>student = {
    "name": "Venrand",
    "age": 38
}

print(student["name"])</pre>

        <p>The result is:</p>

        <pre>Venrand</pre>
    </div>

    <div class="lesson">
        <h2>3. Adding Information ➕</h2>

        <pre>student = {
    "name": "Venrand"
}

student["course"] = "Python"

print(student)</pre>

        <p>
            A new key-value pair has been added.
        </p>
    </div>

    <div class="lesson">
        <h2>4. Changing Information ✏️</h2>

        <pre>student = {
    "name": "Venrand",
    "age": 38
}

student["age"] = 39

print(student["age"])</pre>

        <p>
            The age has been changed from 38 to 39.
        </p>
    </div>

    <div class="lesson">
        <h2>5. Removing Information 🗑️</h2>

        <pre>student = {
    "name": "Venrand",
    "age": 38
}

student.pop("age")

print(student)</pre>

        <p>
            The <strong>pop()</strong> method removes a key-value pair.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this code print?
        </p>

        <pre>person = {
    "name": "John",
    "age": 25
}

print(person["age"])</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div6666>

    <a href="/python/lesson8" class="button">← 8</a><a href="/python/lesson8" class="button">← Lesson 8</a>
<a href="/python/lesson10" class="button">Next Lesson →</a>
<a href="/python/lesson10" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>l
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer === "25") {
        document.getElementById("result").textContent =
            "🎉 Correct! The value of age is 25.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Look at the value stored under the age key.";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson10")
def lesson10():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 10 - Tuples</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 10: Tuples</h2>

        <p>
            A tuple is another way to store multiple values
            in one variable.
        </p>

        <p>
            Tuples are similar to lists, but there is an important
            difference: <strong>tuples cannot normally be changed
            after they are created.</strong>
        </p>
    </div>

    <div class="lesson">
        <h2>1. Creating a Tuple 📦</h2>

        <p>
            Tuples are created using parentheses
            <strong>( )</strong>.
        </p>

        <pre>fruits = ("apple", "banana", "orange")

print(fruits)</pre>
    </div>

    <div class="lesson">
        <h2>2. Accessing Tuple Items 🔍</h2>

        <p>
            Just like lists, tuple indexes start at
            <strong>0</strong>.
        </p>

        <pre>fruits = ("apple", "banana", "orange")

print(fruits[0])</pre>

        <p>The result is:</p>

        <pre>apple</pre>
    </div>

    <div class="lesson">
        <h2>3. Tuples Cannot Be Changed 🔒</h2>

        <p>
            Once a tuple is created, you cannot simply change
            one of its items.
        </p>

        <pre>numbers = (10, 20, 30)</pre>

        <p>
            This makes tuples useful when you want data to remain
            unchanged.
        </p>
    </div>

    <div class="lesson">
        <h2>4. Tuple Unpacking 📦</h2>

        <p>
            You can assign tuple values to different variables.
        </p>

        <pre>person = ("Venrand", 38)

name, age = person

print(name)
print(age)</pre>

        <p>
            The values are assigned to <strong>name</strong>
            and <strong>age</strong>.
        </p>
    </div>

    <div class="lesson">
        <h2>List vs Tuple ⚖️</h2>

        <pre>my_list = [10, 20, 30]

my_tuple = (10, 20, 30)</pre>

        <p>
            Lists use <strong>[ ]</strong> and can be changed.
        </p>

        <p>
            Tuples use <strong>( )</strong> and are generally
            used for values that should remain unchanged.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this code print?
        </p>

        <pre>colors = ("red", "green", "blue")

print(colors[1])</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson9" class="button">← Lesson 9</a>
<a href="/python/lesson11" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim().toLowerCase();

    if (answer === "green") {
        document.getElementById("result").textContent =
            "🎉 Correct! The second item is green.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Remember that indexes start at 0.";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson11")
def lesson11():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 11 - Sets</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 11: Sets</h2>

        <p>
            A set is a collection of unique values.
        </p>

        <p>
            Unlike lists, sets do not allow duplicate items.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Creating a Set 🧩</h2>

        <pre>fruits = {"apple", "banana", "orange"}

print(fruits)</pre>

        <p>
            Sets use curly brackets <strong>{ }</strong>.
        </p>
    </div>

    <div class="lesson">
        <h2>2. Duplicate Values 🔄</h2>

        <p>
            If you add the same value more than once,
            Python keeps only one copy.
        </p>

        <pre>numbers = {1, 2, 2, 3, 3, 3}

print(numbers)</pre>

        <p>
            The set contains only:
        </p>

        <pre>{1, 2, 3}</pre>
    </div>

    <div class="lesson">
        <h2>3. Adding Items ➕</h2>

        <p>
            Use <strong>add()</strong> to add an item.
        </p>

        <pre>fruits = {"apple", "banana"}

fruits.add("orange")

print(fruits)</pre>
    </div>

    <div class="lesson">
        <h2>4. Removing Items ➖</h2>

        <p>
            Use <strong>remove()</strong> to remove an item.
        </p>

        <pre>fruits = {"apple", "banana", "orange"}

fruits.remove("banana")

print(fruits)</pre>
    </div>

    <div class="lesson">
        <h2>5. Sets vs Lists ⚖️</h2>

        <pre>my_list = [1, 2, 2, 3]

my_set = {1, 2, 2, 3}</pre>

        <p>
            The list keeps duplicates, while the set removes
            duplicate values.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            How many unique numbers are in this set?
        </p>

        <pre>numbers = {5, 5, 10, 10, 15}

print(len(numbers))</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson10" class="button">← Lesson 10</a><a href="/python/lesson12" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer === "3") {
        document.getElementById("result").textContent =
            "🎉 Correct! There are 3 unique numbers.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Remember that sets remove duplicates.";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson12")
def lesson12():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 12 - String Manipulation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 12: String Manipulation</h2>

        <p>
            A string is a sequence of characters used to represent
            text in Python.
        </p>

        <pre>name = "Venrand"

print(name)</pre>

        <p>
            Python provides many useful tools for working with strings.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Changing Case 🔤</h2>

        <p>
            The <strong>upper()</strong> method changes text to uppercase.
        </p>

        <pre>name = "venrand"

print(name.upper())</pre>

        <p>Result:</p>

        <pre>VENRAND</pre>

        <p>
            The <strong>lower()</strong> method changes text to lowercase.
        </p>

        <pre>name = "VENRAND"

print(name.lower())</pre>

        <p>Result:</p>

        <pre>venrand</pre>
    </div>

    <div class="lesson">
        <h2>2. Removing Extra Spaces ✂️</h2>

        <p>
            The <strong>strip()</strong> method removes spaces from
            the beginning and end of a string.
        </p>

        <pre>name = "   Venrand   "

print(name.strip())</pre>

        <p>
            The result is:
        </p>

        <pre>Venrand</pre>
    </div>

    <div class="lesson">
        <h2>3. Replacing Text 🔄</h2>

        <p>
            The <strong>replace()</strong> method can replace part
            of a string with different text.
        </p>

        <pre>message = "I love Python"

message = message.replace("Python", "programming")

print(message)</pre>

        <p>Result:</p>

        <pre>I love programming</pre>
    </div>

    <div class="lesson">
        <h2>4. Finding String Length 📏</h2>

        <p>
            The <strong>len()</strong> function tells us how many
            characters are in a string.
        </p>

        <pre>word = "Python"

print(len(word))</pre>

        <p>
            The result is:
        </p>

        <pre>6</pre>
    </div>

    <div class="lesson">
        <h2>5. Combining Strings ➕</h2>

        <p>
            Strings can be joined using the <strong>+</strong> operator.
        </p>

        <pre>first = "Venrand"
last = "Academy"

full_name = first + " " + last

print(full_name)</pre>

        <p>Result:</p>

        <pre>Venrand Academy</pre>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this code print?
        </p>

        <pre>word = "python"

print(word.upper())</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson11" class="button">← Lesson 11</a><a href="/python/lesson13" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer.tolowcase() === "python") {
        document.getElementById("result").textContent =
            "🎉 Correct! upper() changes the text to uppercase.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Remember what upper() does to a string.";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson13")
def lesson13():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 13 - User Input</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 13: User Input</h2>

        <p>
            Python can receive information from a user using
            the <strong>input()</strong> function.
        </p>

        <p>
            This allows our programs to interact with people.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Using input() ⌨️</h2>

        <p>
            The <strong>input()</strong> function waits for the
            user to type something.
        </p>

        <pre>name = input("What is your name? ")

print(name)</pre>

        <p>
            Whatever the user types is stored inside
            the <strong>name</strong> variable.
        </p>
    </div>

    <div class="lesson">
        <h2>2. Using Input with Text 💬</h2>

        <pre>name = input("Enter your name: ")

print("Hello " + name)</pre>

        <p>
            If the user enters <strong>Venrand</strong>, Python prints:
        </p>

        <pre>Hello Venrand</pre>
    </div>

    <div class="lesson">
        <h2>3. Getting Numbers 🔢</h2>

        <p>
            Input normally comes into Python as text.
            To use it as a whole number, we can use
            <strong>int()</strong>.
        </p>

        <pre>age = int(input("Enter your age: "))

print(age)</pre>

        <p>
            Now Python can use the value for mathematical operations.
        </p>
    </div>

    <div class="lesson">
        <h2>4. Doing Calculations ➕</h2>

        <pre>number = int(input("Enter a number: "))

result = number + 10

print(result)</pre>

        <p>
            If the user enters <strong>5</strong>, the result is
            <strong>15</strong>.
        </p>
    </div>

    <div class="lesson">
        <h2>5. A Practical Example 💡</h2>

        <pre>name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello " + name)
print("You are", age, "years old.")</pre>

        <p>
            This program collects two pieces of information
            from the user.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this code print if the user enters
            <strong>10</strong>?
        </p>

        <pre>number = int(input("Enter a number: "))

result = number + 5

print(result)</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson12" class="button">← Lesson 12</a><a href="/python/lesson14" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim();

    if (answer === "15") {
        document.getElementById("result").textContent =
            "🎉 Correct! 10 + 5 = 15.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Add 5 to 10 and try again!";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson14")
def lesson14():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 14 - Error Handling</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 14: Error Handling</h2>

        <p>
            Sometimes a Python program encounters an error.
            Error handling allows us to deal with certain errors
            without stopping the entire program.
        </p>
    </div>

    <div class="lesson">
        <h2>1. The try Statement 🛠️</h2>

        <p>
            The <strong>try</strong> block contains code that
            might produce an error.
        </p>

        <pre>try:
    number = int("hello")
except:
    print("Something went wrong.")</pre>

        <p>
            Instead of crashing, Python moves to the
            <strong>except</strong> block.
        </p>
    </div>

    <div class="lesson">
        <h2>2. The except Statement ⚠️</h2>

        <p>
            The <strong>except</strong> block tells Python
            what to do when an error occurs.
        </p>

        <pre>try:
    number = int("10")
    print(number)
except:
    print("Invalid number.")</pre>

        <p>
            Since <strong>"10"</strong> can be converted to an integer,
            the program prints <strong>10</strong>.
        </p>
    </div>

    <div class="lesson">
        <h2>3. Handling Invalid Input 🔢</h2>

        <pre>try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("Please enter a number.")</pre>

        <p>
            If the user enters text instead of a number,
            Python can display a helpful message.
        </p>
    </div>

    <div class="lesson">
        <h2>4. The finally Statement ✅</h2>

        <p>
            The <strong>finally</strong> block runs whether an
            error occurs or not.
        </p>

        <pre>try:
    print("Hello!")
except:
    print("An error occurred.")
finally:
    print("Program finished.")</pre>
    </div>

    <div class="lesson">
        <h2>Why Error Handling Matters 💡</h2>

        <p>
            Good programs should be able to handle unexpected
            situations and give users useful feedback instead
            of simply crashing.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            What will this code print?
        </p>

        <pre>try:
    number = int("hello")
except ValueError:
    print("Invalid number")</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson13" class="button">← Lesson 13</a><a href="/python/lesson15" class="button">Next Lesson →</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim().toLowerCase();

    if (answer === "invalid number") {
        document.getElementById("result").textContent =
            "🎉 Correct! The conversion causes a ValueError.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. Look at what the except block prints.";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/python/lesson15")
def lesson15():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Lesson 15 - Files</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #222;
        }

        header {
            background: #222;
            color: white;
            padding: 25px;
            text-align: center;
        }

        main {
            max-width: 800px;
            margin: auto;
            padding: 30px 20px;
        }

        .lesson {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        pre {
            background: #222;
            color: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .button {
            display: inline-block;
            padding: 14px 25px;
            background: #222;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
        }

        input {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            padding: 12px 25px;
            background: #222;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        #result {
            font-weight: bold;
            margin-top: 15px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #222;
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>🐍 Venrand Python Academy</h1>
</header>

<main>

    <div class="lesson">
        <h2>Lesson 15: Working with Files</h2>

        <p>
            Python can create, read, write and update files.
            This is useful when programs need to save information.
        </p>
    </div>

    <div class="lesson">
        <h2>1. Opening a File 📂</h2>

        <p>
            Python uses the <strong>open()</strong> function
            to work with files.
        </p>

        <pre>file = open("notes.txt", "r")</pre>

        <p>
            The <strong>"r"</strong> means read mode.
        </p>
    </div>

    <div class="lesson">
        <h2>2. Reading a File 📖</h2>

        <pre>file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()</pre>

        <p>
            The <strong>read()</strong> method reads the contents
            of the file.
        </p>
    </div>

    <div class="lesson">
        <h2>3. Writing to a File ✍️</h2>

        <pre>file = open("notes.txt", "w")

file.write("Hello, Venrand!")

file.close()</pre>

        <p>
            The <strong>"w"</strong> mode writes to a file.
            If the file does not exist, Python can create it.
        </p>
    </div>

    <div class="lesson">
        <h2>4. Adding to a File ➕</h2>

        <pre>file = open("notes.txt", "a")

file.write(" More Python!")

file.close()</pre>

        <p>
            The <strong>"a"</strong> mode means append.
            It adds information to the existing file.
        </p>
    </div>

    <div class="lesson">
        <h2>5. Using with open() ⭐</h2>

        <p>
            A safer and cleaner way to work with files is
            using <strong>with open()</strong>.
        </p>

        <pre>with open("notes.txt", "r") as file:
    content = file.read()

print(content)</pre>

        <p>
            Python automatically handles closing the file
            when the block is finished.
        </p>
    </div>

    <div class="lesson">
        <h2>File Modes 📋</h2>

        <pre>"r" → Read
"w" → Write
"a" → Append</pre>

        <p>
            Choosing the correct mode is important when
            working with files.
        </p>
    </div>

    <div class="lesson">
        <h2>Try It Yourself 💻</h2>

        <p>
            Which file mode is used to <strong>add</strong>
            information to an existing file?
        </p>

        <pre>with open("notes.txt", "___") as file:
    file.write("Hello!")</pre>

        <p>
            Type the answer below:
        </p>

        <form onsubmit="checkAnswer(event); return false;">

            <input
                type="text"
                id="answer"
                placeholder="Type your answer"
                required
            >

            <br><br>

            <button type="submit">Submit Answer</button>

        </form>

        <p id="result"></p>
    </div>

    <a href="/python/lesson14" class="button">← Lesson 14</a><a href="/python/complete" class="button">🏆 Complete Course</a>

    <a href="/" class="button">🏠 Home</a>

</main>

<footer>
    <p>© 2026 Venrand</p>
</footer>

<script>
function checkAnswer(event) {
    event.preventDefault();

    const answer = document.getElementById("answer").value.trim().toLowerCase();

    if (answer === "a") {
        document.getElementById("result").textContent =
            "🎉 Correct! 'a' means append.";
    } else {
        document.getElementById("result").textContent =
            "❌ Not quite. 'a' is the mode used to append information.";
    }

    return false;
}
</script>

</body>
</html>
"""
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            return "<h1>Login successful! 🎉</h1><p>Welcome to the management area.</p>"

        return "<h1>Login failed ❌</h1><p>Wrong username or password.</p>"

    return """
<!DOCTYPE html>
<html>
<head>
    <title>Venrand Management Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <h1>Management Login</h1>

    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <br><br>

        <input type="password" name="password" placeholder="Password" required>
        <br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
