def floodFill(image, sr, sc, newColor):
    originalColor = image[sr][sc]
    if originalColor == newColor:
        return image

    def dfs(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] != originalColor:
            return

        image[r][c] = newColor
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image

# 🧾 Input Section
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

image = []
print("Enter the image row by row (space-separated 0/1 values):")
for _ in range(rows):
    row = list(map(int, input().split()))
    image.append(row)

sr = int(input("Enter starting row (sr): "))
sc = int(input("Enter starting column (sc): "))
newColor = int(input("Enter new color: "))

# 🖌️ Apply Flood Fill
result = floodFill(image, sr, sc, newColor)

# 📤 Output
print("Flood-filled image:")
for row in result:
    print(*row)
