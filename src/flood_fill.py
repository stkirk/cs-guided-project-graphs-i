"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

```plaintext
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```

Notes:

- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
"""
Inputs:
image -> List[List[int]]
sr -> int
sc -> int
new_color -> int

Output:
List[List[int]]
"""
image_str = [
    "##########################################",
    "#                                        #", 
    "#   ##############                       #",
    "#   #             #                      #",
    "#   #       ###    #                     #",
    "#   #      #   #  #                      #",
    "#    #     ##   ##                       #",
    "#    #      #                            #",
    "#     ######                             #",
    "#                                        #",
    "##########################################"
]
image = [list(a) for a in image_str]
def print_image():
    for row in image:
        print("".join(row))

# fill image with any character
def flood_fill(image, row, col, new_char):
    # each character (including spaces) is a node
    # in the example image, '#' signifies a border and spaces are blank space
    # as long as we don't run into a '#', keep going
    if image[row][col] != " ":
        return
    # visit each blank space and replace with new_char
    image[row][col] = new_char

    # compute the neighbors for the start node using (row, col) tuple coordinates
    neighbors = [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1),
    ]
    # loop through the neighbors calling flood_fill on each of them
    for neighbor_row, neighbor_column in neighbors:
        flood_fill(image, neighbor_row, neighbor_column, new_char)

flood_fill(image, 4, 9, '*')
print_image()
flood_fill(image, 1, 12, '.')
print_image()
