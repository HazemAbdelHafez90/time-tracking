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
document.addEventListener('DOMContentLoaded', function() {
    const entriesTable = document.getElementById('entriesTable');
    const entryAddRowBtn = document.getElementById('entryAddRowBtn');
    
    // Update and delete rows
    entriesTable.addEventListener('click', function(e) {
        const target = e.target;
        const parentRow = target.parentElement.parentElement;
        
        if (target.classList.contains('entry-update-row-btn')) {
            updateUserTableRow(parentRow)
        } else if (target.classList.contains('entry-delete-row-btn')) {
            // Delete the row
            deleteEntryTableRow(parentRow);
        }
        else if (target.classList.contains('entry-add-row-btn')) {
            // Delete the row
            addUserTableRow(parentRow);
        }
    });



    entryAddRowBtn.addEventListener('click', function(e)
    {
        const date = document.getElementById('date').value;
        const project = document.getElementById('project').value;
        const convertedTime = document.getElementById('convertedTime').innerText;
        const comments = document.getElementById('comments').value;

        const updatedData = {
            date: date,
            project:project,
            time:convertedTime,
            comments:comments
        };

        $.ajax({
            url: `/user/entries`,
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(updatedData),
            success: function(response) {
                window.location.href = '/';
            },
            error: function(error) {
                console.error(error);
            }
        });

    })


    // Function to delete a table row and make an AJAX request to Flask
    function deleteEntryTableRow(row) {
        const cells = row.cells;
        const updatedData = {
            id: cells[0].textContent
        };
        // Send an AJAX request to the Flask route to delete the row
        $.ajax({
            url: `/user/entries`,
            type: 'DELETE',
            contentType: 'application/json',
            data: JSON.stringify(updatedData),
            success: function(response) {
                // On success, remove the row from the table
                row.remove();
            },
            error: function(error) {
                console.error(error);
            }
        });
    }

    // Function to update a table row
    function updateUserTableRow(row) {
        const cells = row.cells;
        const updatedData = {
            name: cells[1].textContent,
            username: cells[0].textContent
        };

        // Send an AJAX request to the Flask route to update the row
        $.ajax({
            url: `/users`,
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify(updatedData),
            success: function(response) {
                // On success, you can update the UI or display a message
                alert(response);
            },
            error: function(error) {
                console.error(error);
            }
        });
    }

        // Function to update a table row
    function addEntry(row) {
          
    
            // Send an AJAX request to the Flask route to update the row
            $.ajax({
                url: `/users`,
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(updatedData),
                success: function(response) {
                    alert(response)
                    window.location.href = '/';
                },
                error: function(error) {
                    console.error(error);
                }
            });
        }


});
