window.onscroll = function(){
    scrollFunction();
}

function scrollFunction(){
    let logo =$("#logo")
    let search = $('#search')
    let header = $("header")
    if (
        document.body.scrollTop >= 50 ||
        document.documentElement.scrollTop >= 50
    ){
        header.addClass("background")
    }else if (
        document.body.scrollTop < 50 ||
        document.documentElement.scrollTop < 50
    ){
        header.removeClass("background")      
    }
}

//menu bar click
let menuBar = document.querySelector(".navbar-toggler")
let navHeader = document.querySelector("#nav-header")
menuBar.addEventListener("click", ()=>{
   navHeader.classList.toggle("d-none")
})

//search icon click
let searchBtn = document.querySelectorAll(".searchbtn")
let search = document.querySelector("#search")

for(let i of searchBtn){
    i.addEventListener("click", ()=>{
        search.classList.toggle("d-none")
    })
}

let addCartEl = document.querySelectorAll('.add-cart')
let addCollectionEl = document.querySelectorAll('.add-collection')


for (i of addCartEl){
    i.addEventListener('click', ()=>{
        addCart()
        let elId = document.querySelectorAll('.card-body')
        console.log(elId)
    })
    
}

for (i of addCollectionEl){
    i.addEventListener('click', ()=>{
        addCollection()
        let elId = document.querySelectorAll('.card-body')
        console.log(elId[i])
    })
    
}

function addCart(){
    console.log("add to cart")
}

function addCollection(){
    console.log("add to collection")
}