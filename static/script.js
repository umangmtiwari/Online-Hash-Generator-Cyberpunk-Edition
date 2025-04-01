document.getElementById('generateButton').addEventListener('click', generateHash);
document.getElementById('inputText').addEventListener('input', generateHash);  // Live preview

function generateHash() {
    const text = document.getElementById('inputText').value.trim();
    const algorithm = document.getElementById('algorithm').value;

    if (!text) {
        document.getElementById('hashResult').textContent = "⚠️ Enter some text!";
        return;
    }

    const data = { text: text, algorithm: algorithm };

    fetch('/generate-hash', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.error) {
            document.getElementById('hashResult').textContent = `⚠️ ${result.error}`;
        } else {
            document.getElementById('hashResult').textContent = result.hash;
        }
    })
    .catch(error => {
        document.getElementById('hashResult').textContent = "⚠️ Error occurred!";
        console.error(error);
    });
}

// Copy to clipboard
document.getElementById('copyButton').addEventListener('click', function() {
    const hashText = document.getElementById('hashResult').textContent;
    if (hashText) {
        navigator.clipboard.writeText(hashText).then(() => {
            alert("✅ Hash copied to clipboard!");
        }).catch(err => console.error("Copy failed", err));
    }
});
