document.getElementById("sendBtn").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function (event) {
    if (event.key === "Enter") sendMessage();
});

async function sendMessage() {
    const userInput = document.getElementById("userInput");
    const messageText = userInput.value.trim();
    if (!messageText) return;

    // Add user message to chat
    addMessage(messageText, "user-message");

    // Clear input field
    userInput.value = "";

    // Show bot is typing
    addTypingIndicator();

    // Send message to backend
    const responseText = await getResponse(messageText);

    // Remove typing indicator
    removeTypingIndicator();

    // Add bot response
    addMessage(responseText, "bot-message");
}

// Function to get response from backend
async function getResponse(question) {
    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await response.json();
        if (data.task_id) {
            return await fetchResult(data.task_id);
        } else {
            return "⚠️ Error processing request!";
        }
    } catch (error) {
        console.error("Error:", error);
        return "❌ Sorry, something went wrong!";
    }
}

// Function to poll result
async function fetchResult(task_id) {
    while (true) {
        const response = await fetch(`/result/${task_id}`);
        const data = await response.json();
        if (data.status === "completed") {
            return data.result;
        }
        await new Promise((resolve) => setTimeout(resolve, 2000)); // Poll every 2 sec
    }
}

// Function to display message
function addMessage(text, className) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", className);
    messageDiv.textContent = text;

    const messagesContainer = document.getElementById("messages");
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight; // Auto-scroll
}

// Show typing effect
function addTypingIndicator() {
    const typingDiv = document.createElement("div");
    typingDiv.classList.add("message", "bot-message");
    typingDiv.id = "typingIndicator";
    typingDiv.textContent = "Typing...";
    
    const messagesContainer = document.getElementById("messages");
    messagesContainer.appendChild(typingDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Remove typing effect
function removeTypingIndicator() {
    const typingIndicator = document.getElementById("typingIndicator");
    if (typingIndicator) typingIndicator.remove();
}
