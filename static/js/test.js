const modeBtn = document.getElementById("mode");
modeBtn.onchange = (e) => {
  if (modeBtn.checked === true) {
    document.documentElement.classList.remove("light");
    document.documentElement.classList.add("dark");
    document.getElementById("navbar").setAttribute("data-bs-theme", "dark");
    window.localStorage.setItem("mode", "dark");
  } else {
    document.documentElement.classList.remove("dark");
    document.documentElement.classList.add("light");
    document.getElementById("navbar").removeAttribute("data-bs-theme");

    window.localStorage.setItem("mode", "light");
  }
};

const mode = window.localStorage.getItem("mode");
if (mode == "dark") {
  modeBtn.checked = true;
  document.documentElement.classList.remove("light");
  document.documentElement.classList.add("dark");
  document.getElementById("navbar").setAttribute("data-bs-theme", "dark");
}
if (mode == "light") {
  modeBtn.checked = false;
  document.documentElement.classList.remove("dark");
  document.documentElement.classList.add("light");
  document.getElementById("navbar").removeAttribute("data-bs-theme");
}
