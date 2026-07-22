let reportData = null;

const analyzeButton = document.getElementById("analyze-btn");

analyzeButton.addEventListener("click", async ()=>{
    if(fileInput.files.length === 0){
        alert("Please upload a resume.");
        return;
    }
    if(textarea.value.trim()===""){
        alert("Please enter Job Description.");
        return;
    }
    const formData = new FormData();
    formData.append("resume", fileInput.files[0]);
    formData.append("job_description", textarea.value);

    analyzeButton.innerHTML="Analyzing...";
    analyzeButton.disabled=true;

    const processing=document.getElementById("processing");
    processing.classList.remove("hidden");
    document.getElementById("results").style.display="none";

    const steps=document.querySelectorAll(".timeline-step");
    steps.forEach(step=>step.classList.remove("active"));

    for(let i=0;i<steps.length;i++){
        steps[i].classList.add("active");
        await new Promise(resolve=>setTimeout(resolve,500));
    }

    const response=await fetch("/analyze",{
        method:"POST",
        body:formData
    });

    const data=await response.json();
    processing.classList.add("hidden");
    document.getElementById("results").style.display="block";
    reportData = data;
    renderDashboard(data);

    analyzeButton.innerHTML="Analysis Complete";
    analyzeButton.disabled=false;
});

function renderDashboard(data){
    const dashboard=document.getElementById("dashboard");

    let recommendationHtml = "";
    if(data.recommendation && data.recommendation.length > 0){
        recommendationHtml = `
        <div class="info-card recommendation-card">
            <h2>Recommendations to Get Shortlisted</h2>
            <div class="recommendation-list">
                ${data.recommendation.map(rec=>`<div class="recommendation-item">${rec}</div>`).join("")}
            </div>
        </div>`;
    }

    dashboard.innerHTML=`

    <div class="metric-grid">
        <div class="metric-card">
            <h4>Overall Match</h4>
            <h1>${data.overall_score}%</h1>
        </div>
        <div class="metric-card">
            <h4>Semantic Match</h4>
            <h1>${data.semantic_score}%</h1>
        </div>
        <div class="metric-card">
            <h4>Required Skills</h4>
            <h1>${data.required_skill_score}%</h1>
        </div>
        <div class="metric-card">
            <h4>ATS Score</h4>
            <h1>${data.ats_score}%</h1>
        </div>
    </div>

    <div class="info-card">
        <h2>Candidate Information</h2>
        <p><strong>Name:</strong> ${data.candidate.name}</p>
        <p><strong>Email:</strong> ${data.candidate.email}</p>
        <p><strong>Phone:</strong> ${data.candidate.phone}</p>
    </div>

    <div class="info-card">
        <h2>Detected Skills</h2>
        <div class="skill-container">
            ${data.skills.map(skill=>`<span class="skill-chip">${skill}</span>`).join("")}
        </div>
    </div>

    <div class="info-card">
        <h2>Matched Skills</h2>
        <div class="skill-container">
            ${data.matched_skills.map(skill=>`<span class="skill-chip matched">${skill}</span>`).join("")}
        </div>
    </div>

    <div class="info-card">
        <h2>Missing Skills</h2>
        <div class="skill-container">
            ${data.missing_skills.map(skill=>`<span class="skill-chip missing">${skill}</span>`).join("")}
        </div>
    </div>

    <div class="info-card">
        <h2>ATS Feedback</h2>
        <div class="feedback-list">
            ${data.feedback.length > 0 ? data.feedback.map(f=>`<div class="feedback-item">${f}</div>`).join("") : '<p>No issues found. Your resume passes ATS checks.</p>'}
        </div>
    </div>

    ${recommendationHtml}

    `;

    document.getElementById("results").scrollIntoView({
        behavior:"smooth"
    });
}

const downloadBtn = document.getElementById("download-report-btn");

downloadBtn.addEventListener("click", async () => {
    if (!reportData) return;

    const response = await fetch("/download-report", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(reportData)
    });

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "TalentLens_AI_Report.pdf";
    document.body.appendChild(a);
    a.click();
    a.remove();
    window.URL.revokeObjectURL(url);
});
