def tri_area(width, height):
    return width * height * 1/2

def box_area(width, height):
    return width * height

def print_area(width, height):
    print("가로", width, "세로", height,\
        "인 삼각형의 넓이:", tri_area(width, height))