const dropZone = document.getElementById("drop-zone");
const fileInput = document.getElementById("resume");
const preview = document.getElementById("file-preview");

dropZone.addEventListener("click", () => {
    fileInput.click();
});

dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("dragging");
});

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragging");
});

dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("dragging");
    const file = e.dataTransfer.files[0];
    if(file){
        fileInput.files = e.dataTransfer.files;
        showPreview(file);
    }
});

fileInput.addEventListener("change", () => {
    if(fileInput.files.length){
        showPreview(fileInput.files[0]);
    }
});

function showPreview(file){
    const size = (file.size / 1024 / 1024).toFixed(2);
    preview.innerHTML = `
        <div class="preview-card">
            <h3>📄 ${file.name}</h3>
            <p>${size} MB</p>
            <span class="ready">
                ✓ Ready for Analysis
            </span>
        </div>
    `;
}
