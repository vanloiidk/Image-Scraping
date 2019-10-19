Python program for scraping images from pixabay.com
# Python version
Python 3.6
# Install require libraries
## Install chrome browser
```
pip3 install chromium-browser
```
## Install chrome driver
```
pip3 install chromedriver-binary==77.0.3865.40.0
```
## Install selenium
```
pip3 install -U selenium
```
## Clone program from github
```
git clone https://github.com/vanloiidk/Image-Scraping.git
```
## Check out of collection page:

In my case is:[https://pixabay.com/images/search/basketball/](https://pixabay.com/images/search/basketball/)

## Run program
```
cd Image-Scraping/src
python3.6 getImages.py
```
Then you have to enter url of collection and number of pages you want to get:
```
Enter Link:https://pixabay.com/images/search/basketball/
Enter number of pages:1
```
After selenium finish their job, check out new folder has been created and see the magic

You also can find sample caption for each image in file caption.txt
