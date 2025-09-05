document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("button-name").addEventListener("click", async () => {
        const result = await eel.get_number()();
        prompt_alerts(result);
    });

    function prompt_alerts(desc){
        alert(desc);
    }
});
