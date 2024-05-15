n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def max_tilted_rectangle_sum(grid):
    n = len(grid)
    
    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n
    
    max_sum = 0
    
    # Iterate over every possible starting point
    for x in range(n):
        for y in range(n):
            # Try every possible length for each direction d1, d2, d3, d4
            for d1 in range(1, n):  # d1 = top-right
                for d2 in range(1, n):  # d2 = bottom-right
                    if not in_bounds(x + d1, y + d1) or not in_bounds(x + d1 + d2, y + d1 - d2):
                        continue  # If moving d1 top-right and then d2 bottom-right goes out of bounds, skip
                    
                    for d3 in range(1, n):  # d3 = bottom-left
                        if not in_bounds(x + d1 + d2 - d3, y + d1 - d2 - d3):
                            continue  # If further d3 bottom-left goes out of bounds, skip
                        
                        for d4 in range(1, n):  # d4 = top-left
                            # Calculate final position after moving d4 top-left
                            final_x = x + d1 + d2 - d3 - d4
                            final_y = y + d1 - d2 - d3 + d4
                            
                            if final_x != x or final_y != y:
                                continue  # If it doesn't close the rectangle, skip
                            
                            # Now calculate the sum of this tilted rectangle
                            current_sum = 0
                            # Segment 1: top-right
                            for i in range(d1):
                                xi, yi = x + i, y + i
                                if not in_bounds(xi, yi):
                                    break
                                current_sum += grid[xi][yi]
                            # Segment 2: bottom-right
                            for i in range(d2):
                                xi, yi = x + d1 + i, y + d1 - i
                                if not in_bounds(xi, yi):
                                    break
                                current_sum += grid[xi][yi]
                            # Segment 3: bottom-left
                            for i in range(d3):
                                xi, yi = x + d1 + d2 - i, y + d1 - d2 - i
                                if not in_bounds(xi, yi):
                                    break
                                current_sum += grid[xi][yi]
                            # Segment 4: top-left
                            for i in range(d4):
                                xi, yi = x + d1 + d2 - d3 - i, y + d1 - d2 - d3 + i
                                if not in_bounds(xi, yi):
                                    break
                                current_sum += grid[xi][yi]
                            
                            max_sum = max(max_sum, current_sum)
    
    return max_sum

print(max_tilted_rectangle_sum(arr))