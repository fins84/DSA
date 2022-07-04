import linkedLists as List

class testLinkList:
    def linkListTest():
        try:
            linked = List.DSALinkedList()
        except Exception as e:
            print(e)

        for i in range(0, 5):
            try:
                linked.insertFirst(i)
            except Exception as e:
                print(e)

        try:
            assert (linked.peekFirst() == 4), "peek first not working"
        except Exception as e:
            print(e)

        try:
            assert (linked.peekLast() == 0), "peek last not working"
        except Exception as e:
            print(e)

        
        for i in range(4, -1, -1):
            try:
                assert (linked.removeFirst() == i), "remove first not working properly"
            except Exception as e:
                print(e)

        try:
            assert (linked.isEmpty() == True), "Linked list should be empty"
        except Exception as e:
            print(e)

        for i in range(0, 5):
            try:
                linked.insertLast(i)
            except Exception as e:
                print(e)

        try:
            assert (linked.peekFirst() == 0), "peek first not working"
        except Exception as e:
            print(e)

        try:
            assert (linked.peekLast() == 4), "peek last not working"
        except Exception as e:
            print(e)

        for i in range(0, 5, 1):
            try:
                assert (linked.removeFirst() == i), "remove first not working properly"
            except Exception as e:
                print(e)

        try:
            assert (linked.isEmpty() == True), "Linked list should be empty"
        except Exception as e:
            print(e)
    