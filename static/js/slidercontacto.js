"use strict";

// class SliderCreator {
// 	constructor (_id, _numPic, _picName) { //setup

// 		this.numPic = _numPic;
// 		this.picName = _picName;
		
// 		this.elem = document.getElementById(_id);

// 		this.slideIndex = 1;
		
// 		this.opa;

// 		this.opInterval;
// 		this.interval;
// 		this.timeout;

// 		this.showImage(this.slideIndex);

		
// 		this.interval = setInterval(function(){
// 			this.slideIndex++;
// 			this.verifyRange(); 				// verifys that slideIndex is in range (1 to 4 in this case)
// 			this.showImage(this.slideIndex);
// 		}, 5000);
		
// 	}

// 	verifyRange(){
// 		if (this.slideIndex > this.numPic){
// 			this.slideIndex = 1;
// 		}
// 		if (this.slideIndex < 1){
// 			this.slideIndex = this.numPic;
// 		}
// 	}

// 	plusIndex(n){
// 		this.slideIndex += n;
// 		this.verifyRange(); 				// verifys that slideIndex is in range (1 to 4 in this case)
// 		this.showImage(this.slideIndex);    // sums n from buttons (-1) or (+1) in slider
// 		clearInterval(this.interval);
// 		clearTimeout(this.timeout);
// 		this.timeout = setTimeout(function(){
// 			this.interval = setInterval(function(){
// 				this.slideIndex++;
// 				this.verifyRange(); 				// verifys that slideIndex is in range (1 to 4 in this case)
// 				this.showImage(this.slideIndex);
// 			}, 5000);
// 		}, 5000)
// 	}

// 	showImage() {
// 		clearInterval(this.opInterval);

// 		this.elem.style.opacity = "0.4";

// 		this.elem.src = "img/"+ this.picName + this.slideIndex + ".jpg";

// 		this.opa = "0.4";
// 		this.opInterval = setInterval(function(){
// 			if (this.opa >= 1) {
// 				this.elem.style.opacity = 1;
// 			  	clearInterval(this.opInterval);
// 			} else {
// 			  	this.opa += 0.01; 
// 			  	this.elem.style.opacity = this.opa; 
// 			}
// 		}, 10);
// 	} 
// }


//let slider1 = new SliderCreator("image-show", 4, "ban"); 

//---------------------------------------------


class SliderCreator {
	constructor(_id){ //set constructor
		this.elem = document.getElementById(_id); // select the img label
		this.elem.src = "img/ban1.jpg";	// set the initial image
		this.elem.style.opacity = 0.4; // set opacity to 0.4
		this.opInterval; // initialize opInterval (i need this line to my application)
	}

	changeImage(){

		this.elem.src = "img/ban2.jpg"; //change the image
		clearInterval(this.opInterval) // I need to reset opInterval in my application
		this.opInterval = setInterval(function(){ // Set interval to increment opacity each 10 ms
			if (this.elem.style.opacity >= 1) {  // when opInterval variable hits 1
				clearInterval(this.opInterval); // stop the timer opInterval
				this.elem.style.opacity = 1; 	// just incase, forces opacity to one
			} else {
			  	this.elem.style.opacity += 0.01; // else, increment opacity 0.01 each 10 ms
			}
		}, 10);
	}	
}

let slider1 = new SliderCreator("image-show", 4, "ban"); // create new object





//-----------------------------------

// let elem = document.getElementById("image-show");  // elem points image element to manupulate
// let slideIndex = 1;   // Inicialization of variable that moves from 1 to 4
// let numPic = 4; // Maximum pectures to slide on

// let opInterval; // Opacity timer that manipulates opacity of images
// let interval;	 // (timer) Interval of time to slide images
// let timeout;   // (timer) incialization of timer variable

// showImage(slideIndex); // runs function first time to show firs image

// interval = setInterval(function(){ // sets interval to slide images every 5 secons
// 	slideIndex++;				// sums 1 to slideIndex
// 	slideIndex = verifyRange(slideIndex, 1, numPic);// verifys that slideIndex is in range (1 to 4 in this case)
// 	showImage(slideIndex);		// Runs showImage function that changes the image dynamicaly
// }, 5000);



// function verifyRange (variable, minIndex, maxIndex){ // Verify 1 to 4 range of variable
// 	if (variable > maxIndex){
// 		return minIndex;
// 	}
// 	if (slideIndex < minIndex){
// 		return maxIndex;
// 	}
// 	return variable;
// }

// function plusIndex(n){ // function for slider buttons
// 	slideIndex += n; 	// sums n
// 	slideIndex = verifyRange(slideIndex, 1, numPic); 				// verifys that slideIndex is in range (1 to 4 in this case)
// 	showImage(slideIndex); // shows image
// 	clearInterval(interval); // stop interval timer
// 	clearTimeout(timeout);		//stop timeout timer
// 	timeout = setTimeout(function(){  // sets new timeout timer
// 		interval = setInterval(function(){ // sets new interval timer 
// 			slideIndex++;					// sums one to show the next image
// 			slideIndex = verifyRange(slideIndex, 1, numPic);// verifys that slideIndex is in range (1 to 4 in this case)
// 			showImage(slideIndex);		// runs function that show next image
// 		}, 5000)
// 	}, 5000)  // after pressing the button it shows the image 10 seconds and then works automatically again
// }

// function showImage(n) {
// 	clearInterval(opInterval); // clears "opacity interval" that manipulates the image opacity

// 	elem.style.opacity = 0.4; // sets image opacity to 0.4

// 	elem.src = "img/ban" + n + ".jpg"; // changes image source

// 	let opa = 0.4;						// restarts opacity value
// 	opInterval = setInterval(frame, 10); // sets interval to change opacity each 10 ms

// 	function frame() {  // function to change opacity until opa >= 1
// 		if (opa >= 1) {
// 			elem.style.opacity = 1;
// 		  	clearInterval(opInterval); // kills op interval
// 		} else {
// 		  	opa+=0.01; 
// 		  	elem.style.opacity = opa; 
// 		}
// 	}
// }