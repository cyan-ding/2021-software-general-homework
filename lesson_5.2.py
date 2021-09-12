pawn = ">-o"

class pawn:
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
    def coords(self):
        return [self.x, self.y]
        
    def __repr__(self):
        return pawn
class bishop(pawn):
    def __init__(self, x, y, name, color):
        super().__init__(x,y, name,color)
    def __repr__(self):
        return ">-B"
class knight(pawn):
    def __init__(self, x, y, name, color):
        super().__init__(x,y, name,color)
    def __repr__(self):
        return ">-L"
class king(pawn):
    def __init__(self, x, y, name, color):
        super().__init__(x,y, name,color)
    def __repr__(self):
        return ">-M"
class queen(pawn):
    def __init__(self, x, y, name, color):
        super().__init__(x,y, name,color)
    def __repr__(self):
        return ">-Q"
class rook(pawn):
    def __init__(self, x, y, name, color):
        super().__init__(x,y, name,color)
    def __repr__(self):
        return ">-R"




Blackpawn1 = pawn("a", 7, "pawn","black")

Blackpawn2 = pawn("b", 7, "pawn","black")
Blackpawn3 = pawn("c", 7, "pawn","black")
Blackpawn4 = pawn("d", 7, "pawn","black")
Blackpawn5 = pawn("e", 7, "pawn","black")
Blackpawn6 = pawn("f", 7, "pawn","black")
Blackpawn7 = pawn("g", 7, "pawn","black")
Blackpawn8= pawn("h", 7, "pawn","black")

Whitepawn1 = pawn("a", 2, "pawn","whit")

Whiteppawn2 = pawn("b", 2, "pawn","white")
Whiteppawn3 = pawn("c", 2, "pawn","white")
Whiteppawn4 = pawn("d", 2, "pawn","white")
Whiteppawn5 = pawn("e", 2, "pawn","white")
Whiteppawn6 = pawn("f", 2, "pawn","white")
Whiteppawn7 = pawn("g", 2, "pawn","white")
Whiteppawn8= pawn("h", 2, "pawn","white")

blackbishop1 = bishop("c", 8, "bishop", "black")

blackbishop2 = bishop("f", 8, "bishop", "black")

whitebishop2 = bishop("f", 1, "bishop", "black")

whitebishop1 = bishop("c", 1, "bishop", "black")

blackking = king("e", 8, "king", "black")
whiteking = king("e", 1, "king", "white")
blackqueen = queen("d", 8, "queen","black" )
whitequeen = queen("d", 1, "queen", "white")
whiterook1 = rook("a", 1, "rook", "black")
whiterook2 = rook("h", 1, "rook", "black")
blackrook1 = rook("a", 8, "rook", "black")
blackrook2 = rook("h", 8, "rook", "black")
whiteknight = knight("b", 1, "rook", "black")
whiteknight = knight("g", 1, "rook", "black")
blackknight = knight("b", 8, "rook", "black")
blackknight = knight("g", 8, "rook", "black")





