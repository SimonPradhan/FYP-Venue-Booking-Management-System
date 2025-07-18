// chat/static/room.js

console.log("Sanity check from room.js.");

const roomName = JSON.parse(document.getElementById('roomName').textContent);

let chatLog = document.querySelector("#chatLog");
let chatMessageInput = document.querySelector("#chatMessageInput");
const chatMessageSend = document.getElementById("sendchat");
let onlineUsersSelector = document.querySelector("#onlineUsersSelector");
// adds a new option to 'onlineUsersSelector'
function onlineUsersSelectorAdd(value) {
    if (document.querySelector("option[value='" + value + "']")) return;
    let newOption = document.createElement("option");
    newOption.value = value;
    newOption.innerHTML = value;
    onlineUsersSelector.appendChild(newOption);
}

// removes an option from 'onlineUsersSelector'
function onlineUsersSelectorRemove(value) {
    let oldOption = document.querySelector("option[value='" + value + "']");
    if (oldOption !== null) oldOption.remove();
}

// focus 'chatMessageInput' when user opens the page
chatMessageInput.focus();

// submit if the user presses the enter key
chatMessageInput.onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter key
        console.log("chatMessageInput.value.length: " + chatMessageInput.value.length);
        chatMessageSend.click();
    }
};

// clear the 'chatMessageInput' and forward the message
chatMessageSend.onclick = function() {
    console.log("chatMessageInput.value.length: " + chatMessageInput.value);

    if (chatMessageInput.value.length === 0) return;
    // TODO: forward the message to the WebSocket
    console.log("Sending message...");
    console.log(chatSocket);
    // chatSocket.send(JSON.stringify({
    //     "message": chatMessageInput.value,
    // }));
    if (chatSocket.readyState === WebSocket.OPEN) {
        // Send the message
        chatSocket.send(JSON.stringify({
            "message":  chatMessageInput.value
        }));
    } else {
        console.error('WebSocket connection is not open');
    }
    chatMessageInput.value = "";
};  

let chatSocket = null;

function connect() {
    chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + roomName + "/");

    chatSocket.onopen = function(e) {
        console.log("Successfully connected to the WebSocket.");
    }

    chatSocket.onclose = function(e) {
        console.log("WebSocket connection closed unexpectedly. Trying to reconnect in 2s...");
        setTimeout(function() {
            console.log("Reconnecting...");
            connect();
        }, 2000);
    };

    chatSocket.onmessage = function(e) {
        console.log("Listennig");
        const data = JSON.parse(e.data);
        console.log(" data: " + data.message);      

        switch (data.type) {
            case "chat_message":
                chatLog.value += data.user + ": " +  data.message + "\n";
                break;
            default:
                console.error("Unknown message type!");
                break;
        }

        // scroll 'chatLog' to the bottom
        chatLog.scrollTop = chatLog.scrollHeight;
    };

    chatSocket.onerror = function(err) {
        console.log("WebSocket encountered an error: " + err);
        console.log("Closing the socket.");
        chatSocket.close();
    }
}
connect();

onlineUsersSelector.onchange = function() {
    chatMessageInput.value = "/pm " + onlineUsersSelector.value + " ";
    onlineUsersSelector.value = null;
    chatMessageInput.focus();
};