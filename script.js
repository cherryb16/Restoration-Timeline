const timelineContainer = document.getElementById("timeline-events");
const eventDetails = document.getElementById("event-details");
const eventTitle = document.getElementById("event-title");
const eventDescription = document.getElementById("event-description");
const eventLinks = document.getElementById("event-links");

// Fetch and populate timeline with images
fetch("timeline.json")
    .then(response => response.json())
    .then(data => {
        populateTimeline(data);
    })
    .catch(error => console.error("Error loading timeline data:", error));

function populateTimeline(timelineEvents) {
    timelineContainer.innerHTML = ""; // Clear existing content
    timelineContainer.classList.add("horizontal-timeline"); // Add class for styling

    const timelineLine = document.createElement("div");
    timelineLine.classList.add("timeline-line"); // This will be styled as the actual timeline
    timelineContainer.appendChild(timelineLine);

    timelineEvents.forEach((event, index) => {
        const eventDiv = document.createElement("div");
        eventDiv.classList.add("event");

        const eventMarker = document.createElement("div");
        eventMarker.classList.add("event-marker");

        const eventImage = document.createElement("img");
        eventImage.src = event.image;
        eventImage.alt = event.event;
        eventImage.dataset.index = index;

        eventImage.addEventListener("click", function () {
            showEventDetails(event);
        });

        eventDiv.appendChild(eventMarker);
        eventDiv.appendChild(eventImage);
        timelineContainer.appendChild(eventDiv);
    });
}

function showEventDetails(event) {
    document.getElementById("event-date").textContent = event.date; // Ensure date is displayed
    document.getElementById("event-title").textContent = event.event;
    document.getElementById("event-description").textContent = event.description;

    const eventLinks = document.getElementById("event-links");
    eventLinks.innerHTML = ""; // Clear previous links

    if (event.links) {
        for (const [text, url] of Object.entries(event.links)) {
            const link = document.createElement("a");
            link.href = url;
            link.textContent = text;
            link.target = "_blank";
            eventLinks.appendChild(link);
        }
    } else {
        eventLinks.innerHTML = "<p>No additional links available.</p>";
    }

    document.getElementById("event-details").style.display = "block"; // Show details section
}

document.addEventListener("DOMContentLoaded", function () {
    const timelineContainer = document.getElementById("timeline-events");

    if (timelineContainer) {
        // Wait for all images to load before setting scroll position
        window.onload = function () {
            timelineContainer.scrollLeft = 0;
        };
    }
});