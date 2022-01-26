from datetime import datetime
def main():
  print("Date is "+ str(datetime.now().strftime("%d %B %Y %I:%M:%S %p")))
if __name__ == "__main__":
  main()
