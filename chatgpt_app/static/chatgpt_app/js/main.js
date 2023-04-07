
const generateTextBtn = document.querySelector('#generate-text-btn');
const promptInput = document.querySelector('#prompt');
const textContainer = document.querySelector('#text-container');

generateTextBtn.addEventListener('click', () => {
    const prompt = promptInput.value;

    fetch(`/generate_text/?prompt=${prompt}`)
        .then(response => response.json())
        .then(data => {
            const text = data.text;
            textContainer.innerHTML = text;
        })
        .catch(error => console.error(error));
});