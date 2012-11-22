
class State(object):

    """
     Interface for state-specific behaviour

    :version:
    :author:
    """

    def _get_options(self):
        """
         Get the currently available state-specific options

        @return string :
        @author
        """
        pass

    def _get_state_desc(self):
        """
         Returns a string describing the state

        @return string :
        @author
        """
        pass

    def _process_input(self, curr_action):
        """
         Process input in a state-specific way

        @param int curr_action : 
        @return string :
        @author
        """
        pass



