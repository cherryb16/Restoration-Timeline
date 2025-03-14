// Fetch and display the timeline
fetch("./timeline.json")
    .then(response => {
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        return response.json();
    })
    .then(data => {
        console.log("Timeline data loaded:", data);

        const timelineContainer = document.getElementById("timeline");
        if (!timelineContainer) {
            console.error("Error: timeline container not found!");
            return;
        }

        timelineContainer.innerHTML = ""; // Clear previous content

        data.forEach(event => {
            console.log(`Adding event: ${event.event}`);
            console.log(`Image path: ${event.image}`);

            const eventDiv = document.createElement("div");
            eventDiv.classList.add("event");

            eventDiv.innerHTML = `
                <h3>${event.date}: ${event.event}</h3>
                <img src="${event.image}" alt="${event.event}" onerror="this.style.display='none'">
                <p class="event-description">${event.description}</p>
                <div class="event-links">
                    ${Object.entries(event.links).map(([key, link]) => 
                        `<a href="${link}" target="_blank">${key}</a>`).join(" | ")}
                </div>
            `;

            eventDiv.addEventListener("mouseenter", () => {
                eventDiv.querySelector(".event-links").style.display = "block";
            });

            eventDiv.addEventListener("mouseleave", () => {
                eventDiv.querySelector(".event-links").style.display = "none";
            });

            timelineContainer.appendChild(eventDiv);
        });
    })
    .catch(error => console.error("Error loading timeline:", error));