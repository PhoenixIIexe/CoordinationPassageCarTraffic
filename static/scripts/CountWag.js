// Get the first station and add-wag-on-station elements
const station = document.querySelector('.stantion');
const addWag = document.querySelector('.add-wag-on-station');

// Add event listener for mouseover
station.addEventListener('mouseover', (el) => {
    console.log(el);
});

// Add event listener for mouseout
station.addEventListener('mouseout', () => {
    addWag.classList.remove('show');
});