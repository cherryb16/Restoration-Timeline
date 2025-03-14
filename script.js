// Fetch and display the timeline
fetch("timeline.json")
    .then(response => response.json())
    .then(data => {
        const timelineContainer = document.getElementById("timeline");
        data.forEach(event => {
            const eventDiv = document.createElement("div");
            eventDiv.classList.add("event");

            eventDiv.innerHTML = `
                <h3>${event.date}: ${event.event}</h3>
                <p>${event.description}</p>
                ${Object.entries(event.links).map(([key, link]) => 
                    `<a href="${link}" target="_blank">${key}</a>`).join(" | ")}
            `;

            timelineContainer.appendChild(eventDiv);
        });
    })
    .catch(error => console.error("Error loading timeline:", error));