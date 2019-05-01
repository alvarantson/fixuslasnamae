var imgs = document.getElementsByClassName("thumbnailt");
function viewImg(e){
	var clicked = e.target;
	console.log(e)
	e.path[2].classList.toggle("col-sm-2");
	e.path[2].classList.toggle("products");
	e.path[2].classList.toggle("overlay");
	e.path[2].childNodes[5].classList.toggle("hidden");
	//e.path[2].childNodes[1].classList.toggle("hidden");
	e.path[1].classList.toggle("imgbox");
	e.path[0].childNodes[3].classList.toggle("hidden");
	e.path[0].childNodes[5].classList.toggle("hidden");
	clicked.classList.toggle("thumbnailt");
	clicked.classList.toggle("viewImg");
};