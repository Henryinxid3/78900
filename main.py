from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None  # Initialize error variable

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username == 'HENRY-X _x3eaa3x34rs43eaa' and password == 'HENRY-X 2.0':
            # Redirect to the specified link if login is successful
            return redirect('https://hsjsnskosn.onrender.com/')
        else:
            error = 'Invalid username or password. Please try again.'

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Henry Server</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Popins, sans-serif;
            background-image: url('http://imagesaver.darkester.online/uploads/1748422293-311e0a94866ccac525e37a0720603070.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 50px auto; /* Decreased max-width */
            margin: 50px auto; /* Adjusted margin */
            padding: 20px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: white;
            border: 1.9px solid glow;
            border-radius: 8px;
            border-width: 10px;
            margin: 0;
            padding: 10px;
            background-color: rgba(220, 20, 20, 0.5); /* Transparent red background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #fff;
            font-size: 28px;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #000;
        }
        /* Blinking Sukhi Server heading */
        .sukhi-server {
            font-size: 32px;
            color: #ff5e5e;
            animation: blink 1.5s infinite;
            font-weight: bold;
            margin-bottom: 20px;
        }
        @keyframes blink {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0;
            }
        }
        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
            background-color: rgba(255, 255, 255, 0.9);
        }
        form {
        display: flex;
        flex-direction: column; /* Arrange children in a column */
        align-items: center;    /* Center items horizontally */
        }
        
        button {
        width: auto;            /* Change to auto for centered width */
        padding: 12px 20px;     /* Adjust padding for better appearance */
        background-color: #007bff;
        color: #fff;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        margin-top: 15px;
        font-weight: bold;
        font-size: 16px;
        transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
        .admin-contact {
            margin-top: 20px;
            color: #fff;
        }
        .admin-contact a {
            color: #00ff00;
            font-weight: bold;
            text-decoration: none;
        }
        .error-message {
            color: red;
            font-size: 14px;
            margin-top: 10px;
            font-weight: bold;
        }
            .card h2 {
      font-size: 1.8rem;
      color: #fff;
      margin-bottom: 1rem;
    }

    .card p {
      color: #ff693;
      font-size: 1rem;
    }

    .btn {
      display: inline-block;
      margin-top: 1.2rem;
      padding: 0.7rem 1.5rem;
      background: linear-gradient(to right, #FF0000, #ff85c1);
      color: #000;
      border: none;
      border-radius: 50px 10px 50px 10px;
      font-weight: bold;
      font-family: 'Orbitron', sans-serif;
      text-decoration: none;
      box-shadow: 0 0 15px #FF0000;
      transition: all 0.3s ease;
    }

    .btn:hover {
      background: linear-gradient(to right, #ff85c1, #FF0000);
      box-shadow: 0 0 25px #FF0000, 0 0 40px #f0f;
      transform: scale(1.05);
    }

    footer {
      text-align: center;
      padding: 1.5rem;
      background: #1a1a2e;
      color: #ffb6d9;
      font-size: 0.85rem;
      border-top: 2px solid #FF0000;
    }
    </style>
</head>
<body>
    <div class="container">
    <div class="content">
        <img src="https://i.imgur.com/1AKZp6Z.jpeg" style="width: 100%; height: auto; border-radius: 12px;">
        <h1>Officail WEB</h1>
        <h2 class="henry-server">HENRY X SAMAR SERVERS</h2>
        <form action="/" method="POST">  <!-- Changed to / -->
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        {% if error %}
        <div class="error-message">{{ error }}</div>  <!-- Display the error message -->
        {% endif %}
        <div class="admin-contact">
            <p>Need help? <a href="https://wa.me/+919235741670" target="_blank">Contact Admin</a></p>
        </div>

        <div class="card">
      <h2>Paid Servers</h2>
      <p>If You Want To By Server First Contact him !</p>
      <a class="btn" href="https://wa.me/+919235741670" target="_blank">Buy</a>
    </div>
</body>
</html>
    ''', error=error)  # Pass the error to the template

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
