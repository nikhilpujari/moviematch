**Database Management Systems Project Specification - Project Part IV End-to-End Solution Integration and Data-Driven / Database Programming**

**NYU Database Systems Final Project - CSCI-GA-2433**

**Title: “Media and Entertainment: Cinema DB”**
**


` `**1. Ongoing Project Background**

The project centers around a movie recommendation system, tailoring suggestions based on a user's preferences. These recommendations are influenced not only by the individual user's choices but also by the collective voting patterns of other users who share similar movie interests.

This system incorporates of data analysis and machine learning to recommend movies based on user's likings.

**2. Technology used**

The project's GUI is constructed employing a blend of HTML, CSS, and JavaScript for the user interface. PHP serves as the intermediary API, integrating the output from Python scripts and aggregating data from both CSV files and the database.

Our infrastructure leverages Google Cloud (GCloud) services, utilizing it not only for database storage but also to curate a Data Lake, housing both structured and unstructured data. Python acts as the principal tool for machine learning algorithms and comprehensive data analysis.

For seamless user interaction, we've implemented asynchronous behavior using AJAX, ensuring prompt display of responses post-user interaction, specifically during movie voting processes. This architecture aims to create a responsive, dynamic, and user-centric environment.


**4. Project Interface**

![Fig. 1: Homepage](images/ss/fig1.png?raw=true "Homepage")
Fig. 1: Homepage


![Fig. 2: Movie list](images/ss/fig1.png?raw=true "Movie list")
Fig. 2: Movie list

This catalog comprises movies sourced from a Kaggle dataset, delivered in JSON format via AJAX requests. Each movie entry includes a URL field housing the movie poster; in case of a poster loading failure, a default poster is displayed. With every reload, a fresh batch of movies is fetched to enhance variety.

User engagement involves voting for each movie, expressing preferences as 'liked,' 'disliked,' or 'unwatched.' These votes are relayed to a PHP file, which securely stores the voting outcomes within our previously established database. The uniqueness of each user is ensured by utilizing session IDs for identification and data association.


![Fig. 3: Recommended Movies](images/ss/fig3.png?raw=true "Recommended Movies")
Fig. 3: Recommended Movies


The voting data residing in the database is retrieved by correlating it with the user's active session. Leveraging this data, movies with analogous genres are collected. Additionally, the system gathers comparable voting patterns from other users stored in the database. This amalgamation of the user's preferences and collective user behavior is then relayed to a Python script through the intermediary PHP script.

Subsequently, employing **collaborative filtering technique**, the Python script harnesses this consolidated dataset to generate personalized movie recommendations, offering insightful suggestions based on similar user tastes and movie genres.


![Fig 4. News](images/ss/fig4.png?raw=true "News")

Fig 4. News

![Fig 5. News original source](images/ss/fig5.png?raw=true "News original source")

Fig 5. News original source

The project's news session uses unstructured data sourced dynamically from a leading entertainment news website, [https://www.hollywoodreporter.com/c/movies/movie-news/.](https://www.hollywoodreporter.com/c/movies/movie-news/) Through the application of **web scraping** techniques, we fetch **real-time** updates, ensuring the website stays current with the latest news.

This feat is accomplished by employing the powerful **BeautifulSoup** Python library, allowing us to parse and extract pertinent information from the raw HTML structure of the targeted news website. This dynamic integration keeps our platform enriched with up-to-the-minute entertainment updates for users to explore.


![Fig 6. Sentiment Analysis](images/ss/fig6.png?raw=true "Sentiment Analysis")

Fig 6. Sentiment Analysis

![Fig 7. Unstructured Review Polarity Data](images/ss/fig7.png?raw=true "Unstructured Review Polarity Data")

Fig 7. Unstructured Review Polarity Data





The website performs data analysis capabilities on unstructured data hosted within the Google Data Lake. This unstructured data repository contains both positive and negative reviews. The python code utilizes TF-IDF to create feature vectors, performs a train-test split, trains a Logistic Regression model, predicts sentiments on the test set, and evaluates model performance through accuracy metrics and a confusion matrix visual using Seaborn and Matplotlib libraries in Python.


![Fig 8. Website Footer](images/ss/fig8.png?raw=true "Website Footer")

Fig 8. Website Footer

**Thank You**

