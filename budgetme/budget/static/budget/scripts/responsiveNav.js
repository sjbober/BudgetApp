// This function controls the navigation bar when the screen is mobile. If the hamburger is clicked the menu bar will expand, and when it is clicked a second time the menu bar will hide.
let hamburger = document.getElementsByClassName("hamb")[0];
// console.log(hamburger);
hamburger.addEventListener("click",controlNavBar);

let logo = document.getElementsByClassName("logo")[0];
let navLinkList = document.getElementsByClassName("navbar-link");
// console.log(navLinkList);

function controlNavBar() {
    // console.log(navLinkList[0].style.display);
    if (navLinkList[0].parentNode.className == "hide") {
        logo.style.alignSelf = "start";

        for (let i =0; i < navLinkList.length; i++) {
            navLinkList[i].parentNode.className = "";
        }
    }
    else {
        for (let i =0; i < navLinkList.length; i++) {
            navLinkList[i].parentNode.className = "hide";
        }

    }
    
  
}
