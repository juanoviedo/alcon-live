let container = document.getElementById("flexcontainer");
let childNum = container.childElementCount;

let elements = container.children;
let width = elements.item(0).clientWidth;

for (let i = 4; i < childNum; i++){
	elements.item(i).style.maxWidth = width + 'px';
}

addEventListener("resize", ()=>{

	elements = container.children;
	width = elements.item(0).clientWidth;

	for (let i = 4; i < childNum; i++){
		elements.item(i).style.maxWidth = width + 'px';
	}

})