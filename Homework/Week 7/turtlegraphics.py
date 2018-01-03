'''
program to draw turtle fractals
'''

def gasket(n, l, pen):
    # termination
    if n==0 or l<2:
        # draw an equilateral trangle
        pen.forward(l);pen.left(120)
        pen.forward(l);pen.left(120)
        pen.forward(l);pen.left(120)
        return
    #end if
    gasket(n-1, l/2, pen); pen.forward(l); pen.left(120)
    gasket(n-1, l/2, pen); pen.forward(l); pen.left(120)
    gasket(n-1, l/2, pen); pen.forward(l); pen.left(120)

# end def
    


def tree(n, l, pen):
    # termination
    if n==0 or l<2:
        return
    # end if

    pen.forward(l)
    pen.left(45)
    tree(n-1, l/2, pen)
    pen.right(90)
    tree(n-1, l/2, pen)

    pen.left(45)
    pen.backward(l)

#end def

def tree4(n,l, pen):
    # termination
    if n==0 or l<2:
        return
    # end if

    pen.forward(l)
    pen.left(90)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)

    pen.left(90)
    pen.backward(l)

#end def

def k(n, l, pen):
    if n==0 or l<2:
        pen.forward(l)
        return
    #end if
    k(n-1, l/3, pen)
    pen.left(60)
    k(n-1, l/3, pen)
    pen.right(120)
    k(n-1, l/3, pen)
    pen.left(60)
    k(n-1, l/3, pen)

#end def

def flake(n, l, pen):
    k(n, l, pen);pen.right(120)
    k(n, l, pen);pen.right(120)
    k(n, l, pen);pen.right(120)
#end def
    
























    
