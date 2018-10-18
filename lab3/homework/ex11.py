def is_inside(point,rect):
    if rect[0] < point[0] < rect[0] + rect[2] and rect[1] < point[1] < rect[1] + rect[3]:
        return True
    else:
        return False