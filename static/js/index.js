
// console.log("Sanity check from index.js.");

// // focus 'roomInput' when user opens the page
// // document.querySelector("#roomInput").focus();

// // // submit if the user presses the enter key
// // document.querySelector("#roomInput").onkeyup = function(e) {
// //     if (e.keyCode === 13) {  // enter key
// //         document.querySelector("#roomConnect").click();
// //     }
// // };

// // redirect to '/room/<roomInput>/'
// document.querySelector("#user-btn").onclick = function() {
//     // let roomName = document.querySelector("#roomInput").value;
//     console.log("hi");
//     var userid=request.user_id;
//     console.log(userid);
//     console.log(roomName);
//     window.location.pathname = "chat/" + roomName + "/";    
// }
// z
// // redirect to '/room/<roomSelect>/'
// document.querySelector("#roomSelect").onchange = function() {
//     let roomName = document.querySelector("#roomSelect").value.split(" (")[0];
//     window.location.pathname = "chat/" + roomName + "/";
// }

document.getElementById("roomSelect").onchange = function() {
        let roomName = document.querySelector("#roomSelect").value.split(" (")[0];
        window.location.pathname = "chat/" + roomName + "/";
    }
