function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function showNavbar(){
    navbar = document.querySelector('.navbar-mobile-right');
    navbar.style.display="flex";
    navbar.style.left="100%";
    
    navbar.style.left="90%";
    navbar.style.left="80%";
    navbar.style.left="70%";
    navbar.style.left="60%";
    navbar.style.left="50%";
    navbar.style.left="40%";
    navbar.style.left="30%";
    await sleep(0);
    navbar.style.left="20%";
    await sleep(0);
    navbar.style.left="10%";
    await sleep(0);
    navbar.style.left="0%";
}

async function hideNavbar(){
    navbar = document.querySelector('.navbar-mobile-right');
    navbar.style.left="0%";
    await sleep(10);
    navbar.style.left="10%";
    await sleep(10);
    navbar.style.left="20%";
    await sleep(10);
    navbar.style.left="30%";
    await sleep(10);
    navbar.style.left="40%";
    await sleep(10);
    navbar.style.left="50%";
    await sleep(10);
    navbar.style.left="60%";
    await sleep(10);
    navbar.style.left="70%";
    await sleep(10);
    navbar.style.left="80%";
    await sleep(10);
    navbar.style.left="90%";
    await sleep(10);
    navbar.style.left="100%";
    navbar.style.display="none";
}


