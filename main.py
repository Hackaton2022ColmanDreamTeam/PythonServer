import Model_EC2


def main():
    obj = Model_EC2.EC2_Model()
    obj.StartOne("CPUUtilization")
    obj.StartOne("DiskReadOps")


if __name__ == "__main__":
    main()
