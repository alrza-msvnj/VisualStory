var isLoggedIn = false;
var allRecentPosts = [];


$(document).ready(function () {
    debugger;
    isLoggedIn = isAuthenticated();
    if (isLoggedIn) {
        loadProfile();
    }
    initLoginLogoutButtons();
    checkDarkMode();
    initClickEvents();
    getAllRecentPosts();
});


function isAuthenticated() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.split('=');
        if (key.trim() === 'session_id') {
            return true;
        }
    }

    return false;
}

function initLoginLogoutButtons() {
    if (isLoggedIn) {
        $('#loginBtn').hide();
        $('#logoutBtn').show();
    } else {
        $('#loginBtn').show();
        $('#logoutBtn').hide();
    }
}

function checkDarkMode() {
    const theme = localStorage.getItem('theme');
    if (theme === 'light') {
        $('body').removeClass('dark-theme');
        $('#lightModeBtn').remove();
        if ($('#darkModeBtn').length === 0) {
            $('<li id="darkModeBtn"><a href="#"><i class="bi bi-moon-stars"></i></a></li>').insertBefore($('#nav-buttons li:eq(1)')); // Insert before the second <li>
            $('#darkModeBtn').click(function () {
                toggleDarkMode('darkModeBtn');
            })
        }

    } else if (theme === 'dark') {
        $('body').addClass('dark-theme');
        $('#darkModeBtn').remove();
        let b = $('#darkModeBtn')
        if ($('#lightModeBtn').length === 0) {
            $('<li id="lightModeBtn"><a href="#"><i class="bi bi-brightness-high" style="font-size: 16px;position: relative; top: 0.5px;"></i></a></li>').insertBefore($('#nav-buttons li:eq(1)')); // Insert before the second <li>
            $('#lightModeBtn').click(function () {
                toggleDarkMode('lightModeBtn');
            })
        }
    }
}

function initClickEvents() {
    $('#darkModeBtn').click(function () {
        toggleDarkMode('darkModeBtn');
    });
    $('#lightModeBtn').click(function () {
        toggleDarkMode('lightModeBtn');
    });

    $('#postBtn').click(post);

    $('#logoutBtn').click(function (event) {
        logout(event);
    });

    $('#profileBtn').click(function (event) {
        profile(event);
    })
}

function toggleDarkMode(elementId) {
    debugger;
    if (elementId === 'darkModeBtn') {
        localStorage.setItem('theme', 'dark');
    } else if (elementId === 'lightModeBtn') {
        localStorage.setItem('theme', 'light');
    }
    checkDarkMode();
}

function loadProfile() {
    $.ajax({
        url: '/api/user/get_profile_picture',
        type: 'POST',
        contentType: false,
        processData: false,
        success: function (response) {
            if (response.profile_picture) {
                $('#navProfilePicture').attr('src', `../static/assets/profile_pictures/${response.profile_picture}`);
                $('#writePostProfilePicture').attr('src', `../static/assets/profile_pictures/${response.profile_picture}`);
                $('#writePostAuthor').text(response.username)
            }
        }
    });
}

function post() {
    if (!isLoggedIn) {
        window.location.href = '/login';
        return;
    }

    // Serialize form data into an object (dictionary)
    const formData = {};
    formData.content = $('#postContent').val();

    $.ajax({
        url: '/api/post',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function (response) {
            console.log('Login successful:', response);
            location.reload();
        },
        error: function (error) {
            console.error('Login failed:', error);
        }
    });
}

function logout(event) {
    event.preventDefault();

    $.ajax({
        url: 'api/authentication/logout',
        type: 'GET',
        success: function (response, status, xhr) {
            console.log('Logout successful:', response);

            // check if the response contains a redirect URL
            const redirectUrl = xhr.getResponseHeader("X-Redirect-To");
            if (redirectUrl) {
                window.location.href = redirectUrl;  // Redirect to the new page
            } else {
                location.reload();  // If no redirect, just refresh
            }
        },
        error: function (xhr, status, error) {
            console.error('Logout failed:', status, error);
        },
        complete: function () {
            console.log('Request completed.');
        }
    });
}

function profile(event) {
    event.preventDefault();

    if (isLoggedIn) {
        window.location.href = '/profile';
    } else {
        window.location.href = '/login';
    }
}

function getAllRecentPosts() {
    $.ajax({
        url: '/api/post',
        type: 'GET',
        contentType: 'application/json',
        success: function (response) {
            allRecentPosts = response;
            showPosts();
        },
        error: function (error) {
            console.error('Getting recent posts failed:', error);
        }
    });
}

function getUserById(userId) {
    let user;
    $.ajax({
        url: `/api/user/{id}?user_id=${userId}`,
        type: 'GET',
        contentType: 'application/json',
        async: false,
        success: function (response) {
            user = response;
        },
        error: function (error) {
            console.error('Getting user failed:', error);
        }
    });
    return user;
}

function showPosts() {
    let postContainer = "";
    for (let post of allRecentPosts) {
        let user = getUserById(post.user_id);
        let postFrame = `
        <div class="post-container">
            <div class="post-row">
                <div class="user-profile">
                    <img src="../static/assets/profile_pictures/${user.profile_picture}" alt="">
                    <div>
                        <p>${user.username}</p>
                        <span>${post.created_at}</span>
                    </div>
                </div>
            </div>

            <p class="post-text">${post.content}</p>
            <img src="../static/assets/images/feed-image-1.png" alt="" class="post-img">
        </div>`;
        postContainer += postFrame;
    }
    $('#postContainer').append(postContainer);
}
