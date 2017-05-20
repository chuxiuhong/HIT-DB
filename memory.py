# coding=utf8
__author__ = '楚休红'
import logging
import os


class memory():
    def __init__(self, buffer_block_num, disk_block_num, block_size, log_file_path='action.log'):
        '''
        初始化存储系统
        :param buffer_block_num:缓冲区块的数量 
        :param disk_block_num: 磁盘块数量
        :param block_size: 块大小
        '''
        self.__buffer_block_num = buffer_block_num
        self.__disk_block_num = disk_block_num
        self.__block_size = block_size
        self.__buffer_flag = [0] * buffer_block_num
        self.__disk_flag = [0] * disk_block_num
        self.io_num = 0
        self.buffer = [0] * buffer_block_num
        if 'disk' not in set(os.listdir(os.getcwd())):
            os.mkdir('disk')
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_file_path,
                            filemode='w')
        self.__newdisk__()

    def free(self, block_num):
        '''
        释放掉缓冲区的特定块
        :param block_num:块号 
        :return: None
        '''
        logging.debug('free No.%s buffer block' % block_num)
        self.__buffer_flag[block_num] = 0

    def get(self, block_num):
        '''
        获取缓冲区指定块的数据
        :param block_num: 块号
        :return: 块内数据,返回的是list型
        '''
        logging.debug('get No.%s block' % block_num)
        return map(int, self.buffer[block_num].split())

    def set(self, block_num, data):
        '''
        将指定的缓冲区块写入数据，可以是list或者tuple，或者是int
        :param block_num: 块号
        :param data: 待写入的数据，如果是多条数据，用list或tuple传进来
        :return: None
        '''
        if type(data) == list or type(data) == tuple:
            if len(data) > self.__block_size:
                raise ValueError, "Too much data for a block"
            data = ' '.join(map(str, data))
        elif type(data) != int:
            raise ValueError, "Wrong data(should be Integer)"
        self.buffer[block_num] = str(data)
        logging.debug('set No.%s buffer block = %s' % (block_num, data))

    def load(self, buffer_block, disk_block, if_free=True):
        '''
        将磁盘中的指定块写入缓冲区的指定块
        :param buffer_block: 缓冲区块号
        :param disk_block: 磁盘块号
        :param if_free: 是否释放磁盘块
        :return: None
        '''
        self.buffer[buffer_block] = open('./disk/%s.ziqi' % disk_block, 'r').read()
        self.io_num += 1
        if if_free:
            self.__disk_flag[disk_block] = 0
        logging.debug('load No.%s disk block to No.%s buffer block' % (disk_block, buffer_block))

    def store(self, buffer_block, disk_block):
        '''
        将缓冲区块写到磁盘块
        :param buffer_block: 缓冲区块号
        :param disk_block: 磁盘块号
        :return: None
        '''
        with open('./disk/%s.ziqi' % disk_block, 'w') as f:
            f.write(str(self.buffer[buffer_block]))
        self.io_num += 1
        logging.debug('store No.%s buffer block to No.%s disk blocks' % (buffer_block, disk_block))

    def get_io_times(self):
        '''
        返回IO次数
        :return: None
        '''
        return self.io_num

    def draw(self):
        '''
        在终端输出当前Buffer和Disk的存储状态，IO次数
        :return: None
        '''
        lines = max(self.__buffer_block_num, self.__disk_block_num)
        print "%-20s %-30s %-30s" % ("Index", "Buffer", "Disk")
        for index in range(lines):
            if index >= self.__buffer_block_num:
                print "%-20s %-30s %-30s" % (index, '', open('./disk/%s.ziqi' % index, 'r').read())
            elif index >= self.__disk_block_num:
                print "%-20s %-30s %-30s" % (index, self.buffer[index], "")
            else:
                print "%-20s %-30s %-30s" % (index, self.buffer[index], open('./disk/%s.ziqi' % index, 'r').read())
        print "Disk IO load/store times = %s" % self.io_num

    def __newdisk__(self):
        '''
        初始化文件块
        :return: None
        '''
        disk_file_list = os.listdir(os.getcwd())
        for fl in disk_file_list:
            if fl[-5:] == 'ziqi':
                os.remove(fl)
        for i in range(self.__disk_block_num):
            open('./disk/' + str(i) + '.ziqi', 'w')
        logging.debug('init %s disk blocks' % self.__disk_block_num)


p = memory(8,20,3)
p.draw()