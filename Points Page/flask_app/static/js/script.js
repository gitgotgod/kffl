// Sample data (you can replace this with your backend data retrieval)
const users = [
    { id: 1, name: "User 1", points: 10 },
    { id: 2, name: "User 2", points: 5 },
];

const userList = document.getElementById("userList");

// Function to render user list
function renderUserList() {
    userList.innerHTML = "";
    users.forEach(user => {
        const li = document.createElement("li");
        li.textContent = `${user.name} - Points: ${user.points}`;
        userList.appendChild(li);
    });
}

// Function to add a new user
function addUser() {
    const userNameInput = document.getElementById("userName");
    const userName = userNameInput.value.trim();

    if (userName !== "") {
        const newUser = { id: users.length + 1, name: userName, points: 0 };
        users.push(newUser);
        renderUserList();
        userNameInput.value = "";
    }
}

// Attach event listener to the Add User button
const addUserButton = document.getElementById("addUserButton");
addUserButton.addEventListener("click", addUser);

// Initial rendering of user list
renderUserList();
