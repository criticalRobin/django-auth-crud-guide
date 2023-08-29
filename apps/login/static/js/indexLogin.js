const labels = document.querySelectorAll(".form-c label");

function addSpanElements(label) {
    let text = label.innerText;
    label.innerText = "";

    for (let i = 0; i < text.length; i++) {
        let sp = document.createElement("span");
        sp.innerText = text[i];
        sp.style.transitionDelay = `${i * 50}ms`;
        label.appendChild(sp);
    }
}

labels.forEach(label => {
    addSpanElements(label);
});