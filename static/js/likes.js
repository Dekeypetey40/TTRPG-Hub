// Like/Unlike functionality with AJAX
console.log('Likes.js loaded!');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing like handlers...');
    
    // Get CSRF token from cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');
    console.log('CSRF token:', csrftoken ? 'Found' : 'Not found');

    // Add event listeners to all like forms
    const likeForms = document.querySelectorAll('.like-form');
    console.log('Found', likeForms.length, 'like forms');
    
    likeForms.forEach(form => {
        console.log('Attaching listener to form:', form.action);
        form.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent default form submission

            const button = this.querySelector('.btn-like');
            const icon = button.querySelector('i');
            const likeCountSpan = this.parentElement.querySelector('.like-count');
            const url = this.action;

            // Add animation class
            icon.classList.add('like-animate');

            // Send AJAX request
            fetch(url, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken,
                },
                body: new FormData(this)
            })
            .then(response => {
                console.log('Response received:', response.status);
                return response.json();
            })
            .then(data => {
                console.log('Like response:', data);
                
                // Update heart icon based on liked state
                // Keep fa-heart class, only toggle fas/far
                if (data.liked) {
                    // Change to filled heart (solid)
                    console.log('Changing to filled heart (fas)');
                    icon.classList.remove('far');
                    icon.classList.add('fas');
                } else {
                    // Change to empty heart (regular)
                    console.log('Changing to empty heart (far)');
                    icon.classList.remove('fas');
                    icon.classList.add('far');
                }

                // Update like count
                if (likeCountSpan) {
                    likeCountSpan.textContent = data.likes_count;
                    console.log('Updated count to:', data.likes_count);
                } else {
                    console.log('Like count span not found');
                }

                // Remove animation class after animation completes
                setTimeout(() => {
                    icon.classList.remove('like-animate');
                }, 300);
            })
            .catch(error => {
                console.error('Error liking post:', error);
                // Remove animation class on error
                icon.classList.remove('like-animate');
            });
        });
    });
});

