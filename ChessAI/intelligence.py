import chess

class AI:
    def __init__(self, b: chess.Board, c: chess.Color):
        self.board = b
        self.color = c
        self.p_table = [[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]
        self.kn_table = [[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
        self.b_table = [[ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
        [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
        [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
        [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
        [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
        [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
        [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
        self.r_table = [
        [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]]
        self.q_table = [[ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
        [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
        [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]
        self.k_table = [[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
        [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
        [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
        [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]]

    def move(self, depth: int, isTurn: bool, alpha: float, beta: float):
        if depth == 0:
            return None, self.eval(self.board)
        moves = list(self.board.legal_moves)
        if len(moves) == 0:
            if self.board.is_stalemate:
                return None, 0
            elif isTurn:
                return None, -9999
            else:
                return None, 9999
        maxInd = 0
        bestVal = -9999
        if not isTurn:
            bestVal = 9999
        vals = []
        i = 0
        for move in moves:
            self.board.push_uci(str(move))
            pos = self.move(depth - 1, not isTurn, alpha, beta)[1]
            self.board.pop()
            vals.append(pos)
            if (isTurn and pos > bestVal) or (not isTurn and pos < bestVal):
                bestVal = pos
                maxInd = i
            if isTurn:
                alpha = max(bestVal, alpha)
            else:
                beta = min(bestVal, beta)
            if beta <= alpha:
                break
            i += 1
        return moves[maxInd], bestVal

    #from AI's point of view
    def eval(self, b: chess.Board) -> float:
        pos = len(b.pieces(chess.PAWN, chess.WHITE)) + len(b.pieces(chess.BISHOP, chess.WHITE)) * 3 + len(b.pieces(chess.KNIGHT, chess.WHITE)) * 3 + len(b.pieces(chess.ROOK, chess.WHITE)) * 5 + len(b.pieces(chess.QUEEN, chess.WHITE)) * 9 + len(b.pieces(chess.KING, chess.WHITE)) * 90
        pos -= (len(b.pieces(chess.PAWN, chess.BLACK)) + len(b.pieces(chess.BISHOP, chess.BLACK)) * 3 + len(b.pieces(chess.KNIGHT, chess.BLACK)) * 3 + len(b.pieces(chess.ROOK, chess.BLACK)) * 5 + len(b.pieces(chess.QUEEN, chess.BLACK)) * 9 + len(b.pieces(chess.KING, chess.BLACK)) * 90)
        
        #pawns
        for i in list(b.pieces(chess.PAWN, chess.WHITE)):
            row = i // 8; col = i % 8
            pos += (10 + self.p_table[row][col])
        for i in list(b.pieces(chess.PAWN, chess.BLACK)):
            row = 7 - (i // 8); col = i % 8
            pos -= (10 + self.p_table[row][col])

        #knights
        for i in list(b.pieces(chess.KNIGHT, chess.WHITE)):
            row = i // 8; col = i % 8
            pos += (30 + self.kn_table[row][col])
        for i in list(b.pieces(chess.KNIGHT, chess.BLACK)):
            row = 7 - (i // 8); col = i % 8
            pos -= (30 + self.kn_table[row][col])

        #bishops
        for i in list(b.pieces(chess.BISHOP, chess.WHITE)):
            row = i // 8; col = i % 8
            pos += (30 + self.b_table[row][col])
        for i in list(b.pieces(chess.BISHOP, chess.BLACK)):
            row = 7 - (i // 8); col = i % 8
            pos -= (30 + self.b_table[row][col])

        #rooks
        for i in list(b.pieces(chess.ROOK, chess.WHITE)):
            row = i // 8; col = i % 8
            pos += (50 + self.r_table[row][col])
        for i in list(b.pieces(chess.ROOK, chess.BLACK)):
            row = 7 - (i // 8); col = i % 8
            pos -= (50 + self.r_table[row][col])
        
        #queens
        for i in list(b.pieces(chess.QUEEN, chess.WHITE)):
            row = i // 8; col = i % 8
            pos += (90 + self.q_table[row][col])
        for i in list(b.pieces(chess.QUEEN, chess.BLACK)):
            row = 7 - (i // 8); col = i % 8
            pos -= (90 + self.q_table[row][col])

        #kings
        for i in list(b.pieces(chess.KING, chess.WHITE)):
            row = i // 8; col = i % 8
            pos += (900 + self.k_table[row][col])
        for i in list(b.pieces(chess.KING, chess.BLACK)):
            row = 7 - (i // 8); col = i % 8
            pos -= (900 + self.k_table[row][col])

        if self.color == chess.BLACK:
            return -pos
        return pos