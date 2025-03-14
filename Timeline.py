import json

# Timeline data stored as a dictionary
timeline = [
    {
        "event": "The First Vision",
        "date": "Spring 1820",
        "description": "Joseph Smith prays to know which church is true. God the Father and Jesus Christ appear and instruct him not to join any existing churches.",
        "links": {
            "Joseph Smith - History 1:15-20": "https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1?lang=eng&id=p15",
            "Video": "https://www.churchofjesuschrist.org/media/video/2014-06-0001-joseph-smiths-first-vision?lang=eng",
            "Saints Chapter 2": "https://www.churchofjesuschrist.org/study/history/saints-v1/02-hear-him"
        }
    },
    {
        "event": "The Visitation of Moroni",
        "date": "September 21, 1823",
        "description": "The angel Moroni visits Joseph Smith and tells him about the gold plates.",
        "links": {
            "Joseph Smith - History 1:30-49": "https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1?lang=eng&id=p30",
            "Video": "https://www.churchofjesuschrist.org/media/video/1ef19863776b11ef82b6063a8fac2bb3b38c66e0?lang=eng",
            "Saints Chapter 3": "https://www.churchofjesuschrist.org/study/history/saints-v1/03-plates-of-gold"
        }
    },
    {
        "event": "Receiving the Gold Plates",
        "date": "September 22, 1827",
        "description": "Joseph Smith receives the gold plates from Moroni and begins translation.",
        "links": {
            "Book or Mormon Overview": "https://www.churchofjesuschrist.org/study/manual/gospel-topics/book-of-mormon",
            "Video": "https://www.churchofjesuschrist.org/media/video/PD60007269_joseph-smith-and-the-gold-plates?lang=eng",
            "Saints Chapter 3": "https://www.churchofjesuschrist.org/study/history/saints-v1/03-plates-of-gold"
        }
    },
    {
        "event": "Translation of the Book of Mormon",
        "date": "1827-1829",
        "description": "Joseph Smith translates the Book of Mormon through divine means.",
        "links": {
            "Book of Mormon Translation Overview": "https://www.churchofjesuschrist.org/study/manual/gospel-topics-essays/book-of-mormon-translation?lang=eng",
            "Video": "https://www.churchofjesuschrist.org/media/video/2011-03-006-a-book-of-mormon-story",
            "Saints Chapter 6": "https://www.churchofjesuschrist.org/study/history/saints-v1/06-the-gift-and-power-of-god"
        }
    },
    {
        "event": "Restoration of the Priesthood",
        "date": "May 15, 1829",
        "description": "John the Baptist confers the Aaronic Priesthood on Joseph Smith and Oliver Cowdery. Later, Peter, James, and John restore the Melchizedek Priesthood.",
        "links": {
            "Doctrine & Covenants 13": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/13",
            "Video": "https://www.churchofjesuschrist.org/media/video/2010-05-1130-restoration-of-the-priesthood?lang=eng",
            "Saints Chapter 7": "https://www.churchofjesuschrist.org/study/history/saints-v1/07-fellow-servants"
        }
    },
    {
        "event": "Organization of the Church",
        "date": "April 6, 1830",
        "description": "The Church of Jesus Christ of Latter-day Saints is officially organized in Fayette, New York.",
        "links": {
            "Doctrine & Covenants 20": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/20",
            "Video": "https://www.churchofjesuschrist.org/media/video/2010-07-0022-organization-of-the-church?lang=eng",
            "Saints Chapter 8": "https://www.churchofjesuschrist.org/study/history/saints-v1/08-the-rise-of-the-church-of-christ"
        }
    },
    {
        "event": "Early Growth and Revelation",
        "date": "1830–1831",
        "description": "Missionary work expands, including a mission to the Lamanites. The Saints gather to Kirtland, Ohio.",
        "links": {
            "Doctrine & Covenants 37-38": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/37",
            "Video": "https://youtu.be/1I48maW9ScE?si=iR-XOW93eBWGLRtx",
            "Saints Chapter 9": "https://www.churchofjesuschrist.org/study/history/saints-v1/09-come-life-or-come-death"
        }
    },
    {
        "event": "The Law of Consecration Revealed",
        "date": "1831",
        "description": "The Law of Consecration is revealed, commanding Saints to build Zion through stewardship and unity.",
        "links": {
            "Doctrine & Covenants 42": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/42",
            "Video": "https://youtu.be/mydbrzSfvDw?si=8KVXjNeXVnTlyfFk",
            "Saints Chapter 11": "https://www.churchofjesuschrist.org/study/history/saints-v1/11-ye-shall-receive-my-law"
        }
    },
    {
        "event": "Zion and Expulsion from Missouri",
        "date": "1831–1839",
        "description": "Independence, Missouri, is designated as Zion, but persecution forces the Saints to leave due to conflicts with local settlers.",
        "links": {
            "Doctrine & Covenants 57": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/57",
            "Video": "https://www.churchofjesuschrist.org/media/video/31122_000_039?lang=eng&alang=eng&collectionId=5c1de78ee8f16e1e3788514dbc8f04a97b2840bc",
            "Saints Chapter 18": "https://www.churchofjesuschrist.org/study/history/saints-v1/18-the-camp-of-israel"
        }
    },
    {
        "event": "Vision of the Three Degrees of Glory",
        "date": "February 16, 1832",
        "description": "Joseph Smith and Sidney Rigdon receive a vision outlining the Celestial, Terrestrial, and Telestial Kingdoms.",
        "links": {
            "Doctrine & Covenants 76": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/76",
            "Video": "https://www.churchofjesuschrist.org/media/video/2018-03-0100-joseph-smiths-vision-of-heaven?lang=eng",
            "Saints Chapter 14": "https://www.churchofjesuschrist.org/study/history/saints-v1/14-visions-and-nightmares"
        }
    },
    {
        "event": "The Kirtland Temple and Restoration of Priesthood Keys",
        "date": "March–April 1836",
        "description": "The Kirtland Temple is dedicated, and Christ, Moses, Elias, and Elijah appear to restore priesthood keys.",
        "links": {
            "Doctrine & Covenants 110": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/110",
            "Video": "https://youtu.be/iBMl4Qgj4YQ?si=rBaiqaJVgyegjJ8F",
            "Saints Chapter 21": "https://www.churchofjesuschrist.org/study/history/saints-v1/21-the-spirit-of-god"
        }
    },
    {
        "event": "The Nauvoo Period",
        "date": "1839–1844",
        "description": "Nauvoo is established, temple ordinances are revealed, and the Relief Society is organized.",
        "links": {
            "Doctrine & Covenants 124": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/124",
            "Video": "https://www.churchofjesuschrist.org/media/video/2009-02-1038-episode-38-nauvoo-beginnings?lang=eng",
            "Saints Chapter 34": "https://www.churchofjesuschrist.org/study/history/saints-v1/34-build-up-a-city"
        }
    },
    {
        "event": "Martyrdom of Joseph and Hyrum Smith",
        "date": "June 27, 1844",
        "description": "Joseph and Hyrum Smith are martyred at Carthage Jail.",
        "links": {
            "Doctrine & Covenants 135": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/135?lang=eng#",
            "Video": "https://www.churchofjesuschrist.org/media/video/2009-02-1049-episode-49-the-martyrdom-of-joseph-and-hyrum-smith?lang=eng",
            "Saints Chapter 44": "https://www.churchofjesuschrist.org/study/history/saints-v1/44-a-lamb-to-the-slaughter"
        }
    },
    {
        "event": "The Exodus to the West",
        "date": "1846–1847",
        "description": "Brigham Young leads the Saints west, and the Salt Lake Valley is settled in July 1847.",
        "links": {
            "Doctrine and Covenants 136": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/136?lang=eng#study_intro1",
            "Video": "https://www.churchofjesuschrist.org/media/video/2009-02-1035-episode-35-the-mormon-exodus-from-missouri?lang=ase&alang=eng&collectionId=69702fe5b9d07af52d369dfd20b9c5dcf820ba78",
            "Saints Chapter 46": "https://www.churchofjesuschrist.org/study/history/saints-v1/46-endowed-with-power"
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

