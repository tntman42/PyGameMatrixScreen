# Matrix Code

This program creates a window with text that fades in and out, similar to how it is shown in the Matrix movies.


## Keyboard Controls

There is only one control currently, the SPACEBAR pauses the continuous scrolling of the text on the screen.

## Changing the text

Changing what is scrolling in the background, one simply needs to change the text on line `110` or in some way provide an alphabet argument to the `MatrixText` object.

### For Example

```python

108
109     def main():
110         alpha = 'FOLLOW THE RABIT '  # Changing the text on this line 
111                                      # will change the text that appears
112         pygame.display.set_caption('The Matrix')
113         clk = pygame.time.Clock()
114         while True:
115             event_handler()
116             loop(alphabet=alpha)  # Alphabet is sent to objects here
117
118             pygame.display.update()
119             clk.tick(fps)
120
121
122     if __name__ == '__main__':
123         main()


```