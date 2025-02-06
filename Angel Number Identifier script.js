document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".form");
    const angelNumberInput = document.querySelector("#angel_number");

    form.addEventListener("submit", function(event) {
        if (angelNumberInput.value.trim() === "") {
            alert("Please enter a valid angel number.");
            event.preventDefault();
        }
    });

    // Example: Add a slight shake animation to the form when the submit button is clicked
    const button = document.querySelector(".button");
    button.addEventListener("click", function() {
        form.classList.add("shake");

        setTimeout(() => {
            form.classList.remove("shake");
        }, 500); // Remove the shake class after 500ms
    });
});
