from std_msgs.msg import String
from interpreter_callback import CommandParent


class Command(CommandParent):
    def __init__(self, interpreter_info):
        CommandParent.__init__(self)
        self.val = ''


def process_key(val, cmd, interpreter_info):
    return val


def fill_msg(cmd, interpreter_info):
    msg = String()
    msg.data = cmd.val

    return msg
