document.querySelectorAll('.button').forEach((button, index) => {
    if (index === 0) {
        button.addEventListener('click', function () {
            alert('Congrats!');
        });
    } else if (index === 1) {
        button.addEventListener('click', function () {
            alert('Coming soon!');
        });
    }
});
