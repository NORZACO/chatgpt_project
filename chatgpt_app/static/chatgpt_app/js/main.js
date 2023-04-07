
const generateTextBtn = document.querySelector('#generate-text-btn');
const promptInput = document.querySelector('#prompt');
const textContainer = document.querySelector('#text-container');

generateTextBtn.addEventListener('click', () => {
    const prompt = promptInput.value;

    fetch(`/generate_text/?prompt=${prompt}`)
        .then(response => response.json())
        .then(data => {
            const text = data.text;
            textContainer.innerHTML += text; // append new text to existing content
            textContainer.innerHTML += '<br> <hr>'; // add a space between the two texts
            // <br></br>
            promptInput.value = ''; // clear the prompt input field
        })
        .catch(error => console.error(error));
});







function getCurrentTime() {
    let today = new Date();
    let hours = today.getHours();
    let minutes = today.getMinutes();
    hours = (hours < 10 ? "0" : "") + hours;
    minutes = (minutes < 10 ? "0" : "") + minutes;
    return hours + ":" + minutes;
}

function appendMessage(text, className, avatar) {
    const chatlogs = document.getElementById("text-container");
    const chat = document.createElement("div");
    chat.className = "chat";

    const chatAvatar = document.createElement("div");
    chatAvatar.className = "chat-avatar";
    const img = document.createElement("img");
    img.src = avatar;
    chatAvatar.appendChild(img);

    const chatMessage = document.createElement("div");
    chatMessage.className = "chat-message " + className;
    const p = document.createElement("p");
    p.textContent = text;
    chatMessage.appendChild(p);

    const chatTime = document.createElement("div");
    chatTime.className = "chat-time";
    chatTime.textContent = getCurrentTime();

    chatMessage.appendChild(chatTime);
    chat.appendChild(chatAvatar);
    chat.appendChild(chatMessage);

    chatlogs.appendChild(chat);
    chatlogs.scrollTop = chatlogs.scrollHeight;
}

const timestamp = document.querySelector(".chat-time").textContent;
const question = document.querySelector(".chat-message.customer p").textContent;
appendMessage(question, "customer", "{% static 'chatgpt_app/img/customer.png' %}");

document.querySelector(".chat-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const input = document.querySelector("#prompt");
    const promptText = input.value;
    input.value = "";
    if (promptText.trim() === "") {
        return;
    }

    appendMessage(promptText, "ai", "{% static 'chatgpt_app/img/ai.png' %}");
});