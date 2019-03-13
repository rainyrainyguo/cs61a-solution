""" Optional problems for Lab 6 """

## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',)) #注意，这里的'brownie'后面必须有逗号，不然tuple连接不起来
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    i=-1
    def vend():
        nonlocal i
        i=(i+1)%len(snacks)
        return snacks[i]
    return vend