from autorefresh.autorefresh_thread import AutorefreshThread


class AutorefreshThreadWeb(AutorefreshThread):

    def start(self):
        print("starting the fake thread")
