console.log(`initializing`);

let fontSize = Number(localStorage.getItem("fontSize")) || 12; // default font size

const themes = {
    white: "white",
    dark: "dark",
    yellow: "yellow",
    blue: "blue",
};

const initializeTheme = (theme = "") => {
    let themeColor = "text-black";
    let textColor = "text-white";
    let navBgColor = "text-black";

    // remove existing classes first
    $("body").removeClass();
    $("#main-section").removeClass();
    $("#theme-navbar").removeClass();

    if (!theme && !localStorage.getItem("theme")) theme = "white";
    else if (localStorage.getItem("theme") && !theme) theme = localStorage.getItem("theme");

    localStorage.setItem("theme", theme);
    themeColor = getBackgroundColor(theme);
    textColor = getTextColors(theme);
    navBgColor = getNavTheme(theme);

    $("body").addClass(themeColor);
    $("#main-section").addClass(themeColor);
    $("#main-section").addClass(textColor);
    $("#theme-navbar").addClass(navBgColor);

    $(`#${theme}-theme-checkbox`).prop("checked", true);
    $("body").css("font-size", `${fontSize}px`);
};

const getBackgroundColor = (theme) => {
    return `bg-${theme === themes.dark ? "black" : theme}`;
};

const getTextColors = (theme) => {
    return theme === themes.white ? "text-black" : "text-white";
};

const getNavTheme = (theme) => {
    return `bg-${theme === themes.dark ? "blue" : theme}-900`;
};

const toggleTheme = (theme) => {
    initializeTheme(theme);
};

const increaseFont = () => {
    console.log(`Initializing fonts.......`);
    fontSize += 2;
    localStorage.setItem("fontSize", fontSize);
    $("body").css("font-size", `${fontSize}px`);
    console.log(`settings font size to ${fontSize}px`);
};

const decreaseFont = () => {
    console.log(`Initializing fonts.......`);
    fontSize -= 2;
    localStorage.setItem("fontSize", fontSize);
    $("body").css("font-size", `${fontSize}px`);
    console.log(`settings font size to ${fontSize}px`);
};

$("input.btn-check").on("change", function () {
    const theme = $(this).attr("id").replace("-checkbox", "");
    toggleTheme(theme);
});

$("#increase-font-size").on("click", increaseFont);
$("#decrease-font-size").on("click", decreaseFont);

initializeTheme();
