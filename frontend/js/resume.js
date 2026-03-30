if(!localStorage.getItem("token")) {
    window.location.href = "login.html"
}
const API = "http://127.0.0.1:8000";

async function uploadResume() {
    const file = document.getElementById("file").files[0];
    const token = localStorage.getItem("token");

    const formData = new FormData();
    formData.append("file", file);

    document.getElementById("result").innerHTML = `
        <div style="text-align:center;">
            <div class="loader"></div>
            <p>Processing...</p>
        </div>
    `;

    try {
        const response = await fetch(`${API}/upload-resume`, {
            method: "POST",
            headers: {
                "Authorization": "Bearer " + token
            },
            body: formData
        });

        const data = await response.json();

        document.getElementById("result").innerHTML = `
            <h3>Resume Analysis</h3>
            <p><strong>Score:</strong> ${data.score}</p>
            <p><strong>Skills Found:</strong><br>${data.skills_found.join(", ")}</p>
            <p><strong>Grammar Issues:</strong><br>${data.grammar_issues?.join(", ") || "None"}</p>
        `;

    } catch (error) {
        console.error("UPLOAD ERROR:", error);
        document.getElementById("result").innerHTML = `
            <p style="color:red;">Error uploading resume</p>
        `;
    }
}

async function matchJob() {
    const job = document.getElementById("job").value;

    const formData = new FormData();
    formData.append("job_description", job);

    document.getElementById("result").innerHTML = `
        <div style="text-align:center;">
            <div class="loader"></div>
            <p>Processing...</p>
        </div>
    `;

    try {
        const response = await fetch(`${API}/match-job`, {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("result").innerHTML = `
            <h3>Job Match Result</h3>
            <p><strong>Match Score:</strong> ${data.match_score}%</p>
            <p><strong>Matched Skills:</strong><br>${data.matched_skills.join(", ")}</p>
            <p><strong>Missing Skills:</strong><br>${data.missing_skills.join(", ")}</p>
            <p><strong>Suggestions:</strong><br>${data.suggestions.skill_suggestions.join("<br>")}</p>
        `;

    } catch (error) {
        console.error("MATCH ERROR:", error);
        document.getElementById("result").innerHTML = `
            <p style="color:red;">Error matching job</p>
        `;
    }
}