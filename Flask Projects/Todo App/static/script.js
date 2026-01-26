document.addEventListener('DOMContentLoaded', () => {
    const tasks = document.querySelectorAll('.task-item');

    // 1. Staggered Entrance Animation
    // We set initial styles here so it works even before you write your CSS
    tasks.forEach((task, index) => {
        task.style.opacity = '0';
        task.style.transform = 'translateY(20px)';
        task.style.transition = 'opacity 0.4s ease, transform 0.4s ease';

        // Delay each item slightly based on its index
        setTimeout(() => {
            task.style.opacity = '1';
            task.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // 2. Delete Confirmation
    const deleteBtns = document.querySelectorAll('.btn-delete');
    deleteBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (!confirm("Are you sure you want to delete this task?")) {
                e.preventDefault();
            }
        });
    });
});