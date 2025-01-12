$(document).ready(function () {
    debugger;
    checkDarkMode();
    initClickEvents();
});


function initClickEvents() {
    $('#dark-mode-btn').click(function () {
        toggleDarkMode('dark-mode-btn');
    });
    $('#light-mode-btn').click(function () {
        toggleDarkMode('light-mode-btn');
    });
}

function checkDarkMode() {
    const theme = localStorage.getItem('theme');
    if (theme === 'light') {
        $('body').removeClass('dark-theme');
        $('#light-mode-btn').remove();
        if ($('#dark-mode-btn').length === 0) {
            $('<li id="dark-mode-btn"><a href="#"><i class="bi bi-moon-stars"></i></a></li>').insertBefore($('#nav-buttons li:eq(1)')); // Insert before the second <li>
            $('#dark-mode-btn').click(function () {
                toggleDarkMode('dark-mode-btn');
            })
        }

    } else if (theme === 'dark') {
        $('body').addClass('dark-theme');
        $('#dark-mode-btn').remove();
        let b = $('#dark-mode-btn')
        if ($('#light-mode-btn').length === 0) {
            $('<li id="light-mode-btn"><a href="#"><i class="bi bi-brightness-high" style="font-size: 16px;position: relative; top: 0.5px;"></i></a></li>').insertBefore($('#nav-buttons li:eq(1)')); // Insert before the second <li>
            $('#light-mode-btn').click(function () {
                toggleDarkMode('light-mode-btn');
            })
        }
    }
}

function toggleDarkMode(elementId) {
    debugger;
    if (elementId === 'dark-mode-btn') {
        localStorage.setItem('theme', 'dark');
    } else if (elementId === 'light-mode-btn') {
        localStorage.setItem('theme', 'light');
    }
    checkDarkMode();
}
