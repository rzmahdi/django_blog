function toggleMenu(blogId) {
    const menus = document.querySelectorAll('.menu');
    menus.forEach(menu => {
        if (menu.id !== `menu-${blogId}`) {
            menu.style.display = "none";
        }
    });

    const menu = document.getElementById(`menu-${blogId}`);
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

window.onclick = function(event) {
    if (!event.target.matches('.menu-btn')) {
        const menus = document.querySelectorAll('.menu');
        menus.forEach(menu => {
            menu.style.display = "none";
        });
    }
}