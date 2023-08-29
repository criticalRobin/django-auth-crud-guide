const panels = document.querySelectorAll('.panel');
const activePanels = document.querySelectorAll('.panel.active');
const activePanelsArray = Array.from(activePanels);

panels.forEach(panel => {
    panel.addEventListener('click', () => {
        if (!panel.classList.contains("active")) {
            activePanelsArray.push(panel);
            panel.classList.add("active");
            activePanelsArray[0].classList.remove("active");
            activePanelsArray.shift();
        }
    });
});