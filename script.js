document.addEventListener('DOMContentLoaded', function() {
                                                 // Funct to handle form submission
    function handleFormSubmit(event) {
        event.preventDefault();                  // Preventing default form submission

                                               // get the search word from the  input
        var searchWord = document.querySelector('input[name="search_word"]').value;

                                                 // Sending an AJAX request to the backend to search for the word
        
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

                                                               // Funct to display search results 
    function displaySearchResults(results) {
                                                              // clear previous search result
        var searchResultsContainer = document.getElementById('searchResults');
        searchResultsContainer.innerHTML = '';

                                                                // c reate list items for each search result
        results.forEach(function(result) {
            var li = document.createElement('li');
            li.textContent = result;
            searchResultsContainer.appendChild(li);
        });
    }

                                                                  // adding event listener for form submission
    var searchForm = document.querySelector('form');
    searchForm.addEventListener('submit', handleFormSubmit);
});

