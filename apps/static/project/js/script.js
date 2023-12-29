const navBtn = document.querySelector('.nav-btn'),
    navContent = document.querySelector('.nav-content')

navBtn.addEventListener('click', () => {
  navContent.classList.toggle('right-0');
  navContent.classList.toggle('opacity-100')
})

document.addEventListener('DOMContentLoaded', function () {
    let navbar = document.getElementById('navbar');
    let navbarScrollingContent = document.querySelector('#navbar-container');

    // Listen for the scroll event
    window.addEventListener('scroll', function () {
        // Check if the scroll position is greater than 0
        if (window.scrollY > 1) {
            navbarScrollingContent.classList.remove('nav--bg');
            navbar.classList.add('nav--bg');
            navbar.classList.remove('md:top-[10px]')
            navbar.classList.add('md:shadow-lg')
            navbarScrollingContent.classList.remove('md:shadow-lg')
        } else {
            navbar.classList.remove('md:shadow-lg')
            navbarScrollingContent.classList.add('md:shadow-lg')
            navbar.classList.add('md:top-[10px]')
            navbarScrollingContent.classList.add('nav--bg');
            navbar.classList.remove('nav--bg');
        }
    });
});


// Swiper

// let swiper = new Swiper(".mySwiper", {
//   spaceBetween: 30,
//   centeredSlides: true,
//   preventInteractionOnTransition: true,
//   loop: true,
//   speed: 25000,
//   autoplay: {
//     delay: 0,
//     disableOnInteraction: true,
//   },
// });

let swiperAbout = new Swiper(".aboutSwiper", {
    slidesPerView: 2,
    spaceBetween: 30,
    loop: true,
    breakpoints: {
        768: {
            slidesPerView: 4,
        }
    },
    autoplay: {
        delay: 3000, // Set the delay in milliseconds (e.g., 5000 for 5 seconds)
        disableOnInteraction: false, // Allow navigation while autoplay is active
    },
});


// function startMarquee() {
//     const container = document.getElementById("marqueeContainer");
//     const content = document.getElementById("marqueeContent");
//
//     const containerWidth = container.clientWidth;
//     const contentWidth = content.clientWidth;
//
//     let position = 0;
//
//     function move() {
//         position--;
//         if (position < -containerWidth) {
//             position = containerWidth;
//         }
//         content.style.transform = `translateX(${position}px)`;
//         requestAnimationFrame(move);
//     }
//
//     move();
// }
//
//
// document.addEventListener("DOMContentLoaded", startMarquee);


// awards

// function animateValue(obj, start, end, duration) {
//   let startTimestamp = null;
//   const step = (timestamp) => {
//     if (!startTimestamp) startTimestamp = timestamp;
//     const progress = Math.min((timestamp - startTimestamp) / duration, 1);
//     obj.innerHTML = Math.floor(progress * (end - start) + start);
//     if (progress < 1) {
//       window.requestAnimationFrame(step);
//     }
//   };
//   window.requestAnimationFrame(step);
// }

// const obj1 = document.getElementById("value-1");
// const obj2 = document.getElementById("value-2");
// const obj3 = document.getElementById("value-3");
// const obj4 = document.getElementById("value-4");
// animateValue(obj1, 0, 14, 1000);
// animateValue(obj2, 0, 2500, 2500);
// animateValue(obj3, 0, 225, 2000);
// animateValue(obj4, 0, 120, 1500);

new PureCounter();

function selectSize(sizeButton) {
    const sizeButtons = document.querySelectorAll('.size-btn');

    sizeButtons.forEach(btn => {
        // Remove 'selected' class from all buttons
        btn.classList.remove('selected');
    });

    // Add 'selected' class to the clicked button
    sizeButton.classList.add('selected');

    // Set the selected size in the hidden input field
    const selectedSize = sizeButton.getAttribute('data-size');
    document.getElementById('selectedSize').value = selectedSize;
}

// fixed top-0 max-md:bg-light left-0 z-50 w-full mx-auto transition duration-700 nav--bg
// fixed top-0 max-md:bg-light left-0 z-50 w-full mx-auto transition duration-700 nav--bg md:shadow-lg
//transition duration-700 md:rounded-[60px] container duration-400 py-2.5 px-5 flex items-center justify-between
//transition duration-700 md:rounded-[60px] container duration-400 py-2.5 px-5 flex items-center justify-between