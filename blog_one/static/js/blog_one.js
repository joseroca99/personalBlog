window.addEventListener("DOMContentLoaded", () => {
	for (let i = 0; i < 10 * 10; i++) {
	  const rect = document.createElement("div");
	  rect.classList.add("rect");
	  document.querySelector(".containerSpecial").appendChild(rect);
	}


	const tl = gsap
	  .timeline()
	  .from(".rect", {
		scale: 0,
		alpha: 0,
		duration: 1,
		ease: "expo.out",
		repeat: -1,
		repeatDelay: 2,
		yoyo: true,
		stagger: {
		  each: 0.2,
		  from: "center", // 中央から
		  grid: "auto"
		},
	  });

  });