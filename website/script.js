const form = document.getElementById("uploadForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    loading.innerHTML = "⏳ Evaluating assignment...";
    result.textContent = "";

    const pdf = document.getElementById("pdf").files[0];

    if (!pdf) {
        alert("Choose a PDF");
        return;
    }

    const formData = new FormData();
    formData.append("file", pdf);

    try {

        const response = await fetch(
            "http://localhost:5678/webhook-test/submit-assignment",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        loading.innerHTML = "";

        // Show evaluation text
        result.textContent = data.result;

        // Show PDF
        if (data.report) {

            const pdfUrl =
                "http://127.0.0.1:8000/" + data.report;

            const download =
                document.getElementById("download");

            download.href = pdfUrl;
            download.style.display = "inline-block";

            const frame =
                document.getElementById("pdfFrame");

            frame.src = pdfUrl;
            frame.style.display = "block";
        }

    } catch (err) {

        loading.innerHTML = "";
        result.textContent = "Error: " + err;

    }

});