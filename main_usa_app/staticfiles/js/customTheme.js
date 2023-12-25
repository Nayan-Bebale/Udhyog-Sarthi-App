console.log(`initializing`);


let fontSize =  Number(localStorage.getItem("fontSize")) ?? 12; // default font size
const themes = {
	white: "white",
	dark: "dark",
	yellow: "yellow",
	blue: "blue",
};

const backgroundColors = {
	[themes.white]: "bg-white",
	[themes.dark]: "bg-dark",
	[themes.yellow]: "bg-warning",
	[themes.blue]: "bg-primary",
};
const textColors = {
	[themes.white]: "text-black",
	[themes.dark]: "text-white",
	[themes.yellow]: "text-black",
	[themes.blue]: "text-black",
};
const navThemes = {
	[themes.white]: "custom-bg-blue-900",
	[themes.yellow]: "bg-dark",
	[themes.blue]: "custom-bg-orange",
	[themes.dark]: "custom-bg-yellow-300",
};

const initializeTheme = (theme = "") => {
	$("#btn-theme-change-label").text().toLowerCase() === themes.dark ? $("#btn-theme-change-label").text("White") : $("#btn-theme-change-label").text("Dark");
	let themeColor = "text-black";
	let textColor = "text-white";
	console.log(`Initializing theme.......`);

	// remove existing classes first
	$("body").removeClass()
	$("h1").removeClass()
	$("#main-section").removeClass();

	if (!theme && !localStorage.getItem("theme")) theme = "white";
	else if (localStorage.getItem("theme") && !theme) theme = localStorage.getItem("theme");

	localStorage.setItem("theme", theme);
	themeColor = backgroundColors[theme];
	textColor = textColors[theme];
	$("body").addClass(themeColor);
	$("body").addClass(textColor);
	$("h1").addClass(`display-5 animated fadeIn mb-4 ${textColor}`);
	$("#main-section").addClass(themeColor);
	$("#main-section").addClass(textColor);
	$("body").css("font-size", `${fontSize}px`);
	console.log(`theme: ${theme} settings themeColor to ${themeColor}`);
	console.log(`theme: ${theme} settings textColor to ${textColor}`);
};

// initialize font size
const increaseFont = () => {
	console.log(`Initializing fonts.......`);

	if (localStorage.getItem("fontSize")) fontSize = Number(localStorage.getItem("fontSize"));
	fontSize += 2;
	localStorage.setItem("fontSize", fontSize);
	$("body").css("font-size", `${fontSize}px`);
	console.log(`settings font size to ${fontSize}px`);
};
const decreaseFont = () => {
	console.log(`Initializing fonts.......`);
	if (localStorage.getItem("fontSize")) fontSize = Number(localStorage.getItem("fontSize"));
	fontSize -= 2;
	localStorage.setItem("fontSize", fontSize);
	$("body").css("font-size", `${fontSize}px`);
	console.log(`settings font size to ${fontSize}px`);
};

$("#btn-theme-change").on("click", () => initializeTheme($("#btn-theme-change-label").text().toLowerCase()))

$("#increase-font-size").on("click", increaseFont);
$("#decrease-font-size").on("click", decreaseFont);



initializeTheme();
