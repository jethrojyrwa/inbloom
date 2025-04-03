import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import string

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_event_dataset(num_participants=250):
    # Lists for data generation
    events = ['Dance', 'Music', 'Drama', 'Art Exhibition', 'Poetry', 
              'Stand-up Comedy', 'Fashion Show', 'Film Screening', 'Debate', 'Cooking Competition']
    
    genders = ['Male', 'Female', 'Other']
    satisfaction_levels = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
    
    # Create start date and generate 5 consecutive dates
    start_date = datetime(2024, 11, 1)
    event_dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(5)]
    
    # Generate unique participant IDs
    participant_ids = [f"P{str(i+1).zfill(3)}" for i in range(num_participants)]
    
    # Generate more first and last names to ensure we have enough for 250 unique combinations
    first_names = [
        "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", 
        "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
        "Christopher", "Lisa", "Daniel", "Nancy", "Matthew", "Betty", "Anthony", "Sandra", "Mark", "Emily",
        "Donald", "Ashley", "Steven", "Margaret", "Paul", "Kimberly", "Andrew", "Amanda", "Joshua", "Michelle",
        "Kenneth", "Dorothy", "Kevin", "Melissa", "Brian", "Donna", "George", "Carol", "Edward", "Samantha",
        "Ronald", "Christine", "Timothy", "Janet", "Jason", "Catherine", "Jeffrey", "Frances", "Ryan", "Ann",
        "Jacob", "Joyce", "Gary", "Alice", "Nicholas", "Heather", "Eric", "Emma", "Jonathan", "Maria",
        "Stephen", "Alexandra", "Larry", "Sophia", "Justin", "Olivia", "Scott", "Isabella", "Brandon", "Rebecca",
        "Benjamin", "Laura", "Samuel", "Jacqueline", "Gregory", "Taylor", "Alexander", "Victoria", "Frank", "Zoe",
        "Patrick", "Natalie", "Raymond", "Nicole", "Jack", "Charlotte", "Dennis", "Grace", "Jerry", "Amelia",
        "Tyler", "Evelyn", "Aaron", "Hannah", "Jose", "Madison", "Adam", "Abigail", "Henry", "Gabriella",
        "Douglas", "Lily", "Nathan", "Claire", "Peter", "Julia", "Zachary", "Lillian", "Kyle", "Addison",
        "Ethan", "Alexis", "Walter", "Kayla", "Noah", "Savannah", "Jeremy", "Audrey", "Christian", "Allison",
        "Keith", "Leah", "Roger", "Chloe", "Terry", "Mackenzie", "Gerald", "Isabelle", "Harold", "Arianna",
        "Sean", "Faith", "Austin", "Makayla", "Carl", "Reagan", "Arthur", "Madeline", "Lawrence", "Gianna",
        "Dylan", "Anna", "Jesse", "Aaliyah", "Jordan", "Maya", "Bryan", "Lauren", "Billy", "Kaitlyn",
        "Joe", "Madelyn", "Bruce", "Katie", "Gabriel", "Naomi", "Logan", "Lucy", "Albert", "Cassandra",
        "Willie", "Kaylee", "Alan", "Hailey", "Juan", "Alexa", "Wayne", "Alyssa", "Elijah", "Sierra",
        "Randy", "Ellie", "Roy", "Peyton", "Vincent", "Nora", "Ralph", "Molly", "Eugene", "Stella",
        "Russell", "Kylee", "Bobby", "Autumn", "Mason", "Sophie", "Philip", "Elena", "Louis", "Eva",
        "Liam", "Ruby", "Blake", "Kennedy", "Malik", "Jasmine", "Omar", "Quinn", "Aiden", "Brooklyn",
        "Oliver", "Luna", "Carter", "Hazel", "Sebastian", "Aurora", "Wyatt", "Violet", "Gabriel", "Nova",
        "Julian", "Scarlett", "Leo", "Audrey", "Levi", "Bella", "Isaac", "Claire", "Mateo", "Skylar",
        "Samuel", "Paisley", "Lincoln", "Savannah", "Caleb", "Isla", "Owen", "Genesis", "Hudson", "Naomi",
        "Jethro","Eileen","Kusuma","Tushar","BoBo","Elza","Dave","Donkin","Iba","Morningstar"
    ]
    print(len(first_names))

        
    colleges = [
        "Harvard University", "Stanford University", "MIT", "Princeton University",
        "Yale University", "Columbia University", "University of Chicago",
        "California Institute of Technology", "University of Pennsylvania",
        "Oxford University", "Cambridge University", "University of Michigan",
        "University of California, Berkeley", "University of California, Los Angeles",
        "New York University", "Duke University", "University of Southern California",
        "Northwestern University", "Cornell University", "Brown University",
        "University of Texas at Austin", "University of Washington",
        "Carnegie Mellon University", "Georgia Institute of Technology",
        "University of Illinois Urbana-Champaign", "University of Toronto",
        "University of British Columbia", "University of Sydney",
        "National University of Singapore", "Indian Institute of Technology Bombay",
        "Indian Institute of Technology Delhi", "Indian Institute of Science",
        "University of Melbourne", "Peking University", "Tsinghua University",
        "Fudan University", "London School of Economics", "King's College London",
        "Imperial College London", "University College London", "Rice University",
        "Vanderbilt University", "University of Notre Dame", "Boston University",
        "University of California, San Diego", "University of Florida",
        "University of Wisconsin-Madison", "University of North Carolina at Chapel Hill",
        "University of Maryland", "Purdue University", "Pennsylvania State University",
        "Ohio State University", "University of Minnesota", "University of Arizona"
    ]

    # Generate a list of 250 colleges with repetition
    college_list = [random.choice(colleges) for _ in range(250)]
    
    # Generate feedback templates for each event type
    feedback_templates = {
        'Dance': [
            "The choreography was {adj1}. Overall, the dancers showed {adj2} skill.",
            "I found the dance performance to be {adj1} and {adj2}.",
            "The rhythm and movement were {adj1}. The technical execution was {adj2}.",
            "The dancers demonstrated {adj1} coordination. The performance was {adj2}.",
            "The dance ensemble was {adj1} synchronized. The stage presence was {adj2}."
        ],
        'Music': [
            "The musical arrangement was {adj1}. The vocalists were {adj2}.",
            "The band's performance was {adj1} and the acoustics were {adj2}.",
            "The melody was {adj1}. The instrumental solos were {adj2}.",
            "The harmony between instruments was {adj1}. The overall sound quality was {adj2}.",
            "The rhythm section was {adj1}. The vocal performances were {adj2}."
        ],
        'Drama': [
            "The acting was {adj1}. The storyline was {adj2}.",
            "The dramatic tension was {adj1}. The character development was {adj2}.",
            "The dialogues were {adj1}. The plot progression was {adj2}.",
            "The emotional depth of the performance was {adj1}. The staging was {adj2}.",
            "The cast chemistry was {adj1}. The narrative structure was {adj2}."
        ],
        'Art Exhibition': [
            "The artwork displayed was {adj1}. The curation was {adj2}.",
            "The visual impact of the exhibition was {adj1}. The thematic coherence was {adj2}.",
            "The artistic technique was {adj1}. The gallery layout was {adj2}.",
            "The color schemes were {adj1}. The interpretive descriptions were {adj2}.",
            "The conceptual depth was {adj1}. The presentation was {adj2}."
        ],
        'Poetry': [
            "The poetic imagery was {adj1}. The recitation was {adj2}.",
            "The rhythmic flow was {adj1}. The emotional delivery was {adj2}.",
            "The metaphorical content was {adj1}. The poets' presence was {adj2}.",
            "The verse structure was {adj1}. The thematic exploration was {adj2}.",
            "The wordplay was {adj1}. The overall performance was {adj2}."
        ],
        'Stand-up Comedy': [
            "The jokes were {adj1}. The comedian's timing was {adj2}.",
            "The humor was {adj1}. The audience engagement was {adj2}.",
            "The comedic delivery was {adj1}. The material was {adj2}.",
            "The punchlines were {adj1}. The stage presence was {adj2}.",
            "The comic narrative was {adj1}. The improvisation was {adj2}."
        ],
        'Fashion Show': [
            "The clothing designs were {adj1}. The runway presentation was {adj2}.",
            "The fashion collection was {adj1}. The models' walks were {adj2}.",
            "The styling was {adj1}. The thematic coherence was {adj2}.",
            "The fabric choices were {adj1}. The overall aesthetic was {adj2}.",
            "The fashion innovation was {adj1}. The show production was {adj2}."
        ],
        'Film Screening': [
            "The cinematography was {adj1}. The narrative pacing was {adj2}.",
            "The acting performances were {adj1}. The storyline was {adj2}.",
            "The visual effects were {adj1}. The sound design was {adj2}.",
            "The directorial approach was {adj1}. The character development was {adj2}.",
            "The screenplay was {adj1}. The emotional impact was {adj2}."
        ],
        'Debate': [
            "The arguments presented were {adj1}. The rebuttals were {adj2}.",
            "The logical structure was {adj1}. The rhetorical skill was {adj2}.",
            "The evidence provided was {adj1}. The speakers' delivery was {adj2}.",
            "The topic exploration was {adj1}. The counterpoints were {adj2}.",
            "The debating technique was {adj1}. The overall engagement was {adj2}."
        ],
        'Cooking Competition': [
            "The dish presentation was {adj1}. The flavor combinations were {adj2}.",
            "The culinary creativity was {adj1}. The technical skill was {adj2}.",
            "The ingredient usage was {adj1}. The time management was {adj2}.",
            "The plating aesthetics were {adj1}. The taste profile was {adj2}.",
            "The cooking technique was {adj1}. The overall execution was {adj2}."
        ]
    }
    
    # Create adjective lists for feedback generation
    positive_adj = [
        "excellent", "outstanding", "remarkable", "impressive", "exceptional", 
        "superb", "brilliant", "extraordinary", "magnificent", "splendid",
        "phenomenal", "masterful", "stellar", "first-rate", "top-notch",
        "wonderful", "fantastic", "marvelous", "incredible", "amazing"
    ]
    
    neutral_adj = [
        "decent", "adequate", "fair", "satisfactory", "reasonable",
        "acceptable", "standard", "average", "ordinary", "typical",
        "sufficient", "moderate", "passable", "tolerable", "mediocre"
    ]
    
    negative_adj = [
        "disappointing", "lackluster", "underwhelming", "subpar", "unsatisfactory",
        "poor", "weak", "flawed", "deficient", "inadequate",
        "unimpressive", "mediocre", "uninspired", "forgettable", "bland"
    ]
    
    # Create suggestion templates
    suggestion_templates = [
        "Consider improving the {aspect} to enhance the overall experience.",
        "The {aspect} could benefit from some refinement.",
        "I would suggest focusing more on the {aspect} next time.",
        "Perhaps more attention to {aspect} would make it better.",
        "Better {aspect} would significantly improve the event.",
        "Work on the {aspect} to make it more engaging.",
        "Enhancing the {aspect} would make a big difference.",
        "The {aspect} needs some improvement for future events.",
        "I recommend reviewing and upgrading the {aspect}.",
        "Please look into improving the {aspect} for better audience experience."
    ]
    
    event_aspects = {
        'Dance': ["choreography", "synchronization", "music selection", "costume design", "stage utilization"],
        'Music': ["sound quality", "song selection", "instrumental balance", "audience interaction", "acoustics"],
        'Drama': ["script writing", "character development", "stage design", "lighting", "pacing"],
        'Art Exhibition': ["lighting", "artwork arrangement", "descriptive labels", "thematic cohesion", "spatial layout"],
        'Poetry': ["acoustics", "selection diversity", "performance timing", "audience engagement", "venue atmosphere"],
        'Stand-up Comedy': ["joke variety", "audience interaction", "timing", "material freshness", "stage presence"],
        'Fashion Show': ["runway lighting", "music selection", "transition timing", "model coordination", "collection cohesion"],
        'Film Screening': ["seating arrangement", "sound system", "screen quality", "pre-show information", "venue comfort"],
        'Debate': ["time management", "topic selection", "moderator preparation", "audience Q&A", "technical setup"],
        'Cooking Competition': ["equipment availability", "ingredient quality", "judging criteria", "time allocation", "audience viewing angles"]
    }


    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
        "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
        "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
        "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
        "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]

    # Generate a list of 250 states with repetition
    state_list = [random.choice(states) for _ in range(250)]


    
    # Generate data for each participant
    data = []
    for i in range(num_participants):
        participant_id = participant_ids[i]
        name = first_names[i]
        age = random.randint(18, 65)
        gender = random.choices(genders, weights=[0.48, 0.48, 0.04])[0]
        event_name = random.choice(events)
        event_date = random.choice(event_dates)
        event_rating = random.randint(1, 10)
        cl = random.choice(colleges)
        sta = random.choice(states)

        # Generate satisfaction level based on rating
        if event_rating >= 9:
            satisfaction = 'Very Satisfied'
            adj_list = positive_adj
        elif event_rating >= 7:
            satisfaction = 'Satisfied'
            adj_list = positive_adj + neutral_adj
        elif event_rating >= 5:
            satisfaction = 'Neutral'
            adj_list = neutral_adj
        elif event_rating >= 3:
            satisfaction = 'Dissatisfied'
            adj_list = neutral_adj + negative_adj
        else:
            satisfaction = 'Very Dissatisfied'
            adj_list = negative_adj
        
        # Generate feedback
        template = random.choice(feedback_templates[event_name])
        feedback = template.format(
            adj1=random.choice(adj_list),
            adj2=random.choice(adj_list)
        )
        
        # Add some personalization to make feedbacks unique
        additional_comments = [
            f"I {random.choice(['really enjoyed', 'appreciated', 'liked', 'valued'])} the {random.choice(['atmosphere', 'experience', 'event', 'occasion'])}.",
            f"It was my {random.choice(['first', 'second', 'third'])} time attending such an event.",
            f"I would {random.choice(['definitely', 'probably', 'possibly'])} recommend this to friends.",
            f"The venue was {random.choice(['perfect for', 'appropriate for', 'well-suited to'])} this type of event.",
            f"Looking forward to {random.choice(['similar events', 'the next edition', 'future performances'])}.",
            "",  # Empty string for cases where no additional comment is added
        ]
        
        # Add additional comment with 70% probability
        if random.random() < 0.7:
            feedback += " " + random.choice(additional_comments)
        
        # Generate suggestions (or leave empty)
        if event_rating <= 7 and random.random() < 0.8:  # 80% chance for suggestions if rating <= 7
            aspect = random.choice(event_aspects[event_name])
            suggestion = random.choice(suggestion_templates).format(aspect=aspect)
        else:
            suggestion = ""
            if event_rating > 7 and random.random() < 0.3:  # 30% chance for positive suggestions if rating > 7
                aspect = random.choice(event_aspects[event_name])
                suggestion = f"While excellent overall, small improvements in {aspect} could make it perfect."
        
        data.append({
            'Participant_ID': participant_id,
            'Name': name,
            'Age': age,
            'Gender': gender,
            'State':sta,
            'College':cl,
            'Event_Name': event_name,
            'Event_Date': event_date,
            'Feedback_Text': feedback,
            'Satisfaction_Level': satisfaction,
        
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    return df

# Generate the dataset with 250 participants
event_dataset = generate_event_dataset(250)

# Show the first few rows
print(event_dataset.head())

# Save to CSV
event_dataset.to_csv('D:\\MCA\\3rd Trimester\\Advanced Python Programming\\2447122_ETE3\\event_feedback_dataset.csv', index=False)
