document.addEventListener("DOMContentLoaded", function(){

    const bookingForm = document.getElementById("bookingForm");

    if(bookingForm){
        bookingForm.addEventListener("submit", function(e){
            e.preventDefault();
            alert("Room booked successfully at The Perween Residency!");
        });
    }

    const contactForm = document.getElementById("contactForm");

    if(contactForm){
        contactForm.addEventListener("submit", function(e){
            e.preventDefault();
            alert("Thank you for contacting us!");
        });
    }

});