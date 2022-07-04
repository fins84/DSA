import DSAStackTest as stack
import DSAQueueTest as queue
import linkListTest as list
import DSAGraphTest as graph
import menuTest

stack.stackTest()
queue.queueTest()
lList = list.testLinkList()
lList.linkListTest()

graphTest = graph.testGraph()
graphTest.testEmpty()
graphTest.testFalseWithData()
graphTest.testRealWithData()

menu = menuTest.menuTest()
menu.testMenu()
menu.testEmptyRead()