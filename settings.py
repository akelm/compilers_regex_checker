import re

from state import State

# states for (aa|bb)a(b)*(a)? = aa( (a(b)*(a)?) | (b(a)*(b)?))
states = [State(1, None, None, 'N'),
          State(2, None, None, 'N'),
          State(3, 5, None, 'N'),
          State(4, 3, None, 'A'),
          State(None, None, None, 'A'),
          State(5, 4, None, 'A')]

alphabet = {'0', '1'}

pattern = re.compile(r'^(11|00)((10*1?)|(01*0?))$')
