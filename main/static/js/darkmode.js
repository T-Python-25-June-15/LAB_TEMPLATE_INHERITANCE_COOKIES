function toggleDarkMode() {
    const body = document.body;
    const icon = document.getElementById('dark-icon');

    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');

    if (body.classList.contains('dark-mode')) {
        icon.innerText = 'light_mode';
    } else {
        icon.innerText = 'dark_mode';
    }
}
