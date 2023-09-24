$(document).ready(function() {
    $('#usersTable').DataTable({
        searching: true, // Enable searching/filtering
      });
      $('#projectsTable').DataTable({
        searching: true, // Enable searching/filtering
      });
    const usersTable = document.getElementById('usersTable');
    const userAddRowBtn = document.getElementById('userAddRowBtn');
    const projectsTable = document.getElementById('projectsTable');
    const projectAddRowBtn = document.getElementById('projectAddRowBtn');
    

    // Add a new row to the table
    userAddRowBtn.addEventListener('click', function() {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td contenteditable="true">New</td>
            <td contenteditable="true">New</td>
            <td>
                <button class="user-add-row-btn">add</button>
            </td>
        `;
        usersTable.querySelector('tbody').appendChild(newRow);
    });
    
    // Update and delete rows
    usersTable.addEventListener('click', function(e) {
        const target = e.target;
        const parentRow = target.parentElement.parentElement;
        
        if (target.classList.contains('user-update-row-btn')) {
            updateUserTableRow(parentRow)
        } else if (target.classList.contains('user-delete-row-btn')) {
            // Delete the row
            deleteUserTableRow(parentRow);
        }
        else if (target.classList.contains('user-add-row-btn')) {
            // Delete the row
            addUserTableRow(parentRow);
        }
    });


    // Function to delete a table row and make an AJAX request to Flask
    function deleteUserTableRow(row) {
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
    function addUserTableRow(row) {
            const cells = row.cells;
            const updatedData = {
                name: cells[1].textContent,
                username: cells[0].textContent
            };
    
            // Send an AJAX request to the Flask route to update the row
            $.ajax({
                url: `/users`,
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(updatedData),
                success: function(response) {
                    alert(response)
                    window.location.href = '/admin';
                },
                error: function(error) {
                    console.error(error);
                }
            });
        }


    
    // Add a new row to the table
    projectAddRowBtn.addEventListener('click', function() {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td contenteditable="true">New</td>
            <td contenteditable="true">New</td>
            <td>
                <button class="project-add-row-btn">Add</button>
            </td>
        `;
        projectsTable.querySelector('tbody').appendChild(newRow);
    });
    
    // Update and delete rows
    projectsTable.addEventListener('click', function(e) {
        const target = e.target;
        const parentRow = target.parentElement.parentElement;
        
        if (target.classList.contains('project-update-row-btn')) {
            updateProjectTableRow(parentRow)
        } else if (target.classList.contains('project-delete-row-btn')) {
            // Delete the row
            deleteProjectTableRow(parentRow);
        }
        else if (target.classList.contains('project-add-row-btn')) {
            // Delete the row
            addProjectTableRow(parentRow);
        }
    });


    // Function to delete a table row and make an AJAX request to Flask
    function deleteProjectTableRow(row) {
        const cells = row.cells;
        const updatedData = {
            name: cells[0].textContent,
            desc: cells[1].textContent
        };
        // Send an AJAX request to the Flask route to delete the row
        $.ajax({
            url: `/projects`,
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
    function updateProjectTableRow(row) {
        const cells = row.cells;
        const updatedData = {
            name: cells[0].textContent,
            desc: cells[1].textContent
        };

        // Send an AJAX request to the Flask route to update the row
        $.ajax({
            url: `/projects`,
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
    function addProjectTableRow(row) {
            const cells = row.cells;
            const updatedData = {
                name: cells[0].textContent,
                desc: cells[1].textContent
            };
    
            // Send an AJAX request to the Flask route to update the row
            $.ajax({
                url: `/projects`,
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(updatedData),
                success: function(response) {
                    alert(response)
                    window.location.href = '/admin';
                },
                error: function(error) {
                    console.error(error);
                }
            });
        }
});
