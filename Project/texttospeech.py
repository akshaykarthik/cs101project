__author__ = 'Brannon'

import pyttsx


def initdictionary():
    dict[0] = "The bronze statue of George Mason was created by Wendy M. Ross and dedicated on April 12, 1996. " \
              " The 7 and half foot statue shows George Mason presenting his first draft of the " \
              "Virginia Declaration of Rights" \
              " which was later the basis for the U.S. constitutions Bill of Rights."

    dict[1] = "The George W. Johnson Center is a unique facility designed to encourage learning. " \
              "Its programming and use of space emphasizes integration of curricular and extracurricular " \
              "activities of the diverse " \
              "communities that comprise George Mason university ." \
              "It holds the bookstore, classrooms, the library, and many popular dining services."

    dict[2] = "Robinson A houses the English Department and Public and International Affairs Department, " \
              "the College of Education and Human Development, as well as offices and" \
              " classrooms for the College of Health and Human Services." \
              " The Writing Center and the AV Equipment/" \
              "Classroom Support Office as well as a number of classrooms are also located in this building. "

    dict[3] = "Southside boasts seven different food stations catering to all appetites in an all-you-can-eat format." \
              " Classic American fare, vegetarian dishes, international cuisine " \
              "and an endless array of desserts are sure to keep even the pickiest of customers happy."




dict = {}
initdictionary()
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)


def say(i):
    engine.say(dict[i])
    engine.runAndWait()


