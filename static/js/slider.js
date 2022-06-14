

const images = ['admin-block.jpg','band.JPG','siachin.jpg','cultural2.JPG','boxing.jpg','fire.JPG'];

currentImage = 0;

const changeImage = () => {
    currentImage++;
    if (currentImage >= images.length) {
        currentImage = 0;
    }
    document.getElementById('slider').src = `../static/images/${images[currentImage]}`;
}

setInterval(changeImage, 3000);