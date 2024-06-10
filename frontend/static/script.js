document.addEventListener('DOMContentLoaded', function() {
    // Function to handle form submission
    function handleFormSubmit(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Get the search word from the input field
        var searchWord = document.querySelector('input[name="search_word"]').value;

        // Send an AJAX request to the backend to search for the word
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ search_word: searchWord })
        })
        .then(response => response.json())
        .then(data => {
            // Handle search results
            displaySearchResults(data);
        })
        .catch(error => console.error('Error:', error));
    }

    // Function to display search results
    function displaySearchResults(results) {
        // Clear previous search results
        var searchResultsContainer = document.getElementById('searchResults');
        searchResultsContainer.innerHTML = '';

        // Create list items for each search result
        results.forEach(function(result) {
            var li = document.createElement('li');
            li.textContent = result;
            searchResultsContainer.appendChild(li);
        });
    }

    // Add event listener for form submission
    var searchForm = document.querySelector('form');
    searchForm.addEventListener('submit', handleFormSubmit);
});

