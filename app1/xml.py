# from django.shortcuts import render
# from os import listdir, path
# from xml.etree import ElementTree as E
# # from xml.dom import minidom

# # parse an xml file by name
# tree = E.parse("/media/tarek/01D5D0773CD2EF00/ITI/python/labs/lab3/adminpanal/app1/xml/employee.xml")

# def xmlFunction(request):
#         # mydoc = minidom.parse('../xml/library.xml')
#         root= tree.getroot()
#         # print(root)
#         for elem in root:
#             print(elem.find('employee').get('name'))
#         # data={'root':root}
#         # items = mydoc.getElementsByTagName('employeeData')
#         # # one specific item attribute
#         # print('Item #2 attribute:')
#         # # print(items[0].attributes['name'].value)
#         # root=items[0].attributes['name'].value
#         # data={'root':root}
#         return render(request,'xml/xml.html')