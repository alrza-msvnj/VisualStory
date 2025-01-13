$(document).ready(function () {
    debugger;
    checkDarkMode();
    initClickEvents();
});


function initClickEvents() {
    $('#darkModeBtn').click(function () {
        toggleDarkMode('darkModeBtn');
    });
    $('#lightModeBtn').click(function () {
        toggleDarkMode('lightModeBtn');
    });
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

function toggleDarkMode(elementId) {
    debugger;
    if (elementId === 'darkModeBtn') {
        localStorage.setItem('theme', 'dark');
    } else if (elementId === 'lightModeBtn') {
        localStorage.setItem('theme', 'light');
    }
    checkDarkMode();
}
