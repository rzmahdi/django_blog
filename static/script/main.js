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

function toggleCancel(blogId){
    const delete_menu = document.getElementById(`delete-${blogId}`);
    const menu = document.getElementById(`menu-${blogId}`);
    
    delete_menu.style.display = "none";
    menu.style.display = "none";
}