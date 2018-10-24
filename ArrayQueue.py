#!/usr/bin/python3
import pprint

class ArrayQueue:
    def __init__(self):
        self.list = []

        #
        # print("NODE:")
        # print(self.list)

        # for node in self.list.getNodes():
        #     print("NODE: ")
        #     print(node)


    # def point_sorting(self, point):
		# print('X value: ', point.x())
		# return point.x()


    def is_empty(self):
        return False
        #If the size of the array is not zero
        #retun false : True
    def dumper(self):
        print("Content2: ", self.list)

    def insert(self, node):
        self.list.append(node)
        print("WHAT??: ", self.list)
