# allai.space

###### A space for allies, a space for all
#### DubHacks Hack '20 Identity Track Winner

#### By: [Aayushi](https://www.linkedin.com/in/aayushimodi/), [Amartya](https://www.linkedin.com/in/amartyaranganathan/), [Riya](https://www.linkedin.com/in/riyabaheti/), [Darsh](https://www.linkedin.com/in/desaidarsh/)

## Inspiration
In an age of technology and a pandemic, virtual communication is extremely important. We rely on technology to convey our words to others, and oftentimes, it is very easy to misuse them, completely unintentionally. However, using inclusive language is a very powerful way to make a change towards better diversity and inclusion in any space, especially in professional settings. Allai is a tool to enable this, providing suggestions for inclusive language in your own writing.

## What it does
Allai.Space targets inclusive language through three main pillars: vocabulary, sentiment, and syntax. For vocabulary, it examines common biases in language towards race, gender, and ability. The platform will directly replace key terms in typed or pasted text and produce it in a read-only output pane. Regarding sentiment, the web application utilizes the Google Cloud Natural Language program to examine overall sentiment of the passage and color the output pane accordingly. Using emotionally aware language is important for being inclusive not only in the interest of being positive, but also to avoid accidental offense. The final facet, syntax, also utilizes Google Cloud Natural Language. It identifies "entities", specifically people, and tracks any adjectives dependent on them. Based on the sentiment score of the adjective and the entity sentiment score of the person being described, suggestions will be generated in a passive, people-first format (i.e. disabled man will suggest modification to man with disability). Suggestions were generated using the Python Natural Language Toolkit library's Wordnet function.

## How we built it
The frontend was built using HTML/CSS and Javascript. We started by creating just the user interface and connecting input and output text areas. Then, we moved to using Flask to pass data between backend Python files and frontend Javascript. We collected and returned user input as a string, allowing to easily populate it in HTML rendering.

The backend was created using Python combined with Google Cloud's Natural Language API. For vocabulary replacement, we made a dictionary containing harmful terms and their inclusive counterpart. Whenever a harmful word is found in the text, the program replaces it with its counterpart and spits out the new text with the inclusive terms put in. For sentiment analysis, we used the sentiment functionality of Google Cloud Natural Language and CSS styling on the front-end. Finally, for syntax, we used the entity, sentiment, and syntax functionalities to identify and execute necessary suggestions. Using the entity functionality of Google Cloud, we focused only on nouns describing a person (man, user, resident, etc.). After that, we only made suggestions if the adjectives dependent on the entity were negative or created a negative entity sentiment.

## Challenges we ran into
Some challenges we ran into were connecting our frontend and backend programs. When editing the user input text, we tried sending the input to a text file using JavaScript and modifying it. However, we soon realized that JavaScript does not support writing to and from text files from the client-side due to safety reasons. We then changed our approach using Flask to connect our JavaScript and Python classes. We sent the user input as a string from JavaScript to our Python classes and ended up making all our text modifications with Python. Flask allowed us to both POST and GET allowing our web page to run a complete backend to frontend loop every time we submitted input text on our website. We also initially struggled with authentication in Google Cloud, so we started with an individual functionality and walkthrough before exploring other features. We also ran into issues with differentiating punctuation from words such as commas and periods when analyzing words. To split punctuation from the words without adding spaces, we wrote a regular expression that split punctuation from the end of words as its own element.

Additionally, while we liked the domain we purchased from Domain.com (allai.space), we were unfortunately unable to connect with our local Flask host. We hope to do that as we try to launch the platform.

## Accomplishments that we're proud of
We are incredibly proud of our ability to implement almost every facet of the Google Cloud Natural Language API available. Additionally, we made an effort to delegate front-end and back-end tasks in what was largely our first college hackathon experience. As a result, we were able to integrate the two to prioritize both form and function. We learned many new technologies from basic collaboration in Git to natural language processing to web development in Flask. We were familiar with the underlying languages, but these frameworks and APIs helped us develop a full-fledged product.

## What we learned
- Google Cloud Natural Language Processing APIs
- Processing data and files in Python
- Using Flask to connect and pass data between backend Python files and frontend JavaScript/HTML/CSS
- JavaScript/CSS/HTML to develop a clean, organized, and functional webpage
- Collaborating through Git

## What's next for Allai.Space
In the future, we plan to augment the features of Allai.space. A few of the possibilities include denoting the sentiment for each sentence rather than the entire paragraph, allowing users to more easily pull out negative sentences, as well as inline suggestions instead of in a separate box below. We are going to host our web page on the domain allai.space and also hope to create a Chrome extension, allowing Allai’s functionalities to apply to any text field on the browser.
