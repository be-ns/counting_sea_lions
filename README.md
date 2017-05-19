## Counting Sea Lions
### Analyzing NOAA aerial images to get more accurate counts for Sea Lion populations in Alaska
----

Steller sea lions populations in the western Aleutian Islands have declined 94 percent in the last 30 years, making them an  endangered species, at least for the population found in the North Pacific. The data used in this analysis was obtained from unoccupied aircraft systems, and downloaded from [this](https://www.kaggle.com/c/noaa-fisheries-steller-sea-lion-population-count) Kaggle Competition. The desired result would be to subdivide the population and get accurate adult male and female populations as well as juveniles and pups.

"Currently, it takes biologists up to four months to count sea lions from the thousands of images NOAA Fisheries collects each year. Once individual counts are conducted, the tallies must be reconciled to confirm their reliability. The results of these counts are time-sensitive." - From Kaggle

#### This is an example of the images we are using.
 * The Sea Lion population is relatively difficult to pick out by hand - making this a prime job for Machine Learning.
 s
![image example](https://kaggle2.blob.core.windows.net/competitions/kaggle/6116/media/example_noaa_image.jpg)
____
#### Method
* build a convolutional neural network using Keras and Theano on preprocessed images to get accurate counts for each category.
