# A python script that helps to learn japanese

It uses the pykakasi library for converting the words to other writings. The kanjiapi API grabs and returns the data about each kanji in json format.
![Screenshot 2022-04-14 at 01 31 26](https://user-images.githubusercontent.com/36286098/163291183-1dc50f07-f593-4c7b-b2fb-d8921391ed0d.png)

## Improvement ideas

* Filter out the kanji duplicates
* kanjiapi returns the data only for one kanji. Pykakasi separates the words, which can consist of more kanjis and there should be also information about them.
* make it more readable
* save to a file or enable options to dump it somewhere
* read from input/file
* read from speech
* make the text dynamic, with something like https://mediastack.com/sources/japan-news-api
