document.addEventListener('DOMContentLoaded', () => {
    console.log('Workshop loaded successfully!');
    // Example: Dynamically adding a contributor to the list
    const list = document.getElementById('list');
    const li = document.createElement('li');
    li.textContent = 'Naveen - Instructor';
    list.appendChild(li);
});
