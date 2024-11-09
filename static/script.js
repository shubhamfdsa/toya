//// Initialize greeting when the page loads
//window.onload = initializeGreeting;
//
//document.getElementById('askNameButton').addEventListener('click', handleUserName);
//
//async function initializeGreeting() {
//    playVoice("Welcome to my world, what is your name?");
//}
//
//async function handleUserName() {
//    const userInput = document.getElementById('userInput');
//    const chatbox = document.getElementById('chatbox');
//    const userName = userInput.value;
//
//    if (userName.trim() === "") return;
//
//    chatbox.innerHTML += `<div class="user-message">You: ${userName}</div>`;
//
//    playVoice(`Welcome ${userName}, Welcome to my world. Please ask your question.`);
//    chatbox.innerHTML += `<div class="bot-message">Toya: Welcome ${userName}, Welcome to my world. Please ask your question.</div>`;
//
//    chatbox.scrollTop = chatbox.scrollHeight;
//    document.querySelector('.input-container').style.display = 'none';
//    document.getElementById('questionInputContainer').style.display = 'block';
//    userInput.value = "";
//}
//
//async function askQuestion() {
//    const userInput = document.getElementById('questionInput');
//    const chatbox = document.getElementById('chatbox');
//    const prompt = userInput.value;
//
//    if (prompt.trim() === "") return;
//
//    chatbox.innerHTML += `<div class="user-message">You: ${prompt}</div>`;
//
//    try {
//        const response = await fetch('/ask', {
//            method: 'POST',
//            headers: {
//                'Content-Type': 'application/json'
//            },
//            body: JSON.stringify({ prompt })
//        });
//
//        const data = await response.json();
//        const answer = data.answer;
//
//        playVoice(answer);
//        chatbox.innerHTML += `<div class="bot-message">Toya: ${answer}</div>`;
//        chatbox.scrollTop = chatbox.scrollHeight;
//
//    } catch (error) {
//        chatbox.innerHTML += `<div class="bot-message">Error: ${error}</div>`;
//    }
//
//    userInput.value = "";
//}
//
//// Function to use Web Speech API with a female voice
//function playVoice(text) {
//    const utterance = new SpeechSynthesisUtterance(text);
//    utterance.pitch = 1;
//    utterance.rate = 1;
//
//    // Attempt to select a female-sounding voice
//    const voices = window.speechSynthesis.getVoices();
//    const femaleVoice = voices.find(voice => voice.name.includes('Female') || voice.name.includes('Woman') || voice.lang.includes('en'));
//
//    if (femaleVoice) {
//        utterance.voice = femaleVoice;
//    }
//
//    window.speechSynthesis.speak(utterance);
//}
//
//// Refresh the voice list (some browsers require this to load voices)
//window.speechSynthesis.onvoiceschanged = () => {
//    const voices = window.speechSynthesis.getVoices();
//};
