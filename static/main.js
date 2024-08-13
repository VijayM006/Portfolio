// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
  
  // Loading Screen: Hide the loading screen after 1 second
  const loadingScreen = document.getElementById('loading-screen');
  setTimeout(() => {
    loadingScreen.style.display = 'none';
  }, 1000);

  // Smooth Scrolling: Enables smooth scroll for all anchor links starting with '#'
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  // Form Validation: Ensure all fields are filled before submitting the form
  const form = document.getElementById('contact-form');
  form.addEventListener('submit', (event) => {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (!name || !email || !message) {
      alert('Please fill in all fields.');
      event.preventDefault(); // Prevent the form from submitting if any field is empty
    }
  });

});
