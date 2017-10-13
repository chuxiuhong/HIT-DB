from Memory import Memory
import unittest


class Test_memory(unittest.TestCase):
    def setUp(self):
        # init class instance
        self.m = Memory(10, 12, 10)

    def test_write_ram(self):
        # test write ram
        self.m.set(0, [i for i in range(5)])
        self.assertEquals(self.m[0], [i for i in range(5)])
    def test_ram2disk(self):
        self.m.set(0, [i for i in range(5)])
        self.m.store(0,5)
        with open("disk/5.ziqi","r") as f:
            self.assertEquals(f.read(),"0 1 2 3 4")
if __name__ == "__main__":
    unittest.main()