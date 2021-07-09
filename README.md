# IITR-Campus-guide
IITR Campus Guide is a django-based portal for making the lives of students of IITR much easier. The campus guide includes info about the campus, notice board for keeping the students up-to-date with ongoing capus events, a lost-and-found portal, and all other necessary information pertaining to IITR. This is made as a course project under the course csn-291 (OOAD).

Feel free to look around and explore the repo. For any bug reporting, improvement or feature addition, you can open a new issue [here](https://github.com/avvarisreedhar/lost-and-found/issues/new).

## Instructions to use
* Install Python3
* Clone the repo
```
git clone https://github.com/avvarisreedhar/IITR-Campus-guide.git
```
* Install the dependencies
```
cd IITR-Campus-guide/
pip install -r requirements.txt
```
* Run the following commands
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Now, navigate to [localhost](http://127.0.0.1:8000/) to see the site up-and-running.

## License
This project is licensed under the [MIT License](https://mit-license.org/)
