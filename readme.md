# Recommender System Project with Anime

![Anime-Recommender-Thumbnail](static/thumbnail.png)

This repository contains the implementation of various recommender system algorithms on Anime Dataset.

Currently contains:

1. Non-Personal Recommendations
2. Item-Item Nearest Neighbor Collaborative Filtering
3. Content-Based Recommendations

Download the Dataset from [here](https://www.kaggle.com/CooperUnion/anime-recommendations-database)


### Non-Personal Recommendations

Providing non-personal recommendations was not a very difficult task. The rating of the movie was simply weighted based on the popularity of the anime. This can be done by simply multiplying the rating of a particular anime with the number of members that have watched the anime


### Item-Item Nearest Neighbor Collaborative Filtering

A pivot table was created with anime_id as columns and user_id as rows and the ratings of the given by the user to a anime as the pivot table values. Due to this, a large sparse matrix with a lot of null values were created. Then, anime that are similar to each other are found with the help of a similarity metric such as correlation coefficient. Once a user has higly rated an Anime, a similar anime will be recommended to them with this mechanism


### Content-Based Recommendations

Content Based Recommendations does not usually depend on the ratings. It's where we use the dedscription of the item to group similar items and recommend them. This can be done by creating a bag of words representation of the feature that we are going to use to group the items. In this case, It is the Genre. Then, we again find the similarity using genre matches and then recommend a similar movie.