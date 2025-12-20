// Update the clock every second
function updateClock() {
    const now = new Date();
    
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    const timeString = `${hours}:${minutes}:${seconds}`;
    
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const dateString = now.toLocaleDateString('en-US', options);
    
    document.getElementById('time').textContent = timeString;
    document.getElementById('date').textContent = dateString;
}

// Toggle the navigation buttons visibility
function toggleNav() {
    const navContainer = document.getElementById('nav-container');
    const toggleBtn = document.getElementById('toggle-btn');
    
    navContainer.classList.toggle('hidden');
    
    if (navContainer.classList.contains('hidden')) {
        toggleBtn.style.display = 'block';
    } else {
        toggleBtn.style.display = 'none';
    }
}

updateClock();
setInterval(updateClock, 1000);
