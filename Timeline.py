import json

# Timeline data stored as a dictionary
timeline = [
    {
        "event": "The First Vision",
        "date": "Spring 1820",
        "description": "Joseph Smith prays to know which church is true. God the Father and Jesus Christ appear and instruct him not to join any existing churches.",
        "links": {
            "Scripture": "https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1?lang=eng",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-002-the-first-vision",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/02-ask-in-faith"
        }
    },
    {
        "event": "The Visitation of Moroni",
        "date": "September 21, 1823",
        "description": "The angel Moroni visits Joseph Smith and tells him about the gold plates.",
        "links": {
            "Scripture": "https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1?lang=eng",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-003-moroni-appears-to-joseph-smith",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/03-plates-of-gold"
        }
    },
    {
        "event": "Receiving the Gold Plates",
        "date": "September 22, 1827",
        "description": "Joseph Smith receives the gold plates from Moroni and begins translation.",
        "links": {
            "Gospel Topic": "https://www.churchofjesuschrist.org/study/manual/gospel-topics/book-of-mormon",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-004-the-work-of-god",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/04-be-watchful"
        }
    },
    {
        "event": "Translation of the Book of Mormon",
        "date": "1827–1829",
        "description": "Joseph Smith translates the Book of Mormon through divine means.",
        "links": {
            "Gospel Topic": "https://www.churchofjesuschrist.org/study/manual/gospel-topics/book-of-mormon-translation",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-006-a-book-of-mormon-story",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/05-all-is-lost"
        }
        },
    {
        "event": "Restoration of the Priesthood",
        "date": "May 15, 1829",
        "description": "John the Baptist confers the Aaronic Priesthood on Joseph Smith and Oliver Cowdery. Later, Peter, James, and John restore the Melchizedek Priesthood.",
        "links": {
            "Doctrine & Covenants 13": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/13",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-009-restoration-of-the-priesthood",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/07-fellow-servants"
        }
    },
    {
        "event": "Organization of the Church",
        "date": "April 6, 1830",
        "description": "The Church of Jesus Christ of Latter-day Saints is officially organized in Fayette, New York.",
        "links": {
            "Doctrine & Covenants 20": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/20",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-010-the-church-is-organized",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/08-rise-of-the-church"
        }
    },
    {
        "event": "Early Growth and Revelation",
        "date": "1830–1831",
        "description": "Missionary work expands, including a mission to the Lamanites. The Saints gather to Kirtland, Ohio.",
        "links": {
            "Doctrine & Covenants 37-38": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/37",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-013-gathering-to-ohio",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/09-come-to-the-ohio"
        }
    },
    {
        "event": "The Law of Consecration Revealed",
        "date": "1831",
        "description": "The Law of Consecration is revealed, commanding Saints to build Zion through stewardship and unity.",
        "links": {
            "Doctrine & Covenants 42": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/42",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/12-a-perfect-society"
        }
    },
    {
        "event": "Zion and Expulsion from Missouri",
        "date": "1831–1839",
        "description": "Independence, Missouri, is designated as Zion, but persecution forces the Saints to leave due to conflicts with local settlers.",
        "links": {
            "Doctrine & Covenants 57": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/57",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-018-persecution-in-missouri",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/17-the-eyes-of-the-people"
        }
    },
    {
        "event": "Vision of the Three Degrees of Glory",
        "date": "February 16, 1832",
        "description": "Joseph Smith and Sidney Rigdon receive a vision outlining the Celestial, Terrestrial, and Telestial Kingdoms.",
        "links": {
            "Doctrine & Covenants 76": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/76",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/15-a-vision-of-heaven"
        }
    },
    {
        "event": "The Kirtland Temple and Restoration of Priesthood Keys",
        "date": "March–April 1836",
        "description": "The Kirtland Temple is dedicated, and Christ, Moses, Elias, and Elijah appear to restore priesthood keys.",
        "links": {
            "Doctrine & Covenants 110": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/110",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-024-the-kirtland-temple-dedication",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/21-endowed-with-power"
        }
    },
    {
        "event": "The Nauvoo Period",
        "date": "1839–1844",
        "description": "Nauvoo is established, temple ordinances are revealed, and the Relief Society is organized.",
        "links": {
            "Doctrine & Covenants 124": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/124",
            "Saints Chapter": "https://www.churchofjesuschrist.org/study/history/saints-v1/29-the-temple-of-god"
        }
    },
    {
        "event": "Martyrdom of Joseph and Hyrum Smith",
        "date": "June 27, 1844",
        "description": "Joseph and Hyrum Smith are martyred at Carthage Jail.",
        "links": {
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-029-joseph-smith-prophet-of-the-restoration"
        }
    },
    {
        "event": "The Exodus to the West",
        "date": "1846–1847",
        "description": "Brigham Young leads the Saints west, and the Salt Lake Valley is settled in July 1847.",
        "links": {
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-031-the-pioneers-journey-west"
        }
    }
]

# Function to display the timeline
def display_timeline():
    for event in timeline:
        print(f"{event['date']}: {event['event']}")
        print(f"Description: {event['description']}")
        for key, link in event["links"].items():
            print(f"{key}: {link}")
        print("-" * 80)

# Function to export the timeline to JSON
def export_timeline(filename="timeline.json"):
    with open(filename, "w") as file:
        json.dump(timeline, file, indent=4)
    print(f"Timeline exported to {filename}")

if __name__ == "__main__":
    display_timeline()
    export_timeline()


