document.addEventListener("DOMContentLoaded", function() {
    // 1. Find the Save button (Standard Django uses name="_save")
    const saveButtons = document.querySelectorAll('input[name="_save"], button[name="_save"]');

    // 2. Hide them initially
    saveButtons.forEach(btn => {
        btn.style.transition = "all 0.3s ease";
        btn.style.opacity = "0";
        btn.style.pointerEvents = "none"; // Prevent clicking while hidden
    });

    // 3. Listen for any changes in the admin list form
    const form = document.getElementById('changelist-form');
    if (form) {
        form.addEventListener('change', function() {
            // When ANY change happens (checkbox checked, text edited)
            saveButtons.forEach(btn => {
                btn.style.opacity = "1";
                btn.style.pointerEvents = "auto"; // Re-enable clicking

                // Optional: Change text/color to highlight action
                // btn.value = "Save Changes";
                // btn.style.transform = "scale(1.05)";
            });
        });
    }
});