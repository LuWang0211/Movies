# Movies

# IMDb, the Internet Movie Database

https://www.imdb.com/interfaces/

name.basics.tsv.gz
title.akas.tsv.gz
title.basics.tsv.gz
title.crew.tsv.gz
title.episode.tsv.gz
title.principals.tsv.gz
title.ratings.tsv.gz
total 3.0GB

# Data cleaning

Docker, Spark, GCP-BigQuery, AWS - reduce data size to new files
Data after reduction: 1.6GB

# Exploratory data analysis

Q: How is the film rating changing?

https://github.com/zishuijingw/Movies/tree/master/img_folder/rating_over_year.png

With the development of the film industry, the number of movies has increased rapidly, and the number of corresponding comments has also increased. In the yearly film rating, the film score gap is also widening. However, the mean of the film scores did not change significantly.

Q: How actors/actresses influence movie ratings?

  1. Focus on lead actors/actresses
  2. Filter the dataset to get age information
https://github.com/zishuijingw/Movies/tree/master/img_folder/age_over_year.png

There is a gap between the ages of men and women, and the gap does not change over time. But both began to rise at the same time.

Q: Whether the age has an impact on movies ratings?

https://github.com/zishuijingw/Movies/tree/master/img_folder/age_mapping_rating.png

Mathematical calculation of linear correlation：
actresses['averageRating'].corr(actresses['age']) = 0.037979784708851626
actors['averageRating'].corr(actors['age']) = -0.0019829741473593085

-> there is no linear relationship between the two variables

What kind of actors/actresses combination can get a good movie rating?

# Next
1. What kind of actors/actresses combination can get a good movie rating?
2. Is there any difference between movie preferences in different regions?
3. How does movies cost affect movies quality?
4. How the participation of international elements affect movie ratings?


