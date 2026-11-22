
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Portal</title>
    <style>
        body {
            font-family: Arial;
            background: #f1f5f9;
            margin: 40px;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            max-width: 650px;
            margin: auto;
        }
        h1 { color: #2563eb; }
        li { margin: 12px 0; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Student Portal</h1>
        <h2>Welcome, Ahmed!</h2>
        <h3>Student Dashboard</h3>
        <ul>
            <li>Student Profile</li>
            <li>Attendance: 92%</li>
            <li>Subjects: Mathematics, Physics, Chemistry</li>
            <li>Exam Results: View Results</li>
            <li>Study Materials: Available</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
