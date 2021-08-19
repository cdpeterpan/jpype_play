#! python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# https://mp.csdn.net/mp_blog/creation/editor/119800888
import sys
import os
HOME_PATH = os.environ['HOME']
sys.path.append(HOME_PATH + '/.local/lib/python3.8/site-packages')

from jpype import *

DIR = os.path.dirname(os.path.abspath('.'))
IMG_PATH = HOME_PATH + '/Docs/sikulixdemo'

startJVM(r'/usr/lib/jvm/java-11-openjdk-amd64/lib/server/libjvm.so', '-ea', r'-Djava.class.path=/home/pan/Docs/doc_backup/dev_tools/SikuliX/sikulixapi-2.0.5-lux.jar')
java.lang.System.out.println("hello world")
Screen = JClass("org.sikuli.script.Screen")
screen = Screen()
screen.click(IMG_PATH + '/2021-08-19 11-34-12screenshut.png')
screen.click(IMG_PATH + '/2021-08-19 13-29-24list.png')
shutdownJVM()

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

