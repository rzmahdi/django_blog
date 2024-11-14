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

function toggleDelete(blogId){
    const menus = document.querySelectorAll(".delete-menu");
    menus.forEach(menu => {
        if (menu.id !== `delete-${blogId}`){
            menu.style.display = "none";
        }
    });

    const menu = document.getElementById(`delete-${blogId}`);
    if(menu.style.display === "block"){
        menu.style.display = "none";
    }else{
        menu.style.display = "block";
    }
}