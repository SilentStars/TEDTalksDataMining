There are several steps to guide you to execute this project:

1.use the pycharm or the  command line to open the folder. I recommed to use pycharm beacause it is more convient to add some models and packages

2.open polls/background/video_recommendation.py, and then modify the line13,
movies = pd.io.parsers.read_csv('your location/ted_main.csv')
the ted_main.csv is in the folder of polls/background/
(I wanna use the relivate path , but there will be some errors in html, and I will fix it later)

3.use this command 
python manage.py runserver

4.type the follow to your web browser
localhost:8000

plus: some functions of this project and most of the static diagrams are still need to modify