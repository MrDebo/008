import os
if __name__ == "__main__":
   try:
       __import__("igc").lisensi()
   except Exception as e:
       exit(str(e))
