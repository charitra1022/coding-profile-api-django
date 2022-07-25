function displayJson(jsonData) {
    // Display the JSON tree

    let htmlContent = `<input class="path" type="text" hidden>
    <pre id="json-renderer" class="json-tree"></pre>`

    document.getElementById("response-container").innerHTML = htmlContent;

    let $pathTarget = document.querySelectorAll('.path');
    let $source = document.querySelector('#json-renderer');
    const defaultOpts = {};

    JPPicker.render($source, jsonData, $pathTarget, defaultOpts);
}





document.getElementById("submitBtn").addEventListener("click", function () {
    // fetch api response and display json tree on form submission

    // Display the api controls(url container, buttons, etc) after button click
    document.getElementById("api-controls").style.display = "block";

    // Get all DOM Elements
    let urlContainer = document.getElementById("url-container");
    let responseContainer = document.getElementById("response-container");

    // Hide response container when button is clicked. Shown after data is fetched
    responseContainer.style.display = "none";

    // Get values from input fields
    const username = document.getElementById("username").value;
    const platform = document.getElementById("platform").value;

    // API fetch url
    const apiUrl = `https://coding-profile-api.herokuapp.com/codingprofile/?platform=${platform}&username=${username}`;

    // Display url in box
    urlContainer.innerHTML = apiUrl;

    // Fetch data
    // const temUrl = `http://127.0.0.1:8000/codingprofile/?platform=${platform}&username=${username}`
    fetch(apiUrl).then(res => res.json()).then(data => {
        // Display response container
        responseContainer.style.display = "block";

        // Display JSON tree
        displayJson(data);

    });
});


document.getElementById("copyBtn").addEventListener("click", () => {
    // Add url to clipboard on button click

    const url = document.getElementById("url-container").innerText;
    navigator.clipboard.writeText(url);

    // Rename copy button to copied for 5 seconds
    document.getElementById("copyBtn").innerText = "Copied";
    setTimeout(() => {
        document.getElementById("copyBtn").innerText = "Copy";
    }, 5000);
});


