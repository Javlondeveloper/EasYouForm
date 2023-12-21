const navBtn = document.querySelector('.nav-btn'),
  navContent = document.querySelector('.nav-content')

navBtn.addEventListener('click', () => {
  navContent.classList.toggle('left-[0px]')
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
      navbar.classList.add('fixed')
      navbar.classList.remove('absolute')
      navbar.classList.remove('md:top-[10px]')
      navbarScrollingContent.classList.remove('navbar-rounded');
      navbar.classList.add('nav--bg');
    } else {
      navbar.classList.remove('fixed')
      navbar.classList.add('absolute') 
      navbar.classList.add('md:top-[10px]')
      navbarScrollingContent.classList.add('nav--bg');
      navbar.classList.remove('nav--bg');
      navbarScrollingContent.classList.add('navbar-rounded');
    }
  });
});


const mySlider = new Splide('#mySlider', {
  perMove:3,
  perPage: 3,
  gap: '40px',
  arrows: false ,
  type    : 'loop',
  autoplay: true, 
  interval:0,
  speed:200000,
  // focus    : 'center',
  autoWidth: true,
})

mySlider.mount()

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
    768:{
     slidesPerView: 4,
    }
  }
});



function startMarquee() {
  const container = document.getElementById("marqueeContainer");
  const content = document.getElementById("marqueeContent");

  const containerWidth = container.clientWidth;
  const contentWidth = content.clientWidth;

  let position = 0;

  function move() {
    position--;
    if (position < -containerWidth) {
      position = containerWidth;
    }
    content.style.transform = `translateX(${position}px)`;
    requestAnimationFrame(move);
  }

  move();
}


document.addEventListener("DOMContentLoaded", startMarquee);


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