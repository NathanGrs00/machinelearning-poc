document.getElementById("btn-search").addEventListener("click", () => {
    const inputValue = document.getElementById("input-place").value;
    document.getElementById("result-place").textContent = inputValue;
});

document.getElementById("input-place").addEventListener("change", () => {
    const inputValue = document.getElementById("input-place").value;
    document.getElementById("result-place").textContent = inputValue;
});