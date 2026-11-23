# Matrix Rank, Step by Step

A single-page web app that shows, step by step, how to find the rank of a matrix of whole numbers.

- **Row echelon form**: row operations only, with an animated `t` multiply-and-subtract for each step.
- **Normal form**: row and column operations, ending as `[ I 0 ; 0 0 ]`; the size of `I` is the rank.
- Handles zero pivots and repeated rows (they swap or cancel to zero rows).
- Works with whole numbers only. If the numbers get too big to stay exact, the page says so instead of showing a wrong rank.
- Works on phones. No build step, no dependencies: it is one `index.html` file.
