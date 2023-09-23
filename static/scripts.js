const timeInput = document.getElementById('time');
const convertedTimeOutput = document.getElementById('convertedTime');


// Function to format time as HH:MM
function formatTime(hours) {
    const hh = Math.floor(hours);
    const mm = Math.round((hours - hh) * 60);
    const hhStr = hh < 10 ? `0${hh}` : `${hh}`;
    const mmStr = mm < 10 ? `0${mm}` : `${mm}`;
    return `${hhStr}:${mmStr}`;
}

// Update the converted time output when the input changes
timeInput.addEventListener('input', () => {
    const enteredHours = parseFloat(timeInput.value) || 0;
    const formattedTime = formatTime(enteredHours);
    convertedTimeOutput.textContent = formattedTime;
});
function handleSelection(selectElement) {
    const selectedValue = selectElement.value;

    window.location.href = "/user/entries";


    // fetch(`/select_user/${username}`)
    //     .then(response => response.json())
    //     .then(data => {
    //         console.log(data.message);
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //     });
}
