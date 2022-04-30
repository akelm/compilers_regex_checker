import re

from state import State

# states for (aa|bb)a(b)*(a)?
states = [State(1, 2, None, 'N'), State(3, None, None, 'N'), State(None, 3, None, 'N'), State(4, None, None, 'N'),
          State(5, 4, None, 'A'), State(None, None, None, 'A')]

alphabet = {'0', '1'}

pattern = re.compile(r'^(11|00)((10*1?)|(01*0?))$')
