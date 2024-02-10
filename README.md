# Computer Graphics Assignments 
## Bresenham's Line Algorithm Implementation in Python

This Python code implements the **Bresenham's Line Drawing Algorithm**, a popular technique for drawing lines on digital displays. It uses integer arithmetic and decision parameters to ensure accurate line representation even on pixelated screens.

**Key Features:**

* Clear and concise implementation with separate functions for different slopes.
* Visual representation using `matplotlib` for easy understanding.
* Handles lines with various slopes (less than and greater than one).
* Includes predefined test cases for demonstration.

## Outputs
The algorithm was tested with the following cases:

- **Overall Output**: 

![output](assets/Output.png)

## Explanation of the Output 
### CASE 1: (1, 1) to (8, 4)

- **Printing Initial Points:**  It starts by printing the given points `(1, 1)` and `(8, 4)`.
- **Identifying Slope:** The code computes the slope (m) using the formula m = (y2 - y1) / (x2 - x1). In this case, `m = (4 - 1) / (8 - 1) = 3/7`, which is less than 1. So, it prints `Slope is less than one`.
- **Initializing Decision Parameter:** The code initializes the decision parameter `(p)` using the formula `p = 2 * dy - dx`, where `dx` is the change in `x` (7 here) and `dy` is the change in `y (3 here)`. This gives `p = 2 * 3 - 7 = -1`. It also sets the current point to `(1, 1)`.
- **Executing Bresenham's Algorithm:** The code iterates from `x = 1` to `x = 8` `(incrementing x by 1 in each step)`. For each x-coordinate:
  * It calculates the corresponding y-coordinate using the Bresenham's algorithm logic based on the current `p` value.
  * It appends the calculated point `(x, y)` to a list of intermediate points.
  * It updates the `p` value for the next iteration.
- **Printing Intermediate Points:** After the loop, the code prints the list of intermediate points calculated throughout the iteration.
- **Visualization:** Finally, it uses `matplotlib` to create a plot showcasing the line connecting the starting point `(1, 1)` and the ending point `(8, 4)`, along with the calculated intermediate points marked on the line.

Line from (1,1) to (8,4) - Represents a slope where 0 < m < 1. 

![case 1](assets/11-84.png)

### CASE 2: (1, 1) to (4, 8)

#### The steps for Case 2 follow a similar process, with the key difference being:
- **Slope calculation:** `m = (8 - 1) / (4 - 1) = 7/3`, which is `greater than 1`. So, it prints `Slope is greater or equal to one`.
- **Decision parameter initialization:** `p = 2 * dx - dy = 2 * 3 - 7 = -1`. 
- **Bresenham's algorithm execution:** Iterates over `y-coordinates (from 1 to 8)` instead of `x-coordinates`. This is because for `slopes > 1`, the change in `y` is more significant, so iterating over `y` ensures smoother line drawing.

Line from (1,1) to (4,8) - Represents a slope where m > 1.

![case 2](assets/11-48.png)

## Explanation of Adjustments for Bresenham's Line Drawing Algorithm with Slope > 1

In Bresenham's Line Drawing Algorithm, accurate rendering of lines with steep slopes `(m > 1)` requires crucial adjustments to the original algorithm designed for `slopes < 1`. Let's delve into these adjustments in detail:

## Understanding the Original Algorithm:
* Iterates along X-axis: The heart of the original algorithm lies in iterating over horizontal increments (X-changes) and comparing an accumulated error to `2 * dy` (twice the change in Y) to decide whether to increase Y or not.
* Limitations for Steep Slopes: This approach works well for slopes less than 1, where X-changes dominate. However, with slopes greater than 1, `dy` becomes larger, leading to frequent Y increments and inaccurate lines.

## Adjustments for Slopes > 1:

### 1. Swap Axes:
  - **Rationale:** This fundamental change flips the iteration axis from X to Y. Since `dy` dominates `dx` for steep slopes, iterating along Y makes decision steps smaller and more accurate.
  - **Implementation:** Swapping coordinates effectively changes the slope to its reciprocal `(1/m)`, which is always less than 1. This allows us to leverage the original algorithm's logic with minor adjustments.

### 2. Decision Parameter Update:
  - **Original Rule:** `p = p + 2 * dy - 2 * dx`
  - **Adjusted Rule:** `p = p + 2 * dx - 2 * dy` (swap `dx` and `dy`)
  - **Reasoning:** The original rule favors increasing Y due to the larger dy term. Swapping `dx` and `dy` balances the decision towards choosing horizontal steps (X-increments) when appropriate, ensuring smoothness for steep slopes. 

### 3. Plotting Points:
  - **Current Pixel:** Plot the current (`x`, `y`) coordinates.
  - **Next Pixel:** 
    * If `p < 0`, go right (increment `x`).
    * If `p >= 0`, go right and up (increment `x` and `y`). Reasoning: This logic aligns with the swapped axes and adjusted decision parameter, guaranteeing accurate pixel selection even for steep slopes.

## Getting Started:

1. Clone the git repository with `git clone https://github.com/SaYMy-NaMe/Computer-Graphics-Assignments.git`
2. Install `matplotlib` with `pip3 install matplotlib`, or comment the `visual_show` function definition and the calls. (In this case, You won't be able to see the visuals)
3. Run the code (no arguments) to see the test cases.
4. Uncomment the `inputCoordinates` (comment the predefined test cases) function and `n` variable in `main` for user input.


## Author

* Ashrafur Rahman Chowdhury (Reg: 2019831070 | SWE - IICT | SUST)
* Contact: ashrafur035@gmail.com | +880 1798262185
