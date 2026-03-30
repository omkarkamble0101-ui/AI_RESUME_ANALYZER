const API = "http://127.0.0.1:8000";

// 🔐 LOGIN
async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Please fill all fields");
        return;
    }

    const response = await fetch(`${API}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (response.ok && data.access_token) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "resume.html";
    } else {
        alert(data.message || "Login failed");
    }
}


// 📝 REGISTER
async function register() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!name || !email || !password) {
        alert("All fields required");
        return;
    }

    const response = await fetch(`${API}/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, email, password })
    });

    const data = await response.json();

    if (response.ok) {
        alert("Registered successfully! Please login.");
        window.location.href = "login.html";
    } else {
        alert(data.message || "Registration failed");
    }
}