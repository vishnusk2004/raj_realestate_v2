// Django Main JavaScript - Fixed Version
// This replaces the problematic React build

document.addEventListener('DOMContentLoaded', function() {
    console.log('Django main script loaded successfully');
    
    // Initialize any custom functionality here
    initializeForms();
    initializeModals();
    initializeDropdowns();
});

function initializeForms() {
    // Handle form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Let the form submit naturally
            console.log('Form submitted:', form.action);
        });
    });
}

function initializeModals() {
    // Handle modal functionality
    const modals = document.querySelectorAll('[data-modal]');
    modals.forEach(modal => {
        modal.addEventListener('click', function() {
            const target = document.querySelector(this.getAttribute('data-modal'));
            if (target) {
                target.classList.remove('hidden');
            }
        });
    });
    
    // Close modals
    const closeButtons = document.querySelectorAll('[data-close-modal]');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modal = this.closest('.modal');
            if (modal) {
                modal.classList.add('hidden');
            }
        });
    });
}

function initializeDropdowns() {
    // Handle dropdown functionality
    const dropdowns = document.querySelectorAll('[data-dropdown]');
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', function() {
            this.classList.toggle('active');
        });
    });
}

// Utility functions
function showSuccessPopup(message) {
    const popup = document.getElementById('successPopup');
    const messageElement = document.getElementById('successMessage');
    
    if (message && messageElement) {
        messageElement.textContent = message;
    }
    
    if (popup) {
        popup.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }
}

function closeSuccessPopup() {
    const popup = document.getElementById('successPopup');
    if (popup) {
        popup.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }
}

// Export functions for global use
window.showSuccessPopup = showSuccessPopup;
window.closeSuccessPopup = closeSuccessPopup;
