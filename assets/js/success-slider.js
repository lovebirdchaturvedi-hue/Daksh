// success-slider.js
document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".success-slide");
    if (slides.length === 0) return;

    const animations = ["fade-in", "slide-up", "slide-left", "zoom-in"];
    let currentSlide = 0;
    
    // Reset all slides
    slides.forEach(slide => {
        slide.style.display = "none";
        slide.className = "success-slide"; // reset classes
    });

    // Show first slide
    slides[currentSlide].style.display = "flex";
    slides[currentSlide].classList.add("active", "fade-in");

    setInterval(() => {
        slides[currentSlide].style.display = "none";
        slides[currentSlide].className = "success-slide"; // remove old animation class
        
        currentSlide = (currentSlide + 1) % slides.length;
        
        const randomAnimation = animations[Math.floor(Math.random() * animations.length)];
        slides[currentSlide].style.display = "flex";
        // Force reflow
        void slides[currentSlide].offsetWidth;
        slides[currentSlide].classList.add("active", randomAnimation);
    }, 10000); // 10 seconds
});
