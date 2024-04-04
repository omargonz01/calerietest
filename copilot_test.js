function calculateDaysBetweenDates(begin, end) {
    const beginDate = new Date(begin);
    const endDate = new Date(end);
    const timeDifference = endDate.getTime() - beginDate.getTime();
    return Math.ceil(timeDifference / (1000 * 3600 * 24));
}

// find all images without alternate text
// and give them a red border

function test() {
    const images = document.querySelectorAll('img');
    images.forEach((image) => {
        if (!image.alt) {
            image.style.border = '3px solid red';
        }
    });
}

// identify food in the image
// and display the result in the console


function identifyFood() {
    const images = document.querySelectorAll('img');
    images.forEach((image) => {
        fetch('https://api.foodai.org/v1/classify?url=' + image.src)
            .then((response) => response.json())
            .then((data) => console.log(data));
    });
}