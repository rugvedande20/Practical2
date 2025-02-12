def bouncing_ball(width=20, height=10):
    x, y = 0, 0
    dx, dy = 1, 1
    
    while True:
        # Clear screen
        print("\033c", end="")
        
        # Draw the box
        for i in range(height):
            for j in range(width):
                if i == y and j == x:
                    print("O", end="")  # Ball
                else:
                    print(" ", end="")
            print()
        
        # Update position
        x += dx
        y += dy
        
        # Bounce off walls
        if x == 0 or x == width - 1:
            dx *= -1
        if y == 0 or y == height - 1:
            dy *= -1
        
        # Simple delay
        for _ in range(1000000):
            pass

if __name__ == "__main__":
    bouncing_ball()
