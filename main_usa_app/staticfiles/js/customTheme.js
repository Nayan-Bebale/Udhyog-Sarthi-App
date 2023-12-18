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
	[themes.dark]: "bg-black",
	[themes.yellow]: "bg-yellow-500",
	[themes.blue]: "bg-blue-500",
};
const textColors = {
	[themes.white]: "text-black",
	[themes.dark]: "text-white",
	[themes.yellow]: "text-black",
	[themes.blue]: "text-black",
};
const navThemes = {
	[themes.white]: "bg-blue-900",
	[themes.yellow]: "bg-black",
	[themes.blue]: "bg-stone-500",
	[themes.dark]: "bg-yellow-300",
};

const initializeTheme = (theme = "") => {
	let themeColor = "text-black";
	let textColor = "text-white";
	let navBgColor = "text-black";
	console.log(`Initializing theme.......`);

	// remove existing classes first
	$("body").removeClass()
	$("#main-section").removeClass();
	$("#theme-navbar").removeClass();
	Object.keys(themes).forEach((key) => $(`#${key}-theme`).removeClass("bg-gray-900"));

	if (!theme && !localStorage.getItem("theme")) theme = "white";
	else if (localStorage.getItem("theme") && !theme) theme = localStorage.getItem("theme");

	localStorage.setItem("theme", theme);
	themeColor = backgroundColors[theme];
	textColor = textColors[theme];
	navBgColor = navThemes[theme];
	$("body").addClass(themeColor);
	$("#main-section").addClass(themeColor);
	$("#main-section").addClass(textColor);
	$("#theme-navbar").addClass(navBgColor);
	$("#theme-navbar").addClass(textColor);
	$(`#${theme}-theme`).addClass("bg-gray-900");
	$("body").css("font-size", `${fontSize}px`);
	console.log(`theme: ${theme} settings themeColor to ${themeColor}`);
	console.log(`theme: ${theme} settings textColor to ${textColor}`);
	console.log(`theme: ${theme} settings navBgColor to ${navBgColor}`);
};

// initialize theme
const initializeDarkTheme = () => initializeTheme("dark");
const initializeWhiteTheme = () => initializeTheme("white");
const initializeBlueTheme = () => initializeTheme("blue");
const initializeYellowTheme = () => initializeTheme("yellow");

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

$("#dark-theme").on("click", initializeDarkTheme);
$("#white-theme").on("click", initializeWhiteTheme);
$("#blue-theme").on("click", initializeBlueTheme);
$("#yellow-theme").on("click", initializeYellowTheme);

$("#increase-font-size").on("click", increaseFont);
$("#decrease-font-size").on("click", decreaseFont);



initializeTheme();
