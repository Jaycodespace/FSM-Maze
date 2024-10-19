class FSM:
    def __init__(self, initial_state):
        
        self.state = initial_state

    def change_state(self, new_state):
        
        self.state = new_state

    def handle_event(self, event):
        
        self.state.handle_event(event)

    def update(self):
      
        self.state.update()

    def render(self, screen):
        
        self.state.render(screen)
