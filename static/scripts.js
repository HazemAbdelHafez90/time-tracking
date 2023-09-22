// script.js
function handleSelection(selectElement) {
    const selectedValue = selectElement.value;

    fetch(`/select_user/${username}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
