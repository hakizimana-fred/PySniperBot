import sys


class SignalHandler:
    @staticmethod
    def register(sig, frame):
        print("\nCtrl+C detected. Exiting gracefully.")
        sys.exit(0)


# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     pass
