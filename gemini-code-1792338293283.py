from flask import Flask, render_template_string, request

app = Flask(__name__)

# Fake Login Page Template (HTML)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Security Awareness Login</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .login-box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); width: 300px; text-align: center; }
        input[type="text"], input[type="password"] { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
        button { background-color: #007bff; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; width: 100%; }
        button:hover { background-color: #0056b3; }
        .alert { color: red; font-size: 14px; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Corporate Login Simulation</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Username / Email" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Log In</button>
        </form>
    </div>
</body>
</html>
"""

# Awareness Message Template
SUCCESS_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Security Warning</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #ffe6e6; text-align: center; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 10px; display: inline-block; border: 2px solid red; }
        h1 { color: #d9534f; }
    </style>
</head>
<body>
    <div class="card">
        <h1>⚠️ Phishing Simulation Test!</h1>
        <p><strong>Warning:</strong> You just entered credentials on an unauthorized test page.</p>
        <p>In a real attack, your credentials would have been stolen!</p>
        <hr>
        <h3>Safety Tips:</h3>
        <ul style="text-align: left;">
            <li>Always check the URL in the browser bar before typing your password.</li>
            <li>Look for SSL encryption (https://).</li>
            <li>Never click unverified links from suspicious emails.</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    # Note: We do NOT save or store the password to ensure safety
    print(f"[SIMULATION LOG] Phishing test triggered by user: {username}")
    return render_template_string(SUCCESS_TEMPLATE)

if __name__ == '__main__':
    # Runs locally on http://127.0.0.1:5000
    app.run(debug=True)