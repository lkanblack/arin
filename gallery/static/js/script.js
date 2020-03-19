function burger(){
    let burger = document.querySelector('.burger'),
        close = document.querySelector('.close'),
        dropdown = document.querySelector('.dropdown'),
        lang_drop = document.querySelector('.lang-drop'),
        menu = document.querySelector('.menu');

    burger.addEventListener('click', function(){
        menu.classList.toggle('menu-open');
    });
    close.addEventListener('click', function(){
        menu.style.display = "none";
        close.style.display = "none";
        burger.style.display = "flex";
        dropdown.style.display = "flex";
    });
    dropdown.addEventListener('click', function(){
        lang_drop.classList.toggle('open-menu');
    });
}

burger();