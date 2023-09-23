
function handleSelection(selectElement) {
    const selectedValue = selectElement.value;
    document.cookie = 'selectedUser=' + selectedValue;
    window.location.href = "/user/entries/"+selectedValue;


    // fetch(`/select_user/${username}`)
    //     .then(response => response.json())
    //     .then(data => {
    //         console.log(data.message);
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //     });
}



