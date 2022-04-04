import Model_EC2
import serverThreadHandler

def main():
    obj = Model_EC2.EC2_Model()
    obj.StartOne("CPUUtilization")
    obj.StartOne("DiskReadOps")
    s1 = serverThreadHandler.threadHandler(7000)
    s2 = serverThreadHandler.threadHandler(7070)
    s1.start()
    s2.start()

    # obj.StartAll()


if __name__ == "__main__":
    main()
