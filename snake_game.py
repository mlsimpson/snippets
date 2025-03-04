#!/usr/bin/env python3
import curses
import random

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.timeout(100)  # Set input timeout (controls game speed)
    sh, sw = stdscr.getmaxyx()  # Get screen height and width

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food color

    # Create initial snake and food
    snake = [[sh//2, sw//4]]  # Snake starts in the middle-left
    food = [sh//2, sw//2]     # Food starts in the middle

    # Place first food
    stdscr.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(2))

    # Initial direction (right)
    key = curses.KEY_RIGHT

    # Initial score
    score = 0

    # Game loop
    while True:
        # Display score
        stdscr.addstr(0, 2, f"Score: {score}")

        # Get next key (non-blocking)
        next_key = stdscr.getch()
        if next_key != -1:
            key = next_key

        # Calculate next head position based on direction
        head = snake[0].copy()
        if key == curses.KEY_DOWN:
            head[0] += 1
        elif key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_RIGHT:
            head[1] += 1
        elif key == ord('q'):  # Quit game
            break

        # Insert new head
        snake.insert(0, head)

        # Check if snake has eaten the food
        if snake[0] == food:
            # Generate new food
            food = None
            while food is None:
                nf = [random.randint(1, sh-2), random.randint(1, sw-2)]
                if nf not in snake:
                    food = nf
            stdscr.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(2))
            score += 1

            # Increase game speed slightly (every 5 points)
            if score % 5 == 0 and score > 0:
                new_timeout = max(50, 100 - (score // 5) * 5)
                stdscr.timeout(new_timeout)
        else:
            # Remove tail if no food eaten
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        # Draw snake head
        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD, curses.color_pair(1))

        # Check collision with walls
        if (snake[0][0] in [0, sh-1] or snake[0][1] in [0, sw-1] or
            snake[0] in snake[1:]):
            msg = "Game Over!"
            stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg)
            stdscr.addstr(sh//2 + 1, sw//2 - len("Press any key to exit")//2, "Press any key to exit")
            stdscr.refresh()
            stdscr.nodelay(False)  # Turn off non-blocking input
            stdscr.getch()  # Wait for key press
            break

if __name__ == "__main__":
    try:
        # Initialize curses
        curses.wrapper(main)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        pass
    finally:
        print("Snake game exited. Thanks for playing!")

