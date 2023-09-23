document.addEventListener('DOMContentLoaded', function() {
    const editableTable = document.getElementById('editableTable');
    const addRowBtn = document.getElementById('addRowBtn');
    
    // Add a new row to the table
    addRowBtn.addEventListener('click', function() {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td contenteditable="true">New</td>
            <td contenteditable="true">New</td>
            <td contenteditable="true">New</td>
            <td>
                <button class="update-row-btn">Update</button>
                <button class="delete-row-btn">Delete</button>
            </td>
        `;
        editableTable.querySelector('tbody').appendChild(newRow);
    });
    
    // Update and delete rows
    editableTable.addEventListener('click', function(e) {
        const target = e.target;
        const parentRow = target.parentElement.parentElement;
        
        if (target.classList.contains('update-row-btn')) {
            updateTableRow(parentRow)
        } else if (target.classList.contains('delete-row-btn')) {
            // Delete the row
            deleteTableRow(parentRow);
        }
    });

    // Function to delete a table row and make an AJAX request to Flask
    function deleteTableRow(row) {
        const cells = row.cells;
        const updatedData = {
            name: cells[1].textContent,
            username: cells[0].textContent
        };
        // Send an AJAX request to the Flask route to delete the row
        $.ajax({
            url: `/users`,
            type: 'DELETE',
            contentType: 'application/json',
            data: JSON.stringify(updatedData),
            success: function(response) {
                // On success, remove the row from the table
                row.remove();
                alert(response);
            },
            error: function(error) {
                console.error(error);
            }
        });
    }

    // Function to update a table row
    function updateTableRow(row) {
        const cells = row.cells;
        const updatedData = {
            name: cells[1].textContent,
            username: cells[0].textContent
        };

        // Send an AJAX request to the Flask route to update the row
        $.ajax({
            url: `/users/`,
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
});
