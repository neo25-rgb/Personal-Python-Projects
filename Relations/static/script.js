function sendAnswer(answer) {
    fetch("/answer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ answer: answer })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("celebration").classList.remove("hidden");

        confetti({
            particleCount: 200,
            spread: 80,
            origin: { y: 0.6 }
        });
    });
}

function moveButton(button) {
    button.style.position = "absolute";
    button.style.top = Math.random() * window.innerHeight + "px";
    button.style.left = Math.random() * window.innerWidth + "px";
}
function playMusic() {
    document.getElementById("bgMusic").play();
}
