
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kartu Nama Digital</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #090919, #191944, #32105a);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    overflow-x: hidden;
}

.card {
    width: 350px;
    padding: 35px 25px;
    text-align: center;
    border-radius: 25px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(15px);
    box-shadow: 0 0 35px rgba(150,0,255,0.3);
    animation: muncul 1.2s ease;
}

@keyframes muncul {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.profile {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    border: 4px solid #a855f7;
    object-fit: cover;
    margin-bottom: 18px;
    box-shadow: 0 0 20px #a855f7;
}

h1 {
    font-size: 25px;
    margin-bottom: 8px;
}

.job {
    color: #c084fc;
    font-size: 14px;
    margin-bottom: 20px;
}

.description {
    color: #ddd;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 25px;
}

.info {
    background: rgba(255,255,255,0.08);
    padding: 13px;
    border-radius: 12px;
    margin: 10px 0;
    font-size: 14px;
}

.buttons {
    margin-top: 25px;
}

.btn {
    display: block;
    text-decoration: none;
    color: white;
    padding: 13px;
    margin: 12px 0;
    border-radius: 30px;
    background: linear-gradient(90deg,#7c3aed,#c026d3);
    transition: 0.3s;
    font-weight: bold;
}

.btn:hover {
    transform: scale(1.06);
    box-shadow: 0 0 20px #a855f7;
}

footer {
    margin-top: 25px;
    color: #aaa;
    font-size: 11px;
}
</style>
</head>

<body>

<div class="card">

    <img class="profile"
    src="https://i.pravatar.cc/200"
    alt="Foto Profil">

    <h1>Andika Wahyu Saputra</h1>
    <p class="job">Digital Creator | Freelancer</p>

    <p class="description">
        Selamat datang di kartu nama digital saya.
        Hubungi saya untuk kerja sama dan informasi lebih lanjut.
    </p>

    <div class="info">📧 Email: wahyuandika7789@gmail.com</div>
    <div class="info">📱 Telepon: 085702064275</div>
    <div class="info">📍 Lokasi: DIY</div>

    <div class="buttons">
        <a class="btn"
        href="https://wa.me/6281234567890">
        💬 WhatsApp
        </a>

        <a class="btn"
        href="https://instagram.com/username">
        📸 Instagram
        </a>

        <a class="btn"
        href="mailto:emailkamu@gmail.com">
        ✉️ Kirim Email
        </a>
    </div>

    <footer>
        © 2026 Kartu Nama Digital
    </footer>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
