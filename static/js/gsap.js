var animation = gsap.timeline();
animation
	.from('.logo', {opacity: 0, duration: 1, y: -30})
	.from('.social a', { opacity: 0, y: -30, stagger: {each:0.1}}, "<")
	.from('.lineasdenegocio', { opacity: 0, duration: 1, ease: "back.out(1.7)", x: -100 }, "+=0.4")
	.from('.btn-whatsapp', { duration: 2.4, ease: "bounce.out", y: -900})




//gsap.from('.lineasdenegocio', {delay: 1.4, opacity: 0, duration: 1, x: -30});
//gsap.from('.lineasdenegocio', { delay: 2,duration: 2.5, opacity: 0, ease: "elastic.out(1, 0.3)", x: -100 });

