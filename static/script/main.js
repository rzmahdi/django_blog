function toggleMenu(blogId) {
    const menus = document.querySelectorAll('.menu');
    menus.forEach(menu => {
        if (menu.id !== `menu-${blogId}`) {
            menu.classList.remove("show");
        }
    });

    const menu = document.getElementById(`menu-${blogId}`);
    if (menu.classList.contains("show")) {
        menu.classList.remove("show");
    } else {
        menu.classList.add("show");
    }
}

window.onclick = function(event){
    if(!event.target.matches('.menu-btn')){
        const menus = document.querySelectorAll('.menu');
        menus.forEach(menu => {
            menu.classList.remove("show");
        })
    }
}