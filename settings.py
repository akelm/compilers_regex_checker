from state import State

# states for (aa|bb)a(b)*(a)?
states = [State(1, 3, None, 'N'),
          State(2, None, None, 'N'),
          State(4, None, None, 'N'),
          State(None, 2, None, 'N'),
          State(5, 4, None, 'A'),
          State(None, None, None, 'A')]

alphabet = ['a', 'b']


