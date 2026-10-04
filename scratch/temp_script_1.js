// Random viewer count logic (sometimes over 1000)
    document.addEventListener("DOMContentLoaded", function() {
        const countEl = document.getElementById("liveViewerCount");
        if(countEl) {
            const isHigh = Math.random() > 0.7; // 30% chance to be over 1000
            const count = isHigh ? Math.floor(Math.random() * 500) + 1000 : Math.floor(Math.random() * 800) + 100;
            countEl.innerText = count.toLocaleString() + " Exporters currently active and ready to quote";
        }
    });