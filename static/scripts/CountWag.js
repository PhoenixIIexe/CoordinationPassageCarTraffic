const station = document.querySelectorAll('.stantion');
const addWag = document.querySelectorAll('.add-wag-on-station');


console.log(station);
for (let i = 0; i < station.length; ++i) {
    station[i].addEventListener('mouseover', () => {
        addWag[i].style.scale = '1';
        addWag[i].style.opacity = '1';
        addWag[i].style.height = '90px';
        addWag[i].style.width = '915px';
    });
    station[i].addEventListener('mouseout', () => {
        addWag[i].style.scale = '0';
        addWag[i].style.opacity = '0';
        addWag[i].style.height = '0';
        addWag[i].style.width = '0';
    });
}