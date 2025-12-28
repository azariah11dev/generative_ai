document.addEventListener("DOMContentLoaded", () => {
    const text_input = document.getElementById("container-1-text-input");
    const summary_output = document.getElementById("container-1-summary-output");
    const summarize_button = document.getElementById("summarize-button");

    summarize_button.addEventListener("click", async () => {
        try {
            const response = await fetch("http://localhost:8000/summarize", {
                method: "POST",
                mode: "cors",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: text_input.value })
            });

            const data = await response.json();
            summary_output.value = data.summary;
            summary_output.textContent = data.summary;
        } catch (error) {
            console.error("Error:", error);
            summary_output.value = "An error occurred while summarizing the text.";
        }
    });
});