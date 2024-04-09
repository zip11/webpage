class Color:
    HEADER = '\033[95m'  # 粉红色
    OKBLUE = '\033[94m'   # 蓝色
    OKGREEN = '\033[92m'  # 绿色
    WARNING = '\033[93m'  # 黄色
    FAIL = '\033[91m'     # 红色
    ENDC = '\033[0m'      # 结束颜色设置

def print_color(color_code, message):
    """
    打印带有指定颜色的消息。

    Args:
        color_code (str): 控制台颜色代码。
        message (str): 要打印的消息。
    """
    print(color_code + message + Color.ENDC)

def print_blue(message):
    """
    打印蓝色消息。

    Args:
        message (str): 要打印的消息。
    """
    print_color(Color.OKBLUE, message)

def print_green(message):
    """
    打印绿色消息。

    Args:
        message (str): 要打印的消息。
    """
    print_color(Color.OKGREEN, message)

def print_warning(message):
    """
    打印警告消息。

    Args:
        message (str): 要打印的消息。
    """
    print_color(Color.WARNING, message)

def print_fail(message):
    """
    打印失败消息。

    Args:
        message (str): 要打印的消息。
    """
    print_color(Color.FAIL, message)

# 示例用法
print_blue("This is a blue message.")
print_green("This is a green message.")
print_warning("This is a warning message.")
print_fail("This is a failed message.")
