import pdb

def seq(n):
    for i in range(n):
        pdb.set_trace()
        print(n)
        

seq(5)

'''
ipdb> list
ipdb> p locals()
{'n': 5, 'i': 2}
ipdb> h
ipdb> q
'''
