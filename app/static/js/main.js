const textarea = document.getElementById("job-description");
const counter = document.querySelector(".character-count");

textarea.addEventListener("input", ()=>{
    counter.innerHTML = `${textarea.value.length} / 5000`;
});

const getStartedBtn = document.getElementById("get-started-btn");

if (getStartedBtn) {
    getStartedBtn.addEventListener("click", () => {
        document.getElementById("upload").scrollIntoView({
            behavior: "smooth"
        });
    });
}

const learnMoreBtn = document.getElementById("learn-more-btn");

if (learnMoreBtn) {
    learnMoreBtn.addEventListener("click", () => {
        document.getElementById("about").scrollIntoView({
            behavior: "smooth"
        });
    });
}

const navLinks = document.querySelectorAll('a[href^="#"]');

navLinks.forEach(link => {
    link.addEventListener("click", function(e){
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if(target){
            target.scrollIntoView({
                behavior:"smooth"
            });
        }
    });
});
