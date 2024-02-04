document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('.send-button').addEventListener('click', function() {
    var messageInput = document.querySelector('.type-any-questions-you-may-have');
    var message = messageInput.value.trim();
    if (message !== "") {
      appendMessage(message, true);
      messageInput.value = "";
    }
  });
});

function appendMessage(message, isSent) {
  var chatMessages = document.querySelector('.chat-messages');
  var messageElement = document.createElement('div');
  messageElement.classList.add('message');
  if (isSent) {
    messageElement.classList.add('sent');
  } else {
    messageElement.classList.add('received');
  }
  messageElement.textContent = message;
  chatMessages.appendChild(messageElement);
  // Scroll to the bottom
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
