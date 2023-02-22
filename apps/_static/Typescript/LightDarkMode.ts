var themeToggleDarkIcon = document.getElementById('theme_toggle_dark_icon');
var themeToggleLightIcon = document.getElementById('theme_toggle_light_icon');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    // themeToggleLightIcon.classList.add('left-0');
    // themeToggleDarkIcon.classList.add('left-0');
    // DARK MODE
    themeToggleLightIcon.classList.add('translate-x-full');
    themeToggleDarkIcon.classList.add('translate-x-full');
    themeToggleLightIcon.classList.add('opacity-0');

    document.documentElement.classList.add('dark');
    localStorage.setItem('color-theme', 'dark');
    console.log("DARK")
} else {
    // LIGHT MODE
    themeToggleDarkIcon.classList.add('opacity-0');

    document.documentElement.classList.remove('dark');
    localStorage.setItem('color-theme', 'light');
    console.log("LIGHT")
}

var themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {

    // toggle icons inside button
    themeToggleDarkIcon.classList.toggle('translate-x-full');
    // themeToggleDarkIcon.classList.toggle('right-0');
    // themeToggleDarkIcon.classList.toggle('left-0');
    themeToggleDarkIcon.classList.toggle('opacity-0')

    themeToggleLightIcon.classList.toggle('translate-x-full');
    // themeToggleLightIcon.classList.toggle('right-0');
    // themeToggleLightIcon.classList.toggle('left-0');
    themeToggleLightIcon.classList.toggle('opacity-0')

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }

});